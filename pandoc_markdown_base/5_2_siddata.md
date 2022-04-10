## Big Picture

Having evidence that the implementation does what it should and the algorithm itself works on other datasets, let us finally discuss the question if the methodology works for the domain of educational resources.
* Only Faculty! We know that this by far does not test everything the algorithm does or how it performs for other things-to-compare, so the best analysis would just be human studies.
    * We could to the shallow-decisiontrees-thingy for other attributes of the dataset than I currently have (see future work)
* In general we must say that we have really good accuracies and this really seems to indicate that it works.
    
## Fear of dataset differences

* Already when describing the datasets, we noticed that they are quite different. 
* In \autoref{sec:results_datasetdiffs} we looked at how the interim results differed and noticed that 
    * less candidates were produced
    * The #Texts containing a candidate are exponentially decreasing, which means that for many of the candidates that ARE produced the classification to measure the faithfulness has a really hard time
* BUT even with such vastly different look-of-the-dataset from the start AND different intermediate results making the downstream tasks less likely to succeed, the final performance is suprisingly good, indicating that the methodology is robust!
* As established, a very important difference is that more relevant words do not occur more often. \todoparagraph{we assumed before that} because of that, the kappas that compare rankings are not so good. WELL IS THAT THE CASE
* \todoparagraph{MOOORE}
* Auch wenn die Performance schlecht ist, liegt das oft am Dataset
    * IntroAI für dieses Jahr ist in Stud.IP nen komplett anderer Kurs als für letztes jahr 
    * wenn man sich anschaut WAS denn falsch klassifiziert wurde sieht man halt dass die Kurse die offensichtlich nicht Mathe sind eben falsch klassifiziert wurden
    * ...oder wenn dann "logic" in mathe landet, well it's not wrong, it's the dataset
    * Oder eben auch dass die Sachen mit dem dass 2 EIGENTLICH gleiche kurse auf das selbe mappen
    * There is really a lot of crap in the data, like the  "Tutoren sind: Susi Sorglos Willi Wacker" ones. If the performance is not enough, one may also check if taking only the 1000 with the longest decription would help
        * or only those ones where BERT can sucessfully classify the faculty. Again, faculty is not everything, BUT if the faculty CAN be extracted, cases that only list names or places are out (...except FROM the name of place follows the faculty but lets ignore that)






## Actual classification
* So we compared to BERT (85.19% accuracy), and to 3D-embedding (64.3% weighted accuracy), and we robustly achieved 81.4% accuracy \textbf{even when using only a single direction}! We seem to be really good on that regard
* Which Faculties did I classify well and which ones bad?
    * compare with prelimiary results in Johannes sidBERT vergleichen, see slack 29.3. 10:00
    * When looking at the examples per faculty, we observe mixed results. ON the one hand, erziehungswissenschaft is perfect, on the other hand physics and bio/chemie suckt. 
        * when looking at the class frequencies for these well yes, these two are among the smaller classes, but so are [2 others], so whyever them work but bio & pyhsik dont


## Qualitative Analysis

## Post-Hoc-Qualitative Analysis

* Das wie gerade auch in der duplicate-per-combi-of-ndims-and-ncats sichtbar wird dass letztlich halt "kurs 123" und "!!FÄLLT AUS!! kurs 123" auf den selben fallen, was zwar quantiativ scheiße ist aber ACTUALLY GOOD

