This section will introduce conceptual spaces as tool of choice as well as how to generate them and how reasoning on them works, as well as some other related work to what's done in this thesis.

To understand what a CS is, let's start with vector space models in general. VSMs try to represent entities of a certain kind (such as educational resources) together with their associated properties (\eg if they are advanced) and relevant concepts (\eg their faculty). VSMs are used for information retrieval and NLP \cite{deerwester, Lowe} since long before the dawn of modern neural embeddings like \gls{word2vec} \cite{Mikolov2013}. 

Conceptual Spaces are similar in principle, but where in standard embeddings all natural language words (including verbs and adjectives) are simply modelled as vector, in CS there is an explicit disctinction between entities (tokens, vectors, mostly nouns) and their properties and concepts (regions). The domain of a conceptual space does not include all kinds of words or concepts, but only concepts of a certain domain (like movies or university courses). Where the regularities in the VSMs (see \autoref{eq:w2vregularity}) are only implicit, a CS explicitly models meaningful and interpretable human concepts and properties as dimensions\footnote{Which means that in a conceptual space of humans, \emph{man} may be a unit vector}, so in contrast to arbitrary dimnesions that only depend on the random initial setup, there is a clearly interpretable direction for the gender, and the space itself has a clearly defined metric that allows much more geometric and arithmetic reasoning, such as \eg betweeness. Furthermore, CS are organized into multiple low-dimensionsional spaces for different facets of the domain, such that in each of those only a small set of highly correlated properties/concepts is relevant\footnote{A prime example for this is the color-domain, which may consist of the attributes \emph{hue}, \emph{saturation} and \emph{value}.}.
<!-- from \cite{Alshaikh2019}: \q{For instance, in a conceptual space of movies, we may have facets such as genre, language, geographic location, etc. Each facet is associated with its own vector space, which intuitively captures similarity \wrt the corresponding facet. Most of these facet spaces tend to be low-dimensional [...]. This clearly differentiates them from traditional semantic spaces, which often have hundreds of dimensions}) -->
Importantly, a concept in a Conceptual Spaces is not modelled as a vector or point, but as a convex region. <!-- TODO: is this mentioned? (which allows for easy extraction of is-a and part-of relations or prototypical examples vs edge examples, but makes the generation computationally vastly more expensive)--> . 

As much for the differences, let's look into why they were created before formally defining them.

The theory of Conceptual Spaces was first introduced by Peter Gärdenfors in his 2000 book \citetitle{Gardenfors2000a} \cite{Gardenfors2000a} both as a theoretical model of human concept formation, but also as format for knowledge representation in artificial systems \cite{Gardenfors2004}. 

In short, a conceptual space is a gemetric structure that spans a number of \emph{quality dimensions} which denote basic features of the entities it contains. Regions of this space correspond to concepts and points to individual objects (instances/\emph{entities}).The quality dimensions are usually based on perception or sub-symbolic processing and according to the theory, natural categories correspond to convex region in these spaces, which allows for geometric solutions to commonsense reasoning tasks such as \emph{betweeness}.
<!-- TODO: already formal definition?? -->
<!-- TODO: \cite{Derrac2015}: "Conceptual spaces \cite{Gardenfors2000a} are metric spaces which are used to encode the meaning of natural language concepts and properties." -->


Intro to \cite{Gardenfors2000a}: \q{Within cognitive science, two approaches currently dominate the problem of modeling representations. The symbolic approach views cognition as computation involving symbolic manipulation. Connectionism, a special case of associationism, models associations using artificial neuron networks. Peter Gärdenfors offers his theory of conceptual representations as a bridge between the symbolic and connectionist approaches.}

