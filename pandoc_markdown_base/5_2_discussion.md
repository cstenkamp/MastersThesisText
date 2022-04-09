## Results for Placetypes

As shown in \autoref{tab:f1_mainalgos_me_short}, the results outperform those of the literature for their dataset, often with a significant margin. Considering that this implementation replicates \cite{Derrac2015} without major algorithmic improvements for this dataset, and does not contain some of the improvements of \cite{Ager2018, Alshaikh2020}, this is initially surprising.

\paragraph{Errors} 
Naturally, the first thing to check in this situation is to check for errors in the implementation. Following that route it is however important to keep in mind that errors in the actual algorithm are an unlikely candidate for an erroneously high performance. As elaborated before, the performance of the decision-tree is only a surrogate metric to evaluate the resulting semantic directions. Among others this implies that the classification target for the task is disregarded in all algorithm steps except the final evaluation with the decision trees. As long as that is given,  the only realistic source of error that leads to higher-than-expected accuracies reliably is thus in this step. This does not mean that there are certainly no errors in the implementation of the rest, but as long as the classification target is not used, all these errors would only coincidentally lead to better classification results. In contrast to that, there are many sources of errors in the decision tree classification that will likely lead to unrealistically high performances such as mixing up the training- and testing set. In any case, both the algorithm itself and the decision-tree classification was triple-checked for errors and many sanity-checks were performed that all lead to the same conclusion, so from now on we will assume that the results are correct and discuss possible reasons for that\footnote{The code is open-source and available at \url{github.com/cstenkamp/derive_conceptualspaces}, and \me is thankful for any issues.}

\paragraph{1-vs-Rest}

