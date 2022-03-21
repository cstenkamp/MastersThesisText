
Mostly from \cite{Derrac2015}, but tbh not that important for me. However a short paragraph about reasoning-based classifiers and the respective intutitive explanations for known classifiers may be interesting (think 1-NN is "Y is of the same class as X because X closest to Y", but also more complex ones.)

TODO: \todoparagraph{explain here why they have the requirement that the resulting semantic space is euclidian!!}

* Similiarity based reasoning ("If A enjoyed X and Y is similar to X, A will likely also enjoy X")
    * what Amazon does
    * easy to train (similiarity degrees can be obtained from stuff like \gls{word2vec} thank's to the distributional hypothesis)
    * can only be used if there are enough similar concepts (das Problem hat Felix auch bei Siddata gehabt! Was konkret war das nochmal?)
    * context-dependent
* (Logic-Based reasoning/Inference? das was FOL macht? [DESC15] und [VISR12] listen ein paar Einschränkungen/Eigenschaften die das hat I think)
    * Requires the knowledge to be encoded in logic, which is very cumbersome
    * Doesn't allow for any fuzzyness
* Interpolative Reasoning (if we know that undergraduate students and PhD students are both exempt from paying council tax in the UK, we can plausibly conclude that master’s students are also exempt from paying this tax, given that master’s students are conceptually between under- graduate students and PhD students.)
    * Source looking into it ([28] of [DESC15]): M. Abraham, D. Gabbay, U. Schild, Analysis of the talmudic argumen- tum a fortiori inference rule (kal vachomer) using matrix abduction, Studia Logica 92 (2009) 281–364.
* A fortiori Inference (if we know that buying beer is illegal under the age of 18 in the UK, we can plausibly derive that buying whiskey is also illegal under the age of 18, since whiskey is stronger than beer)
* Analogical Reasoning? War das das komplexe "Wakeboarden verhält sich zu Wasserski wie Snowboarden zu Ski"? (TODO: sobald ich das weiß das auch in https://www.notion.so/Inducing-semantic-relations-from-conceptual-spaces-a-data-driven-approach-to-plausible-reasoning-bfca77cbb6334da1a122e57c7e4ea503 hinzufügen!)
    * [29-32] of [DESC15] go into detail
    * If the analogical proportion a : b :: c : d holds, the pairs (a, b) and (c, d) are called relationally similar [42] of [DESC15]
* Extrapolative Reasoning (see [25] of [DESC15])
* approaches that aim to transfer knowledge from one domain to another (see [33] of [DESC15])


#### What about the concepts from logic/knowledgebases/...?
* subsumption ("every pizzeria is a restaurant")
* mutual exclusiveness ("no restaurant can be a beach")
* overlapping concepts ("some bars serve wine but not all")
* is-a
* part-of
