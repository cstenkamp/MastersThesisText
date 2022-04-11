## Features

* Be able to enable/disable or select between all components
	Like...
	- [ ]  the contribution of [AGKS18] or [ALBS20]
	- [ ]  which classifier to use to split positives and negatives in step 1 (SVM, logistic regression)
	- [ ]  Cohen's Kappa vs Accuracy vs NDCG
	- [ ]  Kmeans vs [DESC15]'s clustering-algorithm
	- [ ]  how to create semantic space(step 0) (MDS, PCI, Doc2Vec, Average GloVe ([https://nlp.stanford.edu/projects/glove/](https://nlp.stanford.edu/projects/glove/))
* Hyperparameters
	- [x]  #dims of the vector-space (50,100,200)
	- [ ]  #dims as input to the clustering algorithm (500,1000,2000)
	- [ ]  number of clusters (1*inputdimsforclusalgorithm, 2*inputdimsforclusalgorithm)
* Extracting Candiate Terms
	- The way of DESC15
	- The way I'm doing it right now
	- The Tag-LSI-Sim as [VISR12] do it (page 13:15)
	    [[VISR12] have the Tag-LSI-SIM, die brauch ich](https://www.notion.so/VISR12-have-the-Tag-LSI-SIM-die-brauch-ich-0868f6c7a20147f582029163f39c225e)


## Differences to \mainalgos / Contributions of this thesis

* Because of the nature of the dataset I need to do some things differently 
    * I'm not working with reviews or collections-of-tags, that means their "how does this dimension correspond to the count in the reviews" doesn't make sense
        * their algorithm is tailored to this. Take their success-metric for the SVMs splitting the embedding. The more often the word "scary" comes in the concatenated reviews, the more scary the movie is. Sounds legit. The more often the people that took pictures at a particular place mentioned the "nature" of that, the more relevant "nature" is to that place. Also legit. But in the descriptions for courses that involve a lot of mathematics, it is not necessarily the case that the term "mathematics" occurs often. So due to the different nature of my dataset I have to go beyond their algorithm at some points - in this case it is probably the case that different kinds of mathematical terms actually do occur more often, so I'd need calculate these kinds of kappas not based oon a single term but ALREADY on a cluster of terms (... and I can bootstrap my way there, because after I do this I get more words to add to my cluster, rinse and repeat!)
* Differences bc of different dataset 
    * Because less words
        * Many candidates occur only in some 25 entities, which makes the ranking rather useless (99.999% of values are zero) -> [WHAT]
    * Because nicht je-öfter-desto-scarier
        * Not compare Rankings, but [WHAT]
        * Using WordNet or smth
        * "reclassify" as possible technique to get cluster direction
        * hoher overlap in wörtern von 2 dokumenten -> alle wörter des einen might as well have been in there
    * cluster-to-reclassify with Die-besten-30%-beim-clustern
    * My ways of finding the name of the cluster
    * Ich nehme schon (wie \cite{Ager2018}) andere dinge als measure of faithfulness (precision, recall)


