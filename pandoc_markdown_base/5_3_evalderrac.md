<!-- "Bezug auf die orig-paper ziehen und kritisch reflektieren" -->
## Regarding their algorithm

* See greats overall \& goods overall in \autoref{tab:generated_stats}: bei placetypes sind einfach 21832 von 21833 at some point in kappa >= 0.1


### General algorithm Idea

* Initially I wondered how they got the idea, but having read \cite{Gardenfors2000a}, the idea for their algorithm stood too reason
    * Gärdenfors suggested to use MDS for dimensionality-reduction from high-dimensional input, projecting it into a euclidian space to then do gemetric reasoning, most of which was just implemented by \cite{Derrac2015}. 
    * \cite{Derrac2015} just combined this with the classical NLP pipeline as analyzed by \cite{Turney2010}
    * Their main contribution is to use the performance of the classifier in terms of ranking-scores to measure the faithfulness. And this does seem like a reasonable assumption assuming the distributional hypothesis and the theory mentioned in the lsa-chapter
    * In his chapter "Computational Aspects" where he suggests vector space models, dimensionality reduction algorithms, ANN architectures for the three levels (see cs-chapter), he says:
        The information received by the receptors is too unstructured, so a way of transforming the input into a more \textit{economic} form of representation with a reduced number of dimensions that can be handled on the conceptual or semoblic level is needed \cite[221]{Gardenfors2000a}. Gärdenfors suggests MDS (especially good when dealing with a \textit{phenonemal} CS with pairwise distance judgements from a subject's perception), Shephard's algorithm which reduces number of dimensions sucessively until the rank order would change sustantially, or even ANNs, concretely Kohonen's Self-organizing maps \cite{Kohonen1997}, which automatically reduce the representational complexity of the input while preserving similarities (of beliebiger distance function) among the different input vectors by mapping input vectors with common featurs to \textit{neighboring} neurons in the output map, thus preserving topological relations while making it lower-dimensional.
* What would have been nice tho
    * incorporating modern stuff like neural embeddings to get rid of the bow-problems (see chapter) (see my suggestion)
    * better ways of getting rid of irrelevant clusters (see my suggestion and also problems with stopwords)
    * This is not really a conceptual space - for example only points, for example its too highdimensional (which is what \cite{Alshaikh2019, Alshaikh2020, Alshaikh2021} noticed and worked on)

### Regarding their main contribution of measuring faithfulness with kappa

* The fact that their kappa-metric worked for me really suprised me, considering the different nature of the dataset
    * their merge-candidate-directions-schritt (alle nehmen und die zum closestem herclustern und dann die richtung des T^0.5 übernehmen) ziemlich whack ist, ich schon einige wege hab damit umzugehen but many better ones are imaginable

* They do one SVM per term and then cluster similar ones. Ther terms sometimes occur only in like 50/15000 entities, so the validity of the kappa is should be doubted. \cite{VISR12} and many others first try to find latent stuff, which would improve that by a lot because its a lot less sparse. ("contains-one-of-the-terms" is a lot more than "contains-this-term"). According to \cite{Derrac2015} there are no methods that keep a metric space, however I doubt that is too important (see \ref{sec:discuss_mds})
    * WHY do they always calculate with cosine-distances (eg in my `select_salient_terms`) - I thought the important thing is that we are talking about POINTS, NOT VECTORS  (also - param-combi for closeness by euclidian distance isntead of that) -> FUTURE WORK
    * Why do their distance measures even work? Where does one even notice if they have points and no vectors? Bei der SVM (siehe meine Stackoverflow frage!) ists ja relevant.... und da nutzen sie punkte

### MDS
\label{sec:discuss_mds}

* Another important thing is the relevance of MDS. As stated in \autoref{sec:dim_red}, LSA would be the better choice, and the reason that \textcite{Derrac2015} use MDS is, to get a metric space that keeps distances to allow for geometric solutions for commonsense reasoning (see \autoref{sec:reasoning}) where betweeness and parallelism makes sense. I get that, but:
    * \textcite{Derrac2015} do the explainable classifiers where the that's important on this space, however this space does not have interpretable dimensions! Is THIS their endresult? 
    * No, their end-result is the space where they re-embedded those according to the salient directions! It must be this one, bc otherwise all these steps were irrelevant, because up to there it's a normal VSM via definition. But for that one it's completely irrelevant if the INTERMEDIATE STEP was metric or not (it is unclear what their final result even is!)
    * \cite{Ager2018} and \cite{Alshaikh2020} both don't care for this interim space and only do stuff on the re-embedded one, however keep MDS! As far as I understand, they have no reason to do so and should have used the better LSI (in fact they also use word2vec/glove, so they themselves seem unsure)
* I thougt they would like find a new orthonormal basis of the coordinate system, but they just do the ranking and re-embed. I'm not the best at math, but maybe that would be possible as well?
* I think they too firmly followed gärdenfors suggestion when he said MDS is achsouseful for phenomenal CS which are created from paiwise distances, forgetting that their extra-reembedding-step makes that irrelevant
    * speaking of which, what do we know about that space? What properties can we assume there? I'd definitely say dimensions are still correlated... but is this a metric space? a topological space?
    * shouldn't we follow this by something like PCA to decorrelate dimensions?
    * Is the space filled enough or are all datapoints very close?

### Points as coordinates

* I thought it was important that we are dealing with points, so why cosine distance? I thought that would be for vectors, we should be using euclidean distance! By not doing that on the final space we see again that many assumptions are dropped
* Yes points instead of regions, but I agree that that's a bug and not a feature, and also (critizising CS als solche), computation with regions is computationally incredibly demanding. 
* \cite{Derrac2015}: \q{SVD produces a representation in which entities correspond to vectors, which should be compared in terms of cosine similarity rather than Euclidean distance} (-> spatial relations such as betweeness and parallism wouldn't make sense) - and then proceeds to use cosine-distance?! wtf!! (acutally that may be a problem of ager & alshaikh)

## So are that now conceptual spaces?

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


## So what do I think about all this

How good do I think does the algorithm capture CS? How useful do I think CS are in general (two perspective, as model of human concept formation AND algorithm-that-allows-certain-things-like-reasoning), and how good do I think the algorithm does it? Is the algorithm practical?
* So now we have to answer the question if we achieved do what motivated us in the first place: easily and automatically create structured knowledge bases .My opinion is that the need to create such knowledge bases is absolutely there, but I am more than unsure if this is the best imaginable algorithm. Of course, I see the reasoning for the distancematrix->MDS to ensure the resulting place is actually metric (an assumption more and more dropped by the two followup-papers)... but maybe before and after we can use neural techniques? Like idk doc2vec für die distance matrix, dann gerne MDS, und candidate terms sind dann word embeddings we threshold their closeness to the document embedding? Or also use LSI/LDA? (see my suggestion for an algorithm)