## How to deal with the fact that my dataset is different

Den ganzen "wo ist mein dataset anders als deren" Kram

* Datensatz ist anders als concatenated-movie-reviews und ich deswegen nicht einfach "je öfter 'scary' desco scarier" machen kann. Wege damit umzugehen sind elaboriert in Section XYZ
* Da hatte ich schon mehr sehr alte sachen!!!
* Der Kappa-Score der rankigns vergleicht ist für mich ne kack metric weil ich ebennicht reviews nehme und more-occurences better-candidate heißen -> gucken wie ich stattdessen gute dimensionen und cluster finde (klingt doch so als sei accuracy/f1/... doch wichtig) => WE EXPECT dass accuracy/f1/... zu besseren ergebnissen führt!

## IDK

TODO: Zum Schritt "Clustern" hinzufügen (also WARUM wir clustern):
	* Ich zieh ja Daten als candidate terms raus nach denen man eine Dimension/Richtung benennen kann, wie “scary” bei den filmbeschreibungen. Die kann ich mir dann angucken zwischen 20 und 3000 Begriffen easy, alle mit Zahlenvektor (kommen ja auch aus nem Vector space). Dann will ich die Clustern, also nahe sind ähnlich: In Filmen, in deren Beschreibung das Wort “scary” oft vorkommt, kommt ebenfalls das wort “horror” oder “gore” oft vor. → das sollte ein Cluster sein.

### Clarifications

1) It *IS* okay if common words (like "course") are in clusters, it is NOT the case that as soon as the word occurs once it is said to have a certain property. ("Wenn cluster-threshold zu groß, kommt “A1” in ein cluster mit “Course” and everything is over" is FALSE). However it IS not too good -> A cluster with many words like "course" in it has a high degree of randomness (there is no information gain by such words, it occurs random across courses, a cluster of courses that mention that they are courses is useless) The word occurs randomly, if a course is assumed to have a certain property because of that it's certainly wrong



%TODO:
% * reference yamls again
% * Im Text link zu binder bei results section der auf die notebooks/analyze_results/analyze_pipeline_results.ipynb referenziert, und für die tables auch!
% * Schreiben dass ich einige Claims oder nonclaims von denen prüfe, bspw nutzen sie immer PPMI ohne je tf-idf zu testen
% * Wie lange der ganze Kram dauert - MDS hat quadratic complexity etc
% * Das mit dem Koordinatensystem drehen passiert gar nicht so wie ich dachte dass es passiert...?!
% * Tabelle
% 	* Einduetig rausschreiben welche der 3 paper [DESC15] [AGKS18] [RaZb20] welche parameter-werte verlangen und !!welche optimal waren!! angucken welche Kombi die Beste Performance hatte und die entsprechend markieren (und im yaml haben!)!


% 	* POSSIBLE EXTRA-STEPS FOR ALGORITHM
% 		* BOOTSTRAP MORE CANDIDATES (AFTER EXTRACT CANDIDATES)
% 			* [VISR12]: LSI
% 				* Options:
% 					* What to take for the term-document-matrix
% 						* [VISR12]: 
% 							* tag-applied
% 							* tag-count
% 							* tag-share (the number of times tag t has been applied to item i, divided by the number of times any tag has been applied to item i)
% 						* relative-tag-count (tag-count / text-len) or tag-count / distinct-words-in-text
% 						* See also: https://en.wikipedia.org/wiki/Latent_semantic_analysis#Term-document_matrix
% 				* Parameters:
% 					#dims for the rank reduction (see https://en.wikipedia.org/wiki/Latent_semantic_analysis#Rank-reduced_singular_value_decomposition)

% * Schritte des Algorithmus bewerten:
% 	* "that the better Ht separates entities to which t applies from the others in S,the better \vec{v_t} models the term t." --> wie sinnvoll ist diese measure wenn das verhältnis literally 14.900 zu 100 ist, dann haben halt 99.33% der Daten einen rank von 0 ?!
% 	* DESC15 write they select Kappa "due to its tolerance to class imbalance." -> Does that mean I have to set the weight?! Außerdem weiß ich ja superviel ebennicht, like which weighting they use! I don't like
% 	* Der letzte Schritt mit dem Clustern der good-kappa-ones ist wirklich very basic und hat very much room for improvement



%TODO: maybe describe shortly what the improvements from  Ager2018 Alshaikh2020 were? 

