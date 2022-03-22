	* == ARCHITECTURE left2do ==

		* Meta-workflow vorgreifen
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

				* it can easily be installed on a grid (for SLURM I refer to https://github.com/frankier/singslurm2, but as our university still uses the sun grid engine, there are `.sge` files that allow to run the snakemake-workflow there), etc etc etc!
			* 3 Ways to run:
				* 1, 2, 3, yadda yadda
				* (grid, snakemake, docker, python-package:click, python-package: jupyter)
				* Of course there's also a docker-container, so if you don't want to look at any of the code and just execute for a given dataset, you can run it on any PC with docker with the following command: [...] and for a list of all commands, it is referred to appendix xyz which lists a shitton of ways (all snakemake ones, examples of how to include a config, examples of how to look at results using the `generate-conceptualspace show-data-info` command, examples of how to look at results and intermediate results and plots in jupyterlab, ...)
			* Source-code is ofc open, available under github under this link, it is referred to the signed commit xyz
			* Reference Snakemake-Paper (and at least look a the abstract of that, they also talk about that in science you need reproducible, adaptable and transparency including definitions of what that means!)
			* FOR ALL PLOTS, reference how plots are created or general code examples with the real thing, including how what you're seeing was generated and can be reproduced

		* Foremost design principle: Modularity

				* Dass sich das ding historisch von "speziell für das dateiformat wie DESC15 veröffentlicht hat" über "speziell für siddata2022 (extract kurstypes etc)" zu "möglichst allgemein funktionierende pipeline mit guten dateiformaten und so modular wie irgendwie möglich" entwickelt hat

				-> So this way, when I run the 8th step for the pipeline from the command-line, it figures out if all dependency are there. If they are, I can execute what I want to execute, and if not, it can automatically (using the build-system) create all dependencies - but if the config I demand differs only in the third step from something that is already there, the build system automatically only executes steps 4-7.
				-> Now I have the problem of depencies, were some stuff needs to be scheduled as soon as its dependencies are there etc etc => I need a scheduler

			* Dass eine key component meiner architecture halt ist dass in zwischenschritten produzierte Dinger, egal welcher algorithmus benutzt wurde, am ende das selbe dateiformat hat damit man easy damit weiterarbeiten kann. Und sanity-checks.
			* In the development process of re-creating the algorithm of DESC15, I noticed that most of the time I'll be on hyperparameter tuning -> because of that, the highest focus for the architecture must lie on modularity and scalability - I want to be able to run a shitton of paramameter-combinations as quickly and efficiently as possible
				-> resulting architecture completely modular, and individual steps can be executed using the CLI, AND the combination of all using Snakemake, AND to load interim results 
			* Dass das SKlearn-Preprocessing ein klein wenig meine reihenfolge der steps zerstört und deswegen honestly 2x läuft
			* Der ganze Jsonpersister kram!! von wegen dass logs custom geschrieben werden und so 
			* * How I usually call it (in SIMPLE, with EXAMPLES), also von wegen ich provide einfach den pfad zu nem env-file und in dem env-file steht dann nochmal welche config er lesen soll, so ist drauf geachtet dass ich die selben settings für alle steps der pipeline hab (what wouldn't be the case if I used cmd-args), and that I can this way have fixed configs for the suggested params of eg the papers I rely on 
				* PLOTS from snakemake and also from the json-persister!

		das was in jupyternotebooks sein soll ist in jupyternotebooks... Und auch mit wie man in jedem schritt die parameter einbauen kann, schöne plots wie dieser hier der von snakemake mit dem kommando ausgeführt werden kann, und dieser der nochmal zeigt wann welche konfig relevant ist der mein code mit diesem kommando ausführt

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


		====== REST VOM SNAKEMAKE-PAPER ======: 

			* Then, Snakemake goes on recursively for the latter, until all input files of all jobs are either generated by another job or already present in the used storage
				* The file-centric description of workflows makes it intuitive to to infer dependencies between steps;

			* MODULARIZATION
			* portability: conda integration (one env per rule easy), ocntainer ingetragion 
			* traceability: all information from inputs, outputs, arguments, etc can be exported
			* scalability - supports workflow management systems and also grid engines. Snakemake’s design ensures that scaling a workflow to a spe- cific platform should only entail the modification of command line parameters. The workflow itself can remain untouched
			* Also allows graph partitioning (to reduce overhead when scheduling), caching between workflows, iteratively executing rules condidtional execution, benchmarking (logging runtime, CPU, memory etc), parameter space exploration

		============== Später dazugekommen ==============

		* the automatically generated dependency-plot and the snakemake one 
			* vor allem auch einen mit 20.000 generated files um zu demonstrieren dass dependency resolution schon komplex ist
		* erwähnen dass der snakemake-kram mittlerweile kaum overhead ist weil das auch nur 2-3 Zeilen code pro Rule hat, and that is the same as for the click-commands
		* Dass Snakemake ja auch die Anzahl Cores undso angeben kann und dass man damit ja viel Cluster-Config vorwegnimmt
		* Downsides von Snakemake, dass es halt ebennicht sowas wie CPU tatsächlich nutzt, bzw halt tatsächlich echt fucking wenig tut
		* When talking about docker, mention reproducibility again
		* deutlicher drauf eingehen dass man wegen dem ganzen bums mit intermediate files undso speziell drauf achten muss dass 
			* keine plots/prints verloren gehen
			* man mitschreibt wann welche configs genutzt werden
			* immer eindeutig drauf geachtet wird dass dependencies für genau die konfigurationen as demanded verwendet werden!! 
		* `print(ctx.display_output("embedding"))` and `show-data-info` !!
		* Dass man die configurationen fürs grid in special grid-config-files und dem snakefile festlegt 
		* MORE PLOTS!!! Snakemake-alles-auf-einmal-plot, mein dependency-plot, was-auch-immer noch geht!!
		* dass PPMI und auch viele andere Sachen von der größe des Datasets abhängen und exporbitant RAM verbrauchen



=======================================================================================================================
========================================================= OLD =========================================================
=======================================================================================================================

In this section, I will outline the architecture that was developed in order to achieve the aforementioned results. Getting this architecture right was subject to a lot of trial-and-error and the end-result may look quite cumbersome, but [yadda yadda it needed to be done because of the size of the datasets and resulting runtime, and that I need to run it for many parameter-combinations but many intermediate resuls are shared, which leads to a much shorter runtime overall etc etc]

* In the development process of re-creating the algorithm of DESC15, I noticed that most of the time I'll be on hyperparameter tuning -> because of that, the highest focus for the architecture must lie on modularity and scalability - I want to be able to run a shitton of paramameter-combinations as quickly and efficiently as possible

* One of the main goals of this thesis was to create a better architecture than the shit that was available from the papers I tried to re-do here (DESC15 didn't have any code, one of the others has a link to the repo but it's empty, the last one has >40 unnamed command-line-args!), and I think that was successful: This codebase contains everything and finally fulfills code-standards! It is a proper python-package (that you can run with `python -m derive_conceptualspace`), there is a working Docker-container that can be installed with one command and run on any VM even in a thousand years (fixed dependencies etc, reference a reproducibility paper!), it has workflow-management tools (reference snakemake), it can easily be installed on a grid (for SLURM I refer to https://github.com/frankier/singslurm2, but as our university still uses the sun grid engine, there are `.sge` files that allow to run the snakemake-workflow there), etc etc etc!
* Wie toll das ganze ist dass ich halt mit snakemake zig parameter-kombinationen auf dem cluster ausführen kann und mir dann mit `generate-conceptualspace show-data-info` die dabei generierten outputs (like the metrics for the clusters) angucken kann, und wenn mir die gefallen öffne ich den ganzen kram ebenfalls nochmal in nem jupyter-notebook (wo ich dank config-hash fix erkenne obs die selbe config ist), um mir dort dann bspw die überschneidungen der configs anzuschauen, haach dieser workflow

* I have MANY different parameters & param-combinations that I need to try out
* The pipeline is divisible into distinct steps
* As I often need to try different settings where only at the 8th step the relevant config is different, generating temporary files makes sense, such that I can run the stuff only once up until the 7th step and twice only for the step where it's necessary
* So this way, when I run the 8th step for the pipeline from the command-line, it figures out if all dependency are there. If they are, I can execute what I want to execute, and if not, it can automatically (using the build-system) create all dependencies - but if the config I demand differs only in the third step from something that is already there, the build system automatically only executes steps 4-7.
	* General stuff about snakemake, that the main thing about is is automatic dependency resolvement (which means I can just tell it "hey I need this file" and it creates it, which is good if I need to automatically create dependencies if I want to run step 8 with certain settings), and that it's great if you want to run multiple things at once with optimal usage of CPU/RAM and also very nice for cluster execution
		* speaking of cluster execution: Of course there's also a docker-container, so if you don't want to look at any of the code and just execute for a given dataset, you can run it on any PC with docker with the following command: [...] and for a list of all commands, it is referred to appendix xyz which lists a shitton of ways (all snakemake ones, examples of how to include a config, examples of how to look at results using the `generate-conceptualspace show-data-info` command, examples of how to look at results and intermediate results and plots in jupyterlab, ...)
	* ...but that you have to abuse it a lot to get where I want it to be (have rules that don't rely on files in the same file with rules that do, no good way to debug, apparently small community (no SO answers etc (mit quelle wie viele Fragen es gibt!!!)), the fact that I need nondynamic filenames that are set from the start of the execution)
* The build-system. Allows to build everything from the env-vars (default), to build EVERY possible combination (until a specific step), to build from config-file (where you can have lists for values, and it automatically creates all files necessary for the product of these combinations, to build for a filename, ..)

* SO, if you want to run something, you specify the parameters you want to have (using cmd-line-args, env-vars, a configfile, ... (with explicit way of resolving priorities and making sure that eg. already-used-settings are not changed lateron, ..)), and it automatically resolves which previous files it needs. Then, when loading these files in, you get a bunch of new settings from the dependencies, so again we need to resolve priorities, check for inconsistencies, etc.
	* then there are also settings (debug, randomseed) that ARE allowed to be different from now to the dependencies

* The JsonPersister!! All outputs, all created figures, all settings (including date of their use) etc is all logged, and all intermediary files also note down which dependencies THEY needed (incl. their date of creation and commit), such that going through these files is really easy, and there is of course also a command that allows to go through these files and look at their outputs etc, and of course it's also easy to load these into jupyter (in fact, that's why we need a context that is basically the same but minimally different for click, jupyter and snakemake, as all have different requirements (click: sub-commands and cmd-args (btw, why is it practical that subcommands), jupyter: automatically and easily loading as much as possible, snakemake: config-files work differently and having to do stuff using environment-variables))
* That configurations are only suggested, and their real value is (according to the priorities) only determined when they are needed, and that it fails if an already-used configuration should be overwritten with something different, or if a demanded config differs with what a dependency needed (though only IF it needed it), ...
* How I usually call it (in SIMPLE, with EXAMPLES), also von wegen ich provide einfach den pfad zu nem env-file und in dem env-file steht dann nochmal welche config er lesen soll, so ist drauf geachtet dass ich die selben settings für alle steps der pipeline hab (what wouldn't be the case if I used cmd-args), and that I can this way have fixed configs for the suggested params of eg the papers I rely on 
* PLOTS from snakemake and also from the json-persister!

* Very short subsection of this: Architecture of the fachbereich-classifier using sacred and my code (max 1/2 page!)

=======================================================================================================================
========================================================= NEW =========================================================
=======================================================================================================================


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
				* Scheduling: Because of their dependencies, not all jobs in a workflow can be executed at the same time. Instead, one can imagine partitioning the DAG of jobs into three sections: those that are already finished, those that have already been sched- uled but are not finished yet, and those that have not yet been scheduled (Figure 4a). Let us call the jobs in the latter partition Jo , the set of open jobs. Within Jo , all jobs that have only incom- ing edges from the partition of finished jobs (or no incom- ing edge at all) can be scheduled next. We call this the set J of pending jobs. The scheduling problem a workflow manager like Snakemake has to solve is to select the subset E $\subseteq$ J that leads to an efficient execution of the workflow, while not exceed- ing the given resources like hard drive space, I/O capacity and CPU cores.
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






=======================================================================================================================
===================================================== FROM NOTION =====================================================
=======================================================================================================================










## Combination of Click, Snakemake and my custom JsonPersistor

see https://www.notion.so/c554dae1bb624239bca5bf98faefbbd7?v=05730d22f67142f7b98647466c6ac21e&p=788221252c0a44cbaadb7cba90d5a74f


bei architecture darüber schreiben wie schön ich das mit click, dem json_persister und snakemake gemacht hab (auf jeden Fall nen Snakemake DAG als Grafik rein, und demonstrieren wie im json_persister die dependencied der jeweiligen file schön stehen ("pp_descriptions" wird gebraucht für x, y, z, blablalba)), und ab-wo welche params relevant sind

Reasons:

- Need to try out many many combinations of parameters (→ grid search, possible to run on clusters or HPCs)
- Different subcomponents have different arguments that are merged lateron (like the candidate-term-extraction-method)
- The inividual steps take hours on their own

Features:

- Keeping track of dependencies

    [Dependency-plot from me was here]

<!-- ![generated with command `generate-conceptualspace show-data-info`](Architecture-image) -->

generated with command `generate-conceptualspace show-data-info`

- Snakemake can now be called in a bunch of ways
    - Normal Snakemake-way which allows to specify one explicit out-file
        - *`snakemake --cores 1 -p --directory $MA_DATA_DIR tcsldp_translate/ppmi_3d/pp_keybert_count/clusters.json`*
    - Running `default` or `all`:
        - *`snakemake --cores 1 -p --directory $MA_DATA_DIR default`*
        - *`snakemake --cores 1 -p --directory $MA_DATA_DIR all`*
    - Using arguments to run with demanded settings:
        - *`(export $(cat $MA_ENV_FILE | xargs) && snakemake --cores 1 -p --directory $MA_DATA_DIR default)`*
        - *`MA_EMBED_ALGO=mds snakemake --cores 1 -p --directory $MA_DATA_DIR default`*
- Running all combinations:

    [Hier war ein Snakemake-DAG wie der ALLES gleichzeitig erzeugt]

<!-- ![Created with command `snakemake --cores 1 -np --dag | grep -A99999 "digraph" | dot -Tsvg > dag.svg``](dag-export from snakemake) -->

Created with command `snakemake --cores 1 -np --dag | grep -A99999 "digraph" | dot -Tsvg > dag.svg``

- Die Workflows mit der Architektur! Ich möchte mir ein Zwischenergebnis anschauen? Ich kann das `generate-conceptualspace show-data-info` ausführen, das zeigt mir obige plots, erlaubt mir alte prints sämtlicher Schritte anzuschauen (TODO: sogar die Graphen wiederherzustellen), etc
- Dank JsonSerializer kann ich das ebenfalls leicht in jupyter notebooks einlesen und anschauen, dinge wie `show_info()`nochmal auszuführen... (bspw `analyze_pipeline_results.ipynb`)
- Snakemake um 2400 Parameterkombinationen auf einem Cluster auszuführen, um sämtliche dependencies von einem gerade angescahutem/debuggtem Teil des codes zu autogenerieren (TODO und dann auch das flag dafür), etc
- Dass ich halt mit command-line-args, aber auch mit environment variables arbeiten kann, und dass das mir erlaubt halt für 2 verschiedene datasets easy einfach 2 verschiedene envfiles haben kann, fertig.

Other things how to use the code

- warum man get_setting nutzen muss (weil es dann entweder von envvar oder von default geladen wird, yadda yadda)

Sinn des JSONPersisters:

- forwards all metadata from a loaded json to a saved json (jsonload und jsonstore sind Objekte, man gibt beim speichern an was davon meta-info ist, und alle in einer session geladenen meta-infos werden automatisch gespeichert), und bei anderen infos wie dem git-commmit der jeweils geladenen wir das auch alles gechained, sodass ich bis back zu den übersetzungen weiß was der jew. commit der komponenten war. Die einzelnen steps der pipeline haben dann irgendwo gespeichert haben wovon sie abhängen (#dims, quant_meas, ...)
- Wird die MESS los dass ich im ersten Schritt (pp_descriptions) schon die translate_policy breauche und dann bis zum Ende durschschleifen muss obwohl ich sie für die späteren files nicht mehr brauche → dependency-structure in den zwischen-files.
- warum überhaupt zwischenfiles? Weil ich ja teilweise nur im letzten schritt was anders mache
- Macht ne Ordner-Struktur und filename anhand von relevant attributes (notwending für snakemake)
- Auch über Snakemake hinweg, obwohl man mehrere Dinge gleichzeitig laufen lässt (btw ein nice feature of snakemake, ich hab durchgehend maximale auslastung da das dependency resolution davon gemacht wird), hab ich dennoch die möglichkeit ganz linear die generierten loggings etc anzuscahuen

## FB-Classifier

- auch die special sachen wie dass der fb-classifier checkpointing so macht dass man die #epochs später erhöhen kann und er einfach weitertrainiert etc



TODO: noch nen komplettes job stats von snakemake in die architecture section, 
(I mean this:
Job stats:
job                     count    min threads    max threads
--------------------  -------  -------------  -------------
by_config                   1              1              1
cluster_candidates        108              1              1
create_candidate_svm       35              4              4
create_dissim_mat           1              3              3
create_embedding            3              3              3
total                     148              1              4
)



TODO: feier ich genug wie effizient ich das grid nutze und was für ein achievement das ist (..wenn auch ursprünglich nicht geplant) ?! Like man führt ein kommando aus (`MA_ENV_FILE=siddata.env submit -kwr by_config --configfile config/derrac2015_edited.yml --keep-going`), gibt nen config-file mit ner shitton an param-kombis an und es wird auf 60 Maschinen parallelisiert! NO custom .sge-script schreiben at all etc etc!! grid is SOLVED, it's a tamed tool! Kein tmux nötig um auf dem server zu bleiben, er gibt dir fucking telegram-messages wenn er fertig ist, es ist 100% worry-free! neue code-version fertig, mit egal was für neuen parameters? the pipeline got you
das sind halt gigabyteweise große files, es wird immer schön mitgeschrieben wie lange die einzelnen runtimes der interruptible prozesse waren, and again, 1 command!! no change of your stupid sge-scripts
..und dann zeigt check einem halt alle jobs an und wenn man in nen einzelnen reingucken will macht man `check -j jobnum` MORE OF THAT
...und überhaupt dann dass man ja die dateistruktur angeben kann und er alles entsprechend erzeugt, auch easy für neue datasets... halloooo
...und dass ich meine Struktur halt von sehr früh an daran angepasst hab wie snakemake sie haben will ebendamit das gut auf dem grid klappt
...and again, wie man configs angibt
