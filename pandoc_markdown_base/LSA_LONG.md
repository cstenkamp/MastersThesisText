## Latent Semantic Analysis (LSA) / Latent Semantic Indexing (LSI)


% from \cite{Turney2010}: 
% Context: Smoothing the frequency matrix - keep comparison performance high but the comparision process faster and ignoring irrelevant stuff
% Deerwester et al. (1990) found an elegant way to improve similarity measurements with a mathematical operation on the term–document matrix, X, based on linear algebra. The op- eration is truncated Singular Value Decomposition (SVD), also called thin SVD. 
% Truncated SVD applied to document similarity is called Latent Semantic Indexing (LSI), but it is called Latent Semantic Analysis (LSA) when applied to word similarity.




The only information that can be taken into account when comparing two texts, or a text and a query, are the words it is made up from (...and their constellation, which is why \gls{word2vec} works better than \gls{bow}-approaches). 

However what you really want to compare is their conceptual/semantic content, and that unfortunately doesn't have a 1:1 correspondance to words - language is highly redundant, and the problems with that approach are synonymy (multiple words with one meaning) and polysemy (one word with multiple meanings), so equal words don't necessarily entail same concepts, and same concepts doesn't automatically mean same words. The terms used to describe or index a document typically contain only a fraction of the terms that users as a group will try to look it up under. Automatically adding synonyms worsens the polysemy problem. the words in query and document are both only one sample description of the intended documents, and in principle could have contained many different terms from the ones it does

if there is a great deal of structure, i.e. the occurrence ofsome patterns of words gives us a strong clue as to the likely occurrence of others, then data from one part (or all) of the table can be used to correct other portions

assume there is some underlying latent semantic structure in the data that is partially obscured by the randomness of word choice with respect to retrieval. With statistical techniques, this latent structure can be uncovered (LSI). This takes both terms and documents and projects them into a "semantic" space wherein terms and documents that are closely associated are placed near one another. terms that did not actually appear in a document may still end up close to the document, if that is consistent with the major patterns of association in the data. Position in the space then serves as the new kind of semantic indexing, and retrieval proceeds by using the terms in a query to identify a point in the space, and documents in its neighborhood are returned to the user

We want to use the matrix of observed occurrences of terms applied to documents to estimate parameters of that underlying model

SVD represents both terms and documents as vectors in a space of choosable dimensionality, and the dot product or cosine between points in the space gives their similarity



* useful if something "may just as well have been in there"
* 
* Invented for information retrieval \cite{Deerwester}. LSI is alternative name for LSA in linguistics (specifially information retrieval). 
* designed to solve aforementioned fundamental information retrieval problem \cite{Deerwester} - the unreliability of term-document-association (synonmy - term in query != term in doc, and also term in query == term in wrong doc) Treats it as statistical problem: assume there is an underlying latent semantic structure in the data that is partially obscured by the randomness of word choice with respect to retrieval - use statistical techniques to reduce noise!!
    * The terms used to describe or index a document typically contain only a fraction of the terms that users as a group will try to look it up under. Automatically adding synonyms worsens the polysemy problem. words in query and document are both only one sample description of the intended documents (-> latent info!) -> find some way to predict what terms "really" are implied by a query or apply to a document on the basis of the fallible sample actually found there.
    * Queries against a set of documents that have undergone LSI will return results that are conceptually similar in meaning to the search criteria even if the results don’t share specific word(s) with the search criteria.

