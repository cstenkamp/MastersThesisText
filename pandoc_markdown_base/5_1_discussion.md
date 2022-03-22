Research Question: Ich will die Methodik von dem Paper auf educational resources Applien. Das unbedingt in discussion & conclusion aufgreifen.

%TODO: darauf eingehen ob wir das was uns in the first place motiviert hat, erreicht haben - also ob wir jetzt easy und automatisch structured knowledge bases erzeugen können. My opinion is that the need to create such knowledge bases is absolutely there, but I am more than unsure if this is the best imaginable algorithm. Of course, I see the reasoning for the distancematrix->MDS to ensure the resulting place is actually metric (an assumption more and more dropped by the two followup-papers)... but maybe before and after we can use neural techniques? Like idk doc2vec für die distance matrix, dann gerne MDS, und candidate terms sind dann word embeddings we threshold their closeness to the document embedding? Or also use LSI/LDA?

%TODO: dass sowohl die architektur hierfür, als auch meine Grid-solutions eine major contribution sind die sich sehen lassen können!

In die Conclusion auch die Frage inwieweit das jetzt conceptual spaces sind (sehr viele vereinfachende sachen, like no convex regions but simply dots)
[AGKS18] ist da auch mehr humble als [DESC15] und sagt "The idea of learning semantic spaces with accurate fea- ture directions can be seen as a first step towards methods for learning conceptual space representa- tions from data"
-> SO I'd say just becuase of the fact that we're not talking about points but regions we cannot... and the two follow-ups even drop the metric requirement so there I'd say definitely not.



% * Nochmal drauf zurück dass die ja ppmi statt tf-idf nutzen und ob meine Ergebnisse confirmen können dass es dazu any reason gibt oder nicht
% * Anhand von set-overlapts von meinen placetypes zu deren "die hyperparam kombi die am closesten zu deren ergebnissen ist" sagen können
% * Sagen ob das eigentliche ziel erreicht ist - ich hätte gerne sowas wie könig - mann + frau = königin [in that context reference \cite{Mikolov:Regularities}], nur halt mit mann und frau als einer achse, macht das sinn, ist das rausgekommen?
% * Ich habe schon eine eindeutige Fragestelleung ("Kann man X auf educational resources anwenden") -> danach stringent und explizit vorgehen! Das ist meine Hypothese, these are my methods, this my results, this my conclusion! 


TODO:  In der conclusion noch eindeutig schreiben wie dolle die Architecture geworden ist und wie viel einfacher sie arbeit in der Zukunft macht
