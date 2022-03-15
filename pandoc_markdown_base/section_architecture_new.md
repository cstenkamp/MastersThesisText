Meta-workflow vorgreifen
	* mit snakemake zig parameter-kombinationen auf dem cluster ausführen kann und mir dann mit `generate-conceptualspace show-data-info` die dabei generierten outputs (like the metrics for the clusters) angucken kann, und wenn mir die gefallen öffne ich den ganzen kram ebenfalls nochmal in nem jupyter-notebook (wo ich dank config-hash fix erkenne obs die selbe config ist), um mir dort dann bspw die überschneidungen der configs anzuschauen
	* dass ich ja Ne shitton an Parameter-Kombis ausführen (besonders da wo im Text nicht eindeutig ist bspw ob sie mit dem PPMI-Ranking oder dem Count-Embedding vergleichen)
	* An vielen Schritten kann man sich Dinge angucken (dissimiliarity-matrix und emedding jeweils die closest entitites, bei den clustern sieht man ja ob ähnliche clustern)
	* an möglist vielen stellen gucken können ob's klappt oder nicht -> modularity
	* workflow mit grid und yamls für kombis und runterladen
	*  Grundlage: Das Gelöt ist in Schritte einteilbar, an gewissen Schritten werde gewisse Params relevant


* Main goal: BETTER ARCHITECTURE. Most important things for that: scalability, modularity, transparency, reproducibility, understandability, objectiveness, systematicacy, sustainability, adaptability
	* describing this because I want to encourage extending the code etc and for that not only the algorithm but also the architecture should be described 
	* and I think that was successful: This codebase contains everything and finally fulfills code-standards! 
		* It is a proper python-package (that you can run with `python -m derive_conceptualspace`), there is a working Docker-container that can be installed with one command and run on any VM even in a thousand years (fixed dependencies etc, reference a reproducibility paper!), 
		* it has workflow-management tools (reference snakemake), 
		* it can easily be installed on a grid (for SLURM I refer to https://github.bsection{Impcom/frankier/singslurm2, but as our university still uses the sun grid engine, there are `.sge` files that allow to run the snakemake-workflow there), etc etc etc!
	* 3 Ways to run:
		* Snakemake if you want to run a shitton of param-combis
		* individual steps via the CLI if you're debugging or look at stuff in detail etc, created something new, ..
		* context-loading for jupyter to inspect and plot results
			* wie geil das mit dem load-context in jupyter notebooks ist (ich kann auch von jeder componente `print(ctx.display_output("embedding"))` callen, ich kann configs einlesen, ich kann über alle configs iterieren und dinge von den files plotten, .... . Und auch der Graph von show-data-info der mir zeigt wo die configs zuerst genutzt wurden und da auch nochmal outputs unda lles hat, herrlich
			* wie algorithmisch auch diese arbeit erzeugt ist - I made an architecture that even allows to automatically make tables with names and everything in python to be exported to latex, and just paste it in and interpret it in the text, I can do 20 theses like this in no time from now on!!
		* (grid, snakemake, docker, python-package:click, python-package: jupyter)
		* Of course there's also a docker-container, so if you don't want to look at any of the code and just execute for a given dataset, you can run it on any PC with docker with the following command: [...] and for a list of all commands, it is referred to appendix xyz which lists a shitton of ways (all snakemake ones, examples of how to include a config, examples of how to look at results using the `generate-conceptualspace show-data-info` command, examples of how to look at results and intermediate results and plots in jupyterlab, ...)
	* Source-code is ofc open, available under github under this link, it is referred to the signed commit xyz
	* Reference Snakemake-Paper (and at least look a the abstract of that, they also talk about that in science you need reproducible, adaptable and transparency including definitions of what that means!)
	* FOR ALL PLOTS, reference how plots are created or general code examples with the real thing, including how what you're seeing was generated and can be reproduced



Foremost design principle: Modularity
	* Es ist wichtig dass die Zwischenergebnisse an jedem Step das gleiche Format haben, egal was für ein Algorithmus dazwischen kam
	* I have MANY different parameters & param-combinations that I need to try out
		-> The pipeline is divisible into distinct steps
		-> As I often need to try different settings where only at the 8th step the relevant config is different, generating temporary files makes sense, such that I can run the stuff only once up until the 7th step and twice only for the step where it's necessary
		-> So this way, when I run the 8th step for the pipeline from the command-line, it figures out if all dependency are there. If they are, I can execute what I want to execute, and if not, it can automatically (using the build-system) create all dependencies - but if the config I demand differs only in the third step from something that is already there, the build system automatically only executes steps 4-7.
		-> Now I have the problem of depencies, were some stuff needs to be scheduled as soon as its dependencies are there etc etc => I need a scheduler
		-> Snakemake.
	* Snakemake.
		* wann snakemake sinnvoll ist und wann nicht, von wegen workflow aufteilen, viele parameter haben die an gewissen punkten relevant werden und später nicht mehr sind, etc. Und auch wann das sinnvoll ist auf dem IKW-Grid laufen zu lassen weil wegen 90min runtime und weniger niceness	* Dass sich das ding historisch von "speziell für das dateiformat wie DESC15 veröffentlicht hat" über "speziell für siddata2022 (extract kurstypes etc)" zu "möglichst allgemein funktionierende pipeline mit guten dateiformaten und so modular wie irgendwie möglich" entwickelt hat
			* (wenn workflow aufteilbar in unabhängige steps mit viel param-kombis etc)
		 	* main thing about is is automatic dependency resolvement (which means I can just tell it "hey I need this file" and it creates it, which is good if I need to automatically create dependencies if I want to run step 8 with certain settings)
		 		* ..and I'm abusing it with config-files
		 	* that it's great if you want to run multiple things at once with optimal usage of CPU/RAM and also very nice for cluster execution
			* nicht sinnvoll wenn du nur nen ANN hast mit einem haupt-schritt etc
			* ...but that you have to abuse it a lot to get where I want it to be (have rules that don't rely on files in the same file with rules that do, no good way to debug, apparently small community (no SO answers etc (mit quelle wie viele Fragen es gibt!!!)), the fact that I need nondynamic filenames that are set from the start of the execution)
			* Im Nachhinein nicht sicher ob Snakemake die beste wahl war und dass ich die logik teilweise hart abuse etc (-> reference appendix A)
		* From their paper:
			* has a domain specific language (statements and dclarations that specifically model central components of workflow management, less boilerplate), implemented as extension to the generic python langauge, so access to the full power of it to handle conditions, configuration, etc. 
				* Stuff can also be declared using configuration formats
			* better reproducibility "by allowing the definition and scalable execution of each involved step, including deployment of the software stack needed for each step (e.g. via the Conda package manager  Docker or Singularity containers)
			* Workflows are decomposed into individual *rules*, which describe how to get an output from inputs (shell-command, scriptcall, code, ..). Input and output can be stored on remote storage. What smk then does is resolve the dependencies for those rules. Through wildcards, rules can be generic.
			* Dependencies between jobs are implicit, and inferred auto- matically in the following way. For each input file of a job, Snakemake determines a rule that can generate it— for exam- ple by replacing wildcards again
				* "By replac- ing wildcards with concrete values, Snakemake turns any rule into a job which will be executed in order to generate the defined output files"
			* Then, Snakemake goes on recursively for the latter, until all input files of all jobs are either generated by another job or already present in the used storage
				* From this inference, Snakemake obtains a directed acyclic graph of jobs
				* The file-centric description of workflows makes it intuitive to to infer dependencies between steps;
				* Scheduling: Because of their dependencies, not all jobs in a workflow can be executed at the same time. Instead, one can imagine partitioning the DAG of jobs into three sections: those that are already finished, those that have already been sched- uled but are not finished yet, and those that have not yet been scheduled (Figure 4a). Let us call the jobs in the latter partition Jo , the set of open jobs. Within Jo , all jobs that have only incom- ing edges from the partition of finished jobs (or no incom- ing edge at all) can be scheduled next. We call this the set J of pending jobs. The scheduling problem a workflow manager like Snakemake has to solve is to select the subset E ⊆ J that leads to an efficient execution of the workflow, while not exceed- ing the given resources like hard drive space, I/O capacity and CPU cores.
					* The maximization optimizes four criteria, represented by four separate terms in (1). First, we strive to prefer jobs with high priority. Second, we aim to maximize the number of used cores, i.e. the extent of parallelization. Third, we aim to delete existing temporary files as soon as possible. Fourth, we try to reduce the lifetime of temporary files that cannot be deleted in this pass.
			* MODULARIZATION
			* portability: conda integration (one env per rule easy), ocntainer ingetragion 
			* traceability: all information from inputs, outputs, arguments, etc can be exported
			* scalability - supports workflow management systems and also grid engines. Snakemake’s design ensures that scaling a workflow to a spe- cific platform should only entail the modification of command line parameters. The workflow itself can remain untouched
			* Also allows graph partitioning (to reduce overhead when scheduling), caching between workflows, iteratively executing rules condidtional execution, benchmarking (logging runtime, CPU, memory etc), parameter space exploration

	* Dass eine key component meiner architecture halt ist dass in zwischenschritten produzierte Dinger, egal welcher algorithmus benutzt wurde, am ende das selbe dateiformat hat damit man easy damit weiterarbeiten kann. Und sanity-checks.
	* In the development process of re-creating the algorithm of DESC15, I noticed that most of the time I'll be on hyperparameter tuning -> because of that, the highest focus for the architecture must lie on modularity and scalability - I want to be able to run a shitton of paramameter-combinations as quickly and efficiently as possible
		-> resulting architecture completely modular, and individual steps can be executed using the CLI, AND the combination of all using Snakemake, AND to load interim results 
	* Dass das SKlearn-Preprocessing ein klein wenig meine reihenfolge der steps zerstört und deswegen honestly 2x läuft
	* Der ganze Jsonpersister kram!! von wegen dass logs custom geschrieben werden und so 
	* * How I usually call it (in SIMPLE, with EXAMPLES), also von wegen ich provide einfach den pfad zu nem env-file und in dem env-file steht dann nochmal welche config er lesen soll, so ist drauf geachtet dass ich die selben settings für alle steps der pipeline hab (what wouldn't be the case if I used cmd-args), and that I can this way have fixed configs for the suggested params of eg the papers I rely on 
		* PLOTS from snakemake and also from the json-persister!


* Running on Grid
	* warum? kombinatorische explosion im parameterspace! am ende easy 128 Dinge die jeweils gerne auch 64 Kerne nehmen gleichzeitig laufen lassen muss.
	* Aufs IKW Grid zugeschnitten, and to my knowledge the best one yet!
	* IKW-Grid und pecularities erklären
		* 90 min runtime -> interruptible
	* link \ref{lst:joblog}
	* dass die ansprüche wegen der hardware sind sowohl multiproc als auch interruptible zu sein, was manchmal gar nicht so trivial ist
	* besseren Grid-Workflow als jeder an der Uni Osnabrück je geschrieben hat, kann die Ressourcen perfekt nutzen 
	* can use max. 65 cores, do use 65 cores
	* den cookiecutter für SGE referencen!
	* dass das nochmal ne neue ebene an "hyperparametern" die es zu optimieren gilt ist, da es halt ne grenze ist wie viele slots man als user hat (apparently 65) und halt die 90 min walltime, das heißt abhängig von meiner datensatz-größe will ich kram wie amount of RAM und CPUs so einteilen dass nach Möglichkeit alle in der walltime fertig werden (unterbrochen werden geht aber ist in jedem Fall ineffizienter als einfach fertig werden) while using the machines at my disposal as efficiently as possible
	* automatisch geschedulet, das skript auf die genaue configs des Uni Osnabrück grids angepasst ist (aber doch easy auf alles andere angepasst werden kann) [next to docker und allem!!], mit 3 commands (explizit dokumentiert) erstinstalliert und ausgeführt werden kann [auch in docker!], das was in jupyternotebooks sein soll ist in jupyternotebooks [lol I could also use sacred here]... Und auch mit wie man in jedem schritt die parameter einbauen kann, schöne plots wie dieser hier der von snakemake mit dem kommando ausgeführt werden kann, und dieser der nochmal zeigt wann welche konfig relevant ist der mein code mit diesem kommando ausführt
	* Nen paar Fußnoten wie man Snakemake auf dem Grid laufen lässt
		* https://github.com/Snakemake-Profiles/sge
		* https://doc.ikw.uni-osnabrueck.de/content/grid-computing
		* https://snakemake.readthedocs.io/en/stable/executing/cluster.html#
	* Dass alles was rauspurzelt (plots, prints, results) custom methoden haben muss und hat um im snakemake-grid-workflow zu funktionieren - im grid läufts halt auf individuellen maschinen (mit shared storage (results)) und wird in logfiles an random positionen geschrieben (prints) und da es nicht im mainthread ist kann ich (plots) nicht rendern
	* terabytes of data on the grid storeage, rsynced for inspection
		* seafileupdown

* Very short subsection of this: Architecture of the fachbereich-classifier using sacred and my code (max 0.5 page!)


The build-system / wie du mit der pipeline umgehst
	* Allows to build everything from the env-vars (default), to build EVERY possible combination (until a specific step), to build from config-file (where you can have lists for values, and it automatically creates all files necessary for the product of these combinations, to build for a filename, ..)
	* SO, if you want to run something, you specify the parameters you want to have (using cmd-line-args, env-vars, a configfile, ... (with explicit way of resolving priorities and making sure that eg. already-used-settings are not changed lateron, ..)), and it automatically resolves which previous files it needs. Then, when loading these files in, you get a bunch of new settings from the dependencies, so again we need to resolve priorities, check for inconsistencies, etc.
		* then there are also settings (debug, randomseed) that ARE allowed to be different from now to the dependencies
	* The JsonPersister!! All outputs, all created figures, all settings (including date of their use) etc is all logged, and all intermediary files also note down which dependencies THEY needed (incl. their date of creation and commit), such that going through these files is really easy, and there is of course also a command that allows to go through these files and look at their outputs etc, and of course it's also easy to load these into jupyter (in fact, that's why we need a context that is basically the same but minimally different for click, jupyter and snakemake, as all have different requirements (click: sub-commands and cmd-args (btw, why is it practical that subcommands), jupyter: automatically and easily loading as much as possible, snakemake: config-files work differently and having to do stuff using environment-variables))
		* Configurations are only suggested, and their real value is (according to the priorities) only determined when they are needed, and that it fails if an already-used configuration should be overwritten with something different, or if a demanded config differs with what a dependency needed (though only IF it needed it), ...
			* This however differs for the jsonpersister, also there you can load all combis at once


Show that the demands are fulfilled:
	* modularity <see above>
	* scalability: 	
		* GRID
		* alles was easily auf multiple cpus scaled ist auf multiple CPUs
		* dass PPMI und auch viele andere Sachen von der größe des Datasets abhängen und exporbitant RAM verbrauchen
	* reproducibility & adapatbility: 
		* open, adaptable, ...
		* YAMLs with the exact parameter-combinations to re-create the original configs of \mainalgos
		* wie schnell es geht meinen code auf ein neues dataset zu werfen ;)
		* Automate the analysis to achieve reproducibility
		* if the analysis can be reused for other projects. In practice, this will almost never be a plain reuse, and instead requires adaptability to new circumstances, for example, being able to extend the analysis, replace or modify steps, and adjust parameter choices. Such adaptability can only be achieved if the data analysis can eas- ily be executed in a different computational environment (e.g. at a different institute or cloud environment), thus it has to be scalable and portable again
	* understandability/transparency
		* mit 2 Zeilen code kannst du dir in nem Jupyternotebook nen 3D-Plot anzeigen mit ner SVM die "Mathematik" von nicht-mathe trennt, mit gehighlighted ob "Informatik A" und "Informatik B" beeinander sind
		* `create_svm("mathematik", embedding, dcm, pp_descriptions, highlight=["Informatik A: Algorithmen", "Informatik B: Grundlagen der Software-Entwicklung"])`
		* transparency: the validity of results can only be fully assessed if the parameters, software, and custom code of each analysis step are fully accessible. Readable and well-documented code, parameters and components must be traceable
			* den plot und das show-info-command wann welche params relevant werden 
			* it is crucial that the analysis code is as readable as possible such that it can be easily modified (looking at you, 40 unnamed cmd-args!)


	reproducibility alone is not enough to sustain the hours of work that scientists invest in crafting data analyses. Here, we outlined how the interplay of automation, scalabil- ity, portability, readability, traceability, and documentation can help to reach beyond reproducibility, making data analyses adaptable and transparent.