* Evaluation in Stud.IP (which may then even be used for training something like \cite{VISR12}'s algorithm or the fine-tuing step of \cite{Ager2018})
* Building this thing as component into Siddata, mit einem Interface wie dem Movie Tuner

* Die Erweiterungen für den Algorithmus die ich considered habe die better-suited für mein dataset sein könnten
    * All ways of incorporating wordnet/germanet
    * The stuff that VISR12 did
    * Bootstrapping good clustered directions (with iterative application of SVM-Kappa and just literally with "which words occur in the same texts" and also with the LSA/LDA (which one) method like VISR12 did)


* Die Hyperparameter (also Algorithmen/Komponenten) von \cite{Ager2018} und \cite{Alshaikh2020} die ich noch nicht implementiert hab
    * GloVe anstelle von Dissim-Mat + Embedding
    * Fine-Tuning von Ager2018
    * Iteratively-finding-facets from Alshaik2019 (19!)
    * [I should have a table or a yaml earlier in the text, just mention all the not-implemented stuff from that]