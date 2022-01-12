* Knowledge representation method:
	* Representational format with rich semantics
* Originally created by Peter Gärdenfors \cite{Gardenfors2000a}
	* Created as better tool for semantic web (keep in mind, it's 2000, where that was all the rage)
	* Use case: Should be a representational level below the symbolic level (...making it superflous, as the concept hierachies are generated automatically - the validity of "a robin is a bird" is encoded because it is a subregion ( - the semantic info that OWL and the like capture becomes redundant))
	* Claims to have richer semantic structure than RDS/OWL/the entire idea of ontologies
		* Why? Because information processing is not, as historically thought, pure deductive reasoning (→ syllogisms) - no strict is-a relations but also concepts like similiarity, which the original semantic web languages couldn't represent
		* Other problems with ontologies and reasoning systems are that they assume explicit, unambiguous, universally agreed-upon truths which are explicitly described, which he argues is not how the world is.
	* Benefits:
		* once you have created the structure, the following emerge automatically: 
			* concept hierachies/taxonomies (subregions)
			* identity/equality of concepts (same region)
			* identity/equality of names (same point)
			* characteristics of properties (transitivity, symmetry) (from intrinsic features of dimensions (time is linear because the dimension is linear)). Also constraints like "nothing is both red and green" (disjoint regions)
		* CS and with it ontologies "automatically" (BIG question mark) arise from prototypes + metric domain + voronoi tesselation
		* no need for a symbolic inference engine anymore [WELL BUT this is computationally easily MORE demanding [..SOURCE!!]]
		* Encodes more than just taxonomies of concepts (...which means more can be used for inference/reasoning): similiarity (If the wine I want to have is not avaiable, with the aid of the similarity information provided by the domain structures I can find similar ones - but since similarity is cnotext-dependant, the system can ask me for what dimensions of the wine are important to me to judge similarity!)
		* Metaphors and metonymies are understood by the framework (-> das a fortiori reasoning, wakeboard & snowboard ding, das hat doch auch DESC15 drin!!)
* Problems:
	* Question of how to identify and describe domains not remotely answered
	* Reasioning with regions is computationally extremely demanding

* Principles:
	* informtation organized in spatial structures with dimensions (color, size, shape, ...)
		* dimensions have topological or geometric structures
		* dimensions sorted into domains (h+s+v = color)
		* dimensions are human-interpretable (measurable qualities)
	* distances ^= dissimiliartiy
	* properties: *A property is a convex region in some domain*
	* concepts: *A concept is represented as a set of convex regions in a number of domains together with a prominence assignment to the domains and information about how the regions in different domains are correlated.* 