* When doing classification with decision-trees it is a design-decision if one makes one decision-tree per class that just classifies if it is that class or not, or on the other hand one tree that must predict the exact class membership for all classes. \cite{Ager2018, Alshaikh2020} are both unclear if they did the former or the latter. Generally, AllAtOnce would be the harder task and comparing accuracies of 1vsRest to AllAtOnce an unfair comparison. However, there are a few things that can be assumed
    * Both of them report to have used the sklearn-implementation of decision-trees, just like this work. This specific implementation reportedly uses the CART algorithm \cite{breiman1984classification}, which only allows binary trees, where every node has exactly two children\footnote{\url{https://scikit-learn.org/stable/modules/tree.html\#tree-algorithms-id3-c4-5-c5-0-and-cart}}. Consequently, a decision tree of depth one can only classify $2^1 = 2$ classes, whereas a tree of depth two can classify up to $2^2=4$ classes. <!-- TODO actually for depth 2 it's 2^2 + 2^1 + 2^0 = 7 and thus for depth 1 = 3 --> Due to that, the best achievable accuracy of a perfect depth-1-tree is $\frac{\text{||samples in two most common classes||}}{\text{||samples in all classes||}}$, which is $\frac{176+74}{403} = 0.62$ in the case of Geonames and $\frac{88+82}{391} = 0.43$ for Foursquare (on average! still random assignment to train and test sets!) the latter is lower than what \cite{Alshaikh2020} report. This would be even a lot more pronounced when classifying the movie genre, which has 100 classes. 
    * Also semantically it is reasonable to assume to do 1vsRest: they state extensively that they are looking for a direction for \textit{scarieness} in movies, where the genre corresponding to that \textit{(Horror)} is only one of the genres. This kind of mapping Genre-FeatureDirectionPredictingGenre can only be found with separate trees per genre - and thus generally per class. 
* So, we can assume they did 1vsRest. 

* In \autoref{tab:f1_geonames_foursquare_all}, we reported the results both for the case of 1-vs-rest and all-at-once. In there we see
	* Performances for depth-limited trees are not consistently worse than unbounded trees. Surprising on first glance, but decision trees are known to be prone to overfitting, which can only really happen for unbounded trees.
	* 1vsRest + Unbalanced is the only condition never leading to optimal results
	* for depth-limited trees it holds that 
		* If AllAtOnce, balancing is bad for performance
		* If 1vsRest, balancing is good for performance
	* in unbounded trees
		* weak trend that balancing improves performance a bit
	* Especially for depth-limited trees, 1vsRest improves performance. 
		* Performances for balanced 1vsRest for depth 1 and 2 are abysmal
    * Unweighted scores are always worse.
* Interpretation of that: 
    * As stated above, the depth-limited ones can only predict very few classes, explaining why these are bad at AllAtOnce. For the same reason however they benefit from unbalanced datasets, in which case they just assign the two most common class labels - this happens without balanced sample-weighting: the trees simply assign the respectively most common Geonames/Foursquare class. 
    * TODO!!

\paragraph{Other possible reasons}

* Only a small subset of samples even \textit{have} a class assignment (403 of 1383 in 7 classes in the case of Geonames (see \autoref{fig:scatter_mds_placetypes}), 391 in 9 classes for Foursquare), and the classes are heavily imbalanced (Geonames between 176 and 14 samples per class, Foursquare between 88 and 6)
    * I used the classes as uploaded to \url{https://www.cs.cf.ac.uk/semanticspaces/} by \cite{Derrac2015}, of course there is the chance that they did not make all of their data publicly available (whereas \cite{Ager2018, Alshaikh2020} had access)
    * In general, that is a tiny dataset so the statistical power of any result here is really low - maybe it is just coincidendence
* Regarding the point "I don't even have the improvements of \cite{Ager2018} and \cite{Alshaikh2020}": 
    * The contributions from \cite{Ager2018} were primarily the Fine-Tuning and the condition where averaged word-embeddings are used instead of \gls{mds} (denoted \textbf{AWV}). As can be seen in \autoref{tab:f1_placetypes_long}, these contributions don't seem to affect the classification performance much, being in the same region as those for their MDS-condition which is implemented here as well: There are no really significant improvements that are not given here, giving no reasong to assume that their performance should be superior.  
    * The \textbf{Ortho} condition of \cite{Alshaikh2020} actually does significantly outperform the base algorithm for many configurations. For Foursquare, their performance comes very close to mine, whereas their Geonames-performances are a lot worse than mine, but
        * With the utmost respect, if the code uploaded by \cite{Alshaikh} is really the basis for their implementation, I have reasons to doubt what they say they do and what they do really matches
            * https://github.com/rana-alshaikh/Hierarchical_Linear_Disentanglement/blob/master/Hierarchical_Linear_D4.py#L485-L486: they take the kappa-score from on the raw predictions, not on the rank like \cite{Derrac2015} described and like we do (see \autoref{tab:kappa_measures}) and they also don't weight their kappas. 
            * Apart from observations like this, it is hard to say more about their code, because the two files uploaded by them are not the whole algorithm and they load quite a few files that are not in the repository, and also none of the evaluation on basis of decision tree performance is in the repo
* One difference is as far as I can tell, that we looked for the best configuration \textit{for this particular task}, which is a different one for each combination of dataset $\times$ \gls{dt}-depth $\times$ classification-target. I interpret \mainalgos such that they did hyperparameter-tuning before, using another possibly subjective metric \todoparagraph{test this claim}, and then decided on one (or rather four, see \autoref{tab:f1_placetypes_long}) configuration that was not optimized for the dataset $\times$ \gls{dt}-depth $\times$ classification-target. It should be noted that in this work, the algorithm is also not optimized for that task, but only the best of the 80 different parameter-combinations that were executed is used respectively. At the same time however, some \todoparagraph{which} way to find a hyperparameter-configuration has to be used, and it is unlikely that \mainalgos chose the worst configuration. \autoref{tab:f1_geonames_foursquare_all} displays robust results of a parameter-configuration that proved good on average. As these results, however, also outperform those of \mainalgos significantly, choosing the best configuration seems to play only a minor role for the performance.
* The considered scores for the 1vsRest-condition of this work are calculated from the scores of the individual per-class classifiers both with uniform weighting per class (bottom two rows of \autoref{tab:f1_geonames_foursquare_all}) and also with class weights inversely proportional to class size (middle two rows). Clearly, the condition that weights the indiviudal scores leads to better results. Weighting the score is a reasonable assumption, given that the individual class frequencies are very imbalanced (see \autoref{fig:scatter_mds_placetypes}). Unfortunately, \mainalgos do not explicitly share if they calculated weighted class scores as well. If we assume for now that \mainalgos did report unweighted scores and thus disregard the condition where class-scores are weighted (see bold scores in \autoref{tab:f1_geonames_foursquare_all} or last column of \autoref{tab:f1_placetypes_long})), our results are still comparable with those of \mainalgos and especially in the case of GeoNames-labels a lot closer to those reported in the literature. So while I hereby argue that weighting the scores makes sense, even if that is not the case our results are still acceptable. Again I want to stress that there are only really few and imbalanced labels for this dataset in general, making the statistical power of these results very small.
* We do not have many differents in hyperparameters/algorithm-components than \mainalgos do, but there some. For example using tf-idf as \gls{quant} instead of PPMI: Close inspection of \autoref{tab:best_params} shows that often, the tf-idf results are superior to the PPMI-results, and sometimes the combination of using tf-idf as quantification and tf-idf as dtm-quantification is good. This may lead to two conclusions: Either tf-idf is just better than PPMI under certain conditions, or just that the fact that more different results generated here just increased the statistical chance that good results were among the generated ones.

Summarized: Even though this work did not do much beyond \mainalgos, maybe there were some small things that were done here that gave an edge, such as trying out different or just more hyperparameter-combinations. Maybe the scores here were calculated differently than in \mainalgos, but even if that were the case the results generated here are still comparable. Maybe I had errors, maybe \mainalgos did, but in any case as the dataset is so small exact results do not seem incredibly informative anyway. Most importantly the comparison was performed to check if this implementation is working correctly, and the evidence for that appears very strong.

## Interpreting results: TODO

* Anhand von set-overlapts von meinen placetypes zu deren "die hyperparam kombi die am closesten zu deren ergebnissen ist" sagen können
* ich hätte gerne sowas wie könig - mann + frau = königin \cite{Mikolov:Regularities}, nur halt mit mann und frau als einer achse, macht das sinn, ist das rausgekommen?

## Educational resources

<!-- * Erstmal sanity-check "mein algorithmus performt wie die paper, -> reasonable dass richtig", DANN analyse im hinblich auf die fachbereiche, um dann in der diskussion in "shortcomings" zu sagen "naja jetzt haben wir das auf fachberecihe gemacht aber wie gut der auf anderen domänen performt müsste man human studies" -->

Having evidence that the implementation does what it should and the algorithm itself works on other datasets, let us finally discuss the question if the methodology works for the domain of educational resources.

### Regarding the different datasets 

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


### Interpreting Results
<!-- In den results sind ja quantifizierbare und gute Zahlen drin, das ist ja in der discussion ein argument dafür dass es funktioneirt -->

* So we compared to BERT (85.19% accuracy), and to 3D-embedding (64.3% weighted accuracy), and we robustly achieved 81.4% accuracy \textbf{even when using only a single direction}! We seem to be really good on that regard

* Which Faculties did I classify well and which ones bad?
    * compare with prelimiary results in Johannes sidBERT vergleichen, see slack 29.3. 10:00
    * When looking at the examples per faculty, we observe mixed results. ON the one hand, erziehungswissenschaft is perfect, on the other hand physics and bio/chemie suckt. 
        * when looking at the class frequencies for these well yes, these two are among the smaller classes, but so are [2 others], so whyever them work but bio & pyhsik dont

* ...of course, keep in mind that the results for classifying the faculty are really not 100% of the algo --> We could to the shallow-decisiontrees-thingy for other attributes of the dataset than I currently have (see future work)
    * "naja jetzt haben wir das auf fachberecihe gemacht aber wie gut der auf anderen domänen performt müsste man human studies evaluieren"

#### Qualitative analysis

##### Post-hoc 

* Das wie gerade auch in der duplicate-per-combi-of-ndims-and-ncats sichtbar wird dass letztlich halt "kurs 123" und "!!FÄLLT AUS!! kurs 123" auf den selben fallen, was zwar quantiativ scheiße ist aber ACTUALLY GOOD



### Regarding Hyperparameters

* Nochmal drauf zurück dass die ja ppmi statt tf-idf nutzen und ob meine Ergebnisse confirmen können dass es dazu any reason gibt oder nicht
* my different kappas - yay nor nay?


## Algorithm: Big picture (did we achieve our aims)

What were our original aims and did we achieve them

* ich hätte gerne sowas wie könig - mann + frau = königin \cite{Mikolov:Regularities}, nur halt mit mann und frau als einer achse, macht das sinn, ist das rausgekommen?
* "naja jetzt haben wir das auf fachberecihe gemacht aber wie gut der auf anderen domänen performt müsste man human studies"

* Wie aussagekräftig sind überhaupt die Decisiontree-ergebnisse? -> OB das sinnvoll ist (Tiefer und tiefer drauf eingehen im hinblick darauf wie meaningful die results sind) ("was bedeutet das für mich")

## Results regarding the Implementation and Goals for the architecture (in terms of architecture quality)
<!-- Eine meiner 2 research questions ja war "wie sieht eine gute architecture aus", so if the architecture is good and how it (and thus a good architecture) looks are results!! -->

First of all, we wanted to show that 

* this implementation works
* the results of \mainalgos are not a fluke (that the algorithm works at all)

The results on placetypes have shown that that's the case.


We remember, we also wanted to build a good architecture and set goals for that, such as adaptability to new datasets etc. We said a good architecture would show in adaptability, scability, ..., so we wanna show that these are achieved. 

* We are scalable and can run massively parallel (that you'll have to believe me, it's one command to run on the grid and I would say that's pretty noice).
* Keep in mind when reading the other sections of the results that all plots and tables you'll see are explictly linked and easily re-creatable and runnable
* We ran the stuff on other datasets\footnote{See Table with datasets and the respective notebooks and the quick datasets section} and it ran through, so we're adaptable.
    *  wie schnell es geht den bums auf neue datasets zu werfen (100k coursera, 90k short stories, ...) und dass ich damit schon angefangen hab 

* dass sowohl die architektur hierfür, als auch meine Grid-solutions eine major contribution sind die sich sehen lassen können!
* Development was really easy as soon as the architecture did what it should so yes, future work will be made a lot easier, our goal of "Make a good architecture" (see \autoref{sec:goals_research_questions} is fulfilled.)



## Opinion to / Evaluation of Derrac2015 etc:


\cite{Gardenfors2000a} also said stuff like "Dimensionality Reduction from the high-dimensional input (neurons) eg using MDS into a euclidian space, and then geometric reasoning on that" including some examples of kinds of reasoning, so actually the exact algorithm \cite{Derrac2015} did was extremely naheliegend (put some obvious NLP modelling to that like \cite{Turney2010} explained and you're pretty much exactly at their algorithm) 

He even has a chapter "conceptual aspects", where he suggests vector space models, dimensionality reduction algorithms, ANN architectures, ... (for all of the 3 levels): 
The information received by the receptors is too unstructured, so a way of transforming the input into a more \textit{economic} form of representation with a reduced number of dimensions that can be handled on the conceptual or semoblic level is needed \cite[221]{Gardenfors2000a}. Gärdenfors suggests MDS (especially good when dealing with a \textit{phenonemal} CS with pairwise distance judgements from a subject's perception), Shephard's algorithm which reduces number of dimensions sucessively until the rank order would change sustantially, or even ANNs, concretely Kohonen's Self-organizing maps \cite{Kohonen1997}, which automatically reduce the representational complexity of the input while preserving similarities (of beliebiger distance function) among the different input vectors by mapping input vectors with common featurs to \textit{neighboring} neurons in the output map, thus preserving topological relations while making it lower-dimensional.


backref \autoref{sec:howtoreplicate}: 

It is absolutely crucial in science to ensure that all claims that are made are reproducible and testable. This thesis mostly replicates existing research, and doing so should not have been as much work as it was. Also, while replicating, some Questionable Research Practices came apparent, such as the authors neither publishing their code\footnote{Or referencing a repository that is empty since it's creation in 20XX (\todoparagraph{URL})}, nor being unambiguous about details of their algorithm in their description\footnote{Such as the question about which kappa, and which kappa-weights, and also the \q{MDS trained with the angular differences between the PPMI weighted BoW Vectors}, vs (whatever other thing) elsewhere}, which required a lot of unnecessary trial and error. Or, even opening their data, only doing that only in a form that does not allow for comparison (see datasets-section), or cherry-picking their qualitative analysis (See \todoparagraph{Ich hab irgendwo aufgeschrieben das wievielte Beispiel einer ihrer plots war} (hing es zusammen mit "Paperlesen und den cluster von "pub" für placetypes angucken"?))


\includeMD{pandoc_generated_latex/algo_problems}

In der Discussion kann ich dann auch wieder bezug auf die orig-paper ziehen , und nochmal kritisch reflektieren wie gut meine bewertung ist ("shortcomings"-section)




* dass deren merge-candidate-directions-schritt (alle nehmen und die zum closestem herclustern und dann die richtung des T^0.5 übernehmen) ziemlich whack ist, ich schon einige wege hab damit umzugehen but many better ones are imaginable
* Der Kappa-Score der rankigns vergleicht ist für mich ne kack metric weil ich ebennicht reviews nehme und more-occurences better-candidate heißen -> gucken wie ich stattdessen gute dimensionen und cluster finde (klingt doch so als sei accuracy/f1/... doch wichtig)


Von Software Engineering oder best practices haben die alle ncoh nichts gehört, ich arbeite mit dem guten der Paper und das hier ist die main-function...https://github.com/cstenkamp/Autoencoder-Explanations/blob/master/src/_archive/pipeline.py#L1504-L1516


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
    * Gärdnefors already said stuff like "Dimensionality Reduction from the high-dimensional input (neurons) eg using MDS into a euclidian space, and then geometric reasoning on that" including some examples of kinds of reasoning, so actually the exact algorithm \cite{Derrac2015} did was extremely naheliegend (put some obvious NLP modelling to that like \cite{Turney2010} explained and you're pretty much exactly at their algorithm) 
        * ....but even more reason to make me think that it may have been their error to keep the enforcement that the MDS-result must be a euclidian space, when afterwards they have the additional step of using their rankings anyway! (...which btw brings me to the question what that does to distances?!)




* We say we're dealing with POINTS but we're constantly doing cosine similarity, isn't the important difference between points and vectors that cosine would be relevant for vectors, but euclidian(/..) distance for points?!
    * We're always concerned with points, not with vectors!!! gucken was das für auswirkungen hat!!! (AUCH: points, not convex regions (like CS SHOULD be))     
    * WHY do they always calculate with cosine-distances (eg in my `select_salient_terms`) - I thought the important thing is that we are talking about POINTS, NOT VECTORS  (also - param-combi for closeness by euclidian distance isntead of that)
    * dass mich wundert dass deren distance measure zu funktionieren scheint, wo sie doch ebendoch vectors considert und nicht punkte!
        * ...WO merkt man denn überhaupt dass sie punkte haben und nicht vektoren? Bei der SVM (siehe meine Stackoverflow frage!) ists ja relevant.... und da nutzen sie punkte... riiight? Am I doing it like they did? Are we all doing it correct?
        * (see also "The fact that I don't use intercepts of the decision_planes" in shortcomings )


\cite{Derrac2015}: \q{SVD produces a representation in which entities correspond to vectors, which should be compared in terms of cosine similarity rather than Euclidean distance} (-> spatial relations such as betweeness and parallism wouldn't make sense) - and then proceeds to use cosine-distance?! wtf!! (acutally that may be a problem of ager & alshaikh)



* in Derrac2015 it is pretty unclear what the final result is - their last step is to induce the rankings for the respective semantic directions, but everything else the do on the intermediate embeddings, bc these are a metric space. 
    * Davon ausgehend dass ja eigentlich schon die rankings-by-dimension das endergebnis sind, FRAGE: sind dafür ÜBERHAUPT IRGENDWIE die cluster relevant??! Ich meine es wird nur die distance zur hyperplane vom main-term considered, so why the hell even cluster?!



### Criticism towards the entire concept of CS

* no need for a symbolic inference engine anymore [WELL BUT this is computationally easily MORE demanding [..SOURCE!!]]


## Conclusion

Dass ich ein Tool gebaut hab mit dem man easy die sachen von \mainalgos nach-produzieren kann, auf einem Grid oder als working python package. Auch wenn's nicht alle components von ager/alshaikh enthält ist das framework so geil general dass man die ez hinzufügen kann. I took the algo from the small community and gave an easy tool to the broader scientific community, you're welcome! Running and analyzing a metric ton of parameter-combinations is incredibly easy. If you want to try new parameters, add it to the yaml, throw the grid onto it, wait a bit, download and tada every plot and table you may want is even automatically generated! The workflow is awesome.
(wie dolle die Architecture geworden ist und wie viel einfacher sie arbeit in der Zukunft macht)

Ich habe schon eine eindeutige Fragestelleung ("Kann man X auf educational resources anwenden") -> danach stringent und explizit vorgehen! Das ist meine Hypothese, these are my methods, this my results, this my conclusion!

Ich habs geschafft diesen Algorithmus zu reproduzieren und es scheint ganz gut zu funktionieren, feddisch.

"im vergleich zu demundem haben wir das geliche rausbekommen, ...", "die arbeit extended dasunddas weil wir's in ne andere domäne geschoben haben und ..."

* How good do I think does the algorithm capture CS? How useful do I think CS are in general (two perspective, as model of human concept formation AND algorithm-that-allows-certain-things-like-reasoning), and how good do I think the algorithm does it? Is the algorithm practical?
* So now we have to answer the question if we achieved do what motivated us in the first place: easily and automatically create structured knowledge bases .My opinion is that the need to create such knowledge bases is absolutely there, but I am more than unsure if this is the best imaginable algorithm. Of course, I see the reasoning for the distancematrix->MDS to ensure the resulting place is actually metric (an assumption more and more dropped by the two followup-papers)... but maybe before and after we can use neural techniques? Like idk doc2vec für die distance matrix, dann gerne MDS, und candidate terms sind dann word embeddings we threshold their closeness to the document embedding? Or also use LSI/LDA? (see my suggestion for an algorithm)
* In die Conclusion auch die Frage inwieweit das jetzt conceptual spaces sind (sehr viele vereinfachende sachen, like no convex regions but simply dots)
    * [AGKS18] ist da auch mehr humble als [DESC15] und sagt "The idea of learning semantic spaces with accurate fea- ture directions can be seen as a first step towards methods for learning conceptual space representa- tions from data"
    * SO I'd say just becuase of the fact that we're not talking about points but regions we cannot... and the two follow-ups even drop the metric requirement so there I'd say definitely not.