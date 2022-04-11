## General 

PLOTS HERE:
* Snakemake-Graph mit Configs wie für DESC15
* Beispiel für "faithful" induced ranking vs "not faithful" one


* take stuff from \cite{Turney2010} (->sublime), but not too long

* TODO: Mention where future work could be incorporatted already here


* \cite{Alshaikh2020}: "Their core assumption is that words describing semantically meaningful features can be identified by learning for each candi- date word w a linear classifier which separates the embed- dings of entities that have w in their description from the oth- ers. The performance of the classifier for w then tells us to what extent w describes a semantically meaningful feature"

* architecture is so modular that one can easily exchange some components in some step to do something else
    * however combinatorical explosion of hyperparams (not only numerical, but also "which algo")

* In principle Derrac2015, but with some components from Ager2018 and Alshaikh2020 as well as some own stuff
    * I'll be testing some claims or nonclaims of \mainalgos, bspw nutzen sie immer PPMI ohne je tf-idf zu testen
    * Some stuff different bc aforementioned different nature of the dataset
        * their "how does this dimension correspond to the count in the reviews" doesn't make sense (their success-metric for the SVM is tailored to the one property, so I expect that one to be worse)
        * Ways to deal with that: 
            * it is probably the case that different kinds of mathematical terms actually do occur more often, so I'd need calculate these kinds of kappas not based oon a single term but ALREADY on a cluster of terms (... and I can bootstrap my way there, because after I do this I get more words to add to my cluster, rinse and repeat!)
    * Would it have made sense for me to also use all terms as candidates?  
        * that would mean no ngrams!

* Temporal & Spatial Complexity
    * MDS hat quadratic complexity
    * Didn't find a way to have PPMI without quadratic space req, so we're talking >24GB RAM

* describe shortly what the improvements from  [2,3] were
    * Who said that binary occurence was the best metric? I can't believe that
    * Who said kappa is a bad value?
    * \textcite{Ager2018} 
        * 
    * \textcite{Alshaikh2020}
        * Well, do the stuff iterative cluster stuff
            * "When representing a particular entity in a conceptual space, we need to specify which domains it belongs to, and for each of these domains we need to provide a corresponding vector." 
            * then they show their example of something that is not seperable with a hyperplane unless we specify subdomains, maybe just steal their plot that explains their one contribution to 99%
        * Cluster with affinity propagation
        * Do Kappa on Binary (-> see later)
            * for them, the binary "does the word occur in the description" is the only sensible signal, no ppmi or anything! (page 2, footnote 1 of RaZb20)

* dass das hier auf bag-of-words basiert und dass es daher wie alle bag-of-words sachen das problem hat das einunddasselbe sehr verschieden ausgedrückt werden kann, und LSA wäre einer der wege das zu beheben (another one: word embeddings)


* that I'm using BOW and that I dislike it \cite{Le2014}: "Despite their popularity, bag-of-words features have two major weaknesses: they lose the order- ing of the words and they also ignore semantics of the words. For example, “powerful,” “strong” and “Paris” are equally distant" Bag-of-n-grams would alleviate this, but even though it "considers the word order in short context, it suffers from data sparsity and high dimensionality" (bag of n-grams model would create a very high-dimensional representation that tends to generalize poorly)

* was >15 seithen theoretisch ist lieber als "Munition für Discussion" (wenn meine ergebnisse anders sind als die von dem paper kann ich halt erst dann sagen "das widerspricht demunddem hier, die proposen dass und ich kann es (nicht) confirmen".)


<!-- ##############################################################
     ##############################################################
     ##############################################################  -->

## Steps
* how to split (see other textdoc)

### Preprocess

* Filter out all descriptions that don't have a minimal number of words

### Create Dissimilarity Matrix & Quantify

* In their algorithm, the dissimilarity-matrix is created using distance metrics for the bags-of-words of the respective entities. If the strict requirement for a metric space is dropped however, many different algorithms may instead be used at this point - not only different dimensionality reduction methods for the embedding, but also ones that don't rely on the distance matrix or even the bag-of-words at all, like document-embedding-techniques such as Doc2Vec (eg. used by \cite{which_one??}).
    * How would the algorithm differ then?

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
     ########################################################### -->

## Reasonable Params:

* Translate-policy: Obviously the translation won't be perfect, so we lose quality from translating, but on the other hand if it's in english you can use wordnet, which is a lot better than GermaNet, and also embedding-wise it's better
    * "Da, based on [source die die accuracy von dem gtranslate algorithm mit denen von menschen vergleicht], a gtranslate translation is as good as the average lecturer, it is assumed that translating the texts to english before using an english model can lead to better results
* Candidate word threshold: movies has samples-to-threshold value of 100, placetypes has 35, 20newsgrups has 614 so for 8000 courses any threshold from 2 to 25 seems reasonable? \cite{Derrac2015} say they intentionally kept the number of candidateterms approximate equal (at around 22.000), so to do the same I'd need a threshold of [TODO: optimal value]
* PPMI has high complexity, hence I use tf-idf


<!-- ##############################################################
     ##############################################################
     ##############################################################  -->

## Features

