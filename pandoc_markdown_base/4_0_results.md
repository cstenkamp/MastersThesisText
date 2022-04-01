<!-- Hier: was KOMMT RAUS bei den Sachen die mich interessieren (NUR BESCHREIBEN!nicht drüber reden ob und warum das mit den decisiontrees sinnvoll ist, und erst in der discussion darauf zurückkommen OB das sinnvoll ist -->
<!-- See the stuff from DO_IF_TIME!! -->

Erstmal sanity-check "mein algorithmus performt wie die paper, -> reasonable dass richtig", DANN analyse im hinblich auf die fachbereiche, and interpreting the results in discussion.

### Implementation correct?

* Is my implementation ok
	* throw onto placetypes: \ref{tab:places_results}
		* Display the "closest embeddings": eg. "airplane cabin" und "aircraft cabin"
			* Is that the case for 3D as well? => is 3D any good?
		* compare the results of throwing my code onto their placetypes-dataset and how my results compare to theirs 
			* Set-Overlap of candidate-terms for different #dimensions OF THEM
			* Die Performances von allen \mainalgos in ner tabelle reporten und mit meinen vergleichen, sowohl quantitativ als auch qualitativ!
	* result: set overlap of my extracted candidates for placetypes and theirs (und auch die big_21222.yml ergebnisse danach auswerten) (nicht nur overlap, ich kann auch verhältnis set intersect zu set union machen, und die als true/false positive/negative deklarieren und dann accuracy, f1 etc analysieren und halt anhand dessen "die hyperparam kombi die am closesten zu deren ergebnissen ist" rausbekommen)


### Dataset comparisons (is our dataset worse?)

* Can we produce the same number of features etc than Derrac2015
	* \ref{tab:generated_stuff}

### Methodik auf Domäne?

* Is it reasonable to assume that stuff like faculty CAN be extracted?
	* look at clusterings \ref{fig:scatter_mds}
	* look at 3D-hyperplane \ref{fig:mds_3d_hyperplane}
	* results of FB-Classifier
		* Ich hab ja den Fachbereichs-Classifier gemacht, wenn ich jetzt noch die shallow decision trees mache kann ich ja legit accuracies vergleichen !!
			* To see if it is possible to extract any kind of structured data from the unstructured course descriptions, a Neural Network classifier was trained on the dataset, classifying courses to the faculty they run under. $\rightarrow$ Der FB-Classifier kommt auf $95.33\%$ train, $90.96\%$ Test accuracy nach 10 epochs, that's a lot!!
			==> CORRECTION: auf Siddata2022 kommt er auf $85.19\%$ test, $94.13\%$ train, siehe \todoparagraph{link to notebook}
			* kommt accuracy etc von den shallow decision trees für fachbereich close an die vom fb-classifier?
* Are human categories predictable from our extracted directions?
	* decision tree performance
		* Do the extracted directions look any good if so (QUALITATIVE)
		  -> \ref{fig:dims_for_fb}
    	* How does a machine classification look
		  -> \ref{fig:boxes_rechtswis}	  
* Is the produced embedding (which is necessarily a loss of information) still adequate?
	* compare accuracies: 3D-embedding of us with standard 3D-embedding
		( \ref{fig:boxes_rechtswis} vs \ref{fig:mds_3d_hyperplane} )
	* check if courses can be recovered 
		(TODO: table from `recover_course_from_embeds` results)

#### What we wanted to look at in the Qualitative Analysis

* \ref{fig:3dplot_mathe_infoab}
	* In \autoref{fig:3dplot_mathe_infoab} we see a 3D-Embedding for courses, splitting courses which contain the term "mathematics" from those that don't, also hightlighting the terms "Informatik A" and "Informatik B". We see they are close we see the SVM is not to bad, and even though neiher Info A nor Info B contains the word "mathematik", thy are both on the "mathematical side" of courses. Negative samples are hidden for better visibility, and entities that contain the word more-often-than-the 75th (???) percentile have bigger markers.
* doc-cand-matrix
	* the term-frequencies for terms that I WOULD LIKE are really low
		`for term in ["computer", "mathe", "mathematik", "wissenschaft"]: print(f"TF of `{term}`: {filtered_dcm.term_freq(term, relative=True):.2%}")`: 1.0%, 0%, 0.8%, 3.3%
	* the `Untitled.ipynb` notebook does that already!
* embedding & dissim-mat
	* 3D-Embedding & t-SNE on (veryveryhigh-dim) dissim-mat, colored by Fachbereich 
		* shows that, at least regarding this feature, okay-ish
		* TODO: show one of Placetypes and compare!!!
	* Show 10 courses that are close according to the embedding and manually look if they are similar
		* Look at courses that I KNOW to be similar and check if their embedding is close
			* Language Courses, Mathe für Anwender 1 & 2, Info A & B
* Final Embeddings	
	* Is there a direction for "more advanced course"? 
	* Language Courses, Mathe für Anwender 1 & 2, Info A & B


### Now that we have established that we have reason to assume that our algorithm is good, what does it say about the dataset?



### Best Parameters?


* Highest-ranking descriptions per dimension: \ref{fig:text_per_dim}. We see that using the respectively best-fitting DOCUMENT (without LSI or anything, just the one with the highest ranking!)  is often even the MUCH BETTER direction!!! 
* What leads to the highest number of good-kappas?
	* \todoparagraph{As described in} \autoref{sec:workflow}, a good first approximation is to check how many candidate-terms we get. \autoref{tab:kappa_table} shows the results of many runs with different parameter-combinations with the purpose of figuring out which combination of parameters and kappa-metrics lead to enough candidate-terms (\todoparagraph{Also ref the figure of workflow where I check what threshold was realistic})
	* \ref{tab:cands_per_config}
* What is the BEST CONFIG?
	* TODO: !!!