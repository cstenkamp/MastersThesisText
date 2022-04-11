So far, we established  that Conceptual Spaces are a good framework for that. The part that's missing is the automatic generation. 

### Mehr vorgeplänkel


So we have established that there is a distinction between phenonemal and scientific interpretations of CS \cite[Sec.~1.4]{Gardenfors2000a}. 
<!-- 
* When using CS as framework for a scientific theory, the geometrical/topological structures of the dimensions are chosen by the scientist. The choice of that brings along \q{the *measurement methods* employed to determine the values on the dimensions} (p21)
* When, however, dealing with a *phenonemal* CS, the dimensions have to be infered from the subject's introspection. A good method for that is MDS, introduced by Gärdenfors himself \cite[Sec.~1.7]{Gardenfors2000a}, but \cite[Sec.~6.5]{Gardenfors2000a} he also suggests ANN-based embedding (specifically self-organizing maps.)
-->

So far, the area of application for CS has been small. \cite{Alshaikh2020} say \q{they are commonly used in perceptual domains, e.g. for music cognition [Forth et al., 2010; Chella, 2015], where quality dimensions are carefully chosen to maximize how well the resulting conceptual spaces can predict human similarity judgements} (another music domain example \cite{Schockaert2011}).

Standard problem is that they would have to be manually generated, which of courses is a lot of work, which is where the work of \textcite{Derrac2015} comes in - to generate them in a data-driven fashion.



In any case, we often map regions in the high-dimensional space to point-embeddings, however according to \cite[222]{Gardenfors2000a} that's a feature not a bug because that is GENERALIZATION.


### Okay, let's get to \textcite{Derrac2015}

Like we said, \cite{Gardenfors2000a} said "Dimensionality Reduction from the high-dimensional input (neurons) eg using MDS into a euclidian space, and then geometric reasoning on that" 

The work of \cite{Derrac2015} is great because it basically does what Gärdenfors suggested using classical AI algorithms, and \cite{Ager2018} and \cite{Alshaikh2020} provided some useful additions for it without changing the main logic. So, we'll work with their algorithm, also only making small improvemenents. So the two main areas of work are implementing the original algorithm, and changing small details of it where most appropriate such that it works well for the domain we're interested in.

* Important Features: 
    * Unsupervised, data-driven (in contrast to \cite{VISR12})
    * Modular (subcomponents may be exchanged)
    * Optimized to "look good to humans" (no straight-forward metrics or obvious evaluations)
    * The result is a "feature-based representation"

#### The algorithm

\cite{Alshaikh2020}: "Their core assumption is that words describing semantically meaningful features can be identified by learning for each candi- date word w a linear classifier which separates the embed- dings of entities that have w in their description from the oth- ers. The performance of the classifier for w then tells us to what extent w describes a semantically meaningful feature"

Base idea: unsupervisedly use the text descriptions belonging to the respective entities to identify semantic features from than that may serve as feature direction.

The authors look at three different domains: movies, wines and places. For each of these domains, they collected many samples (like movies) together with descriptions from places where people can leave them (like reviews from IMDB). A representation of a movie is then generated from the bag-of-words of the descriptions of the individual movies, leading to a very high-dimensional, very sparse representation for all movies. 

To make the representations less sparse and more meaningful, the words in the BOW are subsequently PPMI-weighted, which weights words that appear often in the description of a particular movie while being infrequent in the corpus overall higher while setting the representation of stopwords to almost zero (in accordance with \cite{Turney2010}).

This PPMI-weighted BOW is however not yet a euclidian space yet, which is why the authors subsequently use multidimensional scaling (MDS). MDS is a diminsionality reduction technique that attempts to create a euclidian space of lower dimensionality than the original one in which the individual distances of the items are preserved as well as possible. 

With such a space, the concepts of betweeness already makes sense, but so far, the dimensions are not interpretable. So how does one automatically find such directions? In the case of movies, good dimensions may be "scariness", "funniness", "epicness", "family-friendlyness" etc. 

To find these dimensions, the authors look for these words (as well as similar words thanks to clustering) in the reviews. 

Core assumption then is that 1) words/phrases describing semantically meaningful features appear in the text, and 2) words that describe meaningful features correlate with good performances of classifiers separating embeddings of entities that contain that word from those that don't. (a variant of the distributional hypothesis (see Kurs week 2 notes!). 
Linear classifiers have the advantage that their orthogonal can then directly serve as feature axis. 
Thus, if those are given, feature directions can be identified by running such a linear classifier for every single word/phrase that predicts from the embedding whether the word occurs in the descriptions. The performance of the classifier is the extend to which the word describes a simantically meaningful feature, our basic directions.

