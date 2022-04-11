## STEPS


### Create Dissimilarity Matrix & Quantify


* First, we create a Doc-Term-Matrix counting the occurences of every word that occurs in any description and every description.    
    * distinction df und stf!!
    * This may optionally only include those terms that have a term-frequency of at least two (makes the dtm less sparse, but the information if a document contains many terms that are in no other document is lost)
    * This may optionally include n-grams (which makes the dtm a lot more sparse, but alleviates some of the typical problems of bag-of-words-representations at last to a certain degree) (see \ref{sec:techniques:bow} regarding BoW-shortcomings)
* Afterwards, the Doc-Term-Matrix may be converted into a quantification, such that the respective Bag-Of-Word Representations of the documents don't contain the raw counts, but the respective tf-idf/ppmi-representations, relative to all documents and all possible terms.
    * \cite{Derrac2015} always only use PPMI without ever testing tf-idf or giving a reason, I'll try both. Also (ref complexity) PPMI eats RAM
    * \cite{Alshaikh2020} do Kappa on binary (-> see later)
* From this quantified Doc-Term-Matrix, a dissimilarity-matrix is generated. This requires a measure for the dissimlarity - in the original paper, this is what they call "normalized angular difference": $ang(e_i, e_j) = \frac{2}{\pi}*arccos \left( \frac{\vec[m]{v_{e_i}}*\vec[m]{v_{e_j}}}{||\vec[m]{v_{e_i}}||*||\vec[m]{v_{e_i}}||} \right)$, which is equal to $\frac{2}{\pi}*arccos(-cosine+1)$, where **cosine** stands for the default cosine distance.
* My algorithm then saves this dissimilarity-matrix, and what follows is the embedding.
    * For this thesis, the creation of the dissimiliarity-matrix and the embedding are split into individual steps because both have a substantial runtime, and as the number of dimensions for the embedding is only relevant in the embedding-step, a lot of runtime can be saved if the dissimiliarity-matrix can be re-used for different embeddings and dimensions.
* Because this dissimilarity-Matrix is far too high-dimensional and sparse, a dimensionality-reduction is applied. Because it is important to DESC15 that the embedding is a euclidian space, they go for MDS. 

* in \cite{Schockaert2011}, they define similarity through a variation of the Jaccard-distance (IoU, Overlap-Area divided by Union-Area)


### Embed

* Multi-Dimensional Scaling (MDS) as their algorithm of choice, which takes [...]


### Extract Candidates (Steps 4, 5 and 6: Extracting Candidate Terms, Postprocessing them, creating the Doc-Term-Matrix for the Candidate-Terms and filtering it)


* In their placetypes-dataset they just took ALL terms as candidates such that #candidates ~= #candidates for movies
    * I should have done that too but I had a bug so I thougt it were much more
* Possible step after this is to bootstrap more candidates using LSI 
* BC I am using KeyBERT I have to postprocess candidates
* Irrespective of the algorithm to extract keywrds, we'll only extract keywords with a sufficiently high df - lateron we'll need to classify those that contain the keyword vs those that don't, and for this classification to be useful a relevant percentage should be in the positive class. This min-df thus ideally depends on the size of the dataset (and is minimally, say, 25)
* Also in any case, we need the max-ngram size of the keyphrases. This is not explicitly done in DESC15, but as they claim to also extract adjective phrases, I'd say it's at least 5.
* Can extract with KeyBERT (see \autoref{ap:details_keybert}) or by means of a quantification (tf-idf, tf and ppmi). When using this method, those terms and phrases are extracted that have a sufficiently high score of the respective quantification. Note that the respective scores are not global frequencies but depend on the combination of document and term (and the relation of this document to other documents), meaning one term may be important enough to be extracted in one document but not in another. (PPMI eats ram, see appendix & top) 

* As a last step, a doc-term-matrix is created from these postprocessed candidates, of the shape n_docs * n_candidate-terms. 
    * This doc-term-matrix then gets filtered, such that only candidates that have a minimal df or stf are considered from now on, and a quantification is applied to the doc-term-matrix (one of count, binary, tfidf, or binary) 
        * so the relation of term to document may be expressed by something else than count - so if we later compare the ranking induced by the svm to this maybe something else thatn the count stands there - I'm expecting that for my dataset tf-idf is much more valuable than the count bc no concatenated reviews or tags
    


* After this step, the original description-texts are not needed anymore.

### Creating Candidate SVMs & Filter Candidates

Here we bring together the embedding of the individual entities and the extracted keyphrases. For that, we split those samples where a keyphrase occurs from those where it doesn't, using a linear classifier. The orthogonal to the resulting decision-hyperplane is then used as axis, onto which the entities are mapped - the further away from the plane the mapping of a point onto the orthogonal, the more the entity is said to have the attribute encoded by the phrase responsible for the hyperplane. A score function compares the ranking induced by this to the ranking induced by number of occurences (or quantification-value) of the respective keyphrase of all documents, such that only those terms where the correspondance of these rankings exceeds a certain threshold are considered as candidate directions henceforth.

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

### Cluster 

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



### Embed with Semantic Directions (includes find cluster names)
* Das mit dem Koordinatensystem drehen passiert gar nicht so wie ich dachte dass es passiert...?!
* My Techniques to find the cluster-name (keybert, embeddings)
    * die bert-embeddings für die Cluster der candidate directions averagen und den closesten als Name der Dimension geben
    * keybert (thresholded close bert embeddings)
    * TODO: Mention Camel2009 one!!
* In the end we re-embed the entities into a space where each of the vector components is a semantic directions and the value are the respective \gls{rank}ings. That's what we then finally call its \textbf{feature-based representation} 

### Post-processing

* TODO: Basiert der fine-tuning step von \cite{Ager2018} auf Supervised learning?




<!-- ##############################################################
     ##############################################################
     ########################################################### -->

## Make the decision-trees

* Decision-Trees:
    * which additional to test against
    * if all-at-once or one-vs-rest
    * depth of the tree (1, 3, unbound)
    * train-test-split (2:1) or cross-validation

<!-- ##############################################################
     ##############################################################
     ##############################################################  -->



ACTUALLY 2_7_separatrixidstance should be hERE!!!