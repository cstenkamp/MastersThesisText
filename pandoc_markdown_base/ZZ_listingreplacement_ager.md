* logistic regression instead of SVM
* Hyperparameters for metric: Kappa, Accuracy, NDCG
* Explcitly say that the ranking is of the PPMI score in the BoW
* N best-scoring candidate features (N hyperparam)
	* Either Derrac Or k-means
* Centroid of the cluster = Average of the normalized vectors of the words
* Semantic spaces created by
	* MDS from angular differences of PPMI-weighted BoW
	* PCA from angular differences of PPMI-weighted BoW (no quadratic time)
	* Doc2Vec (Le and Mikolov 2014)
	* Averaged pretrained GLoVe of words with df >= 2("surprisingly competative")
	* Averaged pretrained GLoVe, weighted by PPMI
* ndims of embedding 50, 100, 200 
* number of direcitons for cluster INPUT 500, 1000, 2000
	* number of clusters {k, 2k} with k being the ipnut