* Logistic regression instead of SVM
* Hyperparameters for metric: Kappa, Accuracy, NDCG
* Ranking is of the PPMI score in the BoW
* N best-scoring candidate features, with either Derrac's algorithm or k-means
* Centroid of the cluster = Average of the normalized vectors of the words
* Semantic spaces created by either of
	* MDS from angular differences of PPMI-weighted BoW
	* PCA from angular differences of PPMI-weighted BoW (no quadratic time)
	* Doc2Vec \cite{Le2014}
	* Averaged pretrained GLoVe of words with df $\geq$ 2 
	* Averaged pretrained GLoVe, weighted by PPMI
* ndims of embedding one of 50, 100, 200 
* Number of input-dimensions for clustering: 500, 1000, 2000
* Number of clusters {k, 2k} with k being the input-dimensions