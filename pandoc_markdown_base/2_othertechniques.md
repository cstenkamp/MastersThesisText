<!-- Note that those that are not defined here are likely to be found in the Glossary \nameref{glo:defs}. -->


### Relation CS <-> VSMs

Dass Word Embeddings ja relativ nah an CS sind - For example, a well-known property of word embeddings is that many syntactic and semantic relationships can be captured in terms of word vector differences [Mikolov et al., 2013].

To understand what a CS is, let's start with vector space models in general. \Glspl{vsm} represent words or generally \emph{\glspl{entity}} (such as educational resources) together with their associated properties (\eg if they are \emph{advanced}) and relevant concepts (\eg their \emph{faculty}). \Glspl{vsm} are used for information retrieval and \gls{nlp} \cite{deerwester90, Lowe} since long before the dawn of modern neural embeddings like \gls{word2vec} \cite{Mikolov2013}. 

\Glspl{cs} are similar in principle, instead of embedding all natural language words (including verbs and adjectives), in \glspl{cs} there is an explicit disctinction between \emph{entities} (tokens, modelled as vectors) and their \emph{properties} and \emph{concepts} (types, modelled as regions). The domain of a \gls{cs} does not include all kinds of words or concepts, but only concepts of a certain domain (like movies or university courses). Where the regularities in the VSMs (see \autoref{eq:w2vregularity}) are only implicit, a CS explicitly models meaningful and interpretable human concepts and properties as dimensions\footnote{Which means that in a conceptual space of humans, \emph{man} may be a unit vector}, so in contrast to arbitrary dimensions that only depend on the random initial setup, there is a clearly interpretable direction for the gender, and the space itself has a clearly defined metric that allows much more geometric and arithmetic reasoning, such as \eg betweeness. Furthermore, CS are organized into multiple low-dimensionsional spaces for different facets of the domain, such that in each of those only a small set of highly correlated properties/concepts is relevant\footnote{A prime example for this is the color-domain, which may consist of the attributes \emph{hue}, \emph{saturation} and \emph{value}.}.

## Word Embeddings
\subsection{Word Embeddings}
\label{sec:embeddings}

Regarding the dichotomy:
* classical:
	* on the extreme semantic knowledge bases (see reasoning), which can however also help our cause by looking at hyponyms explicitly
	* rely on BoW / Ngrams (loose word order, synonyms compeltely different)
		* to mitigate this: smoothing / noise reduciton / diminsionality reduction / finding latent stuff / finding ways to express similar things similarly (all the same! all done by dimens. red.)
* connectionistic: GANs, word2vec and BERT
	* basically all NLP tasks profit from using embeddings, in contrast to BoW similar words are close 




zum thema word2vec: when talking about bow-representation we said that missing is semantics and information about context, this coutners it. You shall now a word by a company it keeps.


\cite{Ager2018}: "knowledge graph embeddings (Bordes et al., 2013) are used to find plausible missing in- formation in structured knowledge bases, or to ex- ploit such knowledge bases in neural network ar- chitectures."

The only information that can be taken into account when comparing two texts, or a text and a query, are the words it is made up from (...and their constellation, which is why \gls{word2vec} works better than \gls{bow}-approaches). 


werde ich vielleicht noch benutzen zum representative-terms-fürs-cluster-finden. BERT is the best one, blablabla. 
Don't forget to mention distributional hypoth.


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

Best is BERT - based on transfomer (text doesn't need to be added sequentially). 12 stacked self-attention+feedforward encoder layers to create deep phrase embeddings, trained with masked-token inference tasks where the hidden word must be predicted

<!--
### Linear algebra stuff

#### Projecting and playing around with coordinate system

So how do we project the point onto the plane?
* [https://stackoverflow.com/a/17661431] all you have to do is find the perpendicular (abbr here |_) distance from the point P to the plane, then translate P back by the perpendicular distance in the direction of the plane normal. The result is the translated P sits in the plane.


 \includeMD{pandoc_generated_latex/2_7_separatrixdistance} -->

