

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


