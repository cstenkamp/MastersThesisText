
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

