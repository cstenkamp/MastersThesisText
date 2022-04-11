<!-- Note that those that are not defined here are likely to be found in the Glossary \nameref{glo:defs}. -->


* Generally there's the dichotomy classical/smbolistic linguistic <-> connectionistic stuff  (SEE QUOTES!)
    * classical:
        * on the extreme semantic knowledge bases (see reasoning), which can however also help our cause by looking at hyponyms explicitly
        * rely on BoW / Ngrams (loose word order, synonyms compeltely different)
            * to mitigate this: smoothing / noise reduciton / diminsionality reduction / finding latent stuff / finding ways to express similar things similarly (all the same! all done by dimens. red.)
    * connectionistic: GANs, word2vec and BERT
        * basically all NLP tasks profit from using embeddings, in contrast to BoW similar words are close 


### Dimensionality reduction & Latent Dimension detection ( & Topic Modeling )


#### Latent Semantic Analysis (LSA) / Latent Semantic Indexing (LSI)

Language is a model of the world. As however this model is ambiguous and redundant, this relationship is only a statistical one: The same thing can be expressed with different words (synonmy), and sometimes a word has different meaning depending on context (polysemy). Automatically adding synonyms worsens the polysemy problem. The underyling latent semantic structure in texts is obscured by the randomness of word choce. \textbf{Fundamental information retrieval problem} \cite{Deerwester} - the unreliability of term-document-association. We need to find some way to predict what terms "really" are implied by a query/in a document on the basis of the fallible sample actually found.

When comparing two texts (text and query, ...) what we have are the words which are only a sample descrption of the underlying conceptual/semantic context. But language has a lot of structure: We can treat it as statistical problem: The occurrence of some patterns of words gives a strong clue as to the likely occurrence of others! Distributional hypothesis! use the matrix of observed occurrences of terms applied to documents to estimate parameters of the underlying true model. "correct" noise and smooth the frequency matrix and keep comparison performance high or even improve it while decreasing dimnsionality. 

Here comes LSI. Applied to document similarity/information retreival is called \gls{lsi}, but it is called \gls{lsa} when applied to word similarity. \cite{Deerwester} Linear Algebra operation on the term-document matrix: Truncated SVD. 

want: low-dim representation that caputres relation, done mathematically where docs & terms are explicitly represented in the same space, that allows retrieve documents from query terms directly. Solution: matrix factorization (think principal components - express the original doc-term-matrix as multiplication of three other matrices, one being the "hidden information" and then ensure to only take the important values from that)

So create DTM (count-occurence, VISR12 take binary) which is highdim, noisy and sparse, then matrix decomposition: dtm = words-per-topic * topic-importance * topics-distribution-across-docs. breakdown of the original data into linearly independent components. run rank-reduced SVD, which finds a lower-rank approximation to reduce #rows while identifying and keepking relationship patterns. Ignoring small components (->truncated) leads to an approximation model with less dimensions approximating the original similarity behaviours term-term, doc-doc and term-doc but is less noisy and less sparse.

consequence of rank lowering is that some dimensions are combined and depend on more than one term. expected to merge the dimensions associated with terms that have similar meanings - mitigating synonymy. Also makes polysemy better: only the "right components" of polysemous that have similar meaning than the cluster are relevant for the combined-direction

SVD Analyses relationship between docs and terms and treats them equally: represents both as vectors in a single "semantic" space of choosable dimensionality where similar stuff close. Terms that did not actually appear in a document may still end up close to the document, if that is consistent with the major patterns of association in the data (distributional hypothesis again) So stuff that "may just as well have been in there".\footnote{Because if eg. "love story" and "hilarious" are applied to an item, it is likely that "romantic comedy" is also relevant\cite{Derrac2015, VISR12}} Terms can represented as pseudo-docs, a docuemnt with only one term. 

Similarity then = Cosine-distance. Instead of counting occurences we look for close vectors. Queries for doc-retrieval against a set of documents that have undergone LSI will return results that are conceptually similar in meaning to the search criteria even if the results don't share specific word(s) with the search criteria: embed the query and return close documents to it.

VISR12's algo bases mostly on this - find relationships between tags and documents by the cosine similiarity in this concept space: binary term-doc-matrix, create pseudocods for all tags, run LSI, and then tag-lsi-sim(t,i) = cosine distance of LSI-embedded doc and pseudodoc-for-tag.  Nice way to find relevance of tag for doc, good alternative to the entire svm-stuff or also to find similar terms 

This can even be used if a document is the better name for a semantic direction 
\todoparagraph{come back to bot points in discussion}


Why not used here? \cite{Derrac2015}: \q{SVD produces a representation in which entities correspond to vectors, which should be compared in terms of cosine similarity rather than Euclidean distance} -> spatial relations such as betweeness and parallism wouldn't make sense

Idea holds generally still: reduce dimensions distributional hypothesis says similar words are then close 


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

\cite{Ager2018}: "knowledge graph embeddings (Bordes et al., 2013) are used to find plausible missing in- formation in structured knowledge bases, or to ex- ploit such knowledge bases in neural network ar- chitectures."

The only information that can be taken into account when comparing two texts, or a text and a query, are the words it is made up from (...and their constellation, which is why \gls{word2vec} works better than \gls{bow}-approaches). 


werde ich vielleicht noch benutzen zum representative-terms-fürs-cluster-finden. BERT is the best one, blablabla. 
Don't forget to mention \gls{distribhyp}


* BERT als "bestes (except gpt) Neural language Model for documents"  
TODO: Ist word2vec schon nen euclidian space? Why/Why not?



The only information that can be taken into account when comparing two texts, or a text and a query, are the words it is made up from (...and their constellation, which is why \gls{word2vec} works better than \gls{bow}-approaches). 

* word2vec:
	How neural word-embedding-techniques are trained: (\cite{Le2014}): "each word is represented by a vector which is concatenated or averaged with other word vectors in a context, and the resulting vector is used to pre- dict other words in the context. For example, the neural network language model proposed in (Bengio et al., 2006) uses the concatenation of several previous word vectors to form the input of a neural network, and tries to predict the next word. The outcome is that after the model is trained, the word vectors are mapped into a vector space such that semantically similar words have similar vector representations (e.g., “strong” is close to “powerful”)."

	Task is mostly to predict a word given the other words in a context (maximize the average log probability of this word given the context words)

	"This type of models is commonly known as neural language models"! I am allowed to call them!

	After the training converges, words with similar meaning are mapped to a similar position in the vector space

	The dif- ference between word vectors also carry meaning. For ex- ample, the word vectors can be used to answer analogy questions using simple vector algebra: “King” - “man” + “woman” = “Queen” (Mikolov et al., 2013d).

* doc2vec: 
	"On a text classification task, our method convincingly beats bag-of-words models, giving a relative improvement of about 30%"


	Doc2vec also used for Information Retrieval!!
	Dataset from 1mio search queries and paragraphs of the first 10 results. Goal is to identify which of three paragraphs are results of the same query (two are equal, one is random). Goal is small distance for the equals and bigger one for the random. 



### Linear algebra stuff

#### Projecting and playing around with coordinate system

So how do we project the point onto the plane?
* [https://stackoverflow.com/a/17661431] all you have to do is find the perpendicular (abbr here |_) distance from the point P to the plane, then translate P back by the perpendicular distance in the direction of the plane normal. The result is the translated P sits in the plane.


<!-- \includeMD{pandoc_generated_latex/2_7_separatrixdistance} -->