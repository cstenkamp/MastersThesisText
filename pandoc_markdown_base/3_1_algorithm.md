## STEPS


### Create Dissimilarity Matrix & Quantify


* First, we create a Doc-Term-Matrix counting the occurences of every word that occurs in any description and every description.  
    * This may optionally only include those terms that have a term-frequency of at least two (makes the dtm less sparse, but the information if a document contains many terms that are in no other document is lost)
    * This may optionally include n-grams (which makes the dtm a lot more sparse, but alleviates some of the typical problems of bag-of-words-representations at last to a certain degree) (see \ref{sec:techniques:bow} regarding BoW-shortcomings)
* Afterwards, the Doc-Term-Matrix may be converted into a quantification, such that the respective Bag-Of-Word Representations of the documents don't contain the raw counts, but the respective tf-idf/ppmi-representations, relative to all documents and all possible terms.


* My algorithm then saves this dissimilarity-matrix, and what follows is the embedding.
    * For this thesis, the creation of the dissimiliarity-matrix and the embedding are split into individual steps because both have a substantial runtime, and as the number of dimensions for the embedding is only relevant in the embedding-step, a lot of runtime can be saved if the dissimiliarity-matrix can be re-used for different embeddings and dimensions.



### Creating Candidate SVMs and Filter Candidates


"To classify, the authors then use linear classifiers such as \glspl{svm}. The advantage of these is that they create a linear hyperplane that best separates positive from negative entities. The orthogonal of that hyperplane is a vector, which can serve as feature axis: The distance of orthogonally projecting an entity onto this vector induces a ranking of entities. The further away an entities' embedding is from the decision surface on the positive side, the more this feature applies"
    Schon vorher geschrieben, aber drauf zurückkomen dass das ja mit der logik einer svm übereinstimmt

Concretely,  score to assess the performance, comparing not the bare performance but rather if the ranking by distance to decision hyperplane corresponds to ranking of number of occurences of that word.
<!-- (Why is this reasonable? [Wie war das mit stopwords undso..? War das nicht in \cite{Lowe}]) -->
For details why this makes sense it is referred to \cite{Lowe}.
Each of the basic features is then associated with the normal vector of the separating hyperplane as feature directions. These are subsequently clustered (reducing the number of features), and the mean direction of that cluster is then one axis of the new coordinate basis of our new conceptual space.


* ref fig:3d_hyperplane_ortho !!
* neuer plot "wann ist ein induziertes ranking faithful pos/neg example" (grafische Darstellung von "if the ranking induced by the SVM corresponds to the count/PPMI, we see it as faithful measure", also ein beispiel wo's passt und ein Beispiel wo's nicht passt)
* For every candidate-term, take the quantifications from the doc-term-matrix and binarize it, such that we have two classes: one with all descriptions in which the term does occur and one with those where it doesn't.
* On that we then train a linear classifier such as an SVM. From that, we can then calculate binary classification-quality-metrics such as accuracy, precision, recall, f1 and bin2bin-kappa. 
    * dass wir ja nur ne dulli-SVM ohne kernel trick machen, weil wir ja eben with-hyperplane-linear für den eigentlichen space sein wollen (kerneltrick ist ja "Projecten in nem anderen space, damit das was da linear ist bei uns nonlinear ist" und ich will linear sein)
* Additionally, the resulting SVM has a hyperplane as decision surface. The distance of a point to it's orthogonal projection onto that hyperplane can be seen as proportional to how much this point is considered to be in the respective class of the SVM. One can use these distances to enduce a ranking how prototypicality. This ranking can be compared to other heuristics encoding it, such as the ranking induced by the per-term-frequencies of the terms for all documents, or it's PPMI or tf-idf representations.
    * see my grains of salt!
    * \cite{Derrac2015} call this "measure the faithfulness" ...
    * Regarding Kappa-Weighting-Algorithm: (see later)
* \cite{Alshaikh2020}: "The learned vectors will be referred to as feature directions to emphasize the fact that only the ordering induced by the dot product d_i · e matters"
* One of \cite{Ager2018} \cite{Alshaikh2020} said that kappa sucks
* \cite{Alshaikh2020} do Kappa on binary (-> see later)
* Anhang mit Kappa-scores!!

von \cite{Ager2018}:
* We say Feature *Directions* and not feature *vectors* because they are supposed to rank, not measure degrees of similarity! it only tells us "this one has the feature to a higher degree"

