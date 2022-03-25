
### Opinion to / Evaluation of Derrac15 etc:

* Ich hab mir table 1 von [DESC15] angeschaut und mit deren daten nach-implementiert, und teilweise haben sie ihre ergebnisse schon verschönt -> butcher shop ist der place-type der am ~350zigst-meisten (je nach #dims) zwischen marketplace und slaughterhouse ist (see test_paper_table1_claims in test_semanticspace_measures.py)
* Wenn man sich in dem Paper mal die Movie-Cluster anschaut (einfach das textfile) sieht man dass das echt... bescheuert ist, die Cluster sucken hart
* Check my claim in the results for place-types (chapter 6.1), that the classification based on word embeddings may even be better than their SVM_MDS
* Set-overlap of candidate-terms for different #dims is COMPLETELY off!!


### Conclusion regarding results / OUTLOOK

* Would more/better data help? Wenn ich nur die 1000 mit den längsten Beschreibungen behalten würde und dann 10 solcher subsets hätte wären halt die Fälle wie "Tutoren sind: Susi Sorglos Willi Wacker" etc raus
* You could do the shallow-decisiontrees-thingy for other attributes of the dataset than I currently have (possible Attributes für eine Taxonomie von Kursen) (see: https://studip-etherpad.uni-osnabrueck.de:9001/p/SIDDATA_AI_Categories)
    - "Schwierigkeit" -> Durchschnittsnoten?
    - "Komplexität" -> Avg. Semester der Teilnehmer?
    - "Offenheit" -> #Students eines anderen Fachbereichs
    - Aufwand -> #ECTS die der Kurs gibt
    - Vorraussetzungen -> stehen in StudIP, sonst profile der studierenden die ihn belegen
* IntroAI für dieses Jahr ist in Stud.IP nen komplett anderer Kurs als für letztes jahr 
    * Tobias hat was gebaut dass die abgleicht! Und er will k-anonymisierung machen. Das vergrößert die Daten sodass es für jedes Datum mindestens k (say 10) Studierende gibt für die etwas zutrifft. Da muss man Daten wegwerfen.
    * Mit meinen Attributen gibt's einige Probleme. Noten gibt's nicht, "allerschweste Datenschutzbedenken". Was studiert wer und in welchem Semester haben wir nur für den Zeitpunkt der Abfrage -> in kombi mit der k-anonymisierung wirds da schwer zu sagen in welchem semester leute was belegt haben


### Stuff implemented ontop of the algorithm

* DO I have the movietuner?