* Be able to enable/disable or select between all components
	Like...
	- [ ]  the contribution of [AGKS18] or [ALBS20]
	- [ ]  which classifier to use to split positives and negatives in step 1 (SVM, logistic regression)
	- [ ]  Cohen's Kappa vs Accuracy vs NDCG
	- [ ]  Kmeans vs [DESC15]'s clustering-algorithm
	- [ ]  how to create semantic space(step 0) (MDS, PCI, Doc2Vec, Average GloVe ([https://nlp.stanford.edu/projects/glove/](https://nlp.stanford.edu/projects/glove/))
* Hyperparameters
	- [x]  #dims of the vector-space (50,100,200)
	- [ ]  #dims as input to the clustering algorithm (500,1000,2000)
	- [ ]  number of clusters (1*inputdimsforclusalgorithm, 2*inputdimsforclusalgorithm)
* Extracting Candiate Terms
	- The way of DESC15
	- The way I'm doing it right now
	- The Tag-LSI-Sim as [VISR12] do it (page 13:15)
	    [[VISR12] have the Tag-LSI-SIM, die brauch ich](https://www.notion.so/VISR12-have-the-Tag-LSI-SIM-die-brauch-ich-0868f6c7a20147f582029163f39c225e)


<!-- ##############################################################
     ##############################################################
     ##############################################################  -->

## Differences to \mainalgos / Contributions of this thesis

* Because of the nature of the dataset I need to do some things differently 
    * I'm not working with reviews or collections-of-tags, that means their "how does this dimension correspond to the count in the reviews" doesn't make sense
        * their algorithm is tailored to this. Take their success-metric for the SVMs splitting the embedding. The more often the word "scary" comes in the concatenated reviews, the more scary the movie is. Sounds legit. The more often the people that took pictures at a particular place mentioned the "nature" of that, the more relevant "nature" is to that place. Also legit. But in the descriptions for courses that involve a lot of mathematics, it is not necessarily the case that the term "mathematics" occurs often. So due to the different nature of my dataset I have to go beyond their algorithm at some points - in this case it is probably the case that different kinds of mathematical terms actually do occur more often, so I'd need calculate these kinds of kappas not based oon a single term but ALREADY on a cluster of terms (... and I can bootstrap my way there, because after I do this I get more words to add to my cluster, rinse and repeat!)
* Differences bc of different dataset 
    * Because less words
        * Many candidates occur only in some 25 entities, which makes the ranking rather useless (99.999% of values are zero) -> [WHAT]
    * Because nicht je-öfter-desto-scarier
        * Not compare Rankings, but [WHAT]
        * Using WordNet or smth
        * "reclassify" as possible technique to get cluster direction
        * hoher overlap in wörtern von 2 dokumenten -> alle wörter des einen might as well have been in there
    * cluster-to-reclassify with Die-besten-30%-beim-clustern
    * My ways of finding the name of the cluster
    * Ich nehme schon (wie \cite{Ager2018}) andere dinge als measure of faithfulness (precision, recall)

<!-- ##############################################################
     ##############################################################
     ##############################################################  -->

## Evaluation of \mainalgos
    
* TABELLE which parameter-combis were USED, with optimal ones MARKED for \mainalgos (-> also into yaml!)

* Stuff that was ambiguous:
    * "that the better Ht separates entities to which t applies from the others in S,the better \vec{v_t} models the term t."
        * allein von der aussage muss man das mit den induzierten rankings echt nicht machen, sondern halt nur auf classification quality (-> metrics like accuracy) gucken, bzw kappa anhand der binären klasse berechnen 
        * With a candidate-threshold-tf of 100, that means 19.900 values (99.33%) have a rank of zero, how do you deal with that?!
        *  the ranking induced by count, or the baremetal count?
    * Regarding Kappa-Weighting-Algorithm:
        * Yet another point where \cite{Derrac2015} are really low on information what parameters they used. Sklearn allows different weighting types\footnote{\url{https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html\#sklearn.metrics.cohen_kappa_score}} - TODO: explain what that changes respectively!!}, and as this plot: ![kappa_weighting_funcs](graphics/figures/which_weigthing_algo.png){#fig:which_weighting_algo} TODO: also generally write about if Kappa is a good choice (see eg \url{https://en.wikipedia.org/wiki/Cohen%27s_kappa})
    * DESC15 write they select Kappa "due to its tolerance to class imbalance", but don't menation any parameters -> Class imbalance weighting? Also [see plot] which other weighting value?

* in [DESC15] machen die wirklich immer ne SVM für genau einen Term, und gucken sich anschließend an was für terms dann ähnlich clustern. [VISR12] hingegen (und viele andere!) versuchen erst latent kram zu finden, wodurch das das clustering imo viel besser funktionieren wird weil es viel weniger sparse ist (->und die "contains one-of-the-terms" klasse nicht so verschwindend gering ist compared mit der "doesn't-contain-the-one-term") Laut [DESC15] gibt's da keine Methoden die den metric space erhalten, die frage ist halt wie wichtig das ist für das was man erreichen will!

* Der letzte Schritt mit dem Clustern der good-kappa-ones ist wirklich very basic und hat very much room for improvement
* \cite{Alshaikh2020} do Kappa on binary, I can't believe that's good


<!-- ##############################################################
     ##############################################################
     ##############################################################  -->

## What results do I expect? 

* Different nature of the dataset -> I expect their Rank-Compare-Cluster as Faithfulness-of-embedding-measrue to be worse than f1 or smth
* \cite{Alshaikh2020} do Kappa on binary, I can't believe that's good
