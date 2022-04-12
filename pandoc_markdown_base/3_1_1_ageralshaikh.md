

Regarding Ager and Alshaikh:

* RaZb20 tried Doc2Vec instead of MDS and it performed worse!

* \cite{Alshaikh2020} do Kappa on binary, I can't believe that's good


* [AGKS18] haben den candidate-filter-teil konfigurierbar (und sagen bei denen ist accuracy even better than kappa)

* Argue:
    * doc2vec nicht implementiert weil schlechter bei ager.
    * Finetuning nicht drin weil nur marginal besser bei ager (ref tabelle im anhang)
    * ...ähnliche gründe für alshaikh finden

* Binary occurence as best metric? I can't believe that
* Who said kappa is a bad value?

* \textcite{Alshaikh2020}
    * Well, do the stuff iterative cluster stuff
        * "When representing a particular entity in a conceptual space, we need to specify which domains it belongs to, and for each of these domains we need to provide a corresponding vector." 
        * then they show their example of something that is not seperable with a hyperplane unless we specify subdomains, maybe just steal their plot that explains their one contribution to 99%
    * Cluster with affinity propagation
    * Do Kappa on Binary (-> see later)
        * for them, the binary "does the word occur in the description" is the only sensible signal, no ppmi or anything! (page 2, footnote 1 of RaZb20)

## \textcite{Alshaikh2020}

Important to mention that they iteratively find "disentangled" features and thus embed the stuff in several uncorrelated low-dimensional subspaces


## \textcite{Ager2018}

The main contribution of \textcite{Ager2018} is a postprocessing step that changes the final space such the ranking of entities \wrt each feature direction more closely mimics the ranking of frequencies of that direction's cluster words. The reasoning is that the original embeddings from which the feature directions are created are based on global similarity. This makes it very vulnerable to outliers which often take up extreme positions. If one now creates the feature directions from the space, these outliers are assumed to have certain properties. So the space is optimized for that, which limits the quality of feature directions in the space. Problem again is global similarity: If one entity ranks high for a feature, it is very likely that another entity that is close to that will also rank high for this feature, even though it may be something completely different. So to get better feature directions one has to distort the space. 

They do this fully unsupervisedly as an extra step after the full pipeline of \cite{Derrac2015}, by again using the BoW representation of the entites. After the clusters are collected and the entities re-embedded, for each feature a new ranking is computed by the summed frequency of any of a cluster's words per feature and entity. Each entity is thus represented as Bag-of-Clusters and again scored with PPMI to generate a ranking for each cluser/direction. This ranking is then used as a target for a simple \gls{ann} that distorts the space representation.

Generally this is a great idea. Among others the explicit usage of all cluster-words should help, as it is a lot less sparse than a single word that only occurs in 0.6\% of entites. However the results of their approach are mixed: For some of their considered datasets the fine-tuning even decreases performance - according to the authors especially \q{when the considered categorizes are too specialized} \cite{Ager2018}, because the resulting space is too much distorted towards the selected features.\footnote{See also \autoref{tab:f1_placetypes_long}} Considering its bad performance, this contribution was not considered in this work.






## Ager do

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