% * Regarding DESC15 vs AGKS18 vs Alshaikh2020:
% 	* didn't somebody say that cohen's kappa sucks!?!
% 	* Alshaikh2020: 
% 		* use affinity propagation "for getting rid of the clusters of informative words", similar to how they did it in their 2019 paper
% 			-> affinity propagation has a so-called preference parameter, den als config lassen - usual, this parameter is chosen relative to the median µ of the affinity scores. For the methods Sub and Or- tho, we considered values from {0.7µ, 0.9µ, µ, 1.1µ, 1.3µ}
% 		* do kappa ON BINARY!!!
% 		* say that for them, the binary "does the word occur in the description" is the only sensible signal, no ppmi or anything! (page 2, footnote 1 of RaZb20)
% 		* "When representing a particular entity in a conceptual space, we need to specify which domains it belongs to, and for each of these domains we need to provide a corresponding vector." 
% 		* then they show their example of something that is not seperable with a hyperplane unless we specify subdomains, maybe just steal their plot that explains their one contribution to 99%
% 	* DESC15: 
% 		* "Here we use the assumption that the better Ht separates entities to which t applies from the others in S,the better \vec{v_t} models the term t." --> allein von der aussage muss man das mit den induzierten rankings echt nicht machen, sondern halt nur auf classification quality (-> metrics like accuracy) gucken, bzw kappa anhand der binären klasse berechnen --> the ranking induced by count, or the baremetal count?
% * The "Disentangled" from their title means "feature-based"













=======================================================================================================================
========================================================= ??? =========================================================
=======================================================================================================================


















