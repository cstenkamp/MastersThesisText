According to \cite{Turney2010}, vector-space models fall into different categories depending on if the similarity of documents (Term-Document-Model) or of words (Word-Context-Model) is in question.  The former relies on the \textbf{bag-of-word hypothesis}, stating that documents with similar words have similar meaning. The Word-Context-Model relies on the \textit{distributional hypothesis}, stating words that occur in similar context have similar meanings.



https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction: \q{This specific strategy (tokenization, counting and normalization) is called the Bag of Words or “Bag of n-grams” representation. Documents are described by word occurrences while completely ignoring the relative position information of the words in the document.")}

that I'm using BOW and that I dislike it \cite{Le2014}: "Despite their popularity, bag-of-words features have two major weaknesses: they lose the order- ing of the words and they also ignore semantics of the words. For example, “powerful,” “strong” and “Paris” are equally distant" Bag-of-n-grams would alleviate this, but even though it "considers the word order in short context, it suffers from data sparsity and high dimensionality" (bag of n-grams model would create a very high-dimensional representation that tends to generalize poorly)

dass das hier auf bag-of-words basiert und dass es daher wie alle bag-of-words sachen das problem hat das einunddasselbe sehr verschieden ausgedrückt werden kann, und LSA wäre einer der wege das zu beheben (another one: word embeddings)

-> we will go into some details on these steps, LSI is a good candidate to smooth the frqeuncy matrix but bc as we said we need a metric space we (like \cite{Derrac2015}) do MDS


* Write how a Bag-Of-Words is created and what it shortcomings are and find a source that compares how good a Bag-Of-Words (that necessarily doesn't contain and information about their position) can be, compared to better document embeddings like LSTMs, Doc2Vec or whatever else there is (I mean after all, a "not" may be ignored and the meaning inversed which should be supergau), and also how much better it becomes if one also consideres 2-grams, 3-grams, ...


* There is a very important problem in information retrieval and also for our case: Natural language is ambiguous! when trying to match words of queries with words of documents, you want to retrieve on the basis of conceptual content, and individual words provide unreliable evidence about the conceptual topic or meaning of a document. (the words used in the query may not be the same as the ones in the documents, problems here are synonymy (multiple words, same meaning) and polysemy (multiple meanings, same words))
* There are usually many ways to express a given concept, so the literal terms in a user’s query may not match those of a relevant document, or you'll get results for another meaning of the word you're looking for.
=> Very important thing is thus to make similar words close. Both LSI and neural embeddings want to solv ethis.
dass LSA das bag-of-words problem beheben würde


The only information that can be taken into account when comparing two texts, or a text and a query, are the words it is made up from (...and their constellation, which is why \gls{word2vec} works better than \gls{bow}-approaches). 


FIND ME A PLACE

\cite{Ager2018}: \q{However, while LDA only uses bag-of-words (BoW) representations, our fo- cus is specifically on identifying and improving features that are modelled as directions in seman- tic spaces. One advantage of using vector spaces is that they offer more flexibility in how additional information can be taken into account, e.g. they allow us to use neural representation learn- ing methods to obtain these spaces.}