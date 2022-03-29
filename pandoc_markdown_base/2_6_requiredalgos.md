TODO: Ist word2vec schon nen euclidian space? Why/Why not?

## MDS

As described by Gärdenfors himself \cite[Sec.~1.7]{Gardenfors2000a}:

MDS: If the all coordinate components are known, distances are trivial, MDS does the reverse problem, starting from similarity judgements, MDS finds the numnber of dimensions and the scaling of the underlaying phenonemonal space, with the goal of achieving \q{"as high a correlation as possible between the similarity judgements of the subjects and the corresponding distances in the estimated dimensional space."} (p22) (Number of dimensions is chosen, not found by MDS. Metric is chosen (euclidian, city-block). MDS then starts randomly and \q{systematically ajdusts the coordinates to achieve a progressively better fit to the data from the similarity judgments.} (p22)). Some guy almost perfectly recovered the 2D space of hues using MDS and judgements.

\paragraph{Tf-Idf}

\gls{tf-idf} 

Words that are rare overall and frequent in this document are weighted highly.

tf-idf for term $x$ within document $y$:

$$ w_{x,y} = \text{\textit{tf}}_{x,y} * log(\frac{N}{df_x}) $$

with $\text{tf}_{x,y}$ as the term-frequency of $x$ in $y$, \
$df_x$ as the document-frequency (the number of documents containing $x$) \
and $N$ being the total number of documents

%see also: see also: https://towardsdatascience.com/3-basic-approaches-in-bag-of-words-which-are-better-than-word-embeddings-c2cbc7398016

%\cite{Turney2010} (sec 4.2): The most popular way to formalize this idea for term–document matrices is the tf-idf (term frequency × inverse document frequency) family of weighting functions (Sp¨arck Jones, 1972). An element gets a high weight when the corresponding term is frequent in the corresponding document (i.e., tf is high), but the term is rare in other documents in the corpus (i.e., df is low, and thus idf is high). Salton and Buckley (1988) defined a large family of tf-idf weighting functions and evaluated them on information re- trieval tasks, demonstrating that tf-idf weighting can yield significant improvements over raw frequency


\paragraph{PPMI}

% * See also: https://stackoverflow.com/a/58725695/5122790

It was suggested by \cite{Turney2010} to use the \gls{ppmi} measure instead of tf-idf to weight the counts in \glspl{doctermmat}, relying on \cite{Bullinaria2007}'s work taking into account psychological models to extract information about lexical semantics from co-occurence statistics. According to \cite{Turney2010,Bullinaria2007}, \gls{ppmi} performs most plausible to measure semantic similarity in word-context matrices compared to human evaluation. %(sec 4.2) of \cite{Turney2010}: Bullinaria and Levy (2007) demonstrated that PPMI performs better than a wide variety of other weighting approaches when measuring semantic similarity with word-context matrices.



The Paper uses the following \gls{ppmi} definition:\\ 

\noindent $e \in E$ is an entity, $D_e$ a document (bag of words) where that entity occurs.\\
We want to quantify for each term occuring in the corpus $\{D_e | e \in E\}$ how strongly it is associated with $e$.\\
$c(e,t)$ is the number of times term $t$ occurs in document $D_e$. \\
The weight $ppmi(e,t)$ for term $t$ in the vector representing $e$ is then:
\begin{align*}
ppmi(e,t) &= max\left(0, log\left( \frac{p_{et}}{p_{e*}*p_{*t}} \right) \right) \\
          &= max\left(0, pmi(e,t) \right) \\
 pmi(e,t) &= log\left( \frac{p_{et}}{p_{e*}*p_{*t}} \right) \\          
   p_{et} &= \frac{c(e,t)}{\sum_{e'}\sum_{t'} c(e',t')} \\
   p_{e*} &= \sum_{t'}p_{et'} \\
   p_{*t} &= \sum_{e'}p_{e't} \\
\end{align*}

\noindent log of the probability of the $e$-$t$-combination (count of this vs count of all), normalized by the probability of this $e$ with any $t$ times this $t$ with any $e$.\\
To quote the paper: "PPMI will favor terms which are frequently associated with the entity $e$ while being relatively infrequent in the corpus overall"

\vspace{30px}

I found this definition:
\begin{align*}
ppmi(X,i,j) &= max(0, pmi(X,i,j)) \\
pmi(X,i,j)  &= log\left( \frac{X_{ij}}{expected(X,i,j)} \right) \\
            &= log\left( \frac{P(X_{ij})}{P(X_{i*}) * P(X_{*j})} \right)
\end{align*}


\subsection{Dimensionality Reduction}

\subsubsection*{LSI/LSA}

% from \cite{Turney2010}: 
% Context: Smoothing the frequency matrix - keep comparison performance high but the comparision process faster and ignoring irrelevant stuff
% Deerwester et al. (1990) found an elegant way to improve similarity measurements with a mathematical operation on the term–document matrix, X, based on linear algebra. The op- eration is truncated Singular Value Decomposition (SVD), also called thin SVD. 
% Truncated SVD applied to document similarity is called Latent Semantic Indexing (LSI), but it is called Latent Semantic Analysis (LSA) when applied to word similarity.



FROM \cite{deerwester} (huge chunks verbaitm!)

The only information that can be taken into account when comparing two texts, or a text and a query, are the words it is made up from (...and their constellation, which is why \gls{word2vec} works better than \gls{bow}-approaches). 
However what you really want to compare is their conceptual/semantic content, and that unfortunately doesn't have a 1:1 correspondance to words - language is highly redundant, and the problems with that approach are synonymy (multiple words with one meaning) and polysemy (one word with multiple meanings), so equal words don't necessarily entail same concepts, and same concepts doesn't automatically mean same words. The terms used to describe or index a document typically contain only a fraction of the terms that users as a group will try to look it up under. Automatically adding synonyms worsens the polysemy problem. the words in query and document are both only one sample description of the intended documents, and in principle could have contained many different terms from the ones it does

if there is a great deal of structure, i.e. the occurrence ofsome patterns of words gives us a strong clue as to the likely occurrence of others, then data from one part (or all) of the table can be used to correct other portions

assume there is some underlying latent semantic structure in the data that is partially obscured by the randomness of word choice with respect to retrieval. With statistical techniques, this latent structure can be uncovered (LSI). This takes both terms and documents and projects them into a "semantic" space wherein terms and documents that are closely associated are placed near one another. terms that did not actually appear in a document may still end up close to the document, if that is consistent with the major patterns of association in the data. Position in the space then serves as the new kind of semantic indexing, and retrieval proceeds by using the terms in a query to identify a point in the space, and documents in its neighborhood are returned to the user

We want to use the matrix of observed occurrences of terms applied to documents to estimate parameters of that underlying model

SVD represents both terms and documents as vectors in a space of choosable dimensionality, and the dot product or cosine between points in the space gives their similarity

\subsubsection*{Multi-dimensional Scaling}


% Wir müssen some sort of dimensionality reduction machen, und MDS , das versucht distances zu erhalten, ist da natürlich nen guter kandidat (siehe Kurs, Slides 2, von Nico)

\Gls{mds} is a dimensionality reduction technique that builds a vector-space representation from pairwise similarity judgements. It takes a \gls{dissimmat} as input and returns a fixed-dimensional embedding in which original distances are kept as close to the ones of the \gls{dissimmat} as possible. 
 

\subsection{Word Embeddings}

werde ich vielleicht noch benutzen zum representative-terms-fürs-cluster-finden. BERT is the best one, blablabla. 
Don't forget to mention \gls{distribhyp}







=======================================================================================================================
========================================================= OLD =========================================================
=======================================================================================================================





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