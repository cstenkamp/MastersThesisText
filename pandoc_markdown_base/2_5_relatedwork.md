* \cite{Alshaikh2019, Alshaikh2021} use this algorithm as one of their steps or create a similar algorithm to find disentangled features better following the definition CS which implies several low-dimensional domain-specific subspaces.
* Gärdenfors himself suggested that one may use self-organizing maps instead of classical AI/NLP algorithms
* As mentioned before, the whole concepts of vector-space models for words \cite{Mikolov2013} and texts \cite{Le2014,Devlin2019} is related in that represents the meaing of terms, phrases or documents by embedding them in a vector space. However these have arbitrary non-interpretable dimensions and are no metric spaces, thus having no relation of geometry and meaning for \eg betweeness or analogical reasoning.
* \todoparagraph{LSA, elaborated later} 
* \todoparagraph{LDA, elaborated later} [AGKS18] says what they do is similar to LDA -> explain/understand LDA





\todoparagraph{move these two to discussion??}

There are also techniques that extend the algorithm of \textcite{Derrac2015}: \textcite{Alshaikh2019} take a vector space embedding and decompose it to several low-dimensional spaces, such that it more closely corresponds to the definition of a \gls{cs} which are split into multiple domain-specific spaces of low dimension. For that, they take the spaces from \cite{Derrac2015} to then cluster their features by domain and iteratively remove these groups to create multiple subspaces, while ensuring that \gls{word2vec} embeddings close to those of the removed ones are disregarded for future features.

\cite{Alshaikh2021} want to get rid of MDS with it's quadratic space complexity and also write a completely new, unsupervised ANN algorithm based on GloVe embeddings (and suggest that doing that on BERT may be the shit). In it, they learn domain-specific embeddings from the BoW and like \cite{Derrac2015} use classification of candidate-from-text-occurs vs not-occurs for the ANN training while punishing close embeddings like \cite{Alshaikh2019}.