* "if this classifier is sufficiently accurate, it must mean that whether word w relates to object o (i.e. whether it is used in the description of o) is important enough to affect the semantic space representation of o. In such a case, it seems rea- sonable to assume that w describes an important feature for the given domain." !!!!



### Cluster 

\cite{Ager2018}:
* CLustering two-fold: esnure that the feature directions are different, and makes easier to interpret (clusters are more descriptive), and alleviates sparsity issues
* The main idea underlying their approach is to se- lect the cluster centers such that (i) they are among the top-scoring candidate feature directions, and (ii) are as close to being orthogonal to each other as possible


* Why cluster? -> semantically close stuff should have close vectors, because In Filmen, in deren Beschreibung das Wort “scary” oft vorkommt, kommt ebenfalls das wort “horror” oder “gore” oft vor. → das sollte ein Cluster sein.
    * For the same reason LSI makes sense!
* Doesn't one bad word in the cluster destroy it?
    * It *IS* okay if common words (like "course") are in clusters, it is NOT the case that as soon as the word occurs once it is said to have a certain property. ("Wenn cluster-threshold zu groß, kommt “A1” in ein cluster mit “Course” and everything is over" is FALSE). However it IS not too good -> A cluster with many words like "course" in it has a high degree of randomness (there is no information gain by such words, it occurs random across courses, a cluster of courses that mention that they are courses is useless) The word occurs randomly, if a course is assumed to have a certain property because of that it's certainly wrong
* \cite{Alshaikh2020} use affinity propagation "for getting rid of the clusters of informative words", similar to how they did it in their 2019 paper. That one doesn't get the #clusters as param so you can set that only indirectly, but they say it's good
* Dass ich, genau wie (wars ager oder alshaikh?), auch die möglcihkeit hab eine neue svm für die cluster_directions zu machen, und dafür halt den best-30%-weg gehe weil gerne mal zu viele positive samples isnd
	* NACHDEM ich geclustert habe, nochmal ne SVM draufwerfen, und die descriptions in denen signifikant viele Terms aus diesem Cluster vs die mit kaum/keinen begriffen trennen? (Da kann ich ja sogar die thresholds so setzen dass in beiden klassen möglichst gleich viele vorkommen, und edge cases einfach rauswerfen!) -> mich zu nem richtigerem ergebnis bootstrappen  [ähnlich wie Alshaik2020, die ja nochmal ne SVM für das komplette cluster machen]
    * The new techniques to generate the cluster direction
    * Weighted by kappa or other things
    * Re-calculate by re-fitting an SVM (like Alshaikh2020: "Cluster direction found by the normal vector of the hyperplane of a linear classifier separating entities whose description contains at least one of the words from the cluster from the others")
* (see the cluster&filter options)
* Beim letzten Schritt of merging candidate directions es nicht wie die machen (alle nehmen und die zum closestem herclustern und dann die richtung des T^0.5 übernehmen):
	* die mit zu großer distanz ebennicht nehmen
	* Die Richtung (wie Alshaikh2020) eben mit ner neuen SVM-Hyperplane bestimmen

* Centroid of the cluster = Average of the normalized vectors of the words


### Post-processing

* TODO: Basiert der fine-tuning step von \cite{Ager2018} auf Supervised learning?


### Embed with Semantic Directions (includes find cluster names)
* Das mit dem Koordinatensystem drehen passiert gar nicht so wie ich dachte dass es passiert...?!
* My Techniques to find the cluster-name (keybert, embeddings)
    * die bert-embeddings für die Cluster der candidate directions averagen und den closesten als Name der Dimension geben
    * keybert (thresholded close bert embeddings)
    * TODO: Mention Camel2009 one!!
* In the end we re-embed the entities into a space where each of the vector components is a semantic directions and the value are the respective \gls{rank}ings. That's what we then finally call its \textbf{feature-based representation} 




<!-- ##############################################################
     ##############################################################
     ########################################################### -->

## Make the decision-trees

* Metrices are useful that Evaluate the quality of a rank- ing w.r.t. some given relevance scores
* Note that depth 1 trees are only a sin- gle direction and a cut-off, so to perform well, the method needs to identify a highly relevant feature to the considered category. Depth

* Decision-Trees:
    * which additional to test against
    * if all-at-once or one-vs-rest
    * depth of the tree (1, 3, unbound)
    * train-test-split (2:1) or cross-validation


<!-- ##############################################################
     ##############################################################
     ##############################################################  -->



ACTUALLY 2_7_separatrixdistance should be hERE!!!