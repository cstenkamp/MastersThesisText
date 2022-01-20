## Absolute basis

### [truncated] Singular Value Decomposition (SVD)
* Matrix Decomposition algorithm (factorizes a matric into a product of matrices)
* Idea: find the most valuable information and use a lower dimension to represent the same thing
* [4] of [DESC15] uses SVD to find missing properties in conceptnet - but according to [DESC15], "SVD produces a representation in which entities correspond to vectors, which should be compared in terms of cosine similarity rather than Euclidean distance" -> spatial relations such as betweeness and parallism wouldn't make sense

### "nonnegative matrix factorization (NMF)"

(wo kam das vor? Ich glaube DESC15 write that it's the normally used way to do xyz)

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

* Main things: LSA/LSI and LDA. https://towardsdatascience.com/2-latent-methods-for-dimension-reduction-and-topic-modeling-20ff6d7d547
    * LSA mainly dimension reduction;  LDA mainly topic modeling 
    * Input for both: Bag-of-words matrix


### Latent Semantic Analysis (LSA) / Latend Semantic Indexing (LSI)
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
					* M (m*m) = U (m*n left singular) * E (n*n diagonal with pos real vals) * V* (n*m; transpose of m*n right singular)
						(diagonal: values not on main diag = 0; singular: singular if determinant=0 or a square matrix that does not have a matrix inverse.)
				* Regarding optimal #topics: consider each topic as a cluster and find out the effectiveness of a cluster using the Silhouette coefficient.
				* or topic coherence (see https://www.datacamp.com/community/tutorials/discovering-hidden-topics-python for details)


### Latent Dirichlet Allocation (LDA)
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