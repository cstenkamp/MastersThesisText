# FROM COURSE

## Computational Modelling of CS (KURS SLIDES 2)

* Larger context: VSMs \cite{Turney2010}:
    * Term-Document Model for similarity of documents
        * dimensions = terms in the docs (doc-term-matrix)
        * bag-of-word hypothesis: documents with similar words have similar meaning
    * Word-Context-model: simiarity of words    
        * dimensions somehow encodde context word can occur in (explicitly through neural models))
        * distributional hypothesis: words that occur in similar context have similar meanings 
    * pair-pattern model: similarity of relations
        * dimensions = word-pairs that can occur in relation
        * extended distributional hypothesis: releations that occur with similar word paris have similar meaning

* Distance = inverse similarity
    * euclidian, manhattan
    * cosine similarity for vectors

* regions and betweeness
    * convex hull as the set of all convex combinations of a point
    * can be done by linear programming with polynomial cost

* properties we want beyond VSMs  
    * metric space, general distance
    * topological space (neighborhood relation)

* Algorithms: 
    * MDS
    * SVD

## Reasoning about Categories

* \cite{Gardenfors2001}
* Voronoi tessalation around prototypes to generate categories, and then use the *Region Connection Calculus* for reasoning, bridging the gab between geometric and symbolic representation 
* Translate RCC5 relations to reasoning:
    * Discrete (unconnected) Regions (DR)
    * Idential Regions (EQ)
    * Proper Parts / Subregions (PP)
    * PP^{-1}, the inverse 
    * Partial Overlap (PO)


## Completing incomplete knowledge bases


* CS, in contrast to knowledge bases, allow for interpolation and extrapolation of knowledge, allowing for commonsense inference. Apartment in suburbs basic, apartment in centre very-comfortable -> apartment in outskirts in between \cite{Schockaert2011}
* Interpolative reasoning Assumption: \q{intermediary conditions lead to intermediary conclusions} \cite{Schockaert2011}. 
* Extrapolative reasoning assumption: \q{Analogous changes in the conditions should lead to analogous changes in the conclusion} \cite{Schockaert2011}
* To automate such inference, we need a richer form of knowledge than what is available in calssical logic: We need a notion of / Information about \textbf{Betweenness} and \textbf{Directionality}
* in \cite{Schockaert2011}, they define similarity through a variation of the Jaccard-distance (IoU, Overlap-Area divided by Union-Area)


* In ANNs you have quantitative reasoning, based on similarity: a' -> b' holds iff a -> b and a $\approx$ a'
* In CS we have qualitative reasoning:
    * bet(p,q,r) that q lies on the line between p and r
    * par(p,q,r,s) also exists
    * from that many things regarding interpolation and extrapolation follow, geez (bet1, bet2, par1, par2) (slide 64 of 09 of CS course)
* Generalized Modus Ponens: "The more the input A is close to A_i, the more the output B must be close to B_i"






## Reasoning in CS

* According to \cite{Gardenfors2000a}, Representations don't need to be similiar to the objects they represent, but the *similarity relations of the representations* should correspond to those of the objects they represent
* the validity of "a robin is a bird" is encoded because it is a subregion

* once you have created the structure, the following emerge automatically: 
    * concept hierachies/taxonomies (subregions)
    * identity/equality of concepts (same region)
    * identity/equality of names (same point)
    * characteristics of properties (transitivity, symmetry) (from intrinsic features of dimensions (time is linear because the dimension is linear)). Also constraints like "nothing is both red and green" (disjoint regions)
* CS and with it ontologies "automatically" (BIG question mark) arise from prototypes + metric domain + voronoi tesselation
* no need for a symbolic inference engine anymore [WELL BUT this is computationally easily MORE demanding [..SOURCE!!]]
* Encodes more than just taxonomies of concepts (...which means more can be used for inference/reasoning): similiarity (If the wine I want to have is not avaiable, with the aid of the similarity information provided by the domain structures I can find similar ones - but since similarity is cnotext-dependant, the system can ask me for what dimensions of the wine are important to me to judge similarity!)
* Metaphors and metonymies are understood by the framework (-> das a fortiori reasoning, wakeboard & snowboard ding, das hat doch auch DESC15 drin!!)

* Similarity
	* Godman(1972): There is no **overall Similarity** - Similarity is relative, only meaningful in context ("in what respect are these two similar") (Compare recommender systems - amazon's algorithm doesn't know WHAT ABOUT the movies I like it is that I like (and has to make up for that by a shitton of data from me and other users, hoping to just find neihgbors close enough to my taste that makes 1-NN meaningful))
	* Degree of similarity only meaningful relative to a domain/dimension, \q{any measurement of similarity is based on assumptions concerning the properties of a similarity relation} (p110)
	* \q{What is, then, an appropriate theoretical model [for similarity]? Similarity data from direct or indirect measurements are usually interpreted as proximity data, giving information about the distance btween objects in a conpecutal space [...]. Multidimensional scaling is a typical technique for reconstructing spaces from similarity data [...]. [...] I will assume that similarity is a function of distance (and possibly some ohter factors) in a conceptual space. [...] a common assumption [...] is that similarity is an exponentially decaying function of distance.} (p110)
	* Similarity as Shared Properties
		* (assuming clearly defined C and P) \q{two objects falling under different concepts are similar because they have many properties in common}
* Induction
	* Induction goes from single observations to generlatizations.
	* Humans are good at inductive inferences, however our ways of abstraction and induction are only good when it relates to the physical world we're adaped for. \q{"To trust induction as a way of access to the truths of nature ... is to suppose, more nearly, that our quality spaces matches that of cosmos"} (p203) => we can model that with CS! But How can we mechanize induction? 
    But how is obsrevation represented?  And How do we decide what properties are releavnt? How can we generalize? How can *inferences* be made from limited information?
	* Maybe on the subconceptual level? (Sec 6.5)
		* \q{Within the philosophy of science, a disctinction between *perception* and *observation* is sometimes made [...] [that] paralles the one between phenonemal and scientific interpretations of CS} (p220)
		* \q{So how do we distil sensible information from what is recieved by a set of receptors?} (p220) According to Gärdenfors, that is the same as asking \q{How can inferences be made from limited information about an object} (p205)
		* Connectionists say "pattern matching", but we wanna ask the question "Well but what kinds of patterns, and what underlying algorithms ov matching"!!! Important question is "How can we relate the levels, which are sides of the same coin? "
		* (see "Excursion: A CS for the subconceptual level with ANNs")
	* Maybe on "The concecptual level", where the observations are characterized not by symbols, but by an underlying CS. Relation to Prototype Theory, and induction works in that an n CS
        * Correlations between domaisn - 
			* \q{categorical inductive inferences} (p226), where we go from \q{Grizzly bears love onions\\Polar bears love onions\\ \hrule All bears love onions} (p226)
		* Feature-based model instead of category-based model of induction (Sloman (1993))
	* Where on the 3 levels (symbolic, conceptual, subconceptual) is induction? well, seems like some "kinds of induction" (ways of generelization) can be explained by each of the three levels respectively.
	* Importantly, Gärdenfors doesn't see the three levels as being in conflict with each other, they are perspective on the same things, different models for the same phenonemon (..that each capture some aspects of the true one)




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
