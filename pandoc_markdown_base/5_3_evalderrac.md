<!-- "Bezug auf die orig-paper ziehen und kritisch reflektieren" 

### Where I spotted differences

wenn meine ergebnisse anders sind als die von dem paper kann ich halt erst dann sagen "das widerspricht demunddem hier, die proposen dass und ich kann es (nicht) confirmen"

-->






## Outlook 

There are also techniques that extend the algorithm of \textcite{Derrac2015}: \textcite{Alshaikh2019} take a vector space embedding and decompose it to several low-dimensional spaces, such that it more closely corresponds to the definition of a \gls{cs} which are split into multiple domain-specific spaces of low dimension. For that, they take the spaces from \cite{Derrac2015} to then cluster their features by domain and iteratively remove these groups to create multiple subspaces, while ensuring that \gls{word2vec} embeddings close to those of the removed ones are disregarded for future features.

\cite{Alshaikh2021} want to get rid of MDS with it's quadratic space complexity and also write a completely new, unsupervised ANN algorithm based on GloVe embeddings (and suggest that doing that on BERT may be the shit). In it, they learn domain-specific embeddings from the BoW and like \cite{Derrac2015} use classification of candidate-from-text-occurs vs not-occurs for the ANN training while punishing close embeddings like \cite{Alshaikh2019}.


# Regarding their research practices


* Small community, unfortunately (all of these publications share Prof. Steven Schockaert as last author)
    * I assume \mainalgos shared data, at least [2,3] didn't  n-gram problem I mentioned.
* cherry-picking their qualitative analysis 
    * table 1 von [DESC15] angeschaut und mit deren daten nach-implementiert -> ergebnisse verschönt 
        * butcher shop ist der place-type der am ~350zigst-meisten (je nach #dims) zwischen marketplace und slaughterhouse ist 
            * (see test_paper_table1_claims in test_semanticspace_measures.py)
    * Wenn man sich in dem Paper mal die Movie-Cluster anschaut (einfach das textfile) sieht man dass das echt... bescheuert ist, die Cluster sucken hart
* Robustness (see other section)

* Code not published
    * Ager & Alshaikh did publish, but 
        * completely nonsensical, Von Software Engineering oder best practices haben die alle ncoh nichts gehört, ich arbeite mit dem guten der Paper und das hier ist die main-function...https://github.com/cstenkamp/Autoencoder-Explanations/blob/master/src/_archive/pipeline.py#L1504-L1516
        * Alshaikh only years after publication
    * open data but in a form that does not allow for comparison (see datasets-section)

* ambiguous/low-on-information about details/parameters of their algorithm in their description
    * which kappa, which kappa-weights, any Class imbalance weighting?  -- write they select Kappa "due to its tolerance to class imbalance"
        * graphics/figures/which_weigthing_algo.png
    * "that the better Ht separates entities to which t applies from the others in S,the better \vec{v_t} models the term t."
        * binary kappa?
        * With a candidate-threshold-tf of 100, that means 19.900 values (99.33%) have a rank of zero, how do you deal with that?! only pos?
        * \q{measure the correlation between the ranking induced by \vec{v_t} and the number of times t appears in the documents associated with each entity}
            * the ranking induced by count? baremetal count? ranking induced by PPMI?
                    * But Ager say \q{In our case, the rank- ings of the objects o are those induced by the dot products vw · o and the relevance scores are determined by the Pointwise Positive Mutual In- formation (PPMI) score ppmi(w, o), of the word w in the BoW representation of object o}
                    * And Alshaikh \q{To assess classifier perfor- mance, Cohen’s Kappa score, which can be seen as a correc- tion of classification accuracy to deal with class imbalance, is used.}