

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