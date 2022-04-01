<!-- 
Zitat JOHANNES über SidBERT: "When using traditional pattern-matching search, these search queries may yield no results or return courses within another domain that by chance contain the same words but are otherwise unrelated to the domain the student is looking for." (-> zum thema hilft auch in Search engines etc)
-->

### Course Recommendation

This thesis is part of SIDDATA, from the idea to add to this platform a recommender that can generate course-recommendations in new ways (with input and feedback). Keyword Explainable AI.

* Motivation for SIDDATA in general
	* Steal from SIDDATA-Papers (..and cite them)
* What we specifically want to do (our Use Case): Explainable Course Recommendation, "Ich hätte gerne einen Kurs wie Codierungstheorie & Kryptographie, aber mit weniger Mathe"
	=> We want feature-directions.
	* Show Sample: Movie Tuner Interface (here or [*])
	* Standard for Recommendation ist ja der Amazon-Approach "kunden die X kauften kauften auch Y" = Similarity-Based Reasoning
		* That is optimized as fuck by now, but it (similarity-based reasoning) still the most basic reasoning/classification algorithm there is!
	* Feature directions are a thing in Computational Linguistics, see the Astonishing Regularities in Word embeddings 
		* demonstrated in \cite{Mikolov:Regularities}): könig - mann + frau = königin
		* Also: https://devmount.github.io/GermanWordEmbeddings/
		* What's missing from those embeddings explainable recommendation is however that the gender here is an actual axis ("mann" is one of millions of vectors in this space; the vector-space should be such that the very few most relevant "bare properties" of the domain unit linarly independent unit vectors AKA dimensions)
		* So "Codierungstheorie & Kryptographie - Mathe + Info = Kryptographische Algorithmen"
	* So what we precisely need is "human-interpretable feature directions"
		* that would allow us to rank objects according to how much they have the corresponding feature
		* That would be useful in a lot of other tasks related to our use case (see sources of [AGKS18])
			* Interpretable classifiers / Rule-Based Classifiers from the rankings
			* entity-oriented search engines  (can use directions in case of gradual and possibly ill-defined features, like "popular holiday destinations")
			* Recommender systems (especially critique-based ones (working based on feedback, with the user in the loop (which is what SIDDATA wants))
			...especially relying on Keywords-Extraction, such that the user can supply those concepts mentioned in the courses for a recommendation
			* Show Sample: Movie Tuner Interface (here or [*])	
		* That would be a structured knowledge base (see [+])
			* \cite[Chapter 1]{Derrac2015}: Many CL tasks rely on structured  knowledge bases, but getting them in symbolic form occupied (computational) linguists for dozens of years without significant progress, so finding it automatically is a good idea.

### Derrarc2015's algorithm

To achieve what we want, we'd need a vector-space with several properties like linear independent components --> Euclidian Metric
=> Conceptual Spaces fulfill these criteria!
...But we need to generate that data-driven
...Derrarc2015 did such a thing!

* What they did can definitely be used for what I want to do here if it works well enough
* Their motivation is thus also mine: Explainable AI but data-driven 
	* They want to get "commonsense reasoning such as interpolation and a fortiori inference", but learned automatically. 
	* As they claim, "commonsense reasoning" <=> "how different concepts and entities are semantically related" <=> CS
		because "CS qualitative spatial relations" <=> "required semantic relations for reasoning"
		=> Their aim is to create a structured knowledge base (see [+])
* Few grains of salt (no regions but only dots, domain-specific)
* Does their algorithm work for the given dataset?
* Seems like a small community of only these guys
	* Active Community, cool ideas, but only citing themselves and all basing on Derrarc2015 (..and having him as co-author)
	* Sanity-check the validity of their claims as external person
		* Also with other datasets beyond the always-same-style of their ones
	=> "If this algorithm is as good as they claim, that would be great, but we have reasons to not trust their claim so we're checking them."
* Also their published code is crap => I want to create a better architecture that what's available
	* DESC15 didn't have any code, 
	* one of the others has a link to the repo IN THEIR PAPER but it's empty for >3 years
	* the last one has >40 unnamed command-line-args!
	==> This is not how to science, I want to do it better.

==> Before applying it, we should sanity-check their algorithm
==> This thesis should ALSO result in a pipeline die es future research leichter macht ebengenau das zu tun was ich hier tu und die validiät der claims zu prüfen etc.


TODO: quotes from Johannes about how making the choice easier for students is very important, but that categorizing educational resources is a challenge.