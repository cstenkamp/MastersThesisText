Note that those that are not defined here are likely to be found in the Glossary \nameref{glo:defs}.

\cite{Ager2018}: \q{However, while LDA only uses bag-of-words (BoW) representations, our fo- cus is specifically on identifying and improving features that are modelled as directions in seman- tic spaces. One advantage of using vector spaces is that they offer more flexibility in how additional information can be taken into account, e.g. they allow us to use neural representation learn- ing methods to obtain these spaces.}

* Base algorithm is explained and consists of multiple components: preprocessing -> bag-of-ngrams -> quantification -> frequency matrix -> quantification -> mds -> svm -> kappa. Let's get a grasp of the general concepts before going into algorithm details. Also we'll quickly look into what other tools could have been used. As stated above, the algorithm uses generally classical linguistic tools
* Generally there's the dichotomy classical/smbolistic linguistic <-> connectionistic stuff  (SEE QUOTES!)
    * classical:
        * on the extreme semantic knowledge bases (see reasoning), which can however also help our cause by looking at hyponyms explicitly
        * rely on BoW / Ngrams (loose word order, synonyms compeltely different)
    * connectionistic: GANs, word2vec and BERT
        * basically all NLP tasks profit from using embeddings, in contrast to BoW similar words are close 
* And then also stuff like LSA/LDA, which are kinda doing the same as the entire algorithm (see \autoref{tab:f1_mainalgos_me_short}: LDA is still sometimes better than this algo)
* Also, we need some general linear algebra bc after all these are vector spaces, so let's look quickly at projecting and playing around with coordinates

* DESC15: "In information retrieval, it is common to represent documents as vectors with one component for every term occurring in the corpus. In many other applications (and sometimes in information retrieval) some form of dimensionality reduction is typically used to obtain vectors whose components correspond to concepts. One of the most popular techniques, called latent semantic analysis (LSA [39]), uses singular value decomposition (SVD) to this end. Multi-dimensional scaling (MDS [40]) is another popular method for dimen- sionality reduction, which builds a vector-space representation from pairwis



## Classical Linguistics Pipeline

\cite{Lowe,Turney2010} provide a lot of theoretical basis for NLP and what this generally entails

preprocessing -> bag-of-ngrams -> quantification -> frequency matrix -> smoothing

<!-- 
I can take a bit of the definitions from here:
  https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction 
  ("We call vectorization the general process of turning a collection of text documents into numerical feature vectors. This specific strategy (tokenization, counting and normalization) is called the Bag of Words or “Bag of n-grams” representation. Documents are described by word occurrences while completely ignoring the relative position information of the words in the document.")
-->

\textcite{Turney2010} (who in turn rely on \cite{Lowe}) say that generally when generating a \gls{vsm} from texts (without word2vec and this fancy shit), you need these steps:
genrally, VSM construction can be decomposed into a four-step forcess


\begin{description}
    \item[1) Build the Frequency Matrix] start by tokenizing, normalizing, annotating (maybe lemmatizing) etc as preprocessing, then calculate frequencies by counting.
    \item[2) Transform raw frequency counts] \q{we may want to adjust the weights of the elements in the matrix, because common words will have high frequencies, yet they are less informative than rare words} \cite{Turney2010}
    \item[3) Smooth the Space/Frequency matrix] to reduce the amount of random noise and to fill in some of the zero elements in a sparse matrix: \textbf{Dimensionality Reduction}
    \item[4) Calculate similarities] with stuff like cosine-dist. (actually,  there are many different ways to measure the similarity of two vectors.)
\end{description}

As elaborated, important for us is that we don't have ONE SINGLE SIMILARTIY; BUT THAT IT's context-dependent!!!!

-> we will go into some details on these steps, LSI is a good candidate to smooth the frqeuncy matrix but bc as we said we need a metric space we (like \cite{Derrac2015}) do MDS


### Bag-of-Words

\label{sec:techniques:bow}

