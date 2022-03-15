## Absolute basis

### Bag-of-Words

\label{sec:techniques:bow}

* Write how a Bag-Of-Words is created and what it shortcomings are and find a source that compares how good a Bag-Of-Words (that necessarily doesn't contain and information about their position) can be, compared to better document embeddings like LSTMs, Doc2Vec or whatever else there is (I mean after all, a "not" may be ignored and the meaning inversed which should be supergau), and also how much better it becomes if one also consideres 2-grams, 3-grams, ...

### [truncated] Singular Value Decomposition (SVD)
* Matrix Decomposition algorithm (factorizes a matric into a product of matrices)
* Idea: find the most valuable information and use a lower dimension to represent the same thing
* [4] of [DESC15] uses SVD to find missing properties in conceptnet - but according to [DESC15], "SVD produces a representation in which entities correspond to vectors, which should be compared in terms of cosine similarity rather than Euclidean distance" -> spatial relations such as betweeness and parallism wouldn't make sense

### "nonnegative matrix factorization (NMF)"

(wo kam das vor? Ich glaube DESC15 write that it's the normally used way to do xyz)

### Word-Scoring Methods

## Dimension Reduction & Topic Modeling 

* Reasoning to use stuff like this: 
    * "Clustering" the terms [DESC15 (FIND WHAT EXACTLY DESC15 DOES), VISR12] - if eg. "love story" and "hilarious" are applied to an item, it is likely that "romantic comedy" is also relevant
    * most techniques try to find some latent (-> hidden/potential) dimensions from the obvious ones.

* Main things: LSA/LSI and LDA. https://towardsdatascience.com/2-latent-methods-for-dimension-reduction-and-topic-modeling-20ff6d7d547
    * LSA mainly dimension reduction;  LDA mainly topic modeling 
    * Input for both: Bag-of-words matrix


### Latent Semantic Analysis (LSA) / Latend Semantic Indexing (LSI)

DESC15: "In infor- mation retrieval, it is common to represent documents as vectors with one component for every term occurring in the corpus. In many other applica- tions (and sometimes in information retrieval) some form of dimensionality reduction is typically used to obtain vectors whose components correspond to concepts. One of the most popular techniques, called latent semantic analysis (LSA [39]), uses singular value decomposition (SVD) to this end. Multi-dimensional scaling (MDS [40]) is another popular method for dimen- sionality reduction, which builds a vector-space representation from pairwise similarity judgements."

* LSI is alternative name for LSA in linguistics
* *"applies rank-reduced singular value decomposition to a term-document matrix in order to express the documents and terms in a lower dimensional concept space*" (Quote [VISR12])
* [VISR12] use it to find relationships between tags and documents by the cosine similiarity in this concept space: the closeness of a document to a tag is the cosine similarity of the LSI-embedded document and an LSI-embedded pseudo-document that consists of only that tag
* [https://towardsdatascience.com/2-latent-methods-for-dimension-reduction-and-topic-modeling-20ff6d7d547]: 
    * objective: reduce dimensions for classification - distributional hypothesis says similar words are then close
    * How: construct term-document-matrix (using count-occurence, TF/IDF; (VISR12 take binary). Because that is generally very high-dimensional and sparse (and either noisy or includes many low-frequency words), we want to reduce dimensions - for that we use truncated/rank-reduced SVD. Based on this Matrix Factorization, the doc-vectors+the pseudocods are transfomred into a lower-dimensional spaces, and tag-lsi-sim(t,i) is then tha cosine similiarity of a document and the term making up the pseudodoc
* Sources: [39] of [DESC15]

0) https://www.datacamp.com/community/tutorials/discovering-hidden-topics-python
* Latent semantic analysis (LSA)
    * Analyses realationships between a set of documents and the terms they contain.
    * When applied to Information retrieval, it's sometimes called LSI (latent semantic indexing).	
        * LSI used SVD to identify patterns in the relationships between the terms and concepts contained in an unstructured collection of text.Distributaitnal Hypothesis.
        * Correlate semantically related terms that are latent in a collection of text
        * Queries against a set of documents that have undergone LSI will return results that are conceptually similar in meaning to the search criteria even if the results don’t share specific word(s) with the search criteria. 
    * IN LSI, the term-dcoument-matrix is created, and ON THAT you run SVD to reduce the #rows:
        * https://en.wikipedia.org/wiki/Latent_semantic_analysis#Rank-reduced_singular_value_decomposition

    * See https://www.datacamp.com/community/tutorials/discovering-hidden-topics-python: 
        * LSA is typically used as a dimension reduction or noise reducing technique.
        Steps:
        * 1) make term-document-matrix (rows terms, columns docs)
        * 2) matrix decomposition on the document-term matrix using Singular value decomposition to learn latent topics
                -> m = #terms; n = #topics
                Term-Document-Matrix (m*m) = words-per-topic (m*n) * topic-importance (n*n diagonal) * topics-distribution-across-docs (n*n singular)
            * SVD is a matrix factorization method that represents a matrix in the product of two matrices.
                -> M (m*m) = U (m*n left singular) * E (n*n diagonal with pos real vals) * V* (n*m; transpose of m*n right singular)
                    (diagonal: values not on main diag = 0; singular: singular if determinant=0 or a square matrix that does not have a matrix inverse.)
            * Regarding optimal #topics: consider each topic as a cluster and find out the effectiveness of a cluster using the Silhouette coefficient.
            * or topic coherence (see https://www.datacamp.com/community/tutorials/discovering-hidden-topics-python for details)


### Latent Dirichlet Allocation (LDA)

main idea is to learn a representation in terms of salient features, where each of these features is described using a cluster of natural language terms. "This is somewhat similar to Latent Dirichlet Allocation (LDA) which learns a representation of text documents as multinomial distributions over latent topics, where each of these topics corresponds to a multinomial distribution over words (Blei et al., 2003). Topics tend to correspond to salient features, and are typically labelled with the most probable words according to the corre- sponding distribution" [quote: AGKS18]

(there would be a link here) https://towardsdatascience.com/2-latent-methods-for-dimension-reduction-and-topic-modeling-20ff6d7d547
* unsupervised learning, often used for topic modeling.
* Assumption in text: in each text, there are various topics, and each topic consists of various keywords (two layers of aggregation: documents to topics and topics to categories)

1) http://blog.echen.me/2011/08/22/introduction-to-latent-dirichlet-allocation/
2) https://radimrehurek.com/gensim/auto_examples/core/run_topics_and_transformations.html#sphx-glr-auto-examples-core-run-topics-and-transformations-py
3) https://radimrehurek.com/gensim/auto_examples/tutorials/run_lda.html

	The main idea underlying our method is to learn a representation in terms of salient features, where each of these features is de- scribed using a cluster of natural language terms. This is somewhat similar to Latent Dirichlet Al- location (LDA), which learns a representation of text documents as multinomial distributions over latent topics, where each of these topics corre- sponds to a multinomial distribution over words (Blei et al., 2003). Topics tend to correspond to salient features, and are typically labelled with the most probable words according to the corre- sponding distribution. However, while LDA only uses bag-of-words (BoW) representations, our fo- cus is specifically on identifying and improving features that are modelled as directions in seman- tic spaces. One advantage of using vector spaces is that they offer more flexibility in how addi-

### Multi-dimensional scaling (MDS)
* dimensionality reduction
* Used by [DESC15] because distances stay equal
* builds a vector-space representation from pairwise similiarity judgements
* Sources: [40] of [DESC15]


### Projecting and playing around with coordinate system

So how do we project the point onto the plane?
* [https://stackoverflow.com/a/17661431] all you have to do is find the perpendicular (abbr here |_) distance from the point P to the plane, then translate P back by the perpendicular distance in the direction of the plane normal. The result is the translated P sits in the plane.



### Other stuff

I can take a bit of the definitions from here:
  https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction 
  ("We call vectorization the general process of turning a collection of text documents into numerical feature vectors. This specific strategy (tokenization, counting and normalization) is called the Bag of Words or “Bag of n-grams” representation. Documents are described by word occurrences while completely ignoring the relative position information of the words in the document.")