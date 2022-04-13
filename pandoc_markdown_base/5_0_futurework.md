FUTURE WORK

A complete list of considered algorithm-extensions can be found at \url{https://github.com/cstenkamp/MastersThesisText/blob/91d264ad4e369ca87e6826343b4f33bdc235aa0c/pandoc_markdown_base/5_0_futurework.md} or \url{https://github.com/cstenkamp/MastersThesisText/blob/master/pandoc_markdown_base/futurework_long.md}
that lists stuff for EVER STEP

# General
* Build the actual recommender
    * something like the movie tuner
    * interpretable classifiers with decision trees ("Was für einen Kurs willst du?" "Viel Mathe / Wenig Mathe" -> "Viel LinA / Wenig LinA" -> ...) (Figure 3 of Schokhard)
* Put the thing into Siddata 
* Make a study to evaluate usefulness in Stud.IP
    * was man grundsätzlich tun kann ist eine Datenerhebung von studierenden die Daten freiwillig kundtun. Kann man natürlich innerhalb Coxi machen. "Vielleicht is so 'ne Befragung gar nicht so doof". Maybe als Plugin Studip plugin "hier hast du ne liste an kursen in die du eingeschrieben bist, sag doch mal ob der eher schwer/leicht war" etc -> Mit Felix absprechen, kann der ja auch viel gebrauchen
    * which may then even be used for training something like \cite{VISR12}'s algorithm or the fine-tuing step of \cite{Ager2018}


# Algorithm

## Simple Algorithm-Addendums

* Some Hyperparameters from \cite{Ager2018, Alshaikh2020} that I didn't implement yet
* New distance-measures
    * something like levensthein-distance (how many digits do I need to change to make these BoW the same)
    * in \cite{Schockaert2011}, they define similarity through a variation of the Jaccard-distance (IoU, Overlap-Area divided by Union-Area)
* New ways to cluster and merge similar features
    * Instead of cosine similiarity between feature directions, \cite{Alshaikh2019} use the overlap of the positive-samples of two features as similarity measure
    * Different Clusters/Associate-Nongreat-Algorithms (smart weighting function that takes into account the kappa-score of the term and/or the closeness to the original clustercenter (to threshold which cluster they are added to)
    * Different Cluster-Direction-Algorithms (eg by the (weighted-by-kappa-or-closeness-to-center) averaged direction of it's members, )
    * Thresholding the required similarity and performance more optimally
    * Like Ager2018 or Alshaikh2020, I would LIKE to get uninformative clusters, such that I can throw them out.
* Better ways to find a representative clustername (also consider pseudodocs, the algo of \cite{Carmel2009})
    * \cite{Camel2009} one: "One of the first systems that dealt with cluster labeling is the Scatter/Gather application [6]. In this system, in addition to the cluster’s important terms, the titles of documents that are mostly close to the cluster centroid are also considered for labeling, since usually titles are much more readable than a list of terms."

## Complex Algorithm Changes

* Fine-Tuning of \cite{Ager2018}
    * Auch das kann man nochmal erweitern, useful if *the property* is not given: After you figure out which candidate term appears in which texts, figure out which other terms are frequent in these texts while infrequent in texts of the other class and then add these to the candidate-term-set (other way may even be to classify the texts according to if the candidateterm appears in them, and then take the misclassified one also as positive samples) 
* Iterative Hierachical Disentanglement of \cite{Alshaikh} (also to get rid of uninformative clusters)
    * außerdem kann ich ZUSÄTZLICH zu dem wie alshaikhdas gemacht haben auch sagen "ganzen bums von vorne, doctermmatrix neu berechnen mit ALLEN cluser-contents, neue SVM mit full-cluster berechnen, und NOCHMAL die faithfullness messen und AGAIN nur die besten nehmen!"

* Either try to find a real CS with BOTH Euclidian metric AND interpretable directions
* OR acknkowledge that we don't care for Euclidian metric, which allows other techniques
    * wie alle bag-of-words sachen das problem das einunddasselbe sehr verschieden ausgedrückt werden kann 
        * LSA (schon angefangen) and more of what \cite{VISR12} did, Latent Topics
        * Using Doc-Embeddings, Especially BERT
* Getting back regions: \cite{Erk2009} propeses an algorithm for that (prototype-style model that induces a region surrounding a central vec, and an instance-based one that representes degree of variance in each dimension by merging k-nearest-neighbors)


* Die Erweiterungen für den Algorithmus die ich considered habe die better-suited für mein dataset sein könnten (what's realistic is that different kinds of mathematical terms actually do occur more often - Da gibt's several ways mit umzugehen)
	* sich-die-richtigen-wörter-per-candidate-svm-bootstrappen: 
		* NACHDEM ich geclustert habe, nochmal ne SVM draufwerfen, und die descriptions in denen signifikant viele Terms aus diesem Cluster vs die mit kaum/keinen begriffen trennen? (Da kann ich ja sogar die thresholds so setzen dass in beiden klassen möglichst gleich viele vorkommen, und edge cases einfach rauswerfen!) -> mich zu nem richtigerem ergebnis bootstrappen: add more words to cluster, Kappa for the cluster, repeat
		* In dem Fall ist dieses Cluster auch sehr ähnlich zu LSA/dem was VISR12 machen
	* Mit Wordnet/Germanet hypernyms/hyponyns und synonyms zu finden damit ebenfalls zu arbeiten
        * (problem: automatically adding synonyms worsens the polysemy problem \cite{deerwester90})
		* Erst die candidates rausziehen und dann hyponyme angucken und deren count zuum count der number-occurences addieren ("diese entity enhält X wörter die halt hyponyms von dem Term sind") -- wäre dann halt nicht reflected in embedding oder im ersten rausziehen der candidates, ist erst dann used wenn die candidates schon feststehen
		* Kombination von 2 und 3:  Mit Wordnet/Germanet von jedem Term die Hypernyms (Parent) davon rausziehen (also sodass ich hoffentlich bei "analysis" "mathematik" rausbekomme), und dann mit den jeweiligen parents so eine SVM machen (und dann ne setting haben dass ich zwischen x und y level hochgehe, also wenn x=1 und y=2 dann füg ich für "algebra" halt "mathe" und "mathe-parent" als candidate-terms raus, und ebennicht das word selbst [...DANN aber beim counten wie oft es occurt (also doc-term-matrix erstellen) wird es trotzdem gezählt, also wenn ich durch "lineare algebra" + level 1 den begriff "algebra" als candidate extracte, dann zähl ich sowohl die occurences von "algebra" als auch "lineare algebra" dazu - das heißt das rausziehen mit minlevelabove und maxlevelabove ist nur in combi mit "zähl hyponyms als occurence des origterms" sinnvoll )



### Completely different Algorithm

* Whyyy can't I just, like compare doc2vec of the text with doc2vec of the candidate dimensions?! (Like LSA but Neural)
* Another thing, won't PCA in the mix be a good idea? After having found a few important dimensions from the "those-whose-SVMdistancecorrelation-was-good", doesn't it make sense to then also find some other principal components, AKA important directions to explain the distinction between elements that must be given when embedding it onto a lower space that didn't have a word occuring very often in it? Such that our space is a closer representation of the real higher-dim space? And once we did that, couldn't we even find the word-vector closest to the direction of these PCA-vectors to give it a name? Couldn't we even build a whole algorithm like that? Just Neural Document-Embeddings, PCA on that, find the words whose embedding is closest to the top 200 PCA dims, define that as their axisname. Completely neural and thus more independent from the actual choice of words, doesn't lean on stuff from the symbolic level (such that the levels are in the same order that humans have)... Maybe the metric of that space is too unnatural, but to fix that, after doing Embedding->PCA->MappingIntoThatSpace, can't we then create pairwise judgements from distances in each of the principal components (unit vectors of our new space) and than on that an MDS to get a euclidian space, before doing the DeEmbeddingDimensionnames step? Alternatively we can also have a final layer of self-organizing-map-architecture on top for the distances, like even Gärdenfors in his book suggests

* PCA is used in exploratory data analysis and for making predictive models. It is commonly used for dimensionality reduction by projecting each data point onto only the first few principal components to obtain lower-dimensional data while preserving as much of the data's variation as possible. The first principal component can equivalently be defined as a direction that maximizes the variance of the projected data. The i {\displaystyle i} i-th principal component can be taken as a direction orthogonal to the first i − 1 {\displaystyle i-1} i-1 principal components that maximizes the variance of the projected data.  PCA IS ORTHOGONAL  in contrast to ours. 

* You can even train a vsm such that the concepts of subsumption make sense, can't you? Like Dog and Cat are similar because they occur in sentences like "This Dog is cute" and "This cat is Cute". Can't you figure out that "This animal is cute" also holds, and that dog and cat are subconcept of that because all things that hold for animal also hold for dog and cat (as in, each context of animal also occurs as context of dog/cat), but dog and cat are different instances becasue there are some things that only hold fro the one and some that only for the other?



## Analyses

* gucken in welche Richtungen Fachbereiche sich unterscheiden (humanwissenschaften ist mehr psycho als mathe etc)
* would have been nice to check if Ager & Alshaikh's improvements would also have led to Derrac's other classifiers improving
* Levhenstein-distanz-kram
* Taxonomie erstellen
    * Wie DDCs (->daran lässt sich auch immernoch super evaluieren ;)
    * wie's ACCM CCS für Paper ([https://www.acm.org/publications/class-2012](https://www.acm.org/publications/class-2012))
        * damit kann's auch Paper recommenden ;)
    * Conceptual Space an Kursen erstellen (die dann bspw die komplette Domäne der Mathematik erschließen ;)



## Regarding data 

* You could do the shallow-decisiontrees-thingy for other attributes of the dataset than I currently have (possible Attributes für eine Taxonomie von Kursen) (see: https://studip-etherpad.uni-osnabrueck.de:9001/p/SIDDATA_AI_Categories)
    - "Schwierigkeit" -> Durchschnittsnoten?
    - "Komplexität" -> Avg. Semester der Teilnehmer?
    - "Offenheit" -> #Students eines anderen Fachbereichs
    - Aufwand -> #ECTS die der Kurs gibt
    - Vorraussetzungen -> stehen in StudIP, sonst profile der studierenden die ihn belegen