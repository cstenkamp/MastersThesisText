# Usecases Pipeline 

[//]: # TODO: The purpose of this chapter is listing complete and working commands for all ways of how to invoke it! -> Focus on the actual commands and keep it SHORT!!

You can also run stuff from the docker-container, if you want to install it it is referred to \url{https://github.com/cstenkamp/derive_conceptualspaces/blob/main/doc/install_docker.md}, blablabla

## Using Click

Architecture: command -> subcommand -> subsubcommand (every subcommand can load more stuff to the json-persistor and has its own arguments). At any subcommand you can run `--help` to get a list of arguments and commands

This list is ordered by priority of the arguments, so you can combine all the ways below, where the upper ways to set arguments overwrite the lower ones, but you'll be warned if something overwrites something etc.

Minimal way of calling it: `python -m derive_conceptualspace generate-conceptualspace create-candidate-svm`, or using Docker `...`

* With command-line-args
* With `--env-file`  (the env-file can even be an env-var! that's why I can call it with only the env-var "MA_ENV_FILE" in pycharm, and can with only changing the content of the select-env-file change the params for all subcommands)
* With `--conf-file`  (the conf-file arg can even be an env-var!)
* With correct env-vars already set/from default-values 
* What else?

## Using Snakemake

* Minimal way of calling it: `(export $(cat $MA_SELECT_ENV_FILE | xargs) && snakemake --cores 1 -p default)`, or using Docker `...`
* If you have installed the package with pip, you can just do it like this, if not you may need to set the env-var `PYTHONPATH=$(realpath <path/to/repobase>):$PYTHONPATH `
[//]: # Snakemake-args like `--use-conda` etc?
* Running snakemake from a container: pay attention to xyz
* Running snakemake distributedly on a Grid: 

Envoking it: 
* default (with and without env-vars): `snakemake --cores 1 -p default`
* explicit filenames `snakemake ...`
* all / all_for `snakemake ...`
* from_config `snakemake ...`

## In Notebooks

```
assert load_dotenv(abspath(join(os.getcwd(), "..", "config", "siddata.env")))

ctx1 = SnakeContext.loader_context(config=dict(min_words_per_desc=80, dcm_quant_measure="count"))
ctx1.load("pp_descriptions", "filtered_dcm", "embedding", "clusters")
ctx1.obj["filtered_dcm"].show_info(descriptions=ctx1.obj["pp_descriptions"])
```