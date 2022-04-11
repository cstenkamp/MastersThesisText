TOWRITE:


* full table wo ich tf-idf und ppmi vergleiche für einen Placetypes-case
* Noch die Results von der exact config of \cite{Derrac2015} reporten (also kein tf-idf) um zu gucken ob das auf deren niveau ist

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


* Architecture 
	* nen Dag (also von dot) mit den configs wie für desc15 in die Arbeit  (try out `--dag`, `--rulegraph` and `--filegraph`)


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
