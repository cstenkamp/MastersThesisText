TODO: Selbst für sachen wie bag-of-words oder tokenization kann ich entsprechend auf definitionen in section-required-algorithms verweisen

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

In these steps, the individual entities (coursedescriptions, placetypes, concatenated-reviews-per-movie) are embedded into a high-dimensional vector space. Optimally the number of dimensions of this space is decidable without constraints and the resulting space is euclidian. Because of these two requirements, \cite{Derrac2015} selected Multi-Dimensional Scaling (MDS) as their algorithm of choice, which takes a dissimilarity-matrix as input and returns a lower-dimensional embedding in which original distances are kept as close to the ones of the dissimilarity-matrix as possible. In their algorithm, the dissimilarity-matrix is created using the normalized angular distances of the bags-of-words of the respective entities. If the strict requirement for a metric space is dropped however, many different algorithms may instead be used at this point - not only different dimensionality reduction methods for the embedding, but also ones that don't rely on the distance matrix or even the bag-of-words at all, like document-embedding-techniques such as Doc2Vec (eg. used by \cite{which_one??}).

For this thesis, the creation of the dissimiliarity-matrix and the embedding are split into individual steps because both have a substantial runtime, and as the number of dimensions for the embedding is only relevant in the embedding-step, a lot of runtime can be saved if the dissimiliarity-matrix can be re-used for different embeddings and dimensions.

In this step we do

* First, we create a Doc-Term-Matrix counting the occurences of every word that occurs in any description and every description. 
    * This may optionally only include those terms that have a document-frequency of at least two (makes the dtm less sparse, but the information if a document contains many terms that are in no other document is lost)
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

These steps are split into three because they can individually take quite long, depending on the algorithm used to extract the candidates and because, again, there are settings that are only relevant lateron so we save a lot of computational work by saving interim results. Also, by looking at the dependency-graph in figure \ref{fig:dependency_graph} we see that these steps only depend on (each other and) the preprocessed descriptions, which means they can be run in parallel to the creation of the embedding (another good reason for cluster execution)

For these steps, the implementation of this thesis does differ from the one of DESC15. Their method depended on the dataset - as their placetypes-dataset was just a collection of tags and the number of tags with doc-freq >= 2 corresponded to their desired number of candidates anyway (around 22k), they just took all of these as candidates. For their movie-reviews-dataset, they considered all nouns, adjectives, nounphrases and adjective-phrases as detected by a POS-tagger. Doing something similar in the scope of this thesis led to suboptimal results, which is why alternative methods were developed. I would however argue that the difference here doesn't make a relevant difference (TODO: argue that lol). Also, while in the paper they claim to use n-grams as candidates, the dataset they publicly published does not contain n-grams (which is why I didn't use that one).

In these steps we do