* In principle Derrac2015, but with some components from Ager2018 and Alshaikh2020 as well as some own stuff
    * Because of the nature of the dataset I need to do some things differently 
        * I'm not working with reviews or collections-of-tags, that means their "how does this dimension correspond to the count in the reviews" doesn't make sense
            * their algorithm is tailored to this. Take their success-metric for the SVMs splitting the embedding. The more often the word "scary" comes in the concatenated reviews, the more scary the movie is. Sounds legit. The more often the people that took pictures at a particular place mentioned the "nature" of that, the more relevant "nature" is to that place. Also legit. But in the descriptions for courses that involve a lot of mathematics, it is not necessarily the case that the term "mathematics" occurs often. So due to the different nature of my dataset I have to go beyond their algorithm at some points - in this case it is probably the case that different kinds of mathematical terms actually do occur more often, so I'd need calculate these kinds of kappas not based oon a single term but ALREADY on a cluster of terms (... and I can bootstrap my way there, because after I do this I get more words to add to my cluster, rinse and repeat!)
        * In their placetypes-dataset they just took ALL terms as candidates, I have too many for that 
    * Besides, the architecture is so modular that one can easily exchange some components in some step to do something else
    * ...which on the other hand means that I really have a metric ton of hyperparameters (which means not only numerical stuff like a number of dimensions, but also "which algorithm is used in thisandthis step (like mds/isomap/... for dimensionality reduction, or different ways for keyword extraction, or ...))

* While [AGKS18] split the algorithm into 4 Steps (their postprocessing being one of them), I'll subdivide it even more. The steps of [AGKS18] are however: Step 1: Generate candidate feature directions, Step 2: Filter Candidate Feature Directions, Step 3: Cluster Candidate feature Directions, Step 4: Fine-Tune feature directions.

[//]: # TODO: Do I want to have a section for every single step of the pipeline containing what paramters there are in this step?!
 
### Step 1: Pre-process the texts
[list of steps]
* The above can be done manually step-by-step mostly based on NLTK tools, or in one step using `sklearn`'s `CountVectorizer`. 



    * Filter out all descriptions that don't have a minimal number of words

* Configs influencing this Step: 
    * Translate-Policy (translate, original language, only-one-language)
    * PP-Components: sentwise_merge, add_title, add_subtitle, remove_htmltags, sent_tokenize, convert_lower, remove_stopwords, lemmatize, remove_diacritics, remove_punctuation
    * Another config is if this should all be done by Sklearn's sent-tokenizer, in which case some settings (like lemmatizing or sent-tokenizing) are not available (still relevant: stopwords, max_ngram, remove_htmltags, convert_lower, remove_diacritics, only_partnered)
    * MIN_WORDS_PER_DESC

    [//]: # TODO: Do I have everything for preprocessing? max-ngram, min_words_per_desc, ...?


### Step 2 and 3: Create Dissimilarity Matrix and the Embedding


 Multi-Dimensional Scaling (MDS) as their algorithm of choice, which takes 
 
 In their algorithm, the dissimilarity-matrix is created using the normalized angular distances of the bags-of-words of the respective entities. If the strict requirement for a metric space is dropped however, many different algorithms may instead be used at this point - not only different dimensionality reduction methods for the embedding, but also ones that don't rely on the distance matrix or even the bag-of-words at all, like document-embedding-techniques such as Doc2Vec (eg. used by \cite{which_one??}).

For this thesis, the creation of the dissimiliarity-matrix and the embedding are split into individual steps because both have a substantial runtime, and as the number of dimensions for the embedding is only relevant in the embedding-step, a lot of runtime can be saved if the dissimiliarity-matrix can be re-used for different embeddings and dimensions.

In this step we do

* First, we create a Doc-Term-Matrix counting the occurences of every word that occurs in any description and every description. 
    * This may optionally only include those terms that have a term-frequency of at least two (makes the dtm less sparse, but the information if a document contains many terms that are in no other document is lost)
    * This may optionally include n-grams (which makes the dtm a lot more sparse, but alleviates some of the typical problems of bag-of-words-representations at last to a certain degree) (see \ref{sec:techniques:bow} regarding BoW-shortcomings)
* Afterwards, the Doc-Term-Matrix may be converted into a quantification, such that the respective Bag-Of-Word Representations of the documents don't contain the raw counts, but the respective tf-idf[TODO: ref this in required algorithms] or ppmi[TODO: ref this in required algorithms]-representations, relative to all documents and all possible terms.
    * Possible Quantifications: ppmi, tf-idf, tf, count, binary
* From this quantified Doc-Term-Matrix, a dissimilarity-matrix is generated. This requires a measure for the dissimlarity - in the original paper, this is what they call "normalized angular difference": $ang(e_i, e_j) = \frac{2}{\pi}*arccos \left( \frac{\vec[m]{v_{e_i}}*\vec[m]{v_{e_j}}}{||\vec[m]{v_{e_i}}||*||\vec[m]{v_{e_i}}||} \right)$, which is equal to $\frac{2}{\pi}*arccos(-cosine+1)$, where **cosine** stands for the default cosine distance.
* Possible Sanity-check here: look at the close descriptions 
* My algorithm then saves this dissimilarity-matrix, and what follows is the embedding.
* Because this dissimilarity-Matrix is far too high-dimensional and sparse, a dimensionality-reduction is applied. Because it is important to DESC15 that the embedding is a euclidian space, they go for MDS. In my Code, pre-implemented methods are MDS, Isomap and t-SNE (the last one however only works for very little numbers of dimension). Also, in this step, we must decide for a number of dimensions - in my case that's the ones of the replicated paper (20, 50, 100, 200), plus 3 dimensions as sanity-check as it can easily be inspected.
* Grains of salt: MDS-implementation of scikit-learn seems broken unless we initialize from something. Also of course MDS and the other embedding-algorithms have arguments we must decide (most importantly we decide for metric MDS)
* Possible Sanity-check here: look at the close descriptions in the final embedding

Configs influencing this Step: 

* General Technique (either BoW-Embedding + Distance Matrix + Dimensionality-Reduction or Straight Document Embedding)
* If BoW+Distance+Dimensionality-Reduction:
    * DISSIM_MAT_ONLY_PARTNERED
    * NGRAMS_IN_EMBEDDING (and if true MAX_NGRAM)
    * quantification_measure (ppmi, tf-idf, tf, count, binary)
    * dissim_measure (mean_ang_dist, ...)
    * embed-algo (isomap, tsne, mds)
    * embed-dimensions (3, 20, 50, 100, 200)

<!---
* TODO: markieren was für configs die haupt (und zweit- und dritt-) autoren hatten (also for which ones they had more than 1 value, and then the values they also had)
* TODO: in results schon schreiben (und tabellen haben!) wie schön nah sich ähnliche dinge schon in BoW-embedding und dimreduced-embedding sind. Neben den ganzen ["asd (tutorial 1)", "asd (tutorial 2)"] auch welche mit ner mindest-levensthein-distance haben, UND nen Plot wie sehr levensthein-distance und nähe im embedding korellieren. UND ne tabelle wie ähnlich nahe-kurse im BoW-embedding und im dimreduced-embedding sind möglicherweise einfach nen kappa score um das ranking der ähnlichsten zu vergleichen)
* TODO: Tag-share from VISR12
* TODO: When I calculate PPMI here, relative to all documents and all possible terms, ist das relevant/unintended dass die Grundgesamtheit (alle possible terms) ja anders ist als wenn ich das später nur auf den keyphrases mache? Kann ich das optional gleihcsetzen?
* TODO: How these steps differ if we don't use BoW or Dissimilarity-Matrices at all
-->

### Steps 4, 5 and 6: Extracting Candidate Terms, Postprocessing them, creating the Doc-Term-Matrix for the Candidate-Terms and filtering it

<!-- 
TODO: To which steps of DESC15 or whichever one also specified their steps this corresponds
-->



* Due to the aforementioned reasons, using KeyBERT requires a postprocessing of the candidate-terms, as the extracted phrases may not literally occur in the processed descriptions - hence the **postprocess_candidates** step which I need but which doesn't exist in DESC15 or the others. In my implementation however this additionally creates a mapping of keyphrases that can be considered equal. The numeric methods for they keyword-extraction shouldn't require this step, so there it's only a sanity-check double-checking if the keywords are actually in the documents they are extracted from.
* In any case, we'll only extract keywords with a sufficiently high term-frequency - lateron we'll need to classify those that contain the keyword vs those that don't, and for this classification to be useful a relevant percentage should be in the positive class. This min-term-freq thus ideally depends on the size of the dataset (and is minimally, say, 25)
* Also in any case, we need the max-ngram size of the keyphrases. This is not explicitly done in DESC15, but as they claim to also extract adjective phrases, I'd say it's at least 5.
* TODO: write all about keyword-extraction using keybert and pp-keybert!
* Alternatively to the aforementioned KeyBERT-extraction, it is also possible to extract keywords by means of a quantification (tf-idf, tf and ppmi). When using this method, those terms and phrases are extracted that have a sufficiently high score of the respective quantification. Note that the respective scores are not global frequencies but depend on the combination of document and term (and the relation of this document to other documents), meaning one term may be important enough to be extracted in one document but not in another.
* sklearn is used to extract using tf-idf, the ppmi implementation is manual work as I didn't find a library for that. Did I mention we're using scipy sparse csr? good stuff, but even when doing so we're easily eating 20GB RAM
* In case of the quantifications, we extract either all those whose value is bigger than a fixed threshold, or a relative threshold of being in the top X% of all keyphrase-quantifications of all documents, while not extracing more than another absolute and/or relative threshold per-document. The keyphrases in the top Y% of all ones will be extracted anyway, even if it goes above the aforementioned threshold (Y >> X). Another threshold allows to extract a minimal number of the best-scoring keyphrases per-document anyway.
<!--TODO: write in dataset-section how irrelevant the stuff about extraction is for my dataset because there are only 6k unique x-grams anyway so just taking all is the best thing to do anyway -->
* Afterwards, the candidate-terms are postprocessed - this is especially relevant for the KeyBERT-methods, where the extracted candidates may not literally occur in the texts (especially 2+-grams), so this step applies the same processing as done for the descriptions to the candidates and tries to match them to n-grams actually occuring in the text. Those where the matching shouldn't work (or that become longer than the demanded max-n-gram because they would also contain stopwords or smth) are dropped. If a lot of processing needed to be done, a mapping of how it literally occured in the text to how it is now in the bag-of-ngrams is saved as well. For the distributional methods, nothing of this is necessary as the keywords are literally extracted. After this step, the original description-texts are not needed anymore.
* As a last step, a doc-term-matrix is created from these postprocessed candidates, of the shape n_docs * n_candidate-terms. When we make a histogram counting for every keyword how many documents it appears in, we see an exponential decrease (plot: "Docs per Keyword")
* This doc-term-matrix then gets filtered, such that only candidates that have a minimal term-frequency (if use_n_docs_count, otherwise those that occur at least xyz times) are considered from now on, and a quantification is applied to the doc-term-matrix (one of count, binary, tfidf, or binary) (so the relation of term to document may be expressed by something else than count - so if we later compare the ranking induced by the svm to this maybe something else thatn the count stands there - I'm expecting that for my dataset tf-idf is much more valuable than the count bc no concatenated reviews or tags.)

Configs influencing this Step: 

* Extraction-Method (one-of-the-KeyBERTs vs one-of-the-quantifications vs all)
* TODO: KeyBERT stuff
* If all:   
    * min-doc-freq (and theoretically if this is n-docs-count or n-count) TODO: this should be called term-freq!!!!
    * max-ngram
* If by-quantification:
    * extraction_method (tfidf, tf, ppmi)
    * min-doc-freq (and theoretically if this is n-docs-count or n-count) TODO: this should be called term-freq!!!!
    * max-ngram
    * minval_abs or minval_perc (these are per-all-docs), maxperdoc_abs and maxperdoc_rel (per-doc), forcetake_perc, minperdoc
* Then regardless of the extraction_method:
    * candidate_min_term_count (and use_n_docs_count)
    * quantification for the doc-temr-matrix (`dcm_quant_measure`)

<!--
TODO: Write just the right amount about KeyBERT (I mean the algorithm, not how I used it)
-->


### Step 7: Creating Candidate SVMs

This step is the most important one of the algorithm, where we bring together the embedding of the individual entities and the extracted keyphrases. Here we try to split those samples where a keyphrase occurs from those where it doesn't, using a linear classifier. The orthotogonal to the resulting decision-hyperplane is then used as axis, onto which the entities are mapped - the further away from the plane the mapping of a point onto the orthogonal, the more the entity is said to have the attribute encoded by the phrase responsible for the hyperplane. A score function compares the ranking induced by this to the ranking induced by number of occurences (or quantification-value) of the respective keyphrase of all documents, such that only those terms where the correspondance of these rankings exceeds a certain threshold are considered as candidate directions henceforth.

In this step we do

* For every candidate-term, take the quantifications from the doc-term-matrix and binarize it, such that we have two classes: one with all descriptions in which the term does occur and one with those where it doesn't.
* On that we then train a linear classifier such as an SVM. From that, we can then calculate binary classification-quality-metrics such as accuracy, precision, recall, f1 and bin2bin-kappa. 
* Additionally, the resulting SVM has a hyperplane as decision surface. The distance of a point to it's orthogonal projection onto that hyperplane can be seen as proportional to how much this point is considered to be in the respective class of the SVM. One can use these distances to enduce a ranking how prototypicality. This ranking can be compared to other heuristics encoding it, such as the ranking induced by the per-term-frequencies of the terms for all documents, or it's PPMI or tf-idf representations.
* TODO: reformulate! We measure the faithfulness of this yadda yadda 
* To be able to look at the best one lateron, we save a bunch of metrics here, comparing the ranked-data, digitized data, you name it.

Configs influencing this Step: 
* `classifier` (SVM, SVM-with-squared-hinge)
* (later: which metric to be used)

### Step 8: Clustering the directions etc




## Regarding Parameter-Choices
### Preprocessing

* Translate-policy (TODO: rather write here about the accuracy of langdetect and translate and the like): Obviously the translation won't be perfect, so we lose quality from translating, but on the other hand if it's in english you can use wordnet, which is a lot better than GermaNet (https://uni-tuebingen.de/fakultaeten/philosophische-fakultaet/fachbereiche/neuphilologie/seminar-fuer-sprachwissenschaft/arbeitsbereiche/allg-sprachwissenschaft-computerlinguistik/ressourcen/lexica/germanet-1/)

* Kappa-Weighting-Algorithm: Yet another point where \cite{Derrac2015} are really low on information what parameters they used. Sklearn allows different weighting types\footnote{\url{https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html\#sklearn.metrics.cohen_kappa_score}} - TODO: explain what that changes respectively!!}, and as this plot: ![kappa_weighting_funcs](graphics/figures/which_weigthing_algo.png){#fig:which_weighting_algo} TODO: also generally write about if Kappa is a good choice (see eg \url{https://en.wikipedia.org/wiki/Cohen%27s_kappa})

* Candidate word threshold: movies has samples-to-threshold value of 100, placetypes has 35, 20newsgrups has 614 so for 8000 courses any threshold from 2 to 25 seems reasonable? \cite{Derrac2015} say they intentionally kept the number of candidateterms approximate equal (at around 22.000), so to do the same I'd need a threshold of [TODO: optimal value]




TODO: schreiben dass tf-idf allein deswegen the algorithm of choice ist weil ich nicht wüsste wie man PPMI macht ohne dass es für datasets der größe wie ich sie haben will mit "nur" 64GB RAM klarkommt

## Loose Quotes:
* from Alshaikh2020: "Their core assumption is that words describing semantically mean- ingful features can be identified by learning for each candi- date word w a linear classifier which separates the embed- dings of entities that have w in their description from the oth- ers. The performance of the classifier for w then tells us to what extent w describes a semantically meaningful feature"
* from Alshaikh2020: "The learned vectors will be referred to as feature directions to emphasize the fact that only the ordering induced by the dot product d_i · e matters"




# Original [of this thesis] Contributions to the algorithm 


their algorithm is tailored to concatenated-reviews or concatenated-bags-of-tags. Take their success-metric for the SVMs splitting the embedding. The more often the word "scary" comes in the concatenated reviews, the more scary the movie is. Sounds legit. The more often the people that took pictures at a particular place mentioned the "nature" of that, the more relevant "nature" is to that place. Also legit. But in the descriptions for courses that involve a lot of mathematics, it is not necessarily the case that the term "mathematics" occurs often. So due to the different nature of my dataset I have to go beyond their algorithm at some points - in this case it is probably the case that different kinds of mathematical terms actually do occur more often, so I'd need calculate these kinds of kappas not based oon a single term but ALREADY on a cluster of terms (... and I can bootstrap my way there, because after I do this I get more words to add to my cluster, rinse and repeat!)

% * Steht ja schon woanders dass mein Datensatz anders ist als concatenated-movie-reviews und ich deswegen nicht einfach "je öfter 'scary' desco scarier" machen kann. Da gibt's several ways mit umzugehen
	% * Das sich-die-richtigen-wörter-per-candidate-svm-bootstrappen
	% * Mit LSI rausfinden welche Terme genausogut in dem Text hätten vorkommen können (hab ich auch irgendwo schon)
	% * Explizit einfach zu gucken "Welche Terme kommen oft in den gleichen dokumenten vor" (und das inverse (steht iwo im code)), und dann ne candidate SVM für grouped terms anstelle von einzelterms machen (auch schon iwo als code)
	% * Mit Wordnet hypernyms/hyponyns und synonyms zu finden damit ebenfalls zu arbeiten (kann man wit wordnet angeben welches abstraktionsniveau ich haben will?)
	%     * Abstraktionsniveau gibt's nicht in wordnet, das heißt das richtige layer zu finden ist schwer. Was man auf jeden Fall machen kann ist die Terme zu den bases ihrer synsets umzuwandeln (dadurch wird aus "math" und "mathematics" das gleiche), aber in anderen Fällen ist es halt so dass ich die Candidate-Terms schon vorher brauche und nur sagen kann "diese entity enhält X wörter die halt hyponyms von dem Term sind"


# Unsorted algorithm stuff

* Dass ich, genau wie (wars ager oder alshaikh?), auch die möglcihkeit hab eine neue svm für die cluster_directions zu machen, und dafür halt den best-30%-weg gehe weil gerne mal zu viele positive samples isnd

* dass wir ja nur ne dulli-SVM ohne kernel trick machen, weil wir ja eben with-hyperplane-linear für den eigentlichen space sein wollen (kerneltrick ist ja "Projecten in nem anderen space, damit das was da linear ist bei uns nonlinear ist" und ich will linear sein)



* New options:
    * Cluster&Filter:
        * <TODO>Associate-nongreat-algorithm (k-means, DESC15 one, ..?)
        * <TODO>Associate-nongreat-threshold (if those ones that are far away from all are ignored) ("smart weighting function that takes into account the kappa-score of the term and/or the closeness to the original clustercenter (to threshold which cluster they are added to)")
        * <TODO>weight which-candidates-may-cluster: the closer the orthogonals (cosine-dist) AND the closer their intercepts, the more we want to have them in a cluster.
        * <TODO>Cluster-Direction-Algorithm (onlymain, average, weighted-by-kappa-averaged, weighted-by-distance-to-center-averaged, redo-decision-plane)
        * <TODO>the better ways to find the name of the cluster
    * Decision-Trees:
        * which additional to test against
        * if all-at-once or one-vs-rest
        * depth of the tree (1, 3, unbound)
        * train-test-split (2:1) or cross-validation