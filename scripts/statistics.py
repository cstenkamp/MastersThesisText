import subprocess
import git
from os.path import dirname, join, abspath
import pandas as pd
from matplotlib import pyplot as plt
import requests
import io
import zipfile
import tempfile
from datetime import timedelta

FILENAME = join(dirname(__file__), "..", "thesis.tex")

DISP_PAGESMAX = 80
DISP_WORDSMAX = 10000

def return_piped_cmd(cmd, stdin=None):
    cmd = cmd.split("|")
    if not stdin:
        ps = subprocess.Popen(cmd[0].strip().split(" "), stdout=subprocess.PIPE)
    else:
        ps = subprocess.Popen(cmd[0].strip().split(" "), stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        ps.stdin.write(stdin.encode("UTF-8"))
        ps.stdin.close()
    if len(cmd) == 1:
        return ps.stdout.read().decode("UTF-8")
    output = subprocess.check_output(cmd[1].strip().split(" "), stdin=ps.stdout).decode("UTF-8")
    ps.wait()
    return output


def get_todos(fname=None, txt=None):
    if fname:
        with open(fname, "r") as rfile:
            txt = rfile.read()
    txt = txt.replace("% ", "%").lower()
    return txt.count("%todo")


def get_npages(fname):
    tmp = return_piped_cmd(f'pdfinfo {fname.replace(".tex", ".pdf")}')
    return int([i for i in tmp.split("\n") if "Pages:" in i][0][len("Pages:"):].strip())


def github_get_npages(owner, repo, pdfname):
    date_pages = {}
    resp = requests.get(f"https://api.github.com/repos/{owner}/{repo}/actions/artifacts", headers=dict(Accept="application/vnd.github.v3+json"))
    for i in resp.json()["artifacts"]:
        art_id = i["url"][i["url"].rfind("/")+1:]
        re2 = requests.get(f"https://nightly.link/{owner}/{repo}/actions/artifacts/{art_id}.zip")
        if re2.status_code != 404:
            # print(i["created_at"])
            archive = zipfile.ZipFile(io.BytesIO(re2.content))
            with tempfile.NamedTemporaryFile(suffix=".pdf") as wfile:
                wfile.write(archive.read(pdfname))
                n_pages = get_npages(wfile.name)
                # print(f"Pages: {n_pages}")
                date_pages[pd.to_datetime([i["created_at"]]).to_pydatetime()[0]] = n_pages
    return pd.Series(date_pages)

def plot_df(df):
    ax1 = df["Words"].plot(color="red", linestyle="-", marker="o", ylabel="Words")
    ax1.set_ylim(0, max(df["Words"].max(), DISP_WORDSMAX))
    ax2 = ax1.twinx()
    ax2.spines['right'].set_position(('axes', 1.0))
    df["Todos"].plot(ax=ax2, color="blue", linestyle="-", marker="x", ylabel="Todos")
    ax3 = ax1.twinx()
    df["Pages"].plot(ax=ax3, color="yellow", linestyle="", marker="s", ylabel="Pages")
    for ax in [ax2, ax3]: ax.set_ylim((0, max(df["Todos"].max(), df["Pages"].max(), DISP_PAGESMAX)))
    ax3.yaxis.set_ticklabels([])
    lines, labels = list(zip(*[[i[0] for i in ax.get_legend_handles_labels()] for ax in [ax1, ax2, ax3]]))
    plt.legend(lines, labels, loc=0)
    plt.show()


def create_history_df(repo_dir, filename):
    #print(abspath(repo_dir))
    repo = git.Repo(repo_dir)
    all_commits = {}
    for commit in repo.iter_commits():
        txt = (commit.tree / filename).data_stream.read().decode("UTF-8")
        n_words = int(return_piped_cmd("detex | wc -w", stdin=txt).strip())
        n_todos = get_todos(txt=txt)
        # print(datetime.fromtimestamp(commit.committed_date))
        # print(f"words: {n_words}, todos: {n_todos}")
        all_commits[pd.to_datetime(commit.committed_datetime, utc=True)] = [n_words, n_todos]
    df = pd.DataFrame(all_commits, index=["Words", "Todos"]).T
    return df

def merge_page_df(df, date_pages):
    for date in df.index:
        try:
            nearest_datepage_after = date_pages.index[date_pages.index.get_loc(date, method='bfill')]
        except KeyError:
            continue
        if nearest_datepage_after-date <= timedelta(hours=2):
            df.loc[date, "Pages"] = int(date_pages[nearest_datepage_after])
    return df



if __name__ == "__main__":
    #history
    df = create_history_df(dirname(FILENAME), "thesis.tex")
    date_pages = github_get_npages("cstenkamp", "MastersThesisText", "thesis.pdf")
    df = merge_page_df(df, date_pages)
    plot_df(df)

    #current
    n_words = int(return_piped_cmd(f"detex {FILENAME} | wc -w"))
    n_pages = get_npages(FILENAME)
    n_todos = get_todos(FILENAME)
    print(f"Words: {n_words}, Pages: {n_pages}, Todos: {n_todos}")