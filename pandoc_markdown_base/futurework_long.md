# FUTURE WORK / SHORTCOMINGS / OUTLOOK

## Algorithm

### Simple Algorithm-Addendums

There were some Hyperparameters (meaning Algorithmen/Components) of \cite{Ager2018} and \cite{Alshaikh2020}  that I didn't implement yet

* Preprocessing
    * Allow to remove too-high-df-words instead of removing stopwords (-> phrasen wie "Fallen aus")

* Quantifications (dcm-quant-measure)
    * from Tag-Genome:
        * tag-applied (HAVE I ALREADY?)
        * tag-count (HAVE I ALREADY?)
        * tag-share (the number of times tag t has been applied to item i, divided by the number of times any tag has been applied to item i)
        * The preprocessing for the text-freq they do Normalization of word frequencies  (make popular terms that naturally occur more frequently in user reviews not obscure others: compute z-scores by subtracting mean and dividing by standard deviation specific to each tag)
        * relative-tag-count (tag-count / text-len) or tag-count / distinct-words-in-text
        * See also: https://en.wikipedia.org/wiki/Latent_semantic_analysis#Term-document_matrix

* Embedding
    * GloVe/other Doc-Embeddings anstelle von Dissim-Mat + Embedding (like \cite{Ager2018})
    * andere distance measures außer mean-ang-dist ausprobieren (metric space after all!)
    * New distance measures for Dissim-Mat and Embedding: 
        * like levensthein-distance for the BoW-Vectors, how many digits do I need to change to make these BoW the same (for both binary (meaning "chaning a 100 to a zero is ONE change) and non-binary cases (meaning "changing a 100 to a zero is 100 changes"))
        * cosine distance (which is based only on angles, so dist((0,1),(0,0)) == dist((0,100),(0,0)))
        * manhatten/checkerboard/... distance, which is NOT only based on angles

* Merging Clusters & Finding their directions
    * low-hanging fruits!! "We used the logistic regression implementation from scikit-learn to find the directions."
    * Instead of cosine similiarity between feature directions, \cite{Alshaikh2019} use the overlap of the positive-samples of two features as similarity measure
    * Different Associate-Nongreat-Algorithms
        * k-means
        * Derrac2015 one (DO I HAVE IT?)
        * Associate-nongreat-threshold (if those ones that are far away from all are ignored) ("smart weighting function that takes into account the kappa-score of the term and/or the closeness to the original clustercenter (to threshold which cluster they are added to)")
        * weight which-candidates-may-cluster: the closer the orthogonals (cosine-dist) AND the closer their intercepts, the more we want to have them in a cluster.
    * Different Cluster-Direction-Algorithms
        * onlymain, average, weighted-by-kappa-averaged, weighted-by-distance-to-center-averaged, redo-decision-plane
        * don't consider those with too big distance (or too bad kappa or ....)
	* in the cluster-candidates step, there are SO MANY improvements to be made.
		 * I am ordering by kappa and selecting from there on - because "isawyoufirst" is very close to "nature", "nature" will never be picked out as term
		    -> either find a way to select more... informative?? terms from the start, or find a way to, once the corresponding clusters are found, select a good one of that as representative
		        -> use LSI for that (add pseudodocs with only one term and that term as name, and then let all DOCUMENTNAMES be candidates (change in EARLIER STEP!))
		        -> do it like the "enhancing from wikipedia" paper and after the whole clustering, consider the documentnames that fit best as clusterlabels
		 * The fact that for the clustering, all of the T^0.1 ones are added to the "most similar one", I would definititely threshold that, those that are far from are not considered
		 * Like Ager2018 or Alshaikh2020, I would LIKE to get uninformative clusters, such that I can throw them out.
		 * Well, the hierachical way of Alshaikh2020 seemed promising, didn't it?! 
		 * Calculate the direction of the cluster anew, 
		 * 		a) by the (weighted-by-kappa-or-closeness-to-center) averaged direction of it's members, 
		 *      b) by creating a new SVM with "any(or-at-least-x)-of-the-cluster-terms-occur"



