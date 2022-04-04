<!-- How we do the results: 
* Erstmal sanity-check "mein algorithmus performt wie die paper, -> reasonable dass richtig", DANN analyse im hinblich auf die fachbereiche, um dann in der diskussion in "shortcomings" zu sagen "naja jetzt haben wir das auf fachberecihe gemacht aber wie gut der auf anderen domänen performt müsste man human studies"
* In Results nicht drüber reden ob und warum das mit den decisiontrees sinnvoll ist, und erst in der discussion darauf zurückkommen OB das sinnvoll ist (Tiefer und tiefer drauf eingehen im hinblick darauf wie meaningful die results sind) ("was bedeutet das für mich")
* In der Discussion kann ich dann auch wieder bezug auf die orig-paper ziehen "im vergleich zu demundem haben wir das geliche rausbekommen, ...", "die arbeit extended dasunddas weil wir's in ne andere domäne geschoben haben und ...", und nochmal kritisch reflektieren wie gut meine bewertung ist ("shortcomings"-section)
* Ich habe schon eine eindeutige Fragestelleung ("Kann man X auf educational resources anwenden") -> danach stringent und explizit vorgehen! Das ist meine Hypothese, these are my methods, this my results, this my conclusion! 
 -->

Research Question: Ich will die Methodik von dem Paper auf educational resources Applien. Das unbedingt in discussion & conclusion aufgreifen.


## SORT ME

* Neben den Clustern die ich mir anzeigen lassen kann und qualitativ analysieren kann, kann ich mir auch die distances to the origins of the respective dimensions (induced by the clusters), what induces the respective rankings! (see DESC15 p.24u, proj2 of load_semanticspaces.load_projections) anzeigen lassen - da kann ich sagen "term xyz ist bei "nature" am höchsten".
	* FRAGE: sind dafür ÜBERHAUPT IRGENDWIE die cluster relevant??! Ich meine es wird nur die distance zur hyperplane vom main-term considered, so why the hell even cluster?!




## Interpreting results

### Placetypes

* Elaborate why I am better than they 
    *  GRAIN OF SALT: dass sie nie erwähnen ob sie bei den shallow decision trees one-vs-rest machen --> HOW DID THEY achieve even okay-ish accuracies with the shallow decision-trees? a depth 3 tree has max 2^3 = 8 leaves, so if your to-be-categorized has 100 classes, you'll definitely suck!.
        * read https://machinelearningmastery.com/one-vs-rest-and-one-vs-one-for-multi-class-classification/ wegen one-vs-all undso
    * What else?
        * I assume it's bc I looked for the best config for this particular task, which is a different one for each combination of dataset x dt-depth x classification-target, and I assume the others did some hyperparam-tuning before and then decided for one config for all datasets (or rather 3-4 different ones, but independent of dataset,dt-depth,classificaiton-target)
        * Weil ich beste param-kombi nehme (dataset x dt-depth x classification-target) 
            * das ist nicht worauf der algo optimiert ist, ich nehm aber dann das beste von 80
        * verweis auf full-tfidf-vs-ppmi-table: tf-idf ist much better
        * bin mir nicht sicher ob die 1vsrest machen oder nicht
            * begründung dafür... ABER sie schreiben ja auch dass sie sklearn nutzen -> doc sagt muss so
        * dass die für mehr entities labels haben, die aber nicht public sind?


### Siddata

* In den results sind ja quantifizierbare und gute Zahlen drin, das ist ja in der discussion ein argument dafür dass es funktioneirt
    * Welche Fachbereiche hab ich gut klassifiziert und welche schlecth? (...das kann ich auch mit den preliminary results in Johannes sidBERT vergleichen, see slack 29.3. 10:00)
    * Warum-auch-immer Biologie/Chemie und Physik so bescheuerte cluster haben, alle anderen gehen mega klar
