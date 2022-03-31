<!--oder: OUTLOOK -->



## WHAT ONE COULD HAVE DONE IN EVERY ALGORITHM STEP

### Preprocessing


### ...


### Finding Cluster-Names 

* \cite{Camel2009} one!!



* Ich könnte die Schrittweise Anwendung des Algorithmus wie Alshaikh das gemacht haben mit "für die die politisch sind, what's their direction" mit Level 2 für DDC. "Für die die in 'Informatik' eingeteilt sind, wie gut kriegen wir deren sub-categorie hin?"

* Ich kann gucken in welche Richtungen Fachbereiche sich unterscheiden (humanwissenschaften ist mehr psycho als mathe etc)

* Evaluation in Stud.IP (which may then even be used for training something like \cite{VISR12}'s algorithm or the fine-tuing step of \cite{Ager2018})
* Building this thing as component into Siddata, mit einem Interface wie dem Movie Tuner

* Die Erweiterungen für den Algorithmus die ich considered habe die better-suited für mein dataset sein könnten
    * All ways of incorporating wordnet/germanet
    * The stuff that VISR12 did
    * Bootstrapping good clustered directions (with iterative application of SVM-Kappa and just literally with "which words occur in the same texts" and also with the LSA/LDA (which one) method like VISR12 did)


* Die Hyperparameter (also Algorithmen/Komponenten) von \cite{Ager2018} und \cite{Alshaikh2020} die ich noch nicht implementiert hab
    * GloVe anstelle von Dissim-Mat + Embedding
    * Fine-Tuning von Ager2018
    * Iteratively-finding-facets from Alshaik2019 (19!)
    * [I should have a table or a yaml earlier in the text, just mention all the not-implemented stuff from that]


* Make interpretable classifiers with decision trees ("Was für einen Kurs willst du?" "Viel Mathe / Wenig Mathe" -> "Viel LinA / Wenig LinA" -> ...) (Figure 3 of Schokhard)
    * Oder halt sowas wie den Movie Tuner 
* Taxonomie erstellen
    * Wie DDCs (->daran lässt sich auch immernoch super evaluieren ;)
    * wie's ACCM CCS für Paper ([https://www.acm.org/publications/class-2012](https://www.acm.org/publications/class-2012))
        * damit kann's auch Paper recommenden ;)
* Conceptual Space an Kursen erstellen (die dann bspw die komplette Domäne der Mathematik erschließen ;)


### Stuff to add Because nicht je-öfter-desto-scarier
    * Not compare Rankings, but [WHAT]
    * Using WordNet or smth
    * Bootstrap your way to more candidates
        * using LSI or smth (see below)    
	* Das sich-die-richtigen-wörter-per-candidate-svm-bootstrappen
        * war das das mit dem statistical "die haben einen hohen overlap, so that term might as well have been in there"?   
	* Mit LSI rausfinden welche Terme genausogut in dem Text hätten vorkommen können (hab ich auch irgendwo schon)
	* Explizit einfach zu gucken "Welche Terme kommen oft in den gleichen dokumenten vor" (und das inverse (steht iwo im code)), und dann ne candidate SVM für grouped terms anstelle von einzelterms machen (auch schon iwo als code)
	* Mit Wordnet hypernyms/hyponyns und synonyms zu finden damit ebenfalls zu arbeiten (kann man wit wordnet angeben welches abstraktionsniveau ich haben will?)
	    * Abstraktionsniveau gibt's nicht in wordnet, das heißt das richtige layer zu finden ist schwer. Was man auf jeden Fall machen kann ist die Terme zu den bases ihrer synsets umzuwandeln (dadurch wird aus "math" und "mathematics" das gleiche), aber in anderen Fällen ist es halt so dass ich die Candidate-Terms schon vorher brauche und nur sagen kann "diese entity enhält X wörter die halt hyponyms von dem Term sind"
    * After you figure out which candidate term appears in which texts, figure out which other terms are frequent in these texts while infrequent in texts of the other class and then add these to the candidate-term-set (other way may even be to classify the texts according to if the candidateterm appears in them, and then take the misclassified one also as positive samples)

### Low-Hanging-Algorithm-Addendums

* A lot from Tag-Genome 
    * The preprocessing for the text-freq they do Normalization of word frequencies  (make popular terms that naturally occur more frequently in user reviews not obscure others: compute z-scores by subtracting mean and dividing by standard deviation specific to each tag)
    * tag-share as dcm-quant-measure (und andere "relative frequency" geschichten)
* andere distance measures außer mean-ang-dist ausprobieren (metric space after all!)
* implement NDCG
* Instead of cosine similiarity between feature directions, \cite{Alshaikh2019} use the overlap of the positive-samples of two features as similarity measure
* Camel2009's technqiue to find cluster names: 
    * Carmel2009: One of the first systems that dealt with cluster labeling is the Scatter/Gather application [6]. In this system, in addition to the cluster’s important terms, the titles of documents that are mostly close to the cluster centroid are also considered for labeling, since usually titles are much more readable than a list of terms.
    * das kann man wunderbar mit dem lsi-ding [von [VISR12]!] verbinden, dass dann das (pseudo-oder-normal-) doc das dem am nächstem ist der clustername ist (geht recht schnell!!!)

* Extensively test using Doc-Embeddings instead of MDS (one of the MOST IMPORTANT)
* Extensively relying on Wordnet/Germanet 
	
[TODO: add those that I didn't do anymore from ONLY CODE_TODOS MRZ25+ : Base Algorithm Improvements/Additions here! ]

* Cluster&Filter:
    * <TODO>Associate-nongreat-algorithm (k-means, DESC15 one, ..?)
    * <TODO>Associate-nongreat-threshold (if those ones that are far away from all are ignored) ("smart weighting function that takes into account the kappa-score of the term and/or the closeness to the original clustercenter (to threshold which cluster they are added to)")
    * <TODO>weight which-candidates-may-cluster: the closer the orthogonals (cosine-dist) AND the closer their intercepts, the more we want to have them in a cluster.
    * <TODO>Cluster-Direction-Algorithm (onlymain, average, weighted-by-kappa-averaged, weighted-by-distance-to-center-averaged, redo-decision-plane)
    * <TODO>the better ways to find the name of the cluster
        
* Allow to remove too-high-df-words instead of removing stopwords (-> phrasen wie "Fallen aus")

### More Complex Algorithm Addendums


* BOOTSTRAP MORE CANDIDATES (AFTER EXTRACT CANDIDATES)
    * [VISR12]: LSI
        * Options: [see what to take for dtm]]
        * Parameters: #dims for the rank reduction (see https://en.wikipedia.org/wiki/Latent_semantic_analysis#Rank-reduced_singular_value_decomposition)

* What to take for the term-document-matrix
    * [VISR12]: 
        * tag-applied
        * tag-count
        * tag-share (the number of times tag t has been applied to item i, divided by the number of times any tag has been applied to item i)
    * relative-tag-count (tag-count / text-len) or tag-count / distinct-words-in-text
    * See also: https://en.wikipedia.org/wiki/Latent_semantic_analysis#Term-document_matrix



### Suggestion for what may even be a better algorithm

Another thing, won't PCA in the mix be a good idea? After having found a few important dimensions from the "those-whose-SVMdistancecorrelation-was-good", doesn't it make sense to then also find some other principal components, AKA important directions to explain the distinction between elements that must be given when embedding it onto a lower space that didn't have a word occuring very often in it? Such that our space is a closer representation of the real higher-dim space? And once we did that, couldn't we even find the word-vector closest to the direction of these PCA-vectors to give it a name? Couldn't we even build a whole algorithm like that? Just Neural Document-Embeddings, PCA on that, find the words whose embedding is closest to the top 200 PCA dims, define that as their axisname. Completely neural and thus more independent from the actual choice of words, doesn't lean on stuff from the symbolic level (such that the levels are in the same order that humans have)... Maybe the metric of that space is too unnatural, but to fix that, after doing Embedding->PCA->MappingIntoThatSpace, can't we then create pairwise judgements from distances in each of the principal components (unit vectors of our new space) and than on that an MDS to get a euclidian space, before doing the DeEmbeddingDimensionnames step? Alternatively we can also have a final layer of self-organizing-map-architecture on top for the distances, like even Gärdenfors in his book suggests


=======================================================================================================================
===================================================== FROM NOTION =====================================================
=======================================================================================================================



- Make interpretable classifiers with decision trees ("Was für einen Kurs willst du?" "Viel Mathe / Wenig Mathe" -> "Viel LinA / Wenig LinA" -> ...) (Figure 3 of Schokhard)
    - Oder halt sowas wie den Movie Tuner von [
- Taxonomie erstellen
    - Wie DDCs (->daran lässt sich auch immernoch super evaluieren ;)
    - wie's ACCM CCS für Paper ([https://www.acm.org/publications/class-2012](https://www.acm.org/publications/class-2012))
        - damit kann's auch Paper recommenden ;)
- Conceptual Space an Kursen erstellen (die dann bspw die komplette Domäne der Mathematik erschließen ;)

was man grundsätzlich tun kann ist eine Datenerhebung von studierenden die Daten freiwillig kundtun. Kann man natürlich innerhalb Coxi machen. "Vielleicht is so 'ne Befragung gar nicht so doof". Maybe als Plugin Studip plugin "hier hast du ne liste an kursen in die du eingeschrieben bist, sag doch mal ob der eher schwer/leicht war" etc -> Mit Felix absprechen, kann der ja auch viel gebrauchen