CS are often seen as a layer of reasoning that stands in between symbolic processing (classical AI, expert systems, formal logic, syllogisms) and subsymbolic processing /connectionistic AI, modern ML with eg ANNs), something that builds a bridge between these and solves the symbol-grounding problem that classical logic and inference systems have by allowing to symbolistic representations that allow for high-level syllogistic reasoning from noisy real-world data. The need for that is certainly there, as the problem of clasical AI is that you'd have to add a shitton of data by hand, but in contrast to ANNs the results are explainable and its reasoning corresponds to high-level (logical) human reasoning (syllogisms etc). Conceptual Spaces are quite literally in between these two: According to \textcite{Gardenfors2000a}, humans have different forms of representations for concepts, split into three levels:  The symbolic level, the conceptual level and the subconceptual level \cite[204]{Gardenfors2000a}. These are not in conflict, but different perspectives onto the same phenonemon, such that each of the models captures some asbect of the true one. The three levels are:
* Symbolic: Represent observations by describing them in some specified language (formal logic, symbolism, classical AI, "logical positivism", aristotelian concepts)
* Conceptual: Observations are defined not as token of a symbol, but as vector in a conceptual space (of unknown but hopefully modellable quality) (induction/reasoning is thus based on regions and directions) (prototype theory, linear algebra)
* Subconceptual: Observations are the firing of the neurons of our sensory receptors (defined as something before conceptualization) (induction as pattern-matching in that firing) (connectionism, modernAI=ANNs)

Apart from the theory's aspiration to model human concept formation and reasoning \cite[Sec.~6.5]{Gardenfors2000a} however, it is also a a useful knowledge representation method.


