

## What else can we look at/test? 

* Neben den Clustern die ich mir anzeigen lassen kann und qualitativ analysieren kann, kann ich mir auch die distances to the origins of the respective dimensions (induced by the clusters), what induces the respective rankings! (see DESC15 p.24u, proj2 of load_semanticspaces.load_projections) anzeigen lassen - da kann ich sagen "term xyz ist bei "nature" am höchsten".
* ..und umgekehrt! Wenn es eine Mathe-Richtung gibt, welcher Kurs ist DER MATHEMATISCHSTE

* Check in which direction Faculties differ (humanwissenschaften ist mehr psycho als mathe etc)
* What are the most often detected / most often occuring keywords/keyphrases (see THROWN OUT)
    * When we make a histogram counting for every keyword how many documents it appears in, we see an exponential decrease (plot: "Docs per Keyword")
* Are PPMI & tf-idf good measures to extract/detect important terms in entities? -> Look at maximums:
    * `term_doc_matrix.index[np.unravel_index(term_doc_matrix.to_numpy().argmax(), term_doc_matrix.to_numpy().shape)[0]], term_doc_matrix.columns[np.unravel_index(term_doc_matrix.to_numpy().argmax(), term_doc_matrix.to_numpy().shape)[1]]` → 'Information Systems (Wirtschaftsinformatik) M III: IT-Risikomanagement (Übung)' und 'risk'
* Neben den Clustern die ich mir anzeigen lassen kann und qualitativ analysieren kann, kann ich mir auch die distances to the origins of the respective dimensions (induced by the clusters), what induces the respective rankings! (see DESC15 p.24u, proj2 of load_semanticspaces.load_projections) anzeigen lassen - da kann ich sagen "term xyz ist bei "nature" am höchsten".


## What do we expect in Terms of Parameters?


* Candidate-Word-Threshold: movies has samples-to-threshold value of 100, placetypes has 35, 20newsgrups has 614, so for 8000 courses any threshold from 2 to 25 seems reasonable => \cite{Derrac2015} say they intentionally kept the number of candidateterms approximate equal (at around 22.000), so to do the same I'd need a threshold of [TODO: optimal value]
* REGARDING ORIGINAL DATASET: Dass auch die Descriptions echt kurz sind! Ich hab rund 8k samples, um das selbe samples-to-threshold verhältnis zu haben wie DESC15 wäre rechnerisch ein wert von 2 bis 25 sinnvoll (wobei man beachten muss das 2 schon richtig kacke ist weil dann die SVM 2 vs 8000 klassifizieren muss and that will never work -> 25 ist minimum), ABER wenn ich dann 25 nehme hab ich nur 2.4k candidates statt the 22k DESC15 aimed at, which also sucks!! --> CONCLUSION: Datensatz scheint zu klein.
* Candidate-Word-Threshold: movies has samples-to-threshold value of 100, placetypes has 35, 20newsgrups has 614, so for 8000 courses any threshold from 2 to 25 seems reasonable => \cite{Derrac2015} say they intentionally kept the number of candidateterms approximate equal (at around 22.000), so to do the same I'd need a threshold of [TODO: optimal value]
* REGARDING ORIGINAL DATASET: Dass auch die Descriptions echt kurz sind! Ich hab rund 8k samples, um das selbe samples-to-threshold verhältnis zu haben wie DESC15 wäre rechnerisch ein wert von 2 bis 25 sinnvoll (wobei man beachten muss das 2 schon richtig kacke ist weil dann die SVM 2 vs 8000 klassifizieren muss and that will never work -> 25 ist minimum), ABER wenn ich dann 25 nehme hab ich nur 2.4k candidates statt the 22k DESC15 aimed at, which also sucks!! --> CONCLUSION: Datensatz scheint zu klein.

* Mein Datensatz ist anders als deren, so: Der Kappa-Score der rankigns vergleicht ist für mich ne kack metric weil ich ebennicht reviews nehme und more-occurences better-candidate heißen -> gucken wie ich stattdessen gute dimensionen und cluster finde (klingt doch so als sei accuracy/f1/... doch wichtig) => WE EXPECT dass accuracy/f1/... zu besseren ergebnissen führt!
* What parameter-combinations and algorithm-components are the best 
	* What are optimal parameters for Siddta-dataset
	* What are optimal parameters for placetypes-dataset
		* COMPARISON-Table mit \mainalgos
	* Der Plot wie viele candidate-words wir für welchen Kappa-Weighting-Paramter haben (backref auf meinen complain in der intro)
	* Evaluate choices of \mainalgos:
		* Regarding "binary" as quantification: As soon as "course" is in a cluster, the cluster becomes useless if you're binary  (clar.1) => Bad choice (zeigt sich das auch in den Daten)
		* Derrac2015 sagen nie warum sie PPMI over tf-idf wählen, kann ich bestätigen dass das okay so war oder performt tf-idf mindestens so gut wie ppmi?



## Sort-Me

* Explain why we care for the number-of-goodkappas in the next section argh


## What do I expect?

* Different nature of the dataset -> I expect their Rank-Compare-Cluster as Faithfulness-of-embedding-measrue to be worse than f1 or smth
* \cite{Alshaikh2020} do Kappa on binary, I can't believe that's good
