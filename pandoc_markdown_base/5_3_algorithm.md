## Big Picture (did we achieve our aims)
What were our original aims and did we achieve them

* ich hätte gerne sowas wie könig - mann + frau = königin \cite{Mikolov:Regularities}, nur halt mit mann und frau als einer achse, macht das sinn, ist das rausgekommen?
* There is certainly more work to do to increase robustness of the results in the sense that an unambiguous name for the resulting semantic direction comes - that is what we are aiming for. But again, testing the best name is only really possible in human studies.
* Testing only faculty is a big drawback, human studies would help
* Wie aussagekräftig sind überhaupt die Decisiontree-ergebnisse? -> OB das sinnvoll ist (Tiefer und tiefer drauf eingehen im hinblick darauf wie meaningful die results sind) ("was bedeutet das für mich")



## Hyperparams
* Were actually not that important. When finding the best config according to `get_best_conf("fachbereich", verbose=True, balance_classes=True, one_vs_rest=True, dt_depth=1, test_percentage_crossval=0.33)`, what config I received was really mixed, sometimes 50d was best, sometimes 200d. 
* The calculation How to find the best threshold for candidates