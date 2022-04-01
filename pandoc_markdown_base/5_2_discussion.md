<!-- HIER: Results interpretieren (Tiefer und tiefer drauf eingehen im hinblick darauf wie meaningful die results sind) ("was bedeutet das für mich") -->


## Results regarding the Goals for the architecture (in terms of architecture quality)

<!-- Eine meiner 2 research questions ja war "wie sieht eine gute architecture aus", so if the architecture is good and how it (and thus a good architecture) looks are results!! -->


We remember, we also wanted to build a good architecture and set goals for that, such as adaptability to new datasets etc.
We said a good architecture would show in adaptability, scability, ..., so we wanna show that these are achieved. 

* We are scalable and can run massively parallel (that you'll have to believe me, it's one command to run on the grid and I would say that's pretty noice).
* Keep in mind when reading the other sections of the results that all plots and tables you'll see are explictly linked and easily re-creatable and runnable
* We ran the stuff on other datasets\footnote{See Table with datasets and the respective notebooks and the quick datasets section} and it ran through, so we're adaptable.

More basic than that, we want to show that 

* this implementation works
* the results of \mainalgos are not a fluke (that the algorithm works at all)

For those two points lemme present my results for placetypes




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



Research Question: Ich will die Methodik von dem Paper auf educational resources Applien. Das unbedingt in discussion & conclusion aufgreifen.

* In den results sind ja quantifizierbare und gute Zahlen drin, das ist ja in der discussion ein argument dafür dass es funktioneirt


How we do the results: Erstmal sanity-check "mein algorithmus performt wie die paper, -> reasonable dass richtig", DANN analyse im hinblich auf die fachbereiche, um dann in der diskussion in "shortcomings" zu sagen "naja jetzt haben wir das auf fachberecihe gemacht aber wie gut der auf anderen domänen performt müsste man human studies"


* We see in \ref{fig:text_per_dim} that using the respectively best-fitting DOCUMENT (without LSI or anything, just the one with the highest ranking!)  is often even the MUCH BETTER direction!!! 


* In Results nicht drüber reden ob und warum das mit den decisiontrees sinnvoll ist, und erst in der discussion darauf zurückkommen OB das sinnvoll ist (Tiefer und tiefer drauf eingehen im hinblick darauf wie meaningful die results sind) ("was bedeutet das für mich")

* In der Discussion kann ich dann auch wieder bezug auf die orig-paper ziehen "im vergleich zu demundem haben wir das geliche rausbekommen, ...", "die arbeit extended dasunddas weil wir's in ne andere domäne geschoben haben und ...", und nochmal kritisch reflektieren wie gut meine bewertung ist ("shortcomings"-section)

* theoretisch ist es auch möglich bspw nen network mit attention auf gewisse dinge wie fachbereich und anderes zu trainieren und dann rauszusuchen was die wichtigen ausschlaggebenden dinge für das Netzwerk waren

TODO: Welche Fachbereiche hab ich gut klassifiziert und welche schlecth? (...das kann ich auch mit den preliminary results in Johannes sidBERT vergleichen, see slack 29.3. 10:00)

%TODO: darauf eingehen ob wir das was uns in the first place motiviert hat, erreicht haben - also ob wir jetzt easy und automatisch structured knowledge bases erzeugen können. My opinion is that the need to create such knowledge bases is absolutely there, but I am more than unsure if this is the best imaginable algorithm. Of course, I see the reasoning for the distancematrix->MDS to ensure the resulting place is actually metric (an assumption more and more dropped by the two followup-papers)... but maybe before and after we can use neural techniques? Like idk doc2vec für die distance matrix, dann gerne MDS, und candidate terms sind dann word embeddings we threshold their closeness to the document embedding? Or also use LSI/LDA?

%TODO: dass sowohl die architektur hierfür, als auch meine Grid-solutions eine major contribution sind die sich sehen lassen können!

In die Conclusion auch die Frage inwieweit das jetzt conceptual spaces sind (sehr viele vereinfachende sachen, like no convex regions but simply dots)
[AGKS18] ist da auch mehr humble als [DESC15] und sagt "The idea of learning semantic spaces with accurate fea- ture directions can be seen as a first step towards methods for learning conceptual space representa- tions from data"
-> SO I'd say just becuase of the fact that we're not talking about points but regions we cannot... and the two follow-ups even drop the metric requirement so there I'd say definitely not.



I assume \mainalgos \todoparagraph{shared data, at least the didn't  n-gram problem I mentioned.}
sollte ja schon vorher erwähnt haben dass das thema leider nicht über diese small community hinaus geht




% * Nochmal drauf zurück dass die ja ppmi statt tf-idf nutzen und ob meine Ergebnisse confirmen können dass es dazu any reason gibt oder nicht
% * Anhand von set-overlapts von meinen placetypes zu deren "die hyperparam kombi die am closesten zu deren ergebnissen ist" sagen können
% * Sagen ob das eigentliche ziel erreicht ist - ich hätte gerne sowas wie könig - mann + frau = königin [in that context reference \cite{Mikolov:Regularities}], nur halt mit mann und frau als einer achse, macht das sinn, ist das rausgekommen?
% * Ich habe schon eine eindeutige Fragestelleung ("Kann man X auf educational resources anwenden") -> danach stringent und explizit vorgehen! Das ist meine Hypothese, these are my methods, this my results, this my conclusion! 


TODO:  In der conclusion noch eindeutig schreiben wie dolle die Architecture geworden ist und wie viel einfacher sie arbeit in der Zukunft macht

* Development was really easy as soon as the architecture did what it should so yes, future work will be made a lot easier, our goal of "Make a good architecture" (see \autoref{sec:goals_research_questions} is fulfilled.)
*  wie schnell es geht den bums auf neue datasets zu werfen (100k coursera, 90k short stories, ...) und dass ich damit schon angefangen hab 


* Warum-auch-immer Biologie/Chemie und Physik so bescheuerte cluster haben, alle anderen gehen mega klar


## Regarding the algorithm per se

How good do I think does the algorithm capture CS? How useful do I think CS are in general (two perspective, as model of human concept formation AND algorithm-that-allows-certain-things-like-reasoning), and how good do I think the algorithm does it? Is the algorithm practical?


Gärdenfors basically said we could build a CS with "Dimensionality Reduction from the high-dimensional input (neurons) eg using MDS into a euclidian space, and then geometric reasoning on that" including some examples of kinds of reasoning, so actually the exact algorithm \cite{Derrac2015} did was extremely naheliegend (put some obvious NLP modelling to that like \cite{Turney2010} explained and you're pretty much exactly at their algorithm)
....but even more reason to make me think that it may have been their error to keep the enforcement that the MDS-result must be a euclidian space, when afterwards they have the additional step of using their rankings anyway! (...which btw brings me to the question what that does to distances?!)

* We say we're dealing with POINTS but we're constantly doing cosine similarity, isn't the important difference between points and vectors that cosine would be relevant for vectors, but euclidian(/..) distance for points?!

I had this in the algorithm-section before:
* As all of these publications share Prof. Steven Schockaert as last author, it seems plausible that a) the latter ones are legit improvements upon the first, b) at least to a certain degree they can share code and data, c) this field of work is constrained to a small community, without any alternative implementations or substantial improvements from outside of it.
* But Johannes said "I would either leave this part out, as it is implicitly clear from the first sentence or restructure/reformulate it. The way it is right now, it seems like a speculation on your part at least for b) and c). The small size of the community could be a point worth mentioning in the concluding remarks of your thesis."

* Brauch ich mehr/bessere Daten? Wenn ich nur die 1000 mit den längsten Beschreibungen behalten würde und dann 10 solcher subsets hätte wären halt die Fälle wie "Tutoren sind: Susi Sorglos Willi Wacker" etc raus