Thesis goals: We want to automatically generate conceptual spaces for the domain of educational resources to generate explainable recommendation. So far, we established  that Conceptual Spaces are a good framework for that. The part that's missing is the automatic generation. The work of \cite{Derrac2015} is great because it basically does what Gärdenfors suggested using classical AI algorithms, and \cite{Ager2018} and \cite{Alshaikh2019} provided some useful additions for it without changing the main logic. So, we'll work with their algorithm, also only making small improvemenents. So the two main areas of work are implementing the original algorithm, and changing small details of it where most appropriate such that it works well for the domain we're interested in.


TALK ABOUT that actually, in CS concepts (=types) are regions, BUT we have only one-instance-per, so TOKENS, so it's kiiinda reasonable that we have points! IF we would have the collection of "ALL Computer Science 1 Courses" it would be different

% \cite{Alshaikh2019} geht drauf ein warum man infoGAN und VAEs für bilder als pretty much sowas betrachten kann

%Wie funktioniert die Idee des data-driven generieren 

% Base idea: [Derrac and Schockaert, 2015] proposed an unsupervised method which uses text descriptions of the considered entities to identify se- mantic features that can be characterized as directions. Their core assumption is that words describing semantically mean- ingful features can be identified by learning for each candi- date word w a linear classifier which separates the embed- dings of entities that have w in their description from the oth- ers. The performance of the classifier for w then tells us to what extent w describes a semantically meaningful feature. 
% This method trains for each word w in the vocab- ulary a linear classifier which predicts from the embedding of an entity whether w occurs in its description. The words w1, ..., wn for which this classifier performs sufficiently well are then used as basic features. To assess classifier perfor- mance, Cohen’s Kappa score, which can be seen as a correc- tion of classification accuracy to deal with class imbalance, is used. Each of the basic features w is associated with a cor- responding vector dw (i.e. the normal vector of the separat- ing hyperplane learned by the classifier). These directions are subsequently clustered, which serves to reduce the total num- ber of features.
% Zum Thema points vs regions: [CS] where properties and concepts are represented using convex regions, while specific instances of a concept are represented as points. This has a num- ber of important advantages. First, it allows us to distinguish borderline instances of a concept from more prototypical instances, by taking the view that instances which are closer to the center of a region are more typical [9]. A second advantage is that using regions makes it clear whether one concept subsumes another (e.g. every pizzeria is a restaurant), whether two concepts are mutually exclusive (e.g. no restaurant can also be a beach), or whether they are overlapping (e.g. some bars serve wine but not all, some establishments which serve wine are bars but not all). Region based models have been shown to outperform point based models in some natural language processing tasks [41] On the other hand, using regions is computationally more demanding, and learning accurate region boundaries for a given concept would require a prohibitive amount of data. In this paper, we essentially view point based representations as coarse-grained approximations of conceptual spaces, where points correspond to fine-grained categories instead of specific instances, while convex regions are used to model higher-level categories
%...ansonsten hätte ich immernoch die frage ob wir überhaupt points consideren oder nur vektoren, UND warum wie cosine distance consideren und nicht öfter mal euclidian distance, I mean warum ist unser space metric?!


% TODO: Have to write here:
% * that in a CS the axes correspond to human concepts, "concepts" meaning attributes and what-was-the-other-again, according to CS lingo corresponding to nouns and adjectives yadda yadda, darauf referenzier ich mich im Text



* was für teile der CS definition wir behalten und was wir droppen
    * we are only dealing with one domain (movies, placetypes, courses, ..) at a time 
        * this is like CS, but what's missing is a sort of categorization at first.. however that one is never talked about anyway
    * supposed to be regions, but we use vectors.  [TYPES are, which are MADE UP FROM TOKENS]
        * MUCH more computationally efficient
        * the domain is different than the theoretical idea of Gärdenfors - especially stuff like movies and courses, what ARE they? are they type or token? Rather both at once - the region of the course XYZ is composed of only one token, at least until we take into account a much bigger dataset that would allow us to do reasoning on "the set of all introductory computer science courses" or something. (For placetypes however we ARE dealing with types!) 
    * we ARE dealing with a mostly metric space	
        * ..however we use cosine distance instead of euclidian