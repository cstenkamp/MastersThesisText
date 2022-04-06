## Relation to VSMs

Dass Word Embeddings ja relativ nah an CS sind - For example, a well-known property of word embeddings is that many syntactic and semantic relationships can be captured in terms of word vector differences [Mikolov et al., 2013].

To understand what a CS is, let's start with vector space models in general. \Glspl{vsm} represent words or generally \emph{\glspl{entity}} (such as educational resources) together with their associated properties (\eg if they are \emph{advanced}) and relevant concepts (\eg their \emph{faculty}). \Glspl{vsm} are used for information retrieval and \gls{nlp} \cite{deerwester, Lowe} since long before the dawn of modern neural embeddings like \gls{word2vec} \cite{Mikolov2013}. 

\Glspl{cs} are similar in principle, instead of embedding all natural language words (including verbs and adjectives), in \glspl{cs} there is an explicit disctinction between \emph{entities} (tokens, modelled as vectors) and their \emph{properties} and \emph{concepts} (types, modelled as regions). The domain of a \gls{cs} does not include all kinds of words or concepts, but only concepts of a certain domain (like movies or university courses). Where the regularities in the VSMs (see \autoref{eq:w2vregularity}) are only implicit, a CS explicitly models meaningful and interpretable human concepts and properties as dimensions\footnote{Which means that in a conceptual space of humans, \emph{man} may be a unit vector}, so in contrast to arbitrary dimensions that only depend on the random initial setup, there is a clearly interpretable direction for the gender, and the space itself has a clearly defined metric that allows much more geometric and arithmetic reasoning, such as \eg betweeness. Furthermore, CS are organized into multiple low-dimensionsional spaces for different facets of the domain, such that in each of those only a small set of highly correlated properties/concepts is relevant\footnote{A prime example for this is the color-domain, which may consist of the attributes \emph{hue}, \emph{saturation} and \emph{value}.}.
<!-- from \cite{Alshaikh2019}: \q{For instance, in a conceptual space of movies, we may have facets such as genre, language, geographic location, etc. Each facet is associated with its own vector space, which intuitively captures similarity \wrt the corresponding facet. Most of these facet spaces tend to be low-dimensional [...]. This clearly differentiates them from traditional semantic spaces, which often have hundreds of dimensions}) -->
Importantly, a concept in a Conceptual Spaces is not modelled as a vector or point, but as a convex region. <!-- TODO: is this mentioned? (which allows for easy extraction of is-a and part-of relations or prototypical examples vs edge examples, but makes the generation computationally vastly more expensive)--> 

<!-- 
## Do I explain well enough?

* "criterion C defines concepts as regions of conceptual spaces" \cite[111]{Gardenfors2000a}
* properties: *A property is a convex region in some domain*
* information organized in spatial structures with dimensions (color, size, shape, ...)
    * dimensions have topological or geometric structures
    * dimensions sorted into domains (h+s+v = color)
    * dimensions are human-interpretable (measurable qualities)
* Gives an extended notion of what **similarity** is (see reasoning-section)
* related to prototype theory
-->

## MOAR

* There is a distinction between phenonemal and scientific interpretations of CS \cite[Sec.~1.4]{Gardenfors2000a}
	* When using CS as framework for a scientific theory, the geometrical/topological structures of the dimensions are chosen by the scientist. The choice of that brings along \q{the *measurement methods* employed to determine the values on the dimensions} (p21)
	* When, however, dealing with a *phenonemal* CS, the dimensions have to be infered from the subject's introspection. A good method for that is MDS, introduced by Gärdenfors himself \cite[Sec.~1.7]{Gardenfors2000a}, but \cite[Sec.~6.5]{Gardenfors2000a} he also suggests ANN-based embedding (specifically self-organizing maps.)
* Dass der tatsächliche Anwendungsbereich von CS noch sehr begrenzt ist - RaZb20 mention "they are commonly used in perceptual domains, e.g. for music cognition [Forth et al., 2010; Chella, 2015], where quality dimensions are carefully chosen to maximize how well the resulting conceptual spaces can predict human similarity judgements"