* Nochmal drauf zurück dass die ja ppmi statt tf-idf nutzen und ob meine Ergebnisse confirmen können dass es dazu any reason gibt oder nicht
* Anhand von set-overlapts von meinen placetypes zu deren "die hyperparam kombi die am closesten zu deren ergebnissen ist" sagen können
* Sagen ob das eigentliche ziel erreicht ist - ich hätte gerne sowas wie könig - mann + frau = königin [in that context reference \cite{Mikolov:Regularities}], nur halt mit mann und frau als einer achse, macht das sinn, ist das rausgekommen?
* Das wie gerade auch in der duplicate-per-combi-of-ndims-and-ncats sichtbar wird dass letztlich halt "kurs 123" und "!!FÄLLT AUS!! kurs 123" auf den selben fallen, was zwar quantiativ scheiße ist aber ACTUALLY GOOD

### Regarding data

* Auch wenn die Performance schlecht ist, liegt das oft am Dataset
    * wenn man sich anschaut WAS denn falsch klassifiziert wurde sieht man halt dass die Kurse die offensichtlich nicht Mathe sind eben falsch klassifiziert wurden
    * ...oder wenn dann "logic" in mathe landet, well it's not wrong, it's the dataset
    * Oder eben auch dass die Sachen mit dem dass 2 EIGENTLICH gleiche kurse auf das selbe mappen

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

* I am very surprised that the algorithm works on the dataset even though its so much differently than the original ones, so apparently tha glrithm is hinreichgend generell


<!-- ========================================================================= -->
<!-- ========================================================================= -->
<!-- ========================================================================= -->
## Shortcomings

* Erstmal sanity-check "mein algorithmus performt wie die paper, -> reasonable dass richtig", DANN analyse im hinblich auf die fachbereiche, um dann in der diskussion in "shortcomings" zu sagen "naja jetzt haben wir das auf fachberecihe gemacht aber wie gut der auf anderen domänen performt müsste man human studies"
* The fact that I don't use intercepts of the decision_planes in derive_conceptualspace.semantic_directions.create_candidate_svm.select_salient_terms (dass ich beim ganzen koordinatensystem-schieben den intercept ignoriere!)
* dass das hier auf bag-of-words basiert und dass es daher wie alle bag-of-words sachen das problem hat das einunddasselbe sehr verschieden ausgedrückt werden kann, und LSA wäre einer der wege das zu beheben (another one: word embeddings)

<!-- ========================================================================= -->
<!-- ========================================================================= -->
<!-- ========================================================================= -->
## Results regarding the Implementation and Goals for the architecture (in terms of architecture quality)

First of all, we wanted to show that 

* this implementation works
* the results of \mainalgos are not a fluke (that the algorithm works at all)

The results on placetypes have shown that that's the case.


<!-- Eine meiner 2 research questions ja war "wie sieht eine gute architecture aus", so if the architecture is good and how it (and thus a good architecture) looks are results!! -->
We remember, we also wanted to build a good architecture and set goals for that, such as adaptability to new datasets etc. We said a good architecture would show in adaptability, scability, ..., so we wanna show that these are achieved. 

* We are scalable and can run massively parallel (that you'll have to believe me, it's one command to run on the grid and I would say that's pretty noice).
* Keep in mind when reading the other sections of the results that all plots and tables you'll see are explictly linked and easily re-creatable and runnable
* We ran the stuff on other datasets\footnote{See Table with datasets and the respective notebooks and the quick datasets section} and it ran through, so we're adaptable.
    *  wie schnell es geht den bums auf neue datasets zu werfen (100k coursera, 90k short stories, ...) und dass ich damit schon angefangen hab 

* dass sowohl die architektur hierfür, als auch meine Grid-solutions eine major contribution sind die sich sehen lassen können!
* Development was really easy as soon as the architecture did what it should so yes, future work will be made a lot easier, our goal of "Make a good architecture" (see \autoref{sec:goals_research_questions} is fulfilled.)
<!-- In der conclusion noch eindeutig schreiben wie dolle die Architecture geworden ist und wie viel einfacher sie arbeit in der Zukunft macht -->


<!-- ========================================================================= -->
<!-- ========================================================================= -->
<!-- ========================================================================= -->
## Opinion to / Evaluation of Derrac15 etc:

* dass deren merge-candidate-directions-schritt (alle nehmen und die zum closestem herclustern und dann die richtung des T^0.5 übernehmen) ziemlich whack ist, ich schon einige wege hab damit umzugehen but many better ones are imaginable
* Der Kappa-Score der rankigns vergleicht ist für mich ne kack metric weil ich ebennicht reviews nehme und more-occurences better-candidate heißen -> gucken wie ich stattdessen gute dimensionen und cluster finde (klingt doch so als sei accuracy/f1/... doch wichtig)



* Small community, unfortunately
    * I assume \mainalgos shared data, at least the didn't  n-gram problem I mentioned.
    * As all of these publications share Prof. Steven Schockaert as last author, it seems plausible that a) the latter ones are legit improvements upon the first, b) at least to a certain degree they can share code and data, c) this field of work is constrained to a small community, without any alternative implementations or substantial improvements from outside of it.
        * But Johannes said "I would either leave this part out, as it is implicitly clear from the first sentence or restructure/reformulate it. The way it is right now, it seems like a speculation on your part at least for b) and c). The small size of the community could be a point worth mentioning in the concluding remarks of your thesis."


