## Absolute basis

### [truncated] Singular Value Decomposition (SVD)
* Matrix Decomposition algorithm (factorizes a matric into a product of matrices)
* Idea: find the most valuable information and use a lower dimension to represent the same thing
* [4] of [DESC15] uses SVD to find missing properties in conceptnet - but according to [DESC15], "SVD produces a representation in which entities correspond to vectors, which should be compared in terms of cosine similarity rather than Euclidean distance" -> spatial relations such as betweeness and parallism wouldn't make sense

### Word-Scoring Methods

#### tf-idf

term frequency - inverse document frequency. Words that are rare overall and frequent in this document are weighted highly.

tf-idf for term $x$ within document $y$:

$$ w_{x,y} = \text{\textit{tf}}_{x,y} * log(\frac{N}{df_x}) $$

with $\text{tf}_{x,y}$ as the term-frequency of $x$ in $y$, \
$df_x$ as the document-frequency (the number of documents containing $x$) \
and $N$ being the total number of documents

[//]: # see also: https://towardsdatascience.com/3-basic-approaches-in-bag-of-words-which-are-better-than-word-embeddings-c2cbc7398016

#### PPMI

* Source [52] of [DESC15]
* See also: https://stackoverflow.com/a/58725695/5122790

## Dimension Reduction & Topic Modeling 

* Reasoning to use stuff like this: 
    * "Clustering" the terms [DESC15 (FIND WHAT EXACTLY DESC15 DOES), VISR12] - if eg. "love story" and "hilarious" are applied to an item, it is likely that "romantic comedy" is also relevant
    * most techniques try to find some latent (-> hidden/potential) dimensions from the obvious ones.

### Latent Semantic Analysis (LSA) / Latend Semantic Indexing (LSI)
* LSI is alternative name for LSA in linguistics
* *"applies rank-reduced singular value decomposition to a term-document matrix in order to express the documents and terms in a lower dimensional concept space*" (Quote [VISR12])
* [VISR12] use it to find relationships between tags and documents by the cosine similiarity in this concept space: the closeness of a document to a tag is the cosine similarity of the LSI-embedded document and an LSI-embedded pseudo-document that consists of only that tag
* [https://towardsdatascience.com/2-latent-methods-for-dimension-reduction-and-topic-modeling-20ff6d7d547]: 
    * objective: reduce dimensions for classification - distributional hypothesis says similar words are then close
    * How: construct term-document-matrix (using count-occurence, TF/IDF; (VISR12 take binary). Because that is generally very high-dimensional and sparse (and either noisy or includes many low-frequency words), we want to reduce dimensions - for that we use truncated/rank-reduced SVD. Based on this Matrix Factorization, the doc-vectors+the pseudocods are transfomred into a lower-dimensional spaces, and tag-lsi-sim(t,i) is then tha cosine similiarity of a document and the term making up the pseudodoc
* Sources: [39] of [DESC15]



### Latent Dirichlet Allocation (LDA)
(there would be a link here) https://towardsdatascience.com/2-latent-methods-for-dimension-reduction-and-topic-modeling-20ff6d7d547
* unsupervised learning, often used for topic modeling.
* Assumption in text: in each text, there are various topics, and each topic consists of various keywords (two layers of aggregation: documents to topics and topics to categories)


### Multi-dimensional scaling (MDS)
* dimensionality reduction
* Used by [DESC15] because distances stay equal
* builds a vector-space representation from pairwise similiarity judgements
* Sources: [40] of [DESC15]