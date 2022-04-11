
* I wrote before that "taking all words as candidate and running a \gls{pos}-tagger led to suboptimal results in previous experiments, which indicated that the robustness of the algorithm is increased if less candidates are used. This will be forther elaborated in the discussion." -> say something about the number of candidates and how its better the way I do it.

* Which kappa is best and was it important to differentiate?
* Was it worth to test multiple kappas
* Is Accuracy better than Kappa, like Ager assumed?
* compare tf-idf and ppmi (can I confirm that ignoring tf-idf from the start was smart?)


* Were actually not that important. When finding the best config according to `get_best_conf("fachbereich", verbose=True, balance_classes=True, one_vs_rest=True, dt_depth=1, test_percentage_crossval=0.33)`, what config I received was really mixed, sometimes 50d was best, sometimes 200d. 
* The calculation How to find the best threshold for candidates
    * did the threshold help?
* obviously 3d is worst, often didn't even have 6 values with kappa > 0.5
* Did lemmatizing help?
* was ppmi better than tf-idf? on par? worse?
* was the 80 words threshold good?
* were we correct in assuming that accuracy may be better than kappas? (no)

\cite{Ager2018}:
* In principle, we may exptect that accuracy and kappa are best suited for for binary features, as they rely on a hard separation in the space between objects that have the word in their BoW representation and those that do not, while NDCG should be better suited for gradual features. => BUT NO