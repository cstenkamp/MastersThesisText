Note that those that are not defined here are likely to be found in the Glossary \nameref{glo:defs}.


* Generally there's the dichotomy classical/smbolistic linguistic <-> connectionistic stuff  (SEE QUOTES!)
    * classical:
        * on the extreme semantic knowledge bases (see reasoning), which can however also help our cause by looking at hyponyms explicitly
        * rely on BoW / Ngrams (loose word order, synonyms compeltely different)
            * to mitigate this: smoothing / noise reduciton / diminsionality reduction / finding latent stuff / finding ways to express similar things similarly (all the same! all done by dimens. red.)
    * connectionistic: GANs, word2vec and BERT
        * basically all NLP tasks profit from using embeddings, in contrast to BoW similar words are close 




### Dimensionality reduction & Latent Dimension detection ( & Topic Modeling )

* Larger context: VSMs \cite{Turney2010}:
    * Term-Document Model for similarity of documents
        * dimensions = terms in the docs (doc-term-matrix)
        * bag-of-word hypothesis: documents with similar words have similar meaning
    * Word-Context-model: simiarity of words    
        * dimensions somehow encodde context word can occur in (explicitly through neural models))
        * distributional hypothesis: words that occur in similar context have similar meanings 
    * pair-pattern model: similarity of relations
        * dimensions = word-pairs that can occur in relation
        * extended distributional hypothesis: releations that occur with similar word paris have similar meaning


#### Latent Semantic Analysis (LSA) / Latent Semantic Indexing (LSI)

LSA VERY LONG (you can delete everything here)

* Invented for information retrieval \cite{Deerwester}. LSI is alternative name for LSA in linguistics (specifially information retrieval). (Truncated SVD applied to document similarity is called Latent Semantic Indexing (LSI), but it is called Latent Semantic Analysis (LSA) when applied to word similarity.)

* The only information that can be taken into account when comparing two texts, or a text and a query, are the words it is made up from 

However what you really want to compare is their conceptual/semantic content, and that unfortunately doesn't have a 1:1 correspondance to words - language is highly redundant, and the problems with that approach are synonymy (multiple words with one meaning) and polysemy (one word with multiple meanings), so equal words don't necessarily entail same concepts, and same concepts doesn't automatically mean same words (different people use different words in description & search - doc and query are only a sample description which could have used completely different words) Automatically adding synonyms worsens the polysemy problem.

if there is a great deal of structure, i.e. the occurrence ofsome patterns of words gives us a strong clue as to the likely occurrence of others, then data from one part (or all) of the table can be used to correct other portions

assume there is some underlying latent semantic structure in the data that is partially obscured by the randomness of word choice with respect to retrieval. With statistical techniques, this latent structure can be uncovered (LSI). This takes both terms and documents and projects them into a "semantic" space wherein terms and documents that are closely associated are placed near one another. terms that did not actually appear in a document may still end up close to the document, if that is consistent with the major patterns of association in the data. 
    * Distributional Hypothesis! Because if eg. "love story" and "hilarious" are applied to an item, it is likely that "romantic comedy" is also relevant, which may apply \cite{Derrac2015, VISR12}.
    * useful if something "may just as well have been in there"

Position in the space then serves as the new kind of semantic indexing, and retrieval proceeds by using the terms in a query to identify a point in the space, and documents in its neighborhood are returned to the user

So LSA uses truncated singular value decomposition (SVD). SVD represents both terms and documents as vectors in a space of choosable dimensionality, and the dot product or cosine between points in the space gives their similarity

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












For an intuitive understanding, go for 
https://towardsdatascience.com/2-latent-methods-for-dimension-reduction-and-topic-modeling-20ff6d7d547 
or 
https://www.datacamp.com/community/tutorials/discovering-hidden-topics-python
or 
https://en.wikipedia.org/wiki/Latent_semantic_analysis#Rank-reduced_singular_value_decomposition



#### MDS
\subsubsection*{Multi-dimensional Scaling}

Multi-dimensional scaling (MDS [40]) is another popular method for dimen- sionality reduction, which builds a vector-space representation from pairwise similarity judgements."

% Wir müssen some sort of dimensionality reduction machen, und MDS , das versucht distances zu erhalten, ist da natürlich nen guter kandidat (siehe Kurs, Slides 2, von Nico)

