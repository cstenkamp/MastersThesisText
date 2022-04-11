<!-- "Bezug auf die orig-paper ziehen und kritisch reflektieren" -->

### Where I spotted differences

wenn meine ergebnisse anders sind als die von dem paper kann ich halt erst dann sagen "das widerspricht demunddem hier, die proposen dass und ich kann es (nicht) confirmen"



### General algorithm Idea

* in [DESC15] machen die wirklich immer ne SVM für genau einen Term, und gucken sich anschließend an was für terms dann ähnlich clustern. [VISR12] hingegen (und viele andere!) versuchen erst latent kram zu finden, wodurch das das clustering imo viel besser funktionieren wird weil es viel weniger sparse ist (->und die "contains one-of-the-terms" klasse nicht so verschwindend gering ist compared mit der "doesn't-contain-the-one-term") Laut [DESC15] gibt's da keine Methoden die den metric space erhalten, die frage ist halt wie wichtig das ist für das was man erreichen will!

### Other things

* Der letzte Schritt mit dem Clustern der good-kappa-ones ist wirklich very basic und hat very much room for improvement

* better ways of getting rid of irrelevant clusters (see my suggestion and also problems with stopwords)
* their merge-candidate-directions-schritt (alle nehmen und die zum closestem herclustern und dann die richtung des T^0.5 übernehmen) ziemlich whack ist, ich schon einige wege hab damit umzugehen but many better ones are imaginable

* They do one SVM per term and then cluster similar ones. Ther terms sometimes occur only in like 50/15000 entities, so the validity of the kappa is should be doubted. \cite{VISR12} and many others first try to find latent stuff, which would improve that by a lot because its a lot less sparse. ("contains-one-of-the-terms" is a lot more than "contains-this-term"). According to \cite{Derrac2015} there are no methods that keep a metric space, however I doubt that is too important (see \ref{sec:discuss_mds})
    * WHY do they always calculate with cosine-distances (eg in my `select_salient_terms`) - I thought the important thing is that we are talking about POINTS, NOT VECTORS  (also - param-combi for closeness by euclidian distance isntead of that) -> FUTURE WORK
    * Why do their distance measures even work? Where does one even notice if they have points and no vectors? Bei der SVM (siehe meine Stackoverflow frage!) ists ja relevant.... und da nutzen sie punkte

### MDS


* Another important thing is the relevance of MDS. As stated in \autoref{sec:dim_red}, LSA would be the better choice, and the reason that \textcite{Derrac2015} use MDS is, to get a metric space that keeps distances to allow for geometric solutions for commonsense reasoning (see \autoref{sec:reasoning}) where betweeness and parallelism makes sense. I get that, but:
    * \textcite{Derrac2015} do the explainable classifiers where the that's important on this space, however this space does not have interpretable dimensions! Is THIS their endresult? 
    * No, their end-result is the space where they re-embedded those according to the salient directions! It must be this one, bc otherwise all these steps were irrelevant, because up to there it's a normal VSM via definition. But for that one it's completely irrelevant if the INTERMEDIATE STEP was metric or not (it is unclear what their final result even is!)
    * \cite{Ager2018} and \cite{Alshaikh2020} both don't care for this interim space and only do stuff on the re-embedded one, however keep MDS! As far as I understand, they have no reason to do so and should have used the better LSI (in fact they also use word2vec/glove, so they themselves seem unsure)
* I thougt they would like find a new orthonormal basis of the coordinate system, but they just do the ranking and re-embed. I'm not the best at math, but maybe that would be possible as well?
* I think they too firmly followed gärdenfors suggestion when he said MDS is achsouseful for phenomenal CS which are created from paiwise distances, forgetting that their extra-reembedding-step makes that irrelevant
    * speaking of which, what do we know about that space? What properties can we assume there? I'd definitely say dimensions are still correlated... but is this a metric space? a topological space?
    * shouldn't we follow this by something like PCA to decorrelate dimensions?
    * Is the space filled enough or are all datapoints very close?


Given that respective directions are not necessarily orthogonal and that rankings are no Euclidean metric, the final embedding loses some geometric property but gains interpretable directions.

!!!!

### Points as coordinates

