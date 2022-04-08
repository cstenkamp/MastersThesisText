TOWRITE:


* argumentieren
  * doc2vec nicht implementiert weil schlechter bei ager.
  * Finetuning nicht drin weil nur marginal besser bei ager (ref tabelle im anhang)
  * ...ähnliche gründe für alshaikh finden

* As established, a very important difference is that more relevant words do not occur more often. we assumed before that because of that, the kappas that compare rankings are not so good. WELL IS THAT THE CASE


* full table wo ich tf-idf und ppmi vergleiche für einen Placetypes-case
* Noch die Results von der exact config of \cite{Derrac2015} reporten (also kein tf-idf) um zu gucken ob das auf deren niveau ist


* Regarding "Dass ich immer die beste config genommen hab aber durchgehend neue generiere, weswegen viele plots inkompatibel (zeigen andere semantic directions und andere werte für accuracy undso) sind aber alle zeigen halt nice sachen":
  * erstmal wenn ich die cosine distance von "stadtgeographie" und "tourismus"  oder "psychologie" und "gehirn" anschaue sind die extremely nah
  * Die highlights die ich präsentier sind von verschiedenen params und blablabla
  * One thing is important: The NAME itself is irrelevant for the classification performances!! Only the direction is relevant
    * bei den namen ist nur die human-interpretability aus, und die tatsache dass verschiedene aber sinnvolle rauskommen ist eher ein feature als ein bug
  ==> am anfang klarstellen 

  ==> That's actually another result!! Fucking hell, das problem was ich mit derrac hatte ist ja dass die so unglaublich unrobust waren und fast maximal viele verschiedene rauskamen
    * Bei den placetypes-results noch den punkt dabei schreiben dass die so verschieden sind
    * bei mir halt einfach für die verschiedenen configs laufen lassen, die resulting direction clustern und counten wie viele verschiedene terms vorkommen (gehirn vs psyhologie), ob einige besonders oft rauskommen und wi nah (cosine) die sind -> ROBUSTNESS ASSESEN

  * Bei allen plots & tables dabeischreiben ob sie aus ner speziellen oder best-on-avarage kamen

======================================


* Überall
	* ...I USED DOC-FREQ RIGHT ALL ALONG!!! FUCK
	* fig:3d_hyperplane_ortho nicht als screenshot, sondern als svg drin haben, exported from notebook
	* Die Parameter von [AGKS18] und [RaZb20] sowohl in die Tabelle als auch ins yaml packen
	* Die yamls für  [AGKS18] und [RaZb20] machen
	* die ganzen alten jupyternotebooks die ich gemacht hab wieder aufpeppeln und ähnliche Sachen machen (die proof-of-concept ones!!)
	* FIND MORE "FOLLOWUP-PAPERS" and sources that cited them!!!
	
* Datasets
	* Allgemein
		* Update die table mit den wörter-die-soundso-oft-vorkommen to reflect nicht term-freq sondern n-docs-containing-it
	* Siddata
		* Histogram über das Dataset mit Anzahl Wörtern, Anzahl Zeichen, Anzahl Wörter Beschreibung allein, ...
        * Average-Description-Length pro eigenschaft in metadata-table
	* Placetypes
		* Datasets-Tabelle mit den key feature sizes für placetypes vervollständigen	

* Algorithm
	* TABELLE which parameter-combis were USED, with optimal ones MARKED for \mainalgos (-> 
	also into yaml!)
	* neuer plot "wann ist ein induziertes ranking faithful pos/neg example" (grafische Darstellung von "if the ranking induced by the SVM corresponds to the count/PPMI, we see it as faithful measure", also ein beispiel wo's passt und ein Beispiel wo's nicht passt)

	* reference yamls again
	* überall links zu binder!!
	* didn't somebody say that cohen's kappa sucks!?!
	* I may have up to FOUR SECTIONS with the same content
		* Algorithm. Short & Nothing Superflous
		* Implementation Details
		* What-Configs-Are-Available-Where (TABLE??)
		* What-other-things-one-could-have-done-thereandthere

* Architecture 
	* nen Dag (also von dot) mit den configs wie für desc15 in die Arbeit  (try out `--dag`, `--rulegraph` and `--filegraph`)

* Results
	* tab:generated_stuff ist noch nicht complete
	* Find the top-ranked objects for some of the features
    * Levensthein-distance-comparison!
		* Nen Plot der closeness im embedding mit levensthein-distanz und anzahl-gleicher-wörter korreliert und schaut wie explainable das ist
		* in results schon schreiben (und tabellen haben!) wie schön nah sich ähnliche dinge schon in BoW-embedding und dimreduced-embedding sind. Neben den ganzen ["asd (tutorial 1)", "asd (tutorial 2)"] auch welche mit ner mindest-levensthein-distance haben, UND nen Plot wie sehr levensthein-distance und nähe im embedding korellieren. UND ne tabelle wie ähnlich nahe-kurse im BoW-embedding und im dimreduced-embedding sind möglicherweise einfach nen kappa score um das ranking der ähnlichsten zu vergleichen
	* Generate new Occurences-per-Keyphrases plot
		* the `Untitled.ipynb` notebook does that already!
	* Die Decision-Trees für DDC sind auch ziemlich pretty
	* Für ALLE configs die level-1-decisiontrees machen und die terms des jeweils-entscheidenen-clusters collecten
	* Well, WHAT IS THE BEST CONFIG
	* have one analysis-file that shows why kappa_weights=None is bad (and make example for how these kinds of files will look, at beste even with the command to snakemake/schedule them), and then write with these plots about how my workflow of guessing parameters works.
	* Quantitative analysis result: set overlap of my extracted candidates for placetypes and theirs (und auch die big_21222.yml ergebnisse danach auswerten) (nicht nur overlap, ich kann auch verhältnis set intersect zu set union machen, und die als true/false positive/negative deklarieren und dann accuracy, f1 etc analysieren und halt anhand dessen "die hyperparam kombi die am closesten zu deren ergebnissen ist" rausbekommen)
		* `from derive_conceptualspace.load_data.load_semanticspaces import get_all_goodkappa`

	* I don't care for duplicates yet!!
	* TODO: die BESTE Parameter-kombi dafür rausfinden
	* TODO: für ALLE configs die level-1-decisiontrees machen und die terms des jeweils-entscheidenen-clusters collecten
	* TODO: movietuner


* Appendix
	* Algorithm-als-Sourcecode besser machen



* Coderepo - Dokumentation
	* Was für env-vars bare minimum sind (ich glaube at least die MA_SELECT_ENV_FILE)
	* Nochmal drauf achten dass die installation instructions für sämtliche arten (grid, snakemake, docker, python-package:click, python-package: jupyter) auch auf frischen sysetmen klappen
	* WAS IST ANGEBLICH DOKUMENTIERT
		* How to setup
			* docker
			* running on grid
			* install package
		* the grid-repo !!
		* bare metal stuff in the main repo
			* what kinds of analyses exist
			* how to create and load a config-file
			* how to load something in jupyter for inspection
