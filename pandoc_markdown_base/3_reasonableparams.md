
* [Ager/Alshikh] said that binary occurence was the best metric, I cannot believe this (I had reasons for this somewhere, that a bad word in the cluster would destroy it)

* Translate-policy: Obviously the translation won't be perfect, so we lose quality from translating, but on the other hand if it's in english you can use wordnet, which is a lot better than GermaNet, and also embedding-wise it's better
    * "Da, based on [source die die accuracy von dem gtranslate algorithm mit denen von menschen vergleicht], a gtranslate translation is as good as the average lecturer, it is assumed that translating the texts to english before using an english model can lead to better results
* Candidate word threshold: movies has samples-to-threshold value of 100, placetypes has 35, 20newsgrups has 614 so for 8000 courses any threshold from 2 to 25 seems reasonable? \cite{Derrac2015} say they intentionally kept the number of candidateterms approximate equal (at around 22.000), so to do the same I'd need a threshold of [TODO: optimal value]
* PPMI has high complexity, hence I use tf-idf


* WHen extracting ngrams we have to set a max-size, I'd argue its around 5.


### Optimal Parameters and Algorithm Complexity

* Explain why we thresholded at 80 words
* Calculate optimal Number Candidates the way derrac did it, and quickly look at tables 3.1 and 3.2 as basis
* theorize that accuracy may work better than kappa
* Come back to the reason why I extracted less candidates than \mainalgos!

\todoparagraph{In practical terms}, efficient calculation of the PPMI-score for high-dimensional \glspl{doctermmat} requires excessives amounts of RAM, as it does not appear to be implemented in any major Python-library and its calculating requires multiplication of huge matrices.