* Analyses relationships between a set of documents and the terms they contain 
    * if there is a great deal of structure, i.e. the occurrence ofsome patterns of words gives us a strong clue as to the likely occurrence of others, then data from one part (or all) of the table can be used to correct other portions.
        *  We want to use the matrix of observed occurrences of terms applied to documents to estimate parameters of that underlying model
        * want: high-dim representation that caputres relation, done mathematically where docs & terms are explicitly represented in the same space, and retrieve documents from query terms directly, without rotation or interpretation of the underlying axes
        * => SVD represents both terms and documents as vectors in a space of choosable dimensionality, and the dot product or cosine between points in the space gives their similarity
    * by using maths, specifially matrix factorization (think principal components - express the original doc-term-matrix as multiplication of three other matrices, one being the "hidden information" and than ensure to only take the important one for that), more specifically singular-value decomposition which produces  a "semantic" space wherein terms and documents that are closely associated are placed near one another. terms that did not actually appear in a document may still end up close to the document, if that is consistent with the major patterns of association in the data.
        * create DTM and on that run SVD reduce #rows, which identifies patterns in the relationships between the terms and concepts contained in an unstructured collection of text. Distributaitnal Hypothesis.
        * important is the rank-reduced part - it finds a low-rank approximation! makes it less noisy and less sparse!
            * The consequence of the rank lowering is that some dimensions are combined and depend on more than one term: {(car), (truck), (flower)} --> {(1.3452 * car + 0.2828 * truck), (flower)} This mitigates the problem of identifying synonymy, as the rank lowering is expected to merge the dimensions associated with terms that have similar meanings. It also partially mitigates the problem with polysemy, since components of polysemous words that point in the "right" direction are added to the components of words that share a similar meaning. 
        * specific algo: 
            * matrix decomposition on the document-term matrix using Singular value decomposition to learn latent topics 
                -> m = #terms; n = #topics | Term-Document-Matrix (m*m) = words-per-topic (m*n) * topic-importance (n*n diagonal) * topics-distribution-across-docs (n*n singular)
            * SVD is a matrix factorization method that represents a matrix in the product of two matrices.
                -> M (m*m) = U (m*n left singular) * E (n*n diagonal with pos real vals) * V* (n*m; transpose of m*n right singular)
                    (diagonal: values not on main diag = 0; singular: singular if determinant=0 or a square matrix that does not
        * These special matrices show a breakdown of the original data into linearly independent components or "factors". In general many of these components are very small, and may be ignored, leading to an approximate model that contains many fewer factors. Each of the original documents’ similarity behavior is now approximated by its values on this smaller number of factors. The result can be represented geometrically by a spatial configuration in which the dot product or cosine between vectors representing two documents corresponds to their estimated similarity
        * \q{This rectangular matrix is again decomposed into three other matrices of a very special form} - The resulting matrices contain "singular vectors" and "singular values" - \q{breakdown of the original relationships into linearly independent components or factors. Again, many of these components are very small, and may be ignored, leading to an approximate model that contains many fewer dimensions} - In this reduced model all the term-term, document-document and term-document similarity is now approximated by values on this smaller number of dimensions

* Idea: reduce dimensions for classification - distributional hypothesis says similar words are then close 
    * How: construct term-document-matrix (using count-occurence, TF/IDF; (VISR12 take binary). Because that is generally very high-dimensional and sparse (and either noisy or includes many low-frequency words), we want to reduce dimensions - for that we use truncated/rank-reduced SVD. Based on this Matrix Factorization, the doc-vectors+the pseudocods are transfomred into a lower-dimensional spaces, and tag-lsi-sim(t,i) is then tha cosine similiarity of a document and the term making up the pseudodoc
    * \gls{doctermmat}, then dimensionality reduction to get vectors that correspond to concepts. This one \q{applies rank-reduced singular value decomposition to a term-document matrix in order to express the documents and terms in a lower dimensional concept space} \cite{VISR12}

* \textcite{VISR12} use it to find relationships between tags and documents by the cosine similiarity in this concept space: the closeness of a document to a tag is the cosine similarity of the LSI-embedded document and an LSI-embedded pseudo-document that consists of only that tag -- So this packs documents and terms into the same space and expresses their closeness - and thus may be a good alternative to the entire svm-stuff: why not find relevance of keywords/tags per document by this instead of our algorithm (\todoparagraph{come back to this in discussion}) (from \cite{Deerwester}: retrieval proceeds by using the terms in a query to identify a point in the space, and documents in its neighborhood are returned to the user. )

* could use LSA even to find the name of the semantic direction (if the vector of a document is closest to the vectors of the respective entities) 
(-> DISCUSSION)

* SVD: Matrix Decomposition algorithm (factorizes a matric into a product of matrices).  find the most valuable information and use a lower dimension to represent the same thing. 

* Why not used here? \cite{Derrac2015}: \q{SVD produces a representation in which entities correspond to vectors, which should be compared in terms of cosine similarity rather than Euclidean distance} -> spatial relations such as betweeness and parallism wouldn't make sense


## LSI & LDA LINKS



For an intuitive understanding, go for 
https://towardsdatascience.com/2-latent-methods-for-dimension-reduction-and-topic-modeling-20ff6d7d547 
or 
https://www.datacamp.com/community/tutorials/discovering-hidden-topics-python
or 
https://en.wikipedia.org/wiki/Latent_semantic_analysis#Rank-reduced_singular_value_decomposition

LDA:
1) http://blog.echen.me/2011/08/22/introduction-to-latent-dirichlet-allocation/
2) https://radimrehurek.com/gensim/auto_examples/core/run_topics_and_transformations.html#sphx-glr-auto-examples-core-run-topics-and-transformations-py
3) https://radimrehurek.com/gensim/auto_examples/tutorials/run_lda.html