* Write how a Bag-Of-Words is created and what it shortcomings are and find a source that compares how good a Bag-Of-Words (that necessarily doesn't contain and information about their position) can be, compared to better document embeddings like LSTMs, Doc2Vec or whatever else there is (I mean after all, a "not" may be ignored and the meaning inversed which should be supergau), and also how much better it becomes if one also consideres 2-grams, 3-grams, ...


* There is a very important problem in information retrieval and also for our case: Natural language is ambiguous! when trying to match words of queries with words of documents, you want to retrieve on the basis of conceptual content, and individual words provide unreliable evidence about the conceptual topic or meaning of a document. (the words used in the query may not be the same as the ones in the documents, problems here are synonymy (multiple words, same meaning) and polysemy (multiple meanings, same words))
* There are usually many ways to express a given concept, so the literal terms in a user’s query may not match those of a relevant document, or you'll get results for another meaning of the word you're looking for.
=> Very important thing is thus to make similar words close. Both LSI and neural embeddings want to solv ethis.
dass LSA das bag-of-words problem beheben würde


The only information that can be taken into account when comparing two texts, or a text and a query, are the words it is made up from (...and their constellation, which is why \gls{word2vec} works better than \gls{bow}-approaches). 


### Word-weighting

\subsubsection*{Word-weighting techniques}
\label{sec:word_count_techniques}

So, making 100\% sure:

\begin{itemize}
    \item term-frequency tf(term, doc): How often term occurs in doc
    \item doc-frequency df(term):  the number of documents in the corpus that contain the word
    \item summed term-frequncy sdf(term): How often term occurs in ANY DOC = tf(term, doc) forall doc
\end{itemize}

When comparing the \gls{bow}-representations of texts, it is reasonable to give more weight to \emph{surprising} words and less weight to expected ones. \q{The hypothesis is that surprising events, if shared by two vectors, are more discriminative of the similarity between the vectors than less surprising events.} \cite[156]{Turney2010} 
Another crucial reason is, that the entities's are of drastically varying length, so longer entities would naturally dominate shorter ones when only comparing the raw counts - considering relative frequencies instead of absolute ones alleviates such problems.

Because of these reasons, in the algorithm it will often be talked about \glspl{quant}. The algorithms explained below transforms the raw frequency-counts of a document and an \gls{ngram} into some \emph{score}, dependent on the number of occurences of this term in this document as well as the counts of other \glspl{ngram} and other documents. This score is henceforth called a \gls{quant}.
%TODO: term? phrase? n-gram?

#### tf-idf
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

#### PPMI

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


### Dimensionality reduction & Latent Dimension detection ( & Topic Modeling )

\subsection{Dimensionality Reduction}


* We said before that we want to find latent topics (hidden/potential dimensions) from the texts. LSI/LSA & LDA are cool bc they rely on some form of the distrib hypothesis and put everything into a matrix and then find latent stuff using maths by compressing the matrix, assuming that if there is hidden information that will be what it's compressed onto (think autoencoders)
* Kinda "clustering" the terms \cite{Derrac2015, VISR12}: if eg. "love story" and "hilarious" are applied to an item, it is likely that "romantic comedy" is also relevant
* Two techniques: LSA (mainly dimension reduction & noise reduction) and LDA (mainly topic modeling) -> LDA does the same thing as the entire algorithm considered here 




\cite{Derrac2015}: some form of dimensionality reduction is typically used to obtain vectors whose components correspond to concepts. One of the most popular techniques, called latent semantic analysis (LSA [39]), uses singular value decomposition (SVD) to this end. Multi-dimensional scaling (MDS [40]) is another popular method for dimen- sionality reduction, which builds a vector-space representation from pairwise similarity judgements.


DESC15: "In information retrieval, it is common to represent documents as vectors with one component for every term occurring in the corpus. In many other applications (and sometimes in information retrieval) some form of dimensionality reduction is typically used to obtain vectors whose components correspond to concepts. One of the most popular techniques, called latent semantic analysis (LSA [39]), uses singular value decomposition (SVD) to this end. Multi-dimensional scaling (MDS [40]) is another popular method for dimen- sionality reduction, which builds a vector-space representation from pairwise similarity judgements."


#### Latent Semantic Analysis (LSA) / Latent Semantic Indexing (LSI)

[...]

#### MDS
\subsubsection*{Multi-dimensional Scaling}


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



werde ich vielleicht noch benutzen zum representative-terms-fürs-cluster-finden. BERT is the best one, blablabla. 
Don't forget to mention \gls{distribhyp}


* BERT als "bestes (except gpt) Neural language Model for documents"  
TODO: Ist word2vec schon nen euclidian space? Why/Why not?



### Linear algebra stuff

#### Projecting and playing around with coordinate system

So how do we project the point onto the plane?
* [https://stackoverflow.com/a/17661431] all you have to do is find the perpendicular (abbr here |_) distance from the point P to the plane, then translate P back by the perpendicular distance in the direction of the plane normal. The result is the translated P sits in the plane.
