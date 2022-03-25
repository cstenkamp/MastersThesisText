
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


# My implementation on movies & placetypes:

* Display the "closest embeddings": eg. "airplane cabin" und "aircraft cabin"
	* Is that the case for 3D as well? => is 3D any good?
* compare the results of throwing my code onto their placetypes-dataset and how my results compare to theirs 
	* Set-Overlap of candidate-terms for different #dimensions OF THEM
	* Die Performances von allen \mainalgos in ner tabelle reporten und mit meinen vergleichen, sowohl quantitativ als auch qualitativ!

result: set overlap of my extracted candidates for placetypes and theirs (und auch die big_21222.yml ergebnisse danach auswerten) (nicht nur overlap, ich kann auch verhältnis set intersect zu set union machen, und die als true/false positive/negative deklarieren und dann accuracy, f1 etc analysieren und halt anhand dessen "die hyperparam kombi die am closesten zu deren ergebnissen ist" rausbekommen)