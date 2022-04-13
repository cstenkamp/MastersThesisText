
### Create Dissimilarity Matrix & Quantify


* First, we create a Doc-Term-Matrix counting the occurences of every word that occurs in any description and every description.  
    * This may optionally only include those terms that have a term-frequency of at least two (makes the dtm less sparse, but the information if a document contains many terms that are in no other document is lost)
    * This may optionally include n-grams (which makes the dtm a lot more sparse, but alleviates some of the typical problems of bag-of-words-representations at last to a certain degree) (see \ref{sec:techniques:bow} regarding BoW-shortcomings)
* Afterwards, the Doc-Term-Matrix may be converted into a quantification, such that the respective Bag-Of-Word Representations of the documents don't contain the raw counts, but the respective tf-idf/ppmi-representations, relative to all documents and all possible terms.


* My algorithm then saves this dissimilarity-matrix, and what follows is the embedding.
    * For this thesis, the creation of the dissimiliarity-matrix and the embedding are split into individual steps because both have a substantial runtime, and as the number of dimensions for the embedding is only relevant in the embedding-step, a lot of runtime can be saved if the dissimiliarity-matrix can be re-used for different embeddings and dimensions.


