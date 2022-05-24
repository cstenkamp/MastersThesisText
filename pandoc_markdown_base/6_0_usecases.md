<!--
* Per Click (-> command, subcommand, subsubcommand, every subcommand can load more stuff to the json-persistor)
* In a Jupyter-Notebook (Settings werden festgelegt)
* In Snakemake for:
    * default (with and without env-vars)
    * explicit filenames
    * all / all_for
    * from_config  
-->

\vspace{2ex}
This appendix lists complete an working commands on how exactly to invoke the pipeline described in this thesis. There are three main ways to invoke this codebase: Running the complete pipeline using **Snakemake**, running individual components for development or debugging using the CLI of **Click**, or inspecting results in **Jupyter-Notebooks**. The following sections list some examples for all of these use-cases.

# Docker 

As the code is both compiled as a python-package as well as a docker-container, it is possible to invoke all commands listed here for those options as well. For information on how to install a docker-container it is referred to \url{https://github.com/cstenkamp/derive_conceptualspaces/blob/main/doc/install_docker.md}. To build the docker-container, use the following command:
<!-- \vspace{-3ex} -->
```
docker build -f $MA_CODE_BASE/Dockerfile --build-arg git_commit=$(git rev-parse --short HEAD) --build-arg uid=$(id -u) --build-arg gid=$(id -g) --rm --tag derive_conceptualspaces $MA_CODE_BASE
```
<!-- \vspace{-3ex} -->
Afterwards, you can make an alias for the codebase inside a container:
<!-- \vspace{-3ex} -->
```
alias run_ma="docker run -it --rm --user $(id -u):$(id -g) --name derive_conceptualspaces_cont -v $MA_DATA_DIR:/opt/data --env-file $MA_ENV_FILE derive_conceptualspaces"
```
<!-- \vspace{-3ex} -->
And then call anything from inside the container with \eg
<!-- \vspace{-3ex} -->
```
MA_SNAKEMAKE_TELEGRAM=1 ma_cont snakemake --cores 3 -p  --directory /opt/data default
ma_cont python -m derive_conceptualspace generate-conceptualspace create-candidate-svm
```
<!-- \vspace{-3ex} -->

# Using Click

\label{ap:usecase_click}

The `click` python package is used to generate a command-line interface. The structure of a command is recursive: `command \textrightarrow subcommand \textrightarrow subsubcommand`. This perfectly mirrors the structure of this codebase, as every sub-command can accept more configurations and accept another nested set of dependencies (interim results or results from earlier steps) as argument. At any level of subcommand you can run `--help` to get a list of available arguments and commands.

Minimal way of calling it: `python -m derive_conceptualspace generate-conceptualspace create-candidate-svm` if you have installed the package. 


## Passing configurations 

The algorithm allows for many different parameters or selection of sub-components. \newline \urlx{https://github.com/cstenkamp/derive_conceptualspaces/blob/main/derive_conceptualspace/settings.py} contains the default values for the most important parameters, which can be also set in many different ways. Next to the configurations in the `settings.py` file, there are also other configurations that can set when executing this via click, such as `--log` selecting python's log-level. Again, it is encouraged to run any command with `--help` to figure out all possible arguments.

This code-base allows several ways to inform about demanded configurations, which are listed below. Note that this list is ordered by priority of the arguments, so you can combine all the ways below, where the upper ways to set arguments overwrite the lower ones, but you will be warned if a setting is overwritten by a higher higher priority.

* With command-line-arguments. Every command specifies a list of allowed command-line-arguments, such as eg. the command `preprocess-descriptions` allowing the `--language` argument.
* With `--env-file`: Either by giving a command-line-arg that refers to a `.env`-file, or by having the `MA_ENV_FILE` environment-variable set when executing the code. The latter way is the fastest way to change settings for all sub-commands in the development-process: An additional `select_env.env` file can refer to the actual env-file. This ensures that the run configurations for all commands are changed simultaneously and also allows to quickly select a new suite of arguments for individual datasets - which automatically selects new parameters for all sub-commands. See below for the schema of these environment variables.
* With `--conf-file`, referring to a `YAML`-file with configurations. Note that this argument can, again, be an environment variable. Note that when providing several alternatives for a configuration, this mode will select one consistent sample instead of spawning a process for each possible value, which differs from the behaviour when calling it with Snakemake. \url{https://github.com/cstenkamp/derive_conceptualspaces/tree/main/config} contains a number of files with parameter-combinations corresponding to the exact configuration used by any of \mainalgos.
* With correct env-vars already set: When not overwritten by one of the above ways, configurations are automatically drawn from environment-variables if the respective variable exists in the current context. Note that when using environment-varibles, they must be prepended with `MA_`: To overwrite the configuration `PRIM_LAMBDA`, you would need to set the variable `MA_PRIM_LAMBDA`.
* From default-values. If no of the above ways was used to overwrite a configuration, a default-value is used as specified in the `settings.py`.

If a given command relies on interim results, it must be figured out which of the candidates is selected. To resolve the dependencies, the configurations are resolved as described above, and the dependency that exactly fulfills the required configuration is selected. If the dependency itself relied on more configurations, the values for these are added to the state with maximal priority. If their value is to be overwritten lateron, the codebase figures out if there are any conflicts and either gracefully fails or informs of their difference. The latter may be relevant when for example only requiring `DEBUG=True` for a later step of the algorithm.

## Sample usage

With this as background, let us give some samples of how the code is invoked. First, let us look at the respectively used configurations:

### Used Configurations

**Contents of `/path/to/select_env.env`:**
<!-- \vspace{-3ex} -->
```
MA_BASE_DIR=$HOME/path/to/data
MA_CODEPATH=$HOME/path/to/code
MA_CONDAPATH=$HOME/miniconda3
MA_CONDA_ENVNAME=create_cs
MA_CUSTOM_ACCTFILE=$HOME/custom_acctfile.yml
MA_CONFIGDIR={MA_CODEPATH}/config
MA_GRIDCONF={MA_CODEPATH}/workflow/sge/ikw_grid/
MA_ENV_FILE=siddata.env
```
<!-- \vspace{-3ex} -->
Note that this file contains mostly paths. Separating these from the actual configuration is useful especially when running the code on different machines, such as a local machine used for testing plus a high-performance grid or cluster to be deployed to. Using `MA_ENV_FILE`, it is referred to the actual environment-file. This can contain settings specific to individual datasets, such that only this line must be exchanged to inform all possible commands simultaneously of the configurations required for other datasets.

**Contents of `/path/to/code/config/siddata.env`:**
<!-- \vspace{-3ex} -->
```
MA_DEBUG=1
MA_DEBUG_N_ITEMS=500
MA_DATASET=siddata2022
MA_MIN_WORDS_PER_DESC=80
MA_LANGUAGE=de
MA_CONF_FILE=derrac2015.yml
```
<!-- \vspace{-3ex} -->
This file is used to set configurations that are relevant only to one specific dataset. Furthermore it links a `MA_CONF_FILE`, that is used to set configurations that are *global* in the sense that they affect the configuration irrespective of the used dataset. The contents of `/path/to/code/config/derrac2015.yml` that allow to recreate the configuration of \cite{Derrac2015} is listed in \autoref{ap:yaml_for_derrac}.

### Sample Inputs and Outputs

The following examples explicitly export the `MA_SELECT_ENV_FILE` environment variable, but keep in mind that the `python_dotenv` package or you IDE's Plugin to consider environment-files are just as valid. The PyCharm-Run-Configurations used in the development can be found at \url{https://github.com/cstenkamp/derive_conceptualspaces/tree/main/.run}

\newpage
**Create dissimilarity-matrix without command-line-arguments:**
<!-- \vspace{-3ex} -->
```
export $(cat $MA_SELECT_ENV_FILE | xargs)
python -m derive_conceptualspace generate-conceptualspace create-spaces create-dissim-mat
>> Starting up at 23.03.2022, 16:13:52
>> Config-File .../Derive_Conceptualspace/config/derrac2015_edited.yml loaded.
>> Running with the following settings [3ef0e2c137]: CANDIDATE_MIN_TERM_COUNT: 2, CLASSIFIER: SVM, CLASSIFIER_SUCCMETRIC: kappa_rank2rank_onlypos_min, DATASET: siddata2022, [...]
```


**Extract candidate-terms, enforcing the usage of KeyBERT:**
<!-- \vspace{-3ex} -->
```
export $(cat $MA_SELECT_ENV_FILE | xargs)
export MA_PP_COMPONENTS=mfauhtcsldp;MA_TRANSLATE_POLICY=onlyorig;MA_DEBUG=1
python -m derive_conceptualspace prepare-candidateterms --extraction-method keybert extract-candidateterms --no-faster-keybert
>> Starting up at 23.03.2022, 16:35:16
>> Config-File .../Derive_Conceptualspace/config/derrac2015_edited.yml loaded.
>> Debug is active! #Items for Debug: 500
>> Using a random seed: 1
>> conf_file demanded config EXTRACTION_METHOD to be tfidf, but cmd_args overwrites it to keybert
>> The setting DEBUG was False in a dependency and is True here!
>> Running with the following settings [82fe5f58dd]: CANDIDATE_MIN_TERM_COUNT: 2, CLASSIFIER: SVM, [...]
```
<!-- \vspace{-3ex} -->

# Using Snakemake

\label{ap:usecase_snakemake}

This code-base uses Snakemake to allow running the entire pipeline at once. This can be run directly on a local machine, but also scheduled on \eg the Sun Grid Engine. For that, each base command is specified with some required metadata in the Snakefile at \url{https://github.com/cstenkamp/derive_conceptualspaces/blob/main/workflow/Snakefile}. Snakemake can be invoked with many arguments to for example specify the maximal number of cores to consider, specifying the used conda-environment using `--use-conda`, or to make Snakemake continue running if a single rule failed using `--keep-going`. For all possible arguments, it is referred to \url{https://snakemake.readthedocs.io/en/stable/executing/cli.html#all-options}. Besides these arguments, this codebase provides a large set of to invoke and configure the pipeline.

If this codebase is installed as a package (using `pip install`), snakemake can be called exactly as described above. Otherwise, the codebase may not be in your operating system's `PATH`, which means that you may need to set the env-var `PYTHONPATH=$(realpath /path/to/code):$PYTHONPATH`. It is also possible to run snakemake from a container, using a command similar to the one specified above.

<!-- \vspace{-10ex} -->

## Snakemake Use Cases

There are the following ways to invoke the pipeline with Snakemake. Note that to consider an env-file, you can simply export their values first first: \newline `(export $(cat $MA_SELECT_ENV_FILE | xargs); snakemake --cores 1 -p default)`.

\paragraph{default} \eg `snakemake --cores 1 -p default` \newline
Runs a single configuration, namely the default configuration as specified by default-values or currently active environment variables. 

\vspace{-1ex}
\paragraph{all} \eg `snakemake --cores 1 -p all --keep-going` \newline
Runs all configurations from the cartisian product of all allowed values for all configs. Which values are allowed can be specified in the `settings.py` by replacing the definition `DEFAULT_VARNAME` by a collection `ALL_VARNAME`, as can be inspected here: \urlx{https://github.com/cstenkamp/derive_conceptualspaces/blob/main/derive_conceptualspace/settings.py\#L32-L40}. Note that this is a huge 
combinatorical explosion and only recommended with `DEBUG=True`!

\vspace{-1ex}
\paragraph{all_for} \eg `snakemake --cores 1 -p all_for --config for_rule=create_embedding` \newline Runs the cartesian product of all configuration similarly to **all**, however only executes the pipeline up to a specific step, in this example the rule `create_embedding`.

\vspace{-1ex}
\paragraph{by_config} \eg `snakemake --cores 1 -p  by_config --configfile ./config/derrac2015.yml --keep-going` \newline
Is used to run all configurations specified in a config-file. If any of the values of this configuration-files is a list, all these values will be run individually, allowing to execute the pipeline for different parameter-combinations simultaneously (note the different behaviour when using `click`). This configuration-file further allows to specify configurations specific to a dataset, as shown in \autoref{ap:yaml_for_derrac}.

\vspace{-1ex}
\paragraph{\textit{specific files}} \eg `snakemake --cores 1 -p --directory $MA_DATA_DIR siddata/debug_True/fautcsdp_translate_minwords100/embedding_ppmi/dissim_mat.json` \newline
The original way how Snakemake-workflows are invoked. This allows to specify only those configurations that are part of the file-path, resolving configurations and dependencies by the expected positions in it.

## On Grids/HPCs

Additionally to running on a single machine, it is also possible to submit this workflow to a cluster or grid. There is a lot of code to allow to either *schedule* this workflow on the \gls{ikw} grid, or to just run it manually. To run it manually, you can use the `run_manually` script, by \eg `/path/to/code/workflow/sge/run_manually.sh by_config --configfile /path/to/code/config/derrac2015.yml /path/to/code/workflow/sge`.

To schedule the workflow, you first have to install the environment. This can be done by `qsub`ing the `workflow/sge/install_env.sge`-file. Afterwards you may execute \newline `MA_SELECT_ENV_FILE=/path/to/code/config/select_env.env /path/to/code/workflow/sge/submit.sh`. The submit-script takes care of forwarding all envirionment variables and parsing the actual `ENV_FILE` as specified in the `SELECT_ENV_FILE` (even allowing to nest env-vars such as `MA_CONFIGDIR={MA_CODEPATH}/config`). It further provides arguments to kill all already running instances (`-k`), watch the progress after scheduling it (`-w`), and to remove all old logs and outputs (`-r`). A full sample call is for example `MA_ENV_FILE=placetypes.env submit -kwr by_config --configfile config/derrac2015.yml`. Internally, this script calls  `snakemake -p by_config --configfile <configfile> --directory $DATAPATH --profile /path/to/workflow/ikw_grid/sge`. Configurations specific to the grid engine are, next to the `Snakefile`, specified in a `cluster.yaml` file (\urlx{https://github.com/cstenkamp/derive_conceptualspaces/blob/main/workflow/sge/ikw_grid/cluster.yaml\#L13-L20}). This allows to specify the default amount of memory, and also if there is a wall-time such as for the IKW-Grid. This runtime is considered by restarting both the scheduler, and also passing it to the individual runners for them to gracefully shutdown and restart.  

More information on scheduling Snakemake is available in the respective repository (\url{https://github.com/cstenkamp/Snakemake-IKW-SGE-Profile}) and the How-To (\urlx{https://github.com/cstenkamp/derive_conceptualspaces/blob/main/workflow/sge/howto.md})


# In Notebooks

\label{ap:usecase_notebook}

Inspecting code in Notebooks requires a different handling of contexts, as there is not one single context to which new elements are added. Instead, many different contexts are supposed to be loaded quickly and easily for inspection. This code base provides many helper-functions to get individual configurations, the **best** configuration according to a specifiable metric, or to load many individual configurations at once.

Additionally, many helper functions improve the ease of use for loading configurations from `.env`-files and configuration-YAMLS, help in recovering the environment-variables necessary to load a configuration using click, and much more. A sample call to load all configurations for a dataset looks like this:

<!-- \vspace{-3ex} -->
```
setup_logging()
load_envfiles("siddata")
configs, print_cnf = getfiles_allconfigs("clusters", verbose=True)
>> There are 165 different parameter-combis for dataset siddata2022:
>> {'dataset': 'siddata2022',
>> 'language': 'de',
>> 'debug': 'False',
>> 'pp_components': ['mfauhcsd2', 'mfauhtcsldp'],
>> [...]
print_envvars(get_filename(configs[0], get_dependencies=False))
>> MA_DATASET=siddata2022;MA_LANGUAGE=de;MA_DEBUG=False;MA_PP_COMPONENTS=mfauhcsd2 [...]
```
<!-- \vspace{-3ex} -->

To for example get the interim result `featureaxes` of all configurations, you may use this:
<!-- \vspace{-3ex} -->
```
with WorkerPool(DEFAULT_N_CPUS-3, pgbar="Fetching featureaxes..") as pool:
    get_featureaxes = lambda conf: ((ctx := SnakeContext.loader_context(config=conf, silent=True)).get_important_settings(), ctx.load("featureaxes"))
    featureaxes_list, interrupted = pool.work(configs, get_featureaxes)
```
<!-- \vspace{-3ex} -->

The final sample shows how to find and inspect a best-performing parameter-combination according to a decision-tree, and then running functions on interim results as well as inspecting old outputs:

<!-- \vspace{-3ex} -->
```
setup_logging()
load_envfiles("placetypes")
conf, perf = get_best_conf("Geonames", verbose=True, balance_classes=True, one_vs_rest=True, dt_depth=1, test_percentage_crossval=0.3, metric="f1")
ctx = SnakeContext.loader_context(config=conf, silent=False)
pp_descriptions, filtered_dcm = ctx.load("pp_descriptions", "filtered_dcm" loaders=dict(pp_descriptions=DescriptionList.from_json)
ctx.obj["filtered_dcm"].show_info(descriptions=ctx1.obj["pp_descriptions"])
>> [...]
ctx.display_output("pp_descriptions")
>> [...]
```
<!-- \vspace{-3ex} -->