So, the movies are grouped into those that contain the word often enough vs those that don't. A support-vector-machine subsquently finds a hyperplane that best divides the two groups (eg. scary and non-scary), and its quality is assessed. 

Concretely, \cite{Derrac2015} use Cohen's kappa score to assess the performance, comparing not the bare performance but rather if the ranking by distance to decision hyperplane corresponds to ranking of number of occurences of that word.
<!-- (Why is this reasonable? [Wie war das mit stopwords undso..? War das nicht in \cite{Lowe}]) -->
For details why this makes sense it is referred to \cite{Lowe}.
Each of the basic features is then associated with the normal vector of the separating hyperplane as feature directions. These are subsequently clustered (reducing the number of features), and the mean direction of that cluster is then one axis of the new coordinate basis of our new conceptual space.

 \q{The learned vectors will be referred to as feature directions [because] only the ordering induced by the dot product $d_i*e$ matters} \cite{Alshaikh2020}



\textbf{Conceptual Space in our Case = Euclidian space with interpretable dimensions}

Am ende soll rauskommen: A \textbf{feature-based representation}





 ========================================

### TODO ORDER ME SOMEWHERE

 <!-- ich kriege ein Problem - ich muss extrem oft bei required algorithms and techniques auf den algorithm vorgreifen und das macht's echt awkward (später werden wir xyz gebrauchen)..... => BASE IDEA OF THE ALGORITHM MUSS SCHON VOR DER METHODS SECTION, FOR REQUIRED ALGORITHMS, STEHEN!!! -->




### What assumptions are we dropping

* euclidian metric, feddisch. (generally, a CS is not necessarily of euclidian metric, gärdenfors brings some examples of weirder metrics/topological structures)
* The Gropuing into several low-dimensional subspaces per domain is a lot weaker: actually we'd have to embed entities into small spaces of only one domain! This is only kinda picked up again later by \cite{Alshaikh2020}
    * \cite{Alshaikh2020}: "When representing a particular entity in a conceptual space, we need to specify which domains it belongs to, and for each of these domains we need to provide a corresponding vector." 
* Modelling verbs and actions in CS is a whole new chapter, but we're disregarding that
* Modified Betweeness, not as strict but rather levels of betweeeness


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

TALK ABOUT that actually, in CS concepts (=types) are regions, BUT we have only one-instance-per, so TOKENS, so it's kiiinda reasonable that we have points! IF we would have the collection of "ALL Computer Science 1 Courses" it would be different

% Zum Thema points vs regions: [CS] where properties and concepts are represented using convex regions, while specific instances of a concept are represented as points. This has a num- ber of important advantages. First, it allows us to distinguish borderline instances of a concept from more prototypical instances, by taking the view that instances which are closer to the center of a region are more typical [9]. A second advantage is that using regions makes it clear whether one concept subsumes another (e.g. every pizzeria is a restaurant), whether two concepts are mutually exclusive (e.g. no restaurant can also be a beach), or whether they are overlapping (e.g. some bars serve wine but not all, some establishments which serve wine are bars but not all). Region based models have been shown to outperform point based models in some natural language processing tasks [41] On the other hand, using regions is computationally more demanding, and learning accurate region boundaries for a given concept would require a prohibitive amount of data. In this paper, we essentially view point based representations as coarse-grained approximations of conceptual spaces, where points correspond to fine-grained categories instead of specific instances, while convex regions are used to model higher-level categories



#### Problems with this / CS generally

* Question of how to identify and describe domains not remotely answered
* Reasioning with regions is computationally extremely demanding
* We say we're dealing with POINTS but we're constantly doing cosine similarity, isn't the important difference between points and vectors that cosine would be relevant for vectors, but euclidian(/..) distance for points?! I mean warum ist unser space metric?!

* was für teile der CS definition wir behalten und was wir droppen
    * we are only dealing with one domain (movies, placetypes, courses, ..) at a time 
        * this is like CS, but what's missing is a sort of categorization at first.. however that one is never talked about anyway
    * supposed to be regions, but we use vectors.  [TYPES are, which are MADE UP FROM TOKENS]
        * MUCH more computationally efficient
        * the domain is different than the theoretical idea of Gärdenfors - especially stuff like movies and courses, what ARE they? are they type or token? Rather both at once - the region of the course XYZ is composed of only one token, at least until we take into account a much bigger dataset that would allow us to do reasoning on "the set of all introductory computer science courses" or something. (For placetypes however we ARE dealing with types!) 
    * we ARE dealing with a mostly metric space	
        * ..however we use cosine distance instead of euclidian