* I thought it was important that we are dealing with points, so why cosine distance? I thought that would be for vectors, we should be using euclidean distance! By not doing that on the final space we see again that many assumptions are dropped
* Yes points instead of regions, but I agree that that's a bug and not a feature, and also (critizising CS als solche), computation with regions is computationally incredibly demanding. 
* \cite{Derrac2015}: \q{SVD produces a representation in which entities correspond to vectors, which should be compared in terms of cosine similarity rather than Euclidean distance} (-> spatial relations such as betweeness and parallism wouldn't make sense) - and then proceeds to use cosine-distance?! wtf!! (acutally that may be a problem of ager & alshaikh)

### Robustness 

Das problem was ich mit derrac hatte ist ja dass die so unglaublich unrobust waren und fast maximal viele verschiedene rauskamen
    * Bei den placetypes-results noch den punkt dabei schreiben dass die so verschieden sind
    * See greats overall & goods overall in \autoref{tab:generated_stats}: bei    placetypes sind einfach 21832 von 21833 at some point in kappa >= 0.1



## So are that now conceptual spaces?

* This is not really a conceptual space - for example only points, for example its too highdimensional (which is what \cite{Alshaikh2019, Alshaikh2020, Alshaikh2021} noticed and worked on)

* sehr viele vereinfachende sachen, like no convex regions but simply dots, however that's general reasonable 
* still high-dimensional, that's not good
    * [AGKS18] ist da auch mehr humble als [DESC15] und sagt "The idea of learning semantic spaces with accurate fea- ture directions can be seen as a first step towards methods for learning conceptual space representa- tions from data"
* We know nothing about the properties (is it metric,...) of the final space!
* The fundamental information retrieval problem - no 1:1 correspondance to words and meanings (polysemy, synonymy)! two people choose the same main key word for a single well-known object less than 20% of the time [[1] of \cite{Deerwester}]
    * Can use LSA to, once the corresponding clusters are found, select a good one of that as representative: add pseudodocs with only one term and that term as name, and then let all DOCUMENTNAMES be candidates

## Regarding their research practices

backref \autoref{sec:howtoreplicate}: 

* It is absolutely crucial in science to ensure that all claims that are made are reproducible and testable. This thesis mostly replicates existing research, and doing so should not have been as much work as it was. Also, while replicating, some Questionable Research Practices came apparent, such as the authors neither publishing their code\footnote{Or referencing a repository that is empty since it's creation in 20XX (\todoparagraph{URL})}, nor being unambiguous about details of their algorithm in their description\footnote{Such as the question about which kappa, and which kappa-weights, and also the \q{MDS trained with the angular differences between the PPMI weighted BoW Vectors}, vs (whatever other thing) elsewhere}, which required a lot of unnecessary trial and error. Or, even opening their data, only doing that only in a form that does not allow for comparison (see datasets-section), or cherry-picking their qualitative analysis (See \todoparagraph{Ich hab irgendwo aufgeschrieben das wievielte Beispiel einer ihrer plots war} (hing es zusammen mit "Paperlesen und den cluster von "pub" für placetypes angucken"?))

* Von Software Engineering oder best practices haben die alle ncoh nichts gehört, ich arbeite mit dem guten der Paper und das hier ist die main-function...https://github.com/cstenkamp/Autoencoder-Explanations/blob/master/src/_archive/pipeline.py#L1504-L1516

* Small community, unfortunately
    * I assume \mainalgos shared data, at least the didn't  n-gram problem I mentioned.
    * As all of these publications share Prof. Steven Schockaert as last author, it seems plausible that a) the latter ones are legit improvements upon the first, b) at least to a certain degree they can share code and data, c) this field of work is constrained to a small community, without any alternative implementations or substantial improvements from outside of it.
        * But Johannes said "I would either leave this part out, as it is implicitly clear from the first sentence or restructure/reformulate it. The way it is right now, it seems like a speculation on your part at least for b) and c). The small size of the community could be a point worth mentioning in the concluding remarks of your thesis."