* Extract the candidate-terms from the descriptions. This can be done either based on the frequency (meaning all terms with a minimal document-frequency), based on some notion of *importance* (based on scores like tf-idf or ppmi), or by more complex means of figuring out *important* keywords and keyphrases. 
    * As an example of the latter one, the **KeyBERT**-algorithm\footnote{\url{https://github.com/MaartenGr/KeyBERT}} is used in this thesis. To quote their README, "KeyBERT is a minimal and easy-to-use keyword extraction technique that leverages BERT embeddings to create keywords and keyphrases that are most similar to a document". 
    * The KeyBERT-model was incorporated in two ways, either on the original texts (advantage: that what it's trained on; disadvantage: requires a lot of post-processing as it's nontrivial to match the extracted phrases to the processed descriptions again, as they are possibly lemmatized, possibly stopwords are removed, and also the results of the keybert-algorithm doesn't split words the same way than nltk/sklearn do), or on the preprocessed texts (advantage: it is trivial to match extracted phrases to the processed descriptions, disadvange: not what keybert is trained on, so maybe worse results).
* Due to the aforementioned reasons, using KeyBERT requires a postprocessing of the candidate-terms, as the extracted phrases may not literally occur in the processed descriptions - hence the **postprocess_candidates** step which I need but which doesn't exist in DESC15 or the others. In my implementation however this additionally creates a mapping of keyphrases that can be considered equal. The numeric methods for they keyword-extraction shouldn't require this step, so there it's only a sanity-check double-checking if the keywords are actually in the documents they are extracted from.
* In any case, we'll only extract keywords with a sufficiently high document-frequency - lateron we'll need to classify those that contain the keyword vs those that don't, and for this classification to be useful a relevant percentage should be in the positive class. This min-doc-freq thus ideally depends on the size of the dataset (and is minimally, say, 25)
* Also in any case, we need the max-ngram size of the keyphrases. This is not explicitly done in DESC15, but as they claim to also extract adjective phrases, I'd say it's at least 5.
* TODO: write all about keyword-extraction using keybert and pp-keybert!
* Alternatively to the aforementioned KeyBERT-extraction, it is also possible to extract keywords by means of a quantification (tf-idf, tf and ppmi). When using this method, those terms and phrases are extracted that have a sufficiently high score of the respective quantification. Note that the respective scores are not global frequencies but depend on the combination of document and term (and the relation of this document to other documents), meaning one term may be important enough to be extracted in one document but not in another.
* sklearn is used to extract using tf-idf, the ppmi implementation is manual work as I didn't find a library for that. Did I mention we're using scipy sparse csr? good stuff, but even when doing so we're easily eating 20GB RAM
* In case of the quantifications, we extract either all those whose value is bigger than a fixed threshold, or a relative threshold of being in the top X% of all keyphrase-quantifications of all documents, while not extracing more than another absolute and/or relative threshold per-document. The keyphrases in the top Y% of all ones will be extracted anyway, even if it goes above the aforementioned threshold (Y >> X). Another threshold allows to extract a minimal number of the best-scoring keyphrases per-document anyway.
<!--TODO: write in dataset-section how irrelevant the stuff about extraction is for my dataset because there are only 6k unique x-grams anyway so just taking all is the best thing to do anyway -->
* Afterwards, the candidate-terms are postprocessed - this is especially relevant for the KeyBERT-methods, where the extracted candidates may not literally occur in the texts (especially 2+-grams), so this step applies the same processing as done for the descriptions to the candidates and tries to match them to n-grams actually occuring in the text. Those where the matching shouldn't work (or that become longer than the demanded max-n-gram because they would also contain stopwords or smth) are dropped. If a lot of processing needed to be done, a mapping of how it literally occured in the text to how it is now in the bag-of-ngrams is saved as well. For the distributional methods, nothing of this is necessary as the keywords are literally extracted. After this step, the original description-texts are not needed anymore.
* As a last step, a doc-term-matrix is created from these postprocessed candidates, of the shape n_docs * n_candidate-terms. When we make a histogram counting for every keyword how many documents it appears in, we see an exponential decrease (plot: "Docs per Keyword")
* This doc-term-matrix then gets filtered, such that only candidates that have a minimal document-frequency (if use_n_docs_count, otherwise those that occur at least xyz times) are considered from now on, and a quantification is applied to the doc-term-matrix (one of count, binary, tfidf, or binary) (so the relation of term to document may be expressed by something else than count - so if we later compare the ranking induced by the svm to this maybe something else thatn the count stands there - I'm expecting that for my dataset tf-idf is much more valuable than the count bc no concatenated reviews or tags.)

Configs influencing this Step: 

* Extraction-Method (one-of-the-KeyBERTs vs one-of-the-quantifications vs all)
* TODO: KeyBERT stuff
* If all:   
    * min-doc-freq (and theoretically if this is n-docs-count or n-count)
    * max-ngram
* If by-quantification:
    * extraction_method (tfidf, tf, ppmi)
    * min-doc-freq (and theoretically if this is n-docs-count or n-count)
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
* Additionally, the resulting SVM has a hyperplane as decision surface. The distance of a point to it's orthogonal projection onto that hyperplane can be seen as proportional to how much this point is considered to be in the respective class of the SVM. One can use these distances to enduce a ranking how prototypicality. This ranking can be compared to other heuristics encoding it, such as the ranking induced by the per-document-frequencies of the terms for all documents, or it's PPMI or tf-idf representations.
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