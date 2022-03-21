

% Hab keine Metriken, aber was ich mir anschauen kann ist:

% - Ich zieh ja Daten als candidate terms raus nach denen man eine Dimension/Richtung benennen kann, wie “scary” bei den filmbeschreibungen. Die kann ich mir dann angucken zwischen 20 und 3000 Begriffen easy, alle mit Zahlenvektor (kommen ja auch aus nem Vector space). Dann will ich die Clustern, also nahe sind ähnlich: In Filmen, in deren Beschreibung das Wort “scary” oft vorkommt, kommt ebenfalls das wort “horror” oder “gore” oft vor. → das sollte ein Cluster sein.
% - Bei Kursen wäre ein Beispiel dafür “A1” und “A2”. Hab ich random in den Daten gesehen, klingt plausibel dass die ein Cluster sind, weil beide eben oft in Sprachkursen vorkommen. They aren’t.
% - Dann kann ich verschiedene Thresholds haben für minimale Ähnlichkeit. Wenn der zu klein ist, kommt nix in ein Cluster, wenn der zu groß ist, kommt “A1” in ein cluster mit “Course” and everything is over.
% - Dazwischen MÜSSTE ich erstmal mal noch viel härter die Kandidaten filtern, mega viel davon, wie das Wort “course”, ist crap. Warum? Es kommt über die Bank in komplett verschiedenen random Kursen vor, und zwar in like half of them. Wenn A1 in nem cluster mit course ist hab ich keinen information gain, weil dann ist das nicht das cluster der Sprachkurse sondern das von random 50% der Kurse.
% - → Man könnte meinen man kann Wörter die oft vorkommen (high doc freq) keine Keywords mehr werden. ABER es gibt auch wörter die oft vorkommen aber doch inhalt haben - das wort “science” kommt in coxi öfter vor als in kosmetologie oder Sportkursen. Oder das wort math, genau das will ich ja als dimension haben, kommt in supervielen kursen vor (SOLLTE MAN MEINEN, aber mein kack code erkennt es nicht als Keyword: ``ctx.obj["filtered_dcm"].doc_freq("computer", rel=True)` GOD WTF=
% - → Also naja, doc-freq ists halt auch nciht. Und ich starre drauf, seh’s nicht funktionieren, weiß nicht was ich machen soll.

% ---

% - Das word “computer” kommt in 2.7% Der Kursen vor?! Math in 0ß!



% OLD ONE FROM NOTION: Die Plots von visualize_mds_data.ipynb plotten und dabeischreiben dass mein Datensatz, zumindest was mein einziges leicht-zu-bekommendes Feature (→ Fachbereichtszugehörtigkeit) ja gar nicht so geil aussieht im Gegensatz zu bpsw movies

% was backslashorigalgos paper angeht: 
% Ich hab mir table 1 von [DESC15] angeschaut und mit deren daten nach-implementiert, und teilweise haben sie ihre ergebnisse schon verschönt -> butcher shop ist der place-type der am ~350zigst-meisten (je nach #dims) zwischen marketplace und slaughterhouse ist (see test_paper_table1_claims in test_semanticspace_measures.py)
% Wenn man sich in dem Paper mal die Movie-Cluster anschaut (einfach das textfile) sieht man dass das echt... bescheuert ist, die Cluster sucken hart

% * viel showcasen. Also mir 10 Kurse raussuchen die laut algorithmus nahe beieinander sind und sagen "hier, wir sehen die sehen tatsächlich related aus".
% * Drauf eingehen dass ich nicht wirklich metriken habe. This is not classification, I don't get a "87% accuracy" and can compare that, ich krieg cluster und muss mir angucken ob die "ähnlich sind wie ein mensch das macht" -> qualitative und quantitative analyse, beides mit grains of salt (quantiativ ertrickst metriken halt nen bissle -> Clustert das so dass ich den fachbereich dadrin wiedererkenne? )
% * Brauch ich mehr/bessere Daten? Wenn ich nur die 1000 mit den längsten Beschreibungen behalten würde und dann 10 solcher subsets hätte wären halt die Fälle wie "Tutoren sind: Susi Sorglos Willi Wacker" etc raus
% * ...ich kann auch mit Johannes' Datensatz mit Mapping Kurstitel -> DDCs vergleichen und gucken ob die shallow decision trees was ähnliches wie die DDCs extracten können als weiteren Klassifizerungs-Task nehmen! (see Masterarbeit/OTHER/study_behavior_analysis/EducationalResource-2022-01-20.csv), dann kann ich auch das Siddata/SidBert-Paper von Johannnes Referenzieren!
% * Was man als testing halt machen kann ist nen decision tree based on their features zu machen und zu gucken ob der einen held out test dataset klassifizieren kann.
% * Ein anderer Weg zum testen wäre auch ein classifier der nur anhand der most salient generated features versucht den kurs wiederherzustellen (das zeigt natürlich nicht ob es similar to how humans do it but part of it)
% * Metrik: Gucken ob es ähnlich wie FB Clustert => Da kann ich dann die Parameterkombi die die im paper gemacht haben plus nen paar andere in ne tabelle packen und fertig
% * Check my claim in the results for place-types (chapter 6.1), that the classification based on word embeddings may even be better than their SVM_MDS!!!
% * Ich hab ja den Fachbereichs-Classifier gemacht, wenn ich jetzt noch die shallow decision trees mache kann ich ja legit accuracies vergleichen

\begin{itemize}
	\item \cite{Derrac2015} evaluated using a bunch of commonsense reasoning based classifiers (want to show that at least as performant than standard approaches, but can give intuitive explanations) (these reasoning-classifiers can be linked to intuitive explanations: 1-NN is "Y is of the same class as X because X closest to Y", but also more complex ones.) 
	\item 
\end{itemize}

* This is clustering and looking if it corresponds to human judgement, which unfortunately doesn't allow for a simple accuracy and be done with it.
* So, the papers that did this come up with a few things
* [TODO: the shallow decisiontrees of one of the followups]
* DESC15 "evaluate the practical usefulness of the considered semantic relations" by checking "their use in commonsense reasoning based classifiers", like interpolation and a fortiori inference (chap 5)


* DESC15 tests like this: Section 6.1: Evaluate whether the derived relations are sufficiently accurate for classification, and 6.2 is then comparison with crowdsourcing experiments (more subjective aspects, the question “are the relations useful explanations?”)

