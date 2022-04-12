<!-- "Bezug auf die orig-paper ziehen und kritisch reflektieren" 

### Where I spotted differences

wenn meine ergebnisse anders sind als die von dem paper kann ich halt erst dann sagen "das widerspricht demunddem hier, die proposen dass und ich kann es (nicht) confirmen"

-->

# General algorithm Idea: Other things


* Der letzte Schritt mit dem Clustern der good-kappa-ones ist wirklich very basic und hat very much room for improvement
    * their merge-candidate-directions-schritt (alle nehmen und die zum closestem herclustern und dann die richtung des T^0.5 übernehmen) ziemlich whack ist, ich schon einige wege hab damit umzugehen but many better ones are imaginable
    * better ways of getting rid of irrelevant clusters (see my suggestion and also problems with stopwords)

* They do one SVM per term and then cluster similar ones. Ther terms sometimes occur only in like 50/15000 entities, so the validity of the kappa is should be doubted. \cite{VISR12} and many others first try to find latent stuff, which would improve that by a lot because its a lot less sparse. ("contains-one-of-the-terms" is a lot more than "contains-this-term" - that knowledge is also used by the postprocessing of Ager even though shitty.). According to \cite{Derrac2015} there are no methods that keep a metric space, however as discussed I doubt that is too important (see \ref{sec:discuss_mds})


## Robustness 

Das problem was ich mit derrac hatte ist ja dass die so unglaublich unrobust waren und fast maximal viele verschiedene rauskamen
    * Bei den placetypes-results noch den punkt dabei schreiben dass die so verschieden sind
    * See greats overall & goods overall in \autoref{tab:generated_stats}: bei    placetypes sind einfach 21832 von 21833 at some point in kappa >= 0.1


# Is that a CS?



## Points as coordinates - on Types and Tokens

Unlike many ther NLP approaches that rely on embedding (see \autoref{sec:embeddings}), in a Conceptual Space, natural language terms are not modelled as points or vectors, but as convex regions. 
    * \cite{Derrac2015} - advantages: 
        * It allows \q{to distinguish borderline instances of a concept from more prototypical instances, by taking the view that instances which are closer to the center of a region are more typical} \cite{Derrac2015} (they cite \cite{Gardenfors2000a})
        * There are really good Region-based models, eg \cite{Erk2009}
        * As we said when describing the RCC, stuff liek subsumption, mutual exclusiveness etc are obivous
BUT \cite{Derrac2015} drop this assumption and work with vectors (OR POINTS) instead of regions.
    * \cite{Derrac2015}: \q{In this paper, we essentially view point based representations as coarse-grained approximations of conceptual spaces, where points correspond to fine-grained categories instead of specific instances, while convex regions are used to model higher-level categories}
    * \cite[222]{Gardenfors2000a}: mapping regions in the high-dimensional space to point-embeddings is a feature not a bug because that is GENERALIZATION.
    * I think that makes sense: A point in such a region is one specific instance of such a concept - you could say that regions denote \textbf{types}, with the individual points corresponding to their \textbf{tokens}. -- the domain is different than the theoretical idea of Gärdenfors - especially stuff like movies and courses, what ARE they? are they type or token? Rather both at once - the region of the course XYZ is composed of only one token, at least until we take into account a much bigger dataset that would allow us to do reasoning on "the set of all introductory computer science courses" or something. (For placetypes however we ARE dealing with types!)  we have only one-instance-per, so TOKENS, so it's kiiinda reasonable that we have points! IF we would have the collection of "ALL Computer Science 1 Courses" it would be different
    * "learning accurate region boundaries for a given concept would require a prohibitive amount of data" \cite{Derrac2015}
    * Contra CS: computation with regions is computationally very demanding
    * If you'd want regions, a good approach would be to just generate the type from its token. In the case of educational resources, every instance of a course is a token and thus a point/vector, and you can build your region "Introductory classes to Computer Science" by the minimal complex region that encompasses all tokens of "Informatik A" and "Introduction to Algorithmen" etc
        * to get regions back, \cite{Erk2009} propeses an algorithm for that (region surrounding a central vec, or instance-based (with degree of variance in each dimension) by merging k-nearest-neighbors) ==> Future Work




### Points vs Vectors
* I thought it was important that we are dealing with points, so why cosine distance? I thought that would be for vectors, we should be using euclidean distance! By not doing that on the final space we see again that many assumptions are dropped  
    * isn't the important difference between points and vectors that cosine would be relevant for vectors, but euclidian(/..) distance for points?! I mean warum ist unser space metric?!
    * cosine distance used eg in my `select_salient_terms`: Do they really do that on the kidns of spaces where they claim regions are important?
    * Future work: closeness by euclidian distance 
* \cite{Derrac2015}: \q{SVD produces a representation in which entities correspond to vectors, which should be compared in terms of cosine similarity rather than Euclidean distance} (-> spatial relations such as betweeness and parallism wouldn't make sense) - and then proceeds to use cosine-distance?! wtf!! (acutally that may be a problem of ager & alshaikh)

* Why do their distance measures even work? Where does one even notice if they have points and no vectors? Bei der SVM (siehe meine Stackoverflow frage!) ists ja relevant.... und da nutzen sie punkte



## Outlook 

There are also techniques that extend the algorithm of \textcite{Derrac2015}: \textcite{Alshaikh2019} take a vector space embedding and decompose it to several low-dimensional spaces, such that it more closely corresponds to the definition of a \gls{cs} which are split into multiple domain-specific spaces of low dimension. For that, they take the spaces from \cite{Derrac2015} to then cluster their features by domain and iteratively remove these groups to create multiple subspaces, while ensuring that \gls{word2vec} embeddings close to those of the removed ones are disregarded for future features.

\cite{Alshaikh2021} want to get rid of MDS with it's quadratic space complexity and also write a completely new, unsupervised ANN algorithm based on GloVe embeddings (and suggest that doing that on BERT may be the shit). In it, they learn domain-specific embeddings from the BoW and like \cite{Derrac2015} use classification of candidate-from-text-occurs vs not-occurs for the ANN training while punishing close embeddings like \cite{Alshaikh2019}.


# Regarding their research practices

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
