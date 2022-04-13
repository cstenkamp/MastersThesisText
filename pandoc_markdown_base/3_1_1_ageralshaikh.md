

Regarding Ager and Alshaikh:

* RaZb20 tried Doc2Vec instead of MDS and it performed worse!

* \cite{Alshaikh2020} do Kappa on binary, I can't believe that's good


* [AGKS18] haben den candidate-filter-teil konfigurierbar (und sagen bei denen ist accuracy even better than kappa)

* Argue:
    * doc2vec nicht implementiert weil schlechter bei ager.
    * Finetuning nicht drin weil nur marginal besser bei ager (ref tabelle im anhang)
    * ...ähnliche gründe für alshaikh finden

* Binary occurence as best metric? I can't believe that
* Who said kappa is a bad value?

* \textcite{Alshaikh2020}
    * Well, do the stuff iterative cluster stuff
        * "When representing a particular entity in a conceptual space, we need to specify which domains it belongs to, and for each of these domains we need to provide a corresponding vector." 
        * then they show their example of something that is not seperable with a hyperplane unless we specify subdomains, maybe just steal their plot that explains their one contribution to 99%
    * Cluster with affinity propagation
    * Do Kappa on Binary (-> see later)
        * for them, the binary "does the word occur in the description" is the only sensible signal, no ppmi or anything! (page 2, footnote 1 of RaZb20)

## \textcite{Alshaikh2020}

Important to mention that they iteratively find "disentangled" features and thus embed the stuff in several uncorrelated low-dimensional subspaces






## Ager do
(see ZZ_listingreplacement_ager.md)