\Gls{mds} is a dimensionality reduction technique that builds a vector-space representation from pairwise similarity judgements. It takes a \gls{dissimmat} as input and returns a fixed-dimensional embedding in which original distances are kept as close to the ones of the \gls{dissimmat} as possible. 
 
-> See meine Stichpunkte in der discussion ob MDS jetzt sinnvoll war oder nicht

From a set of pairwise distances, induce a finite space with fixed dimensions. Formally:

given distances $d(p_i, p_j) \forall 1 \leq i, i \leq j$ and dimension k, compute points $v_1, ..., v_n \in \mathds{R}^k$ that maintains distances as well as possible by minimizing 

$$ \sum_{i=1}^{n-1}\sum_{j=i+1}^{n}(d(p_i, p_j) - \lVert v_i - v_j \rVert)^2 $$

Can be used for dimensionality reduction

\cite{Alshaikh2021}:  MDS has quadratic space complexity 

As described by Gärdenfors himself \cite[Sec.~1.7]{Gardenfors2000a}:

MDS: If the all coordinate components are known, distances are trivial, MDS does the reverse problem, starting from similarity judgements, MDS finds the numnber of dimensions and the scaling of the underlaying phenonemonal space, with the goal of achieving \q{"as high a correlation as possible between the similarity judgements of the subjects and the corresponding distances in the estimated dimensional space."} (p22) (Number of dimensions is chosen, not found by MDS. Metric is chosen (euclidian, city-block). MDS then starts randomly and \q{systematically ajdusts the coordinates to achieve a progressively better fit to the data from the similarity judgments.} (p22)). Some guy almost perfectly recovered the 2D space of hues using MDS and judgements.

* dimensionality reduction
* Used by [DESC15] because distances stay equal
* builds a vector-space representation from pairwise similiarity judgements
* Sources: [40] of [DESC15]

## Other stuff / General NLP Techniques


### Semantic Knowledge Bases

\subsubsection*{Semantic Knowledge Bases}

Lexical databases of semantic relations between words, the most famous of which being WordNet,\footnote{\url{https://wordnet.princeton.edu/}} link words in a graph that encodes explicit semantic relations like synonyms and hyponyms (subtypes/ \emph{is-a}-relationships). While neural %TODO: nicht neural, aber halt data-driven? naja das was word2vec undso sind... by-context-created/trained...?! similarity-based? -> DISTRIBUTIONAL MODELS (ones trained from the co-occurrence patterns of temrs)
embeddings may encode similar information implicitly, when relying on dictionary-based word encodings they are an important tool when using classical linguistic techniques. For the developed algorithm, the information how many hyponyms of a candidate word for a semantic direction %TODO: did I explain the algorithm well enough before this to throw this much information at the reader?!
occur in its corresponding text-corpus is highly relevant. To do that, WordNet \cite{Miller1995} and it's German equivalent, GermaNet \cite{hamp-feldweg-1997-germanet,Henrich},\footnote{\url{(https://uni-tuebingen.de/fakultaeten/philosophische-fakultaet/fachbereiche/neuphilologie/seminar-fuer-sprachwissenschaft/arbeitsbereiche/allg-sprachwissenschaft-computerlinguistik/ressourcen/lexica/germanet-1/)}} are required in the respective step.




### Word Embeddings
\subsection{Word Embeddings}
\label{sec:embeddings}

The only information that can be taken into account when comparing two texts, or a text and a query, are the words it is made up from (...and their constellation, which is why \gls{word2vec} works better than \gls{bow}-approaches). 


werde ich vielleicht noch benutzen zum representative-terms-fürs-cluster-finden. BERT is the best one, blablabla. 
Don't forget to mention \gls{distribhyp}


* BERT als "bestes (except gpt) Neural language Model for documents"  
TODO: Ist word2vec schon nen euclidian space? Why/Why not?



### Linear algebra stuff

#### Projecting and playing around with coordinate system

So how do we project the point onto the plane?
* [https://stackoverflow.com/a/17661431] all you have to do is find the perpendicular (abbr here |_) distance from the point P to the plane, then translate P back by the perpendicular distance in the direction of the plane normal. The result is the translated P sits in the plane.
<!-- \includeMD{pandoc_generated_latex/2_7_seperatrixdistance} -->