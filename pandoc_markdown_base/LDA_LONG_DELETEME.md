### Latent Dirichlet Allocation (LDA)

\label{sec:lda}

\cite{Blei2003}

\cite{Blei2003}: \q{LDA is a three-level hierarchical Bayesian model, in which each item ofa collection is modeled as a finite mixture over an underlying set of topics. Each topic is, in turn, modeled as an infinite mixture over an underlying set of topic probabilities. In the context of text modeling, the topic probabilities provide an explicit representation of a document.}
    * efficient approximate inference techniques based on variational methods and an EM algorithm for empirical Bayes parameter estimation
    * report results in document modeling, text classification, and collaborative filtering, comparing

\cite{Ager2018}: The main idea underlying our method is to learn a representation in terms of salient features, where each of these features is de- scribed using a cluster of natural language terms. This is somewhat similar to Latent Dirichlet Al- location (LDA), which learns a representation of text documents as multinomial distributions over latent topics, where each of these topics corre- sponds to a multinomial distribution over words (Blei et al., 2003). Topics tend to correspond to salient features, and are typically labelled with the most probable words according to the corre- sponding distribution. However, while LDA only uses bag-of-words (BoW) representations, our fo- cus is specifically on identifying and improving features that are modelled as directions in seman- tic spaces. One advantage of using vector spaces is that they offer more flexibility in how additional information can be taken into account, e.g. they allow us to use neural representation learn- ing methods to obtain these spaces. Many ex- tensions of LDA have been proposed to incorpo- rate additional information as well, e.g. aiming to avoid the need to manually specify the num- ber of topics (Teh et al., 2004), modelling corre- lations between topics (Blei and Lafferty, 2005), or by incorporating meta-data such as authors or time stamps (Rosen-Zvi et al., 2004; Wang and McCallum, 2006). Nonetheless, such techniques for extending LDA offer less flexibility than neu- ral network models, e.g. for exploiting numerical attributes or visual features



main idea is to learn a representation in terms of salient features, where each of these features is described using a cluster of natural language terms. "This is somewhat similar to Latent Dirichlet Allocation (LDA) which learns a representation of text documents as multinomial distributions over latent topics, where each of these topics corresponds to a multinomial distribution over words (Blei et al., 2003). Topics tend to correspond to salient features, and are typically labelled with the most probable words according to the corre- sponding distribution" [quote: AGKS18]

(there would be a link here) https://towardsdatascience.com/2-latent-methods-for-dimension-reduction-and-topic-modeling-20ff6d7d547
* unsupervised learning, often used for topic modeling.
* Assumption in text: in each text, there are various topics, and each topic consists of various keywords (two layers of aggregation: documents to topics and topics to categories)

1) http://blog.echen.me/2011/08/22/introduction-to-latent-dirichlet-allocation/
2) https://radimrehurek.com/gensim/auto_examples/core/run_topics_and_transformations.html#sphx-glr-auto-examples-core-run-topics-and-transformations-py
3) https://radimrehurek.com/gensim/auto_examples/tutorials/run_lda.html

	The main idea underlying our method is to learn a representation in terms of salient features, where each of these features is de- scribed using a cluster of natural language terms. This is somewhat similar to Latent Dirichlet Al- location (LDA), which learns a representation of text documents as multinomial distributions over latent topics, where each of these topics corre- sponds to a multinomial distribution over words (Blei et al., 2003). Topics tend to correspond to salient features, and are typically labelled with the most probable words according to the corre- sponding distribution. However, while LDA only uses bag-of-words (BoW) representations, our fo- cus is specifically on identifying and improving features that are modelled as directions in seman- tic spaces. One advantage of using vector spaces is that they offer more flexibility in how addi-

Ager/Alshaikh also compare with LDA, explain why it is comparable in what it does

main idea is to learn a representation in terms of salient features, where each of these features is described using a cluster of natural language terms. "This is somewhat similar to Latent Dirichlet Allocation (LDA) which learns a representation of text documents as multinomial distributions over latent topics, where each of these topics corresponds to a multinomial distribution over words (Blei et al., 2003). Topics tend to correspond to salient features, and are typically labelled with the most probable words according to the corre- sponding distribution" [quote: AGKS18]













For an intuitive understanding, go for 
https://towardsdatascience.com/2-latent-methods-for-dimension-reduction-and-topic-modeling-20ff6d7d547 
or 
https://www.datacamp.com/community/tutorials/discovering-hidden-topics-python
or 
https://en.wikipedia.org/wiki/Latent_semantic_analysis#Rank-reduced_singular_value_decomposition


