There's also \cite{Alshaikh2021}

\cite{VISR12} and their tag genome, the fact that the algorithm detailed here is basically only one step in \cite{Alshaikh2019}, Gärdenfors himself suggested that one may use self-organizing maps instead of classical AI/NLP algorithms


%Direkt am Anfang schreiben dass ich halt auf den main algorithmus eingehe und das laut meiner research diese 3 paper am besten den main algo beschreiben} (bzw sinnvoll erweitern) - was nicht heißt dass das die einzigen in dem kontext sind, Alshaikh2019 bspw nutzen ja den main algorithmus, aber ja nur als komponente, und haben andere Ziele was sie dann damit machen

* Ich kann hier sogar auf Johannes' SidBERT eingehen hehe

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

### Tag-Genome

[AGKS18] says that [Vig et al (2012)] propose a movie recommendation system in which the user can specify that they want to see suggestions for movies that are “similar to this one, but scarier”.

Tag Genome, is based on keywords that users have explicitly as- signed to movies, together with a supervised learning process aimed at re- ducing the sparsity of these assignments and to learn a degree of relevance for terms (rather than just having binary assignments).

=> Schreiben dass in nem Klassifikationstask von DESC15 "welches keyword beschreibt den unterschied zwischen film1 und film2 am besten?" tag genome DEUTLICH besser war, aber well das ist halt supervised.


### SidBERT

TODO: Bert in required algorithms als "bestes Neural language Model" vorstellen!

With the "Academic Interests" recommender there is already a system in place that recommends courses, having seen the same need to aid students in finding educational resources, information about which is only implicit. It does that by using a custom head on a BERT encoder that maps courses onto 905 classes derived from the third DDC \cite{Dewey1876} level 

AI-based application that categories courses and ohter learning materials into knowledge categories. Deep ANN that classifies courses and user requests to DDC [source], "a categorization system commonly deployed in libraries around the globe" based on title and description, matching DDCs of searches and courses

"Information on the content discussed in the scope of the educational resources, however, is implicit and must be inferred by the user by reading the resource title or through contextual information" 

DDC has hierachical tree stucture with 10 childs at each level. Childs are subtopics of thir parents, things can have multiple DDCs.

SidBERT: SidBERT is BERT-base model + custom classification head, from Huggingface-transformers. trained on 1.3m book titles & descriptions (uni/hannover/bremen uni + german national libray) 3-4 level.

BERT - based on transfomer (text doesn't need to be added sequentially). 12 stacked self-attention+feedforward encoder layers to create deep phrase embeddings, trained with masked-token inference tasks where the hidden word must be predicted

Currently 62.2% recall, 45.2% accuracy for 905 classes (chance would be 0.11) (CITE TO BE PUBLISHED), preliminary qualitative analysis showing that the internal representation does indeed partially capture the hierachical structure of DDCs.


### LSA

* Explain the logic of LSA as written in the main LSA paper paper
    * that it's useful if something "may just as well have been in there"
    * Ager/Alshaikh also compare with LSA, explain why it is comparable in what it does
    * that you could use LSA even to find the name of the semantic direction (if the vector of a document is closest to the vectors of the respective entities)
    * dass LSA das bag-of-words problem beheben würde
    * Can use this to, once the corresponding clusters are found, select a good one of that as representative: add pseudodocs with only one term and that term as name, and then let all DOCUMENTNAMES be candidates

* [AGKS18] says what they do is similar to LDA -> explain/understand LDA