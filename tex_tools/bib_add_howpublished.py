import re #regex: @[a-z]+\{([\s\S]*?)\}
import argparse


def parse_command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    return parser.parse_args()


def main():
    args = parse_command_line_args()
    with open(args.filename, "r") as rfile:
        origtxt = rfile.read()
        txt = """Automatically generated by Mendeley Desktop 1.19.8
Any changes to this file will be lost if it is regenerated by Mendeley.

BibTeX export options can be customized via Options -> BibTeX in Mendeley Desktop
Chris' script ran over it.

""" + ("\n".join(add_howpublished(origtxt)))
    with open(args.filename, "w") as wfile:
        wfile.write(txt)

########################################################################################################################

def generate_parangroups(txt):
    #https://stackoverflow.com/a/38212061/5122790
    stack = 0
    startIndex = None
    lasti = 0
    for i, c in enumerate(txt):
        if c == '{':
            if stack == 0:
                startIndex = i + 1 # string to extract starts one index later
                label = (tmp := txt[lasti:i])[tmp.rfind("\n") if tmp.rfind("\n") > -1 else None:]
            # push to stack
            stack += 1
        elif c == '}':
            # pop stack
            stack -= 1
            if stack == 0:
                yield label, txt[startIndex:i]
                lasti = i


def add_howpublished(txt):
    for label, group in generate_parangroups(txt):
        content = group[group.find(",")+2:]
        keyvals = {k.strip(" \n="): v.strip() for k, v in generate_parangroups(content)}  #dict(re.findall("([a-z]+) = \{([\s\S]*?)\}", content))
        if label[2:] == "misc":
            if "url" in keyvals.keys() and not "howpublished" in keyvals.keys():
                keyvals["howpublished"] = '\\url{'+keyvals["url"]+'}'
        yield f"@{label[2:]}{{"+group[:group.find(",")]+",\n"+"\n".join([f"{key} = {{{val}}}," for key, val in keyvals.items()])[:-1]+"\n}\n"


if __name__ == '__main__':
    main()