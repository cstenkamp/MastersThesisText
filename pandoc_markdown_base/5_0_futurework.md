
 And once we did that, couldn't we even find the word-vector closest to the direction of these PCA-vectors to give it a name?

* Couldn't we even build a whole algorithm like that? 
* distancematrix -> MDS only required if metric.

Other way: BERT-embedding. Yields vectors, not points, but this means we can compare similarity using something like LSA (only neural, compare embeddings) -> candidateterms are not verbatim phrases but thresholded close vectors in a common space of docs and terms. 
* Just Neural Document-Embeddings, PCA on that, find the words whose embedding is closest to the top 200 PCA dims, define that as their axisname. Completely neural and thus more independent from the actual choice of words, doesn't lean on symbolic stuff.
* Maybe the metric of that space is too unnatural, but to fix that, after doing Embedding->PCA->MappingIntoThatSpace, can't we then create pairwise judgements from distances in each of the principal components (unit vectors of our new space) and than on that an MDS to get a Euclidean space, before doing the DeEmbeddingDimensionnames step? Or cohonen-networks?
