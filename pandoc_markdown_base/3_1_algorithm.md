## STEPS


### Create Dissimilarity Matrix & Quantify


* First, we create a Doc-Term-Matrix counting the occurences of every word that occurs in any description and every description.  
    * This may optionally only include those terms that have a term-frequency of at least two (makes the dtm less sparse, but the information if a document contains many terms that are in no other document is lost)
    * This may optionally include n-grams (which makes the dtm a lot more sparse, but alleviates some of the typical problems of bag-of-words-representations at last to a certain degree) (see \ref{sec:techniques:bow} regarding BoW-shortcomings)
* Afterwards, the Doc-Term-Matrix may be converted into a quantification, such that the respective Bag-Of-Word Representations of the documents don't contain the raw counts, but the respective tf-idf/ppmi-representations, relative to all documents and all possible terms.


* My algorithm then saves this dissimilarity-matrix, and what follows is the embedding.
    * For this thesis, the creation of the dissimiliarity-matrix and the embedding are split into individual steps because both have a substantial runtime, and as the number of dimensions for the embedding is only relevant in the embedding-step, a lot of runtime can be saved if the dissimiliarity-matrix can be re-used for different embeddings and dimensions.




### Cluster 

Each of the basic features is then associated with the normal vector of the separating hyperplane as feature directions. These are subsequently clustered (reducing the number of features), and the mean direction of that cluster is then one axis of the new coordinate basis of our new conceptual space.

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