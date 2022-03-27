<!--oder: OUTLOOK -->

* Ich könnte die Schrittweise Anwendung des Algorithmus wie Alshaikh das gemacht haben mit "für die die politisch sind, what's their direction" mit Level 2 für DDC. "Für die die in 'Informatik' eingeteilt sind, wie gut kriegen wir deren sub-categorie hin?"



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


* Make interpretable classifiers with decision trees ("Was für einen Kurs willst du?" "Viel Mathe / Wenig Mathe" -> "Viel LinA / Wenig LinA" -> ...) (Figure 3 of Schokhard)
    * Oder halt sowas wie den Movie Tuner 
* Taxonomie erstellen
    * Wie DDCs (->daran lässt sich auch immernoch super evaluieren ;)
    * wie's ACCM CCS für Paper ([https://www.acm.org/publications/class-2012](https://www.acm.org/publications/class-2012))
        * damit kann's auch Paper recommenden ;)
* Conceptual Space an Kursen erstellen (die dann bspw die komplette Domäne der Mathematik erschließen ;)


### Low-Hanging-Algorithm-Addendums

* A lot from Tag-Genome 
    * The preprocessing for the text-freq they do Normalization of word frequencies  (make popular terms that naturally occur more frequently in user reviews not obscure others: compute z-scores by subtracting mean and dividing by standard deviation specific to each tag)
    * tag-share as dcm-quant-measure (und andere "relative frequency" geschichten)
* andere distance measures außer mean-ang-dist ausprobieren (metric space after all!)
* implement NDCG
* Instead of cosine similiarity between feature directions, \cite{Alshaikh2019} use the overlap of the positive-samples of two features as similarity measure
* Camel2009's technqiue to find cluster names: 
    * Carmel2009: One of the first systems that dealt with cluster labeling is the Scatter/Gather application [6]. In this system, in addition to the cluster’s important terms, the titles of documents that are mostly close to the cluster centroid are also considered for labeling, since usually titles are much more readable than a list of terms.
    * das kann man wunderbar mit dem lsi-ding [von [VISR12]!] verbinden, dass dann das (pseudo-oder-normal-) doc das dem am nächstem ist der clustername ist (geht recht schnell!!!)

* Extensively test using Doc-Embeddings instead of MDS (one of the MOST IMPORTANT)
* Extensively relying on Wordnet/Germanet 
	
[TODO: add those that I didn't do anymore from ONLY CODE_TODOS MRZ25+ : Base Algorithm Improvements/Additions here! ]

### Suggestion for what may even be a better algorithm

Another thing, won't PCA in the mix be a good idea? After having found a few important dimensions from the "those-whose-SVMdistancecorrelation-was-good", doesn't it make sense to then also find some other principal components, AKA important directions to explain the distinction between elements that must be given when embedding it onto a lower space that didn't have a word occuring very often in it? Such that our space is a closer representation of the real higher-dim space? And once we did that, couldn't we even find the word-vector closest to the direction of these PCA-vectors to give it a name? Couldn't we even build a whole algorithm like that? Just Neural Document-Embeddings, PCA on that, find the words whose embedding is closest to the top 200 PCA dims, define that as their axisname. Completely neural and thus more independent from the actual choice of words, doesn't lean on stuff from the symbolic level (such that the levels are in the same order that humans have)... Maybe the metric of that space is too unnatural, but to fix that, after doing Embedding->PCA->MappingIntoThatSpace, can't we then create pairwise judgements from distances in each of the principal components (unit vectors of our new space) and than on that an MDS to get a euclidian space, before doing the DeEmbeddingDimensionnames step? Alternatively we can also have a final layer of self-organizing-map-architecture on top for the distances, like even Gärdenfors in his book suggests


=======================================================================================================================
===================================================== FROM NOTION =====================================================
=======================================================================================================================



- Make interpretable classifiers with decision trees ("Was für einen Kurs willst du?" "Viel Mathe / Wenig Mathe" -> "Viel LinA / Wenig LinA" -> ...) (Figure 3 of Schokhard)
    - Oder halt sowas wie den Movie Tuner von [
- Taxonomie erstellen
    - Wie DDCs (->daran lässt sich auch immernoch super evaluieren ;)
    - wie's ACCM CCS für Paper ([https://www.acm.org/publications/class-2012](https://www.acm.org/publications/class-2012))
        - damit kann's auch Paper recommenden ;)
- Conceptual Space an Kursen erstellen (die dann bspw die komplette Domäne der Mathematik erschließen ;)

was man grundsätzlich tun kann ist eine Datenerhebung von studierenden die Daten freiwillig kundtun. Kann man natürlich innerhalb Coxi machen. "Vielleicht is so 'ne Befragung gar nicht so doof". Maybe als Plugin Studip plugin "hier hast du ne liste an kursen in die du eingeschrieben bist, sag doch mal ob der eher schwer/leicht war" etc -> Mit Felix absprechen, kann der ja auch viel gebrauchen