* Finding  Cluster-Names
    * \cite{Camel2009} one: "One of the first systems that dealt with cluster labeling is the Scatter/Gather application [6]. In this system, in addition to the cluster’s important terms, the titles of documents that are mostly close to the cluster centroid are also considered for labeling, since usually titles are much more readable than a list of terms."
        * das kann man wunderbar mit dem lsi-ding [von [VISR12]!] verbinden, dass dann das (pseudo-oder-normal-) doc das dem am nächstem ist der clustername ist (geht recht schnell!!!)
    * We see in \ref{tab:text_per_dim} that using the respectively best-fitting DOCUMENT (without LSI or anything, just the one with the highest ranking!)  is often even the MUCH BETTER direction!!! 
    * that you could use LSA even to find the name of the semantic direction (if the vector of a document is closest to the vectors of the respective entities)
    * Others...?


* Postprocessing
    * The Fine-Tuning of \cite{Ager2018}


* Distance-Functions
    * in \cite{Schockaert2011}, they define similarity through a variation of the Jaccard-distance (IoU, Overlap-Area divided by Union-Area)

### Complex Algorithm-Addendums

* Premises von LSI & LDA einbauen, die haben schon vektoren
    * Documentnames as additional candidates
    * Better Latent stuff detection, directly having directions 

* dass das hier auf bag-of-words basiert und dass es daher wie alle bag-of-words sachen das problem hat das einunddasselbe sehr verschieden ausgedrückt werden kann, und LSA wäre einer der wege das zu beheben (another one: word embeddings)

* [AGKS18] speculates that performance could be improved for such categories by integrating domain knowledge into the fine-tuning method. ==> Maybe combine this with [ALBS20]??
* Footnote 22 from [DESC15]: For some abstract properties, the most appropriate term may not occur in the corpus. In such cases, external resources such as WordNet or Wikipedia could be used to identify additional terms that are relevant for the considered domain.

* Extensively relying on Wordnet/Germanet AT DIFFERENT POINTS (TODO:!)
* Iteratively-finding-facets from Alshaik2019 (19!)
* Ich könnte die Schrittweise Anwendung des Algorithmus wie Alshaikh das gemacht haben mit "für die die politisch sind, what's their direction" mit Level 2 für DDC. "Für die die in 'Informatik' eingeteilt sind, wie gut kriegen wir deren sub-categorie hin?"
* Use LSA or other latent analyze things (should have been explained here)
* außerdem kann ich ZUSÄTZLICH zu dem wie alshaikhdas gemacht haben auch sagen "ganzen bums von vorne, doctermmatrix neu berechnen mit ALLEN cluser-contents, neue SVM mit full-cluster berechnen, und NOCHMAL die faithfullness messen und AGAIN nur die besten nehmen!"
* [VISR12] have the Tag-LSI-SIM, die brauch ich

