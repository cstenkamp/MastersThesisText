* The fact that I don't use intercepts of the decision_planes in derive_conceptualspace.semantic_directions.create_candidate_svm.select_salient_terms (dass ich beim ganzen koordinatensystem-schieben den intercept ignoriere!)
* Anhand von set-overlapts von meinen placetypes zu deren "die hyperparam kombi die am closesten zu deren ergebnissen ist" sagen können
* dass sie, wenn sie die orthogonalen der decision-planes averagen, definitiv auch den intercept berücksichtigen müssten!
        (...would they? I mean they are only concerned with direction and ranking, so there it's just an added, irrelevant, constant)
* Check my claim in the results for placetypes (chapter 6.1), that the classification based on word embeddings may even be better than their SVM_MDS


* In his chapter "Computational Aspects" gärdenfors says:
even ANNs, concretely Kohonen's Self-organizing maps \cite{Kohonen1997}, which automatically reduce the representational complexity of the input while preserving similarities (of beliebiger distance function) among the different input vectors by mapping input vectors with common featurs to \textit{neighboring} neurons in the output map, thus preserving topological relations while making it lower-dimensional.

* TABELLE which parameter-combis were USED, with optimal ones MARKED for \mainalgos (-> also into yaml!)



* Old one
    * Levensthein-distance-comparison!
		* Nen Plot der closeness im embedding mit levensthein-distanz und anzahl-gleicher-wörter korreliert und schaut wie explainable das ist
		* in results schon schreiben (und tabellen haben!) wie schön nah sich ähnliche dinge schon in BoW-embedding und dimreduced-embedding sind. Neben den ganzen ["asd (tutorial 1)", "asd (tutorial 2)"] auch welche mit ner mindest-levensthein-distance haben, UND nen Plot wie sehr levensthein-distance und nähe im embedding korellieren. UND ne tabelle wie ähnlich nahe-kurse im BoW-embedding und im dimreduced-embedding sind möglicherweise einfach nen kappa score um das ranking der ähnlichsten zu vergleichen
	* Generate new Occurences-per-Keyphrases plot
		* the `Untitled.ipynb` notebook does that already!
	* Die Decision-Trees für DDC sind auch ziemlich pretty
	* Für ALLE configs die level-1-decisiontrees machen und die terms des jeweils-entscheidenen-clusters collecten
	* have one analysis-file that shows why kappa_weights=None is bad (and make example for how these kinds of files will look, at beste even with the command to snakemake/schedule them), and then write with these plots about how my workflow of guessing parameters works.
	* Quantitative analysis result: set overlap of my extracted candidates for placetypes and theirs (und auch die big_21222.yml ergebnisse danach auswerten) (nicht nur overlap, ich kann auch verhältnis set intersect zu set union machen, und die als true/false positive/negative deklarieren und dann accuracy, f1 etc analysieren und halt anhand dessen "die hyperparam kombi die am closesten zu deren ergebnissen ist" rausbekommen)
		* `from derive_conceptualspace.load_data.load_semanticspaces import get_all_goodkappa`