* Ich hab mir table 1 von [DESC15] angeschaut und mit deren daten nach-implementiert, und teilweise haben sie ihre ergebnisse schon verschönt -> butcher shop ist der place-type der am ~350zigst-meisten (je nach #dims) zwischen marketplace und slaughterhouse ist (see test_paper_table1_claims in test_semanticspace_measures.py)
* Wenn man sich in dem Paper mal die Movie-Cluster anschaut (einfach das textfile) sieht man dass das echt... bescheuert ist, die Cluster sucken hart
* Check my claim in the results for place-types (chapter 6.1), that the classification based on word embeddings may even be better than their SVM_MDS
* Set-overlap of candidate-terms for different #dims is COMPLETELY off!!

* dass sie nie erwähnen ob sie bei den shallow decision trees one-vs-rest machen --> HOW DID THEY achieve even okay-ish accuracies with the shallow decision-trees? a depth 3 tree has max 2^3 = 8 leaves, so if your to-be-categorized has 100 classes, you'll definitely suck!
* dass sie, wenn sie die orthogonalen der decision-planes averagen, definitiv auch den intercept berücksichtigen müssten!
        (...would they? I mean they are only concerned with direction and ranking, so there it's just an added, irrelevant, constant)

* Robustness: Dass over all n-dims (20, 50, 100, 200) einfach 21832 (literally alle bis auf einen!) candidates in T^0.1 sind (ALSO FAST ALLE), und T^0.5 könnte schlechtestenfalls 740 (400+200+100+40) werte haben, bestenfalls 400, und hat 697 - soll heißen WELCHE ausgewählt werden ist kraass abhängig von der #dimensions, which is bad
    ==> I would really like to say somthing about the robustness of this algorithm for multiple runs. For that I can either take my own runs which I don't know if they are okay or theirs across dimensions. (Maybe some 2d-plot looking like a confusion matrix showing the overlap of T^0.5 terms, also intersection over union, for different runs (and also for the 4 n-dims in orig desc15))

* Regarding the fact that they say that they have to use MDS    
    * My line of arugmentation here:
        * Gerade für betweenness macht es sehr sinn dass es ein metric space ist
        * Deswegen macht Derrac2015 MDS, it being the only one dass distances erhält
        * ABER Derrac2015 re-embedded halt nach dem step mit MDS das ganze in nen neuen space, which should make it completely irrelevant ob der zwischenschritt jetzt metric war oder nicht
        * ABER Derrac2015 testet halt für betweeness in ebendiesem zwischenspace und ebennicht im final space
        * ABER Ager2018 und Alshaikh2020 interessieren sich nicht für den zwischenspace, behalten aber trotzdem MDS -> I think they are wrong in their assumption
    
    * ..mein grain-of-salt dass ich nicht sicher bin ob es relevant ist dass der schritt von dem sie sagen dass er metric sein muss metric sein muss?!
    * In deren Papern klang das so als würden sie die Dinge für die das relevant ist (betweenness etc) schon vor dem re-embedden machen!
    * in [DESC15] machen die wirklich immer ne SVM für genau einen Term, und gucken sich anschließend an was für terms dann ähnlich clustern. [VISR12] hingegen (und viele andere!) versuchen erst latent kram zu finden, wodurch das das clustering imo viel besser funktionieren wird weil es viel weniger sparse ist (->und die "contains one-of-the-terms" klasse nicht so verschwindend gering ist compared mit der "doesn't-contain-the-one-term") Laut [DESC15] gibt's da keine Methoden die den metric space erhalten, die frage ist halt wie wichtig das ist für das was man erreichen will!

    * Uhhhm ist es nicht scheißegal ob der ursprüngliche space metrisch (MDS) ist oder nicht, wenn letztlich EBENNICHT nur das koordinatensystem gedreht wird sondern die rankings für die einzelnen word-directions genutzt werden?! weil ob das metrisch ist oder nicht ist doch komplett unabhängig davon obs ursprünglisch metrisch war?!
    * Gärdenfors basically said we could build a CS with "Dimensionality Reduction from the high-dimensional input (neurons) eg using MDS into a euclidian space, and then geometric reasoning on that" including some examples of kinds of reasoning, so actually the exact algorithm \cite{Derrac2015} did was extremely naheliegend (put some obvious NLP modelling to that like \cite{Turney2010} explained and you're pretty much exactly at their algorithm)
    * ....but even more reason to make me think that it may have been their error to keep the enforcement that the MDS-result must be a euclidian space, when afterwards they have the additional step of using their rankings anyway! (...which btw brings me to the question what that does to distances?!)

* We say we're dealing with POINTS but we're constantly doing cosine similarity, isn't the important difference between points and vectors that cosine would be relevant for vectors, but euclidian(/..) distance for points?!
    * We're always concerned with points, not with vectors!!! gucken was das für auswirkungen hat!!! (AUCH: points, not convex regions (like CS SHOULD be))     
    * WHY do they always calculate with cosine-distances (eg in my `select_salient_terms`) - I thought the important thing is that we are talking about POINTS, NOT VECTORS  (also - param-combi for closeness by euclidian distance isntead of that)
    * dass mich wundert dass deren distance measure zu funktionieren scheint, wo sie doch ebendoch vectors considert und nicht punkte!
        * ...WO merkt man denn überhaupt dass sie punkte haben und nicht vektoren? Bei der SVM (siehe meine Stackoverflow frage!) ists ja relevant.... und da nutzen sie punkte... riiight? Am I doing it like they did? Are we all doing it correct?
        * (see also "The fact that I don't use intercepts of the decision_planes" in shortcomings )



## Conclusion

Ich habs geschafft diesen Algorithmus zu reproduzieren und es scheint ganz gut zu funktionieren, feddisch.

* How good do I think does the algorithm capture CS? How useful do I think CS are in general (two perspective, as model of human concept formation AND algorithm-that-allows-certain-things-like-reasoning), and how good do I think the algorithm does it? Is the algorithm practical?
* So now we have to answer the question if we achieved do what motivated us in the first place: easily and automatically create structured knowledge bases .My opinion is that the need to create such knowledge bases is absolutely there, but I am more than unsure if this is the best imaginable algorithm. Of course, I see the reasoning for the distancematrix->MDS to ensure the resulting place is actually metric (an assumption more and more dropped by the two followup-papers)... but maybe before and after we can use neural techniques? Like idk doc2vec für die distance matrix, dann gerne MDS, und candidate terms sind dann word embeddings we threshold their closeness to the document embedding? Or also use LSI/LDA? (see my suggestion for an algorithm)
* In die Conclusion auch die Frage inwieweit das jetzt conceptual spaces sind (sehr viele vereinfachende sachen, like no convex regions but simply dots)
    * [AGKS18] ist da auch mehr humble als [DESC15] und sagt "The idea of learning semantic spaces with accurate fea- ture directions can be seen as a first step towards methods for learning conceptual space representa- tions from data"
    * SO I'd say just becuase of the fact that we're not talking about points but regions we cannot... and the two follow-ups even drop the metric requirement so there I'd say definitely not.