* Die Erweiterungen für den Algorithmus die ich considered habe die better-suited für mein dataset sein könnten (...dass mein Datensatz anders ist als concatenated-movie-reviews und ich deswegen nicht einfach "je öfter 'scary' desco scarier" machen kann. (but what's realistic is that different kinds of mathematical terms actually do occur more often) -- Da gibt's several ways mit umzugehen)
	* sich-die-richtigen-wörter-per-candidate-svm-bootstrappen: 
		* NACHDEM ich geclustert habe, nochmal ne SVM draufwerfen, und die descriptions in denen signifikant viele Terms aus diesem Cluster vs die mit kaum/keinen begriffen trennen? (Da kann ich ja sogar die thresholds so setzen dass in beiden klassen möglichst gleich viele vorkommen, und edge cases einfach rauswerfen!) -> mich zu nem richtigerem ergebnis bootstrappen  [ähnlich wie Alshaik2020, die ja nochmal ne SVM für das komplette cluster machen]
		* In dem Fall ist dieses Cluster auch sehr ähnlich zu LSA/dem was VISR12 machen
		* Sowohl dabei als auch beim direction-des-clusters-finden kann ich die ja bei kappa weighten
	* I'd need calculate these kinds of kappas not based on a single term but ALREADY on a cluster of terms (... and I can bootstrap my way there, because after I do this I get more words to add to my cluster, rinse and repeat!
	* Mit LSI rausfinden welche Terme genausogut in dem Text hätten vorkommen können ("similar directions finden") (schon in unfinished_commands)
	* Explizit einfach zu gucken "Welche Terme kommen oft in den gleichen dokumenten vor" (also per set union) (und das inverse (steht iwo in unfinished_commands)), und dann ne candidate SVM für grouped terms anstelle von einzelterms machen ("wenn ein term in vielen ähnlichen vorkommt tun wir so als wäre er auch hier")
	* Mit Wordnet/Germanet hypernyms/hyponyns und synonyms zu finden damit ebenfalls zu arbeiten
		* allerwenigstens eine PP-Component make-to-synsetbase (die Terme zu den bases ihrer synsets umzuwandeln (dadurch wird aus "math" und "mathematics" das gleiche))
		* Erst die candidates rausziehen und dann hyponyme angucken und deren count zuum count der number-occurences addieren ("diese entity enhält X wörter die halt hyponyms von dem Term sind") -- wäre dann halt nicht reflected in embedding oder im ersten rausziehen der candidates, ist erst dann used wenn die candidates schon feststehen
		* Alternativ gucken dass ich das abstraktionsniveau habe das dafür sorgt das ich möglichst naher an gewünschter anzahl candidates kome? (Problem: Abstraktionsniveau gibt's nicht in wordnet, das heißt das richtige layer zu finden ist schwer)
		* Kombination von 2 und 3:  Mit Wordnet/Germanet von jedem Term die Hypernyms (Parent) davon rausziehen (also sodass ich hoffentlich bei "analysis" "mathematik" rausbekomme), und dann mit den jeweiligen parents so eine SVM machen (und dann ne setting haben dass ich zwischen x und y level hochgehe, also wenn x=1 und y=2 dann füg ich für "algebra" halt "mathe" und "mathe-parent" als candidate-terms raus, und ebennicht das word selbst [...DANN aber beim counten wie oft es occurt (also doc-term-matrix erstellen) wird es trotzdem gezählt, also wenn ich durch "lineare algebra" + level 1 den begriff "algebra" als candidate extracte, dann zähl ich sowohl die occurences von "algebra" als auch "lineare algebra" dazu - das heißt das rausziehen mit minlevelabove und maxlevelabove ist nur in combi mit "zähl hyponyms als occurence des origterms" sinnvoll )
    * All ways of incorporating wordnet/germanet
    * The stuff that VISR12 did
    * Bootstrapping good clustered directions (with iterative application of SVM-Kappa and just literally with "which words occur in the same texts" and also with the LSA/LDA (which one) method like VISR12 did)
    * Not compare Rankings, but [WHAT]
    * Bootstrap your way to more candidates (using LSI or smth (see below)    )
	* Das sich-die-richtigen-wörter-per-candidate-svm-bootstrappen (war das das mit dem statistical "die haben einen hohen overlap, so that term might as well have been in there"?  )
	* Mit LSI rausfinden welche Terme genausogut in dem Text hätten vorkommen können (hab ich auch irgendwo schon)
	* Explizit einfach zu gucken "Welche Terme kommen oft in den gleichen dokumenten vor" (und das inverse (steht iwo im code)), und dann ne candidate SVM für grouped terms anstelle von einzelterms machen (auch schon iwo als code)
	* Mit Wordnet hypernyms/hyponyns und synonyms zu finden damit ebenfalls zu arbeiten (kann man wit wordnet angeben welches abstraktionsniveau ich haben will?)
	    * Abstraktionsniveau gibt's nicht in wordnet, das heißt das richtige layer zu finden ist schwer. Was man auf jeden Fall machen kann ist die Terme zu den bases ihrer synsets umzuwandeln (dadurch wird aus "math" und "mathematics" das gleiche), aber in anderen Fällen ist es halt so dass ich die Candidate-Terms schon vorher brauche und nur sagen kann "diese entity enhält X wörter die halt hyponyms von dem Term sind"
    * After you figure out which candidate term appears in which texts, figure out which other terms are frequent in these texts while infrequent in texts of the other class and then add these to the candidate-term-set (other way may even be to classify the texts according to if the candidateterm appears in them, and then take the misclassified one also as positive samples)
    * it is probably the case that different kinds of mathematical terms actually do occur more often, so I'd need calculate these kinds of kappas not based oon a single term but ALREADY on a cluster of terms (... and I can bootstrap my way there, because after I do this I get more words to add to my cluster, rinse and repeat!)


* BOOTSTRAP MORE CANDIDATES (AFTER EXTRACT CANDIDATES)
    * [VISR12]: LSI
        * Options: [see what to take for dtm]]
        * Parameters: #dims for the rank reduction (see https://en.wikipedia.org/wiki/Latent_semantic_analysis#Rank-reduced_singular_value_decomposition)


#### Getting back regions
If you wanted to get regions back, \cite{Erk2009} propeses an algorithm for that (prototype-style model that induces a region surrounding a central vec, and an instance-based one that representes degree of variance in each dimension by merging k-nearest-neighbors)

You can even train a vsm such that the concepts of subsumption make sense, can't you? Like Dog and Cat are similar because they occur in sentences like "This Dog is cute" and "This cat is Cute". Can't you figure out that "This animal is cute" also holds, and that dog and cat are subconcept of that because all things that hold for animal also hold for dog and cat (as in, each context of animal also occurs as context of dog/cat), but dog and cat are different instances becasue there are some things that only hold fro the one and some that only for the other?



### Completely different Algorithm

* Whyyy can't I just, like compare doc2vec of the text with doc2vec of the candidate dimensions?!
* Another thing, won't PCA in the mix be a good idea? After having found a few important dimensions from the "those-whose-SVMdistancecorrelation-was-good", doesn't it make sense to then also find some other principal components, AKA important directions to explain the distinction between elements that must be given when embedding it onto a lower space that didn't have a word occuring very often in it? Such that our space is a closer representation of the real higher-dim space? And once we did that, couldn't we even find the word-vector closest to the direction of these PCA-vectors to give it a name? Couldn't we even build a whole algorithm like that? Just Neural Document-Embeddings, PCA on that, find the words whose embedding is closest to the top 200 PCA dims, define that as their axisname. Completely neural and thus more independent from the actual choice of words, doesn't lean on stuff from the symbolic level (such that the levels are in the same order that humans have)... Maybe the metric of that space is too unnatural, but to fix that, after doing Embedding->PCA->MappingIntoThatSpace, can't we then create pairwise judgements from distances in each of the principal components (unit vectors of our new space) and than on that an MDS to get a euclidian space, before doing the DeEmbeddingDimensionnames step? Alternatively we can also have a final layer of self-organizing-map-architecture on top for the distances, like even Gärdenfors in his book suggests


<!-- ========================================================================= -->
<!-- ========================================================================= -->
<!-- ========================================================================= -->
## Things ontop

* Building this thing as component into Siddata
    * with a Movie Tuner Interface

<!-- ========================================================================= -->
<!-- ========================================================================= -->
<!-- ========================================================================= -->
## Analyses

* gucken in welche Richtungen Fachbereiche sich unterscheiden (humanwissenschaften ist mehr psycho als mathe etc)
* Evaluation in Stud.IP 
    * was man grundsätzlich tun kann ist eine Datenerhebung von studierenden die Daten freiwillig kundtun. Kann man natürlich innerhalb Coxi machen. "Vielleicht is so 'ne Befragung gar nicht so doof". Maybe als Plugin Studip plugin "hier hast du ne liste an kursen in die du eingeschrieben bist, sag doch mal ob der eher schwer/leicht war" etc -> Mit Felix absprechen, kann der ja auch viel gebrauchen
    * which may then even be used for training something like \cite{VISR12}'s algorithm or the fine-tuing step of \cite{Ager2018}
* would have been nice to check if Ager & Alshaikh's improvements would also have led to Derrac's other classifiers improving
* theoretisch ist es auch möglich bspw nen network mit attention auf gewisse dinge wie fachbereich und anderes zu trainieren und dann rauszusuchen was die wichtigen ausschlaggebenden dinge für das Netzwerk waren
* Levhenstein-distanz-kram

* Make interpretable classifiers with decision trees ("Was für einen Kurs willst du?" "Viel Mathe / Wenig Mathe" -> "Viel LinA / Wenig LinA" -> ...) (Figure 3 of Schokhard)
    * Oder halt sowas wie den Movie Tuner 
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
* Mit meinen Attributen gibt's einige Probleme. Noten gibt's nicht, "allerschweste Datenschutzbedenken". Was studiert wer und in welchem Semester haben wir nur für den Zeitpunkt der Abfrage -> in kombi mit der k-anonymisierung wirds da schwer zu sagen in welchem semester leute was belegt haben
* IntroAI für dieses Jahr ist in Stud.IP nen komplett anderer Kurs als für letztes jahr 
    * Tobias hat was gebaut dass die abgleicht! Und er will k-anonymisierung machen. Das vergrößert die Daten sodass es für jedes Datum mindestens k (say 10) Studierende gibt für die etwas zutrifft. Da muss man Daten wegwerfen.