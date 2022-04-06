<!-- Hier: was KOMMT RAUS bei den Sachen die mich interessieren (NUR BESCHREIBEN!nicht drüber reden ob und warum das mit den decisiontrees sinnvoll ist, und erst in der discussion darauf zurückkommen OB das sinnvoll ist -->
<!-- See the stuff from DO_IF_TIME!! -->


<!-- TODO: add parts of the "How to Evaluate" section back (currently comments in text)-->


Erstmal sanity-check "mein algorithmus performt wie die paper, -> reasonable dass richtig", DANN analyse im hinblich auf die fachbereiche, and interpreting the results in discussion.

PLOTS HERE	
* Plots/Tables mit set-overlaps von meinen placetypes zu deren
* Die in den Zwischenschritten rauspurzelnden Sachen, wie "entities with close embeddings"
* Nen Plot der closeness im embedding mit levensthein-distanz und anzahl-gleicher-wörter korreliert und schaut wie explainable das ist

* TODO: mehr qualitative stuff rein
	* Which are the most frequent phrases (done in Untitled.ipynb)
	* 


### Implementation correct?

* Is my implementation ok
	* throw onto placetypes:
		* Display the "closest embeddings": eg. "airplane cabin" und "aircraft cabin"
			* Is that the case for 3D as well? => is 3D any good?
		* Set-Overlap of candidate-terms for different #dimensions OF THEM

	* result: set overlap of my extracted candidates for placetypes and theirs (und auch die big_21222.yml ergebnisse danach auswerten) (nicht nur overlap, ich kann auch verhältnis set intersect zu set union machen, und die als true/false positive/negative deklarieren und dann accuracy, f1 etc analysieren und halt anhand dessen "die hyperparam kombi die am closesten zu deren ergebnissen ist" rausbekommen)
		* `from derive_conceptualspace.load_data.load_semanticspaces import get_all_goodkappa`
	* gucken ob die clustercenters ("nature", ..) von denen auch bei mir gut sind für placetypes => AND THEN ALSO FIGURE OUT THE DATA FOR THE TABLE FOR PLACETYPES

	* TODO: Add table: ALL hyperparams I had for placetypes
	* full table wo ich tf-idf und ppmi vergleiche für einen Placetypes-case um später den case zu machen dass tf-idf besser ist



### Methodik auf Domäne?

* ...		
	* DDC
		* decision-trees for that (`notebooks/analyze_results/siddata/decisiontrees_bestconfig.ipynb`)
		* TODO: schaff ich's level 2 davon auch zu machen wie \cite{Alshaikh2020}?



* Is the produced embedding (which is necessarily a loss of information) still adequate?
	* Can we recover courses from the detected direcitons?
		* for that, we train unbounded decision trees without a train/test-split and check if the prediction can recover
		* "Ein anderer Weg zum testen wäre auch ein classifier der nur anhand der most salient generated features versucht den kurs wiederherzustellen (das zeigt natürlich nicht ob es similar to how humans do it but part of it) -> recover_course_from_embeds.ipynb"
	* compare accuracies: 3D-embedding of us with standard 3D-embedding
		( \ref{fig:boxes_rechtswis} vs \ref{fig:mds_3d_hyperplane} )
	* check if courses can be recovered 
		(TODO: table from `recover_course_from_embeds` results)
			* btw diese table auch shcreiben dass "der space nicht genug ausgefüllt ist", course of dimensionality, in 3D ist like 80% des unitcubevolumens im unitball, im 200D nur like 0.00001%

* confusion matrix?!


#### What we wanted to look at in the Qualitative Analysis

* doc-cand-matrix
	* the term-frequencies for terms that I WOULD LIKE are really low
		`for term in ["computer", "mathe", "mathematik", "wissenschaft"]: print(f"TF of `{term}`: {filtered_dcm.term_freq(term, relative=True):.2%}")`: 1.0%, 0%, 0.8%, 3.3%
	* the `Untitled.ipynb` notebook does that already!

* embedding & dissim-mat
	* 3D-Embedding & t-SNE on (veryveryhigh-dim) dissim-mat, colored by Fachbereich 
		* shows that, at least regarding this feature, okay-ish
		* TODO: show one of Placetypes and compare!!!
	* Show 10 courses that are close according to the embedding and manually look if they are similar
		* Look at courses that I KNOW to be similar and check if their embedding is close (eg Language Courses, Mathe für Anwender 1 & 2, Info A & B)
* Final Embeddings	
	* Is there a direction for "more advanced course"? 
	* Language Courses, Mathe für Anwender 1 & 2, Info A & B

* Das wie gerade auch in der duplicate-per-combi-of-ndims-and-ncats sichtbar wird dass letztlich halt "kurs 123" und "!!FÄLLT AUS!! kurs 123" auf den selben fallen, was zwar quantiativ scheiße ist aber ACTUALLY GOOD (das ist aber granulare interpretation, das eher in discussion. "nen paar sachen kann man einfacher diskutieren als umfassend data-driven machen")

* Für die Fälle wo verschiedene parameter-configurationen verschiedene Ergebnisse haben und ich nciht verhindern kann dass ich an verschiedenen stellen der results section verschiedene Dinge Zeige.... Kann ich einfach mal am Anfang exemplarisch zeigen dass alle diese Begriffe aber nah beieinander liegen und das daher valide ist


### Now that we have established that we have reason to assume that our algorithm is good, what does it say about the dataset?

(-> mention in discussion! examples where I detect duplicates etc)


### Best Parameters?


* Highest-ranking descriptions per dimension: \ref{fig:text_per_dim}. We see that using the respectively best-fitting DOCUMENT (without LSI or anything, just the one with the highest ranking!)  is often even the MUCH BETTER direction!!! 


* reclassify-algorithm better than desc15-one (\ref{tab:text_per_dim})
	* NUR ZEIGEN!! ERST IN DER DISCUSSION SAGEN DASS ICHS BESSER FINDE
	* weiteres line of reasoning hier: wäre-das-nicht-sogar-ein-guter-candidate-für-die-direction-name?