* Ich hab mir table 1 von [DESC15] angeschaut und mit deren daten nach-implementiert, und teilweise haben sie ihre ergebnisse schon verschönt -> butcher shop ist der place-type der am ~350zigst-meisten (je nach #dims) zwischen marketplace und slaughterhouse ist (see test_paper_table1_claims in test_semanticspace_measures.py)

* Robustness: Dass over all n-dims (20, 50, 100, 200) einfach 21832 (literally alle bis auf einen!) candidates in T^0.1 sind (ALSO FAST ALLE), und T^0.5 könnte schlechtestenfalls 740 (400+200+100+40) werte haben, bestenfalls 400, und hat 697 - soll heißen WELCHE ausgewählt werden ist kraass abhängig von der #dimensions, which is bad
    ==> I would really like to say somthing about the robustness of this algorithm for multiple runs. For that I can either take my own runs which I don't know if they are okay or theirs across dimensions. (Maybe some 2d-plot looking like a confusion matrix showing the overlap of T^0.5 terms, also intersection over union, for different runs (and also for the 4 n-dims in orig desc15))
    * Set-overlap of candidate-terms for different #dims is COMPLETELY off!!
    
* Wenn man sich in dem Paper mal die Movie-Cluster anschaut (einfach das textfile) sieht man dass das echt... bescheuert ist, die Cluster sucken hart



* Stuff that was ambiguous:
    * "that the better Ht separates entities to which t applies from the others in S,the better \vec{v_t} models the term t."
        * allein von der aussage muss man das mit den induzierten rankings echt nicht machen, sondern halt nur auf classification quality (-> metrics like accuracy) gucken, bzw kappa anhand der binären klasse berechnen 
        * With a candidate-threshold-tf of 100, that means 19.900 values (99.33%) have a rank of zero, how do you deal with that?!
        *  the ranking induced by count, or the baremetal count?
    * Regarding Kappa-Weighting-Algorithm:
        * Yet another point where \cite{Derrac2015} are really low on information what parameters they used. Sklearn allows different weighting types\footnote{\url{https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html\#sklearn.metrics.cohen_kappa_score}} - TODO: explain what that changes respectively!!}, and as this plot: ![kappa_weighting_funcs](graphics/figures/which_weigthing_algo.png){#fig:which_weighting_algo} TODO: also generally write about if Kappa is a good choice (see eg \url{https://en.wikipedia.org/wiki/Cohen%27s_kappa})
    * DESC15 write they select Kappa "due to its tolerance to class imbalance", but don't menation any parameters -> Class imbalance weighting? Also [see plot] which other weighting value?


## So what do I think about all this

How good do I think does the algorithm capture CS? How useful do I think CS are in general (two perspective, as model of human concept formation AND algorithm-that-allows-certain-things-like-reasoning), and how good do I think the algorithm does it? Is the algorithm practical?
* So now we have to answer the question if we achieved do what motivated us in the first place: easily and automatically create structured knowledge bases .My opinion is that the need to create such knowledge bases is absolutely there, but I am more than unsure if this is the best imaginable algorithm. Of course, I see the reasoning for the distancematrix->MDS to ensure the resulting place is actually metric (an assumption more and more dropped by the two followup-papers)... but maybe before and after we can use neural techniques? Like idk doc2vec für die distance matrix, dann gerne MDS, und candidate terms sind dann word embeddings we threshold their closeness to the document embedding? Or also use LSI/LDA? (see my suggestion for an algorithm)



## Outlook 

There are also techniques that extend the algorithm of \textcite{Derrac2015}: \textcite{Alshaikh2019} take a vector space embedding and decompose it to several low-dimensional spaces, such that it more closely corresponds to the definition of a \gls{cs} which are split into multiple domain-specific spaces of low dimension. For that, they take the spaces from \cite{Derrac2015} to then cluster their features by domain and iteratively remove these groups to create multiple subspaces, while ensuring that \gls{word2vec} embeddings close to those of the removed ones are disregarded for future features.

\cite{Alshaikh2021} want to get rid of MDS with it's quadratic space complexity and also write a completely new, unsupervised ANN algorithm based on GloVe embeddings (and suggest that doing that on BERT may be the shit). In it, they learn domain-specific embeddings from the BoW and like \cite{Derrac2015} use classification of candidate-from-text-occurs vs not-occurs for the ANN training while punishing close embeddings like \cite{Alshaikh2019}.












### What assumptions are we dropping

* we are only dealing with one domain (movies, placetypes, courses, ..) at a time (like CS, but what's missing is a sort of categorization at first.. however that one is never talked about anyway)
* EITHER we have euclidean metric OR we have interpretable direcitons, NOT BOTH
* The Gropuing into several low-dimensional subspaces per domain is a lot weaker: actually we'd have to embed entities into small spaces of only one domain! This is only kinda picked up again later by \cite{Alshaikh2020}
    * \cite{Alshaikh2020}: "When representing a particular entity in a conceptual space, we need to specify which domains it belongs to, and for each of these domains we need to provide a corresponding vector." 



#### On types and tokens

* supposed to be regions, but we use vectors.  [TYPES are, which are MADE UP FROM TOKENS]
    * MUCH more computationally efficient
    * the domain is different than the theoretical idea of Gärdenfors - especially stuff like movies and courses, what ARE they? are they type or token? Rather both at once - the region of the course XYZ is composed of only one token, at least until we take into account a much bigger dataset that would allow us to do reasoning on "the set of all introductory computer science courses" or something. (For placetypes however we ARE dealing with types!) 

Unlike many ther NLP approaches that rely on embedding (see \autoref{sec:embeddings}), in a Conceptual Space, natural language terms are not modelled as points or vectors, but as convex regions. A point in such a region is one specific instance of such a concept - you could say that regions denote \textbf{types}, with the individual points corresponding to their \textbf{tokens}. 

According to \cite{Derrac2015}, using regions instead of points has some clear advantages:
* It allows \q{to distinguish borderline instances of a concept from more prototypical instances, by taking the view that instances which are closer to the center of a region are more typical} \cite{Derrac2015} (they cite \cite{Gardenfors2000a})
* Concept Subsumption ("every pizzeria is a restaurant"), mutual exclusiveness (no restaurant can also be a beach), overlapping concepts (some bars serve wine but not all, some establishments which serve wine are bars but not all) 
* (their [41] says that "Region based models have been shown to outperform point based models in some natural language processing tasks")


In their algorithm, \cite{Derrac2015} drop this assumption and work with vectors instead of regions.
<!-- \q{In this paper, we essentially view point based representations as coarse-grained approximations of conceptual spaces, where points correspond to fine-grained categories instead of specific instances, while convex regions are used to model higher-level categories} -->
While this may seem to stand in strong contrast to an important component of the theory, 
* Computational Complexity on regions is vastly higher than for poitns or vectors
* "learning accurate region boundaries for a given concept would require a prohibitive amount of data" \cite{Derrac2015}
* Gärdenfors himself said when discussing if self-orgazinizing maps are useful that that is a GOOD THING, because that IS GENERALIZATION
* If you'd want regions, a good approach would be to just generate the type from its token. In the case of educational resources, every instance of a course is a token and thus a point/vector, and you can build your region "Introductory classes to Computer Science" by the minimal complex region that encompasses all tokens of "Informatik A" and "Introduction to Algorithmen" etc

TALK ABOUT that actually, in CS concepts (=types) are regions, BUT we have only one-instance-per, so TOKENS, so it's kiiinda reasonable that we have points! IF we would have the collection of "ALL Computer Science 1 Courses" it would be different

% Zum Thema points vs regions: [CS] where properties and concepts are represented using convex regions, while specific instances of a concept are represented as points. This has a num- ber of important advantages. First, it allows us to distinguish borderline instances of a concept from more prototypical instances, by taking the view that instances which are closer to the center of a region are more typical [9]. A second advantage is that using regions makes it clear whether one concept subsumes another (e.g. every pizzeria is a restaurant), whether two concepts are mutually exclusive (e.g. no restaurant can also be a beach), or whether they are overlapping (e.g. some bars serve wine but not all, some establishments which serve wine are bars but not all). Region based models have been shown to outperform point based models in some natural language processing tasks [41] On the other hand, using regions is computationally more demanding, and learning accurate region boundaries for a given concept would require a prohibitive amount of data. In this paper, we essentially view point based representations as coarse-grained approximations of conceptual spaces, where points correspond to fine-grained categories instead of specific instances, while convex regions are used to model higher-level categories

In any case, we often map regions in the high-dimensional space to point-embeddings, however according to \cite[222]{Gardenfors2000a} that's a feature not a bug because that is GENERALIZATION.

* We say we're dealing with POINTS but we're constantly doing cosine similarity, isn't the important difference between points and vectors that cosine would be relevant for vectors, but euclidian(/..) distance for points?! I mean warum ist unser space metric?!
