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
