
Maximum occurrences:
`term_doc_matrix.index[np.unravel_index(term_doc_matrix.to_numpy().argmax(), term_doc_matrix.to_numpy().shape)[0]], term_doc_matrix.columns[np.unravel_index(term_doc_matrix.to_numpy().argmax(), term_doc_matrix.to_numpy().shape)[1]]`

→ 'Information Systems (Wirtschaftsinformatik) M III: IT-Risikomanagement (Übung)' und 'risk'


* Brauch ich mehr/bessere Daten? Wenn ich nur die 1000 mit den längsten Beschreibungen behalten würde und dann 10 solcher subsets hätte wären halt die Fälle wie "Tutoren sind: Susi Sorglos Willi Wacker" etc raus



* The original papers of course came up with some tricks: What we can do is EXPLAINABLE CLASSIFIERS
	* little detail how Derrac2015 did that
		* \cite{Derrac2015} evaluated using a bunch of commonsense reasoning based classifiers (want to show that at least as performant than standard approaches, but can give intuitive explanations) (these reasoning-classifiers can be linked to intuitive explanations: 1-NN is "Y is of the same class as X because X closest to Y", but also more complex ones.) 
		* DESC15 "evaluate the practical usefulness of the considered semantic relations" by checking "their use in commonsense reasoning based classifiers", like interpolation and a fortiori inference (chap 5)
		* Section 6.1: Evaluate whether the derived relations are sufficiently accurate for classification, and 6.2 is then comparison with crowdsourcing experiments (more subjective aspects, the question “are the relations useful explanations?”)
	* Explain the idea behind the shallow decision-trees
		* decision tree based on their features, check if it can classify a held out test dataset
		* "To evaluate whether the discovered features are semantically meaningful, we test how similar they are to natural categories, by training depth-1 decision trees"
		* My Argumentation that the way Ager & Alshaikh report their accuracies it must be the case that they did that per class (see also Slack with Johannes!)
	* Ein anderer Weg zum testen wäre auch ein classifier der nur anhand der most salient generated features versucht den kurs wiederherzustellen (das zeigt natürlich nicht ob es similar to how humans do it but part of it)

* A result is certainly a thing like the movie-tuner! Can I implement that thing quickly?? If yes, that's a separate section!


# Results regarding the Goals for the architecture 

<!-- Eine meiner 2 research questions ja war "wie sieht eine gute architecture aus", so if the architecture is good and how it (and thus a good architecture) looks are results!! -->


We remember, we also wanted to build a good architecture and set goals for that, such as adaptability to new datasets etc.
We said a good architecture would show in adaptability, scability, ..., so we wanna show that these are achieved. 
More basic than that, we want to show that 

* this implementation works
* the results of \mainalgos are not a fluke (that the algorithm works at all)

For those two points lemme present my results for placetypes


## My implementation on movies & placetypes:

* Display the "closest embeddings": eg. "airplane cabin" und "aircraft cabin"
	* Is that the case for 3D as well? => is 3D any good?
* compare the results of throwing my code onto their placetypes-dataset and how my results compare to theirs 
	* Set-Overlap of candidate-terms for different #dimensions OF THEM
	* Die Performances von allen \mainalgos in ner tabelle reporten und mit meinen vergleichen, sowohl quantitativ als auch qualitativ!

result: set overlap of my extracted candidates for placetypes and theirs (und auch die big_21222.yml ergebnisse danach auswerten) (nicht nur overlap, ich kann auch verhältnis set intersect zu set union machen, und die als true/false positive/negative deklarieren und dann accuracy, f1 etc analysieren und halt anhand dessen "die hyperparam kombi die am closesten zu deren ergebnissen ist" rausbekommen)

## Results in terms of architecture quality

* We are scalable and can run massively parallel (that you'll have to believe me, it's one command to run on the grid and I would say that's pretty noice).
* Keep in mind when reading the other sections of the results that all plots and tables you'll see are explictly linked and easily re-creatable and runnable
* We ran the stuff on other datasets\footnote{See Table with datasets and the respective notebooks and the quick datasets section} and it ran through, so we're adaptable.