The theory of Conceptual Spaces \cite{Gardenfors2000a, Gardenfors2004} is 
	* a model of human conceptualization/concept formation and reasoning (\cite[Sec.~6.5]{Gardenfors2000a}: he's suggesting what kinds of models (and what algorisms to generate them) may be good at doing similar kinds of reasoning as humans (again explainable AI, where ANNs can solve it but not tell us how, this can))
	* but also created as a tool to express semantic relations that is superior to previous appraoches of a symbolistic, ontology-based semantic web. Knowledge representation method, a representational format with rich semantics. Created as better tool for semantic web (keep in mind, it's 2000, where that was all the rage)
		* Claims to have richer semantic structure than RDS/OWL/the entire idea of ontologies (Because information processing is not, as historically thought, pure deductive reasoning (→ syllogisms) - no strict is-a relations but also concepts like similiarity, which the original semantic web languages couldn't represent)
		* Other problems with ontologies and reasoning systems are that they assume explicit, unambiguous, universally agreed-upon truths which are explicitly described, which he argues is not how the world is.
=> So on the one hand it's a framework for scientific theories, but on the other hand a model of human concept formation from phenomenal observations.

 \cite[Sec.~6.7]{Gardenfors2000a} No matter if CS actually truely represents human concept formation, some (models of) kinds of reasoning can be done on that level that cannot be done on symbolistic or subconceptual level but only on the level that CS is at, so it's still a useful tool


So, in conceptual spaces, concepts are represented as convex regions in [high-dimensional/domain-specific], human interpretable spaces. For example, the concept of "apple" is a region that in the dimension "color" is somewhere between red and green, in the dimension "form" at roughly round, in the dimension "taste" somwhere between sweet and sour, etc. 
Every instance of an apple is thus a vector that lies inside the high-dimensional region of the concept. This allows for high-level reasoning, such as the question "does any Instance of concept X fit into my bag?" -> If the "size" dimension of the whole region is smaller than the size of my bag, it will.



====================== FROM CS COURSE ====================

* Classical Logic & Inference system have the symbol grounding problem.
* Conceputal Layer in between symbolic layer (formal logic, natural language) and subsymbolic layer (sensor values, real world): gemometic representation, human cognition
* there are quality dimensions. These can either be integral (hue & saturation) or seperable (temperature and weight)
* domain = set of integral dimensions that are separable from others. (eg. color).
* Distances on individual dimensions need to be aggregated - he suggests euclidian for integral, manhattan for seperable. Context can influence distance by putting weights on dimensions. Distance inversely related to similiarity.
* betweenness iff d(x,y) + d(y,z) = d(x,z). Macht nen square bei manhattan distances!!
* convec because in that way interpolations between two points don't leave the set.
* Criterion P: a natural property is a convex region of a domain in a conceputal space.
* Connects to prototype theory! central point of each region corresponds to prototype
* relative properties: define them as region on a relative scale, resized this according to contrast class ("tall" iff in the upper third of all relevant objects)
* Concepts: Combination of properties (different properties are differently important (influenced by context), and potentially correlated (taste and color in apples))
* Criterion C: A natural concept is represented as a set of convex regions in a number of domains together with an assignment of salience weights to the domains and information about how the regions in different domains are correlated.
* Concept combination: Either narrow down (correlations may yield more updates - green banana is bitter), or, if modifier incompatible with original value, replace that information (pink elephant), or, if incompatible with most domains, remove incompatible domains (stone lion doesn't have a life span or habitat)

==================================================================
* CS are often said to be something in between classical, symbolistic AI approaches on the one hand, and connectionistic ANN-based modern ML on the other, something that may possibly build a bridge between the two (we'll soon see that it's literally very much in between those!). Such a bridge is seen as very important bc the problem of classical AI is that it is a lot of manual data, you'd have to add countless facts or smth by hand, but the advantage of it over ML is that it's explainable and its reasoning corresponds to high-level (logical) human reasoning (syllogisms etc), so a bridge that crates the former from the latter would be awesome.
	* Intro to \cite{Gardenfors2000a}: \q{Within cognitive science, two approaches currently dominate the problem of modeling representations. The symbolic approach views cognition as computation involving symbolic manipulation. Connectionism, a special case of associationism, models associations using artificial neuron networks. Peter Gärdenfors offers his theory of conceptual representations as a bridge between the symbolic and connectionist approaches.}

* According to \textcite{Gardenfors2000a}, here are different forms of representation we humans have for concepts (chapter 1,2), which he says can be represented by three levels of accounting for observations: The symbolic level, the conceptual level and the subconceptual leven (p204).  Importantly, Gärdenfors doesn't see the three levels as being in conflict with each other, they are perspective on the same things, different models for the same phenonemon (..that each capture some aspects of the true one)
	* Symbolic: Represent observations by describing them in some specified language (formal logic, symbolism, classical AI, "logical positivism", aristotelian concepts)
	* Conceptual: Observations are defined not as token of a symbol, but as vector in a conceptual space (of unknown but hopefully modellable quality) (induction/reasoning is thus based on regions and directions) (prototype theory, linear algebra)
	* Subconceptual: Observations are the firing of the neurons of our sensory receptors (defined as something before conceptualization) (induction as pattern-matching in that firing) (connectionism, modernAI=ANNs)
 \cite[Sec.~6.7]{Gardenfors2000a} No matter if CS actually truely represents human concept formation, some (models of) kinds of reasoning can be done on that level that cannot be done on symbolistic or subconceptual level but only on the level that CS is at, so it's still a useful tool


 Originally created by Peter Gärdenfors \cite{Gardenfors2000a}, want to stand in between subsymbolic processing and symbolic processing: Like in subsymbolism, concepts are represented in high-dimensional spaces, but because the dimensions of these spaces are not arbitrary but human-interpretable, it allows for symbolistic high-level reasoning.
	* would also solve the symbol-grounding problem that Classical Logic & Inference systems have

==================================================================

* Representation of concepts. Note that, as Gärdenfors states, Representations don't need to be similiar to the objects they represent, but the *similarity relations of the representations* should correspond to those of the objects they represent

Use case: Should be a representational level below the symbolic level (...making it superflous, as the concept hierachies are generated automatically - the validity of "a robin is a bird" is encoded because it is a subregion ( - the semantic info that OWL and the like capture becomes redundant))

\cite{Derrac2015}: "Conceptual spaces \cite{Gardenfors2000a} are metric spaces which are used to encode the meaning of natural language concepts and properties."
	* In practice most often euclidian.
	* typically each dimension corresponds to a primitive cognitive feature, and CS are grouped by "domain" (REALLY?)
		* the thing that they are basically split into untrennbare dinge like HSV for color
		* I said "typically high-dimensional", but rather the opposite!
	* Important is that it basically only contains stuff for which the space dimensions make sense (you wouldn't find kings in a concpetual space of cabbages)
	* Specific entities (instances of a concept) then correspond to points in the conceptual space, while natural concepts and properties are posited to correspond to convex regions
	* !!Distinction of concepts and properties!!
	* Criterion C and Criterion P:
		* TODO like in the CS Slides!!
		* "criterion C defines concepts as regions of conceptual spaces" \cite[111]{Gardenfors2000a}

	* Principles:
		* informtation organized in spatial structures with dimensions (color, size, shape, ...)
			* dimensions have topological or geometric structures
			* dimensions sorted into domains (h+s+v = color)
			* dimensions are human-interpretable (measurable qualities)
		* distances ^= dissimiliartiy
		* properties: *A property is a convex region in some domain*
		* concepts: *A concept is represented as a set of convex regions in a number of domains together with a prominence assignment to the domains and information about how the regions in different domains are correlated.* 





TODO: Define "Conceptual Space" explicitly
Definition 2: \textbf{Conceptual Space} The term refers to xyz.


#### WHAT TO SAY NOW

Well, an intro into CS 

* metric space (not necessarily of euclidian metric, gärdenfors brings some examples of weirder metrics/topological structures)
* criterion C and criterion P
* Gives an extended notion of what **similarity** is (see reasoning-section)
* related to prototype theory

#### MOAR

* There is a distinction between phenonemal and scientific interpretations of CS \cite[Sec.~1.4]{Gardenfors2000a}
	* When using CS as framework for a scientific theory, the geometrical/topological structures of the dimensions are chosen by the scientist. The choice of that brings along \q{the *measurement methods* employed to determine the values on the dimensions} (p21)
	* When, however, dealing with a *phenonemal* CS, the dimensions have to be infered from the subject's introspection. A good method for that is MDS, introduced by Gärdenfors himself \cite[Sec.~1.7]{Gardenfors2000a}, but \cite[Sec.~6.5]{Gardenfors2000a} he also suggests ANN-based embedding (specifically self-organizing maps.)


* That Gärdenfors is often critizised as being inprecise or smth in the definition, but tbh hat er pretty specific instructions on how to create them computationally

#### Regarding Reasoning 

* once you have created the structure, the following emerge automatically: 
    * concept hierachies/taxonomies (subregions)
    * identity/equality of concepts (same region)
    * identity/equality of names (same point)
    * characteristics of properties (transitivity, symmetry) (from intrinsic features of dimensions (time is linear because the dimension is linear)). Also constraints like "nothing is both red and green" (disjoint regions)
* CS and with it ontologies "automatically" (BIG question mark) arise from prototypes + metric domain + voronoi tesselation
* no need for a symbolic inference engine anymore [WELL BUT this is computationally easily MORE demanding [..SOURCE!!]]
* Encodes more than just taxonomies of concepts (...which means more can be used for inference/reasoning): similiarity (If the wine I want to have is not avaiable, with the aid of the similarity information provided by the domain structures I can find similar ones - but since similarity is cnotext-dependant, the system can ask me for what dimensions of the wine are important to me to judge similarity!)
* Metaphors and metonymies are understood by the framework (-> das a fortiori reasoning, wakeboard & snowboard ding, das hat doch auch DESC15 drin!!)











Now the standard problem with conceptual spaces is that they would have to be manually generated, which of courses is a lot of work, which is where the work of [Schokeart et al] comes in - to generate them in a data-driven fashion.


* Dass der tatsächliche Anwendungsbereich von CS noch sehr begrenzt ist - RaZb20 mention "they are commonly used in perceptual domains, e.g. for music cognition [Forth et al., 2010; Chella, 2015], where quality dimensions are carefully chosen to maximize how well the resulting conceptual spaces can predict human similarity judgements"
* Dass Word Embeddings ja relativ nah an CS sind - For ex- ample, a well-known property of word embeddings is that many syntactic and semantic relationships can be captured in terms of word vector differences [Mikolov et al., 2013].



### Data-Driven CS Generation 

For that, the authors look at three different domains: movies, wines and places. For each of these domains, they collected many samples (like movies) together with descriptions from places where people can leave them (like reviews from IMDB). A representation of a movie is then generated from the bag-of-words of the descriptions of the individual movies, leading to a very high-dimensional, very sparse representation for all movies. 
To make the representations less sparse and more meaningful, the words in the BOW are subsequently PPMI-weighted, which weights words that appear often in the description of a particular movie while being infrequent in the corpus overall higher while setting the representation of stopwords to almost zero. 
This PPMI-weighted BOW is however not yet a euclidian space yet, which is why the authors subsequently use multidimensional scaling (MDS). MDS is a diminsionality reduction technique that attempts to create a euclidian space of lower dimensionality than the original one in which the individual distances of the items are preserved as well as possible. 

With such a space, the concepts of betweeness already makes sense, but so far, the dimensions are not interpretable. So how does one automatically find such directions? In the case of movies, good dimensions may be "scariness", "funniness", "epicness", "family-friendlyness" etc. 
To find these dimensions, the authors look for these words (as well as similar words thanks to clustering) in the reviews. Then the movies are grouped into those that contain the words from the cluster often enough vs those that don't. A support-vector-machine subsquently finds a hyperplane that best divides the two groups (eg. scary and non-scary), and the orthogonal of that hyperplane is used as one axis of the new coordinate basis. 

* \cite{Gardenfors2000a} also said stuff like "Dimensionality Reduction from the high-dimensional input (neurons) eg using MDS into a euclidian space, and then geometric reasoning on that" including some examples of kinds of reasoning, so actually the exact algorithm \cite{Derrac2015} did was extremely naheliegend (put some obvious NLP modelling to that like \cite{Turney2010} explained and you're pretty much exactly at their algorithm) 
	* He even has a chapter "conceptual aspects", where he suggests vector space models, dimensionality reduction algorithms, ANN architectures, ... (for all of the 3 levels)
	* ....but even more reason to make me think that it may have been their error to keep the enforcement that the MDS-result must be a euclidian space, when afterwards they have the additional step of using their rankings anyway! (...which btw brings me to the question what that does to distances?!)



* We also drop the requirement that actually we'd have to embed entities into small spaces of only one domain! This is only kinda picked up again later by \cite{Alshaikh2020}
	* \cite{Alshaikh2020}: "When representing a particular entity in a conceptual space, we need to specify which domains it belongs to, and for each of these domains we need to provide a corresponding vector." 






#### On types and tokens

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



#### Excursion: A CS for the subconceptual level with ANNs

* The Information received by the receptors is too rich and too unstructured, \q{What is needed is some way of transforming and organizing the input into a mode that can be ahndled on the conpcetual or symbolic level. This basically involves finding a more *economic* form of representation: going from the subconceptual to the conceptual level usually involves a *reduction of the number of dimensions* that are represented} (p221)
* \eg MDS, Shephard's algorithm of "start high-dim and then sucessively reduce dimensionality until no furhther dimensions can be limitnated without a substantial disagreement between the rank order generated by the metric assignment and the original rank order" (often no more than 2-3D)
* But we an also think about ANNs - Concreteley \q{Kohonen's (1988, 1995) *self-organizing maps*.}, that automatically \q{*reduce the representational complexity* of the input} (221) (=question "How can one generalize from single observations to general laws" on subconceptual level)
	* Self-organizing map is an ANN (with most often 2-3D array of neurons as output), that does the connections such that \q{similarities occuring among different input vectos are [...] *preserved* in the mapping, in the sense that input vectors with common features are mapped onto *neighboring* neurons in the output map. The degree of similarity between two input vectors is determined by some (instrinsitc) *distance* measure}, of which he suggested many (sec 2.4). Preserve most topological relations while making it lower-dim. 
	* That maps highdim regions to point-embeddings, and THAT IS GENERALIZATION (answer to question 2)


### Reasoning in CS

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




#### Problems with CS

* Question of how to identify and describe domains not remotely answered
* Reasioning with regions is computationally extremely demanding
* We say we're dealing with POINTS but we're constantly doing cosine similarity, isn't the important difference between points and vectors that cosine would be relevant for vectors, but euclidian(/..) distance for points?! 