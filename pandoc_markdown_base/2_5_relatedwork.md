% Von Software Engineering oder best practices haben die alle ncoh nichts gehört, ich arbeite mit dem guten der Paper und das hier ist die main-function...https://github.com/cstenkamp/Autoencoder-Explanations/blob/master/src/_archive/pipeline.py#L1504-L1516

% 

% dass das alles vergleichbar mit InfoGAN etc für Bilder ist.. (siehe auch text von \cite{Alshaikh2019})

% \cite{Derrac2015}: "It is convenient to represent the meaning of terms or documents as points,vectors or regions in a Euclidean space. Such representations are known as vector-space models [...].  ==> FUCKING WORD2VEC!!!
 
% \cite{Derrac2015}: some form of dimensionality reduction is typically used to obtain vectors whose components correspond to concepts. One of the most popular techniques, called latent semantic analysis (LSA [39]), uses singular value decomposition (SVD) to this end. Multi-dimensional scaling (MDS [40]) is another popular method for dimen- sionality reduction, which builds a vector-space representation from pairwise similarity judgements.

=======================================================================================================================
========================================================= OLD =========================================================
=======================================================================================================================

main idea is to learn a representation in terms of salient features, where each of these features is described using a cluster of natural language terms. "This is somewhat similar to Latent Dirichlet Allocation (LDA) which learns a representation of text documents as multinomial distributions over latent topics, where each of these topics corresponds to a multinomial distribution over words (Blei et al., 2003). Topics tend to correspond to salient features, and are typically labelled with the most probable words according to the corre- sponding distribution" [quote: AGKS18]

* Obvious candidates:
    * Well, first of all of course I'm basing my stuff on [DESC15]
    * I hope that I can also bring in some stuff of the follow-up papers of this, eg [1, 2, 3]
    * Just as much as [DESC15] is similar to it, my work is similar to [THE MOVIETAGGER THINGY]


* Das was ich mache ist ja eig auch sehr nah an Topic Modeling:
    * https://www.datacamp.com/community/tutorials/discovering-hidden-topics-python: 
    * "Topic Modeling automatically discover the hidden themes from given documents. It is an unsupervised text analytics algorithm that is used for finding the group of words from the given document. These group of words represents a topic. There is a possibility that, a single document can associate with multiple themes. for example, a group words such as 'patient', 'doctor', 'disease', 'cancer', ad 'health' will represents topic 'healthcare'"
    * Topic modeling is the process of discovering groups of co-occurring words in text documents. These group co-occurring related words makes "topics". It is a form of unsupervised learning, so the set of possible topics are unknown.
    * In contrast to classification it's unsupervised and not single-class

## Tag-Genome

Tag Genome, is based on keywords that users have explicitly as- signed to movies, together with a supervised learning process aimed at re- ducing the sparsity of these assignments and to learn a degree of relevance for terms (rather than just having binary assignments).

=> Schreiben dass in nem Klassifikationstask von DESC15 "welches keyword beschreibt den unterschied zwischen film1 und film2 am besten?" tag genome DEUTLICH besser war, aber well das ist halt supervised.