<!-- 
So far, we established  that Conceptual Spaces are a good framework for that. The part that's missing is the automatic generation. 

### Mehr vorgeplänkel


So we have established that there is a distinction between phenonemal and scientific interpretations of CS \cite[Sec.~1.4]{Gardenfors2000a}. 

* When using CS as framework for a scientific theory, the geometrical/topological structures of the dimensions are chosen by the scientist. The choice of that brings along \q{the *measurement methods* employed to determine the values on the dimensions} (p21)
* When, however, dealing with a *phenonemal* CS, the dimensions have to be infered from the subject's introspection. A good method for that is MDS, introduced by Gärdenfors himself \cite[Sec.~1.7]{Gardenfors2000a}, but \cite[Sec.~6.5]{Gardenfors2000a} he also suggests ANN-based embedding (specifically self-organizing maps.)


 small. \cite{Alshaikh2020} say \q{they are commonly used in perceptual domains, e.g. for music cognition [Forth et al., 2010; Chella, 2015], where quality dimensions are carefully chosen to maximize how well the resulting conceptual spaces can predict human similarity judgements} (another music domain example \cite{Schockaert2011}).


Standard problem is that they would have to be manually generated, which of courses is a lot of work, which is where the work of \textcite{Derrac2015} comes in - to generate them in a data-driven fashion.




### Okay, let's get to \textcite{Derrac2015}

Like we said, \cite{Gardenfors2000a} said "Dimensionality Reduction from the high-dimensional input (neurons) eg using MDS into a euclidian space, and then geometric reasoning on that" 

and \cite{Ager2018} and \cite{Alshaikh2020} provided some useful additions for it without changing the main logic. So, we'll work with their algorithm, also only making small improvemenents. So the two main areas of work are implementing the original algorithm, and changing small details of it where most appropriate such that it works well for the domain we're interested in.


#### The algorithm

\cite{Alshaikh2020}: "Their core assumption is that words describing semantically meaningful features can be identified by learning for each candi- date word w a linear classifier which separates the embed- dings of entities that have w in their description from the oth- ers. The performance of the classifier for w then tells us to what extent w describes a semantically meaningful feature"


Base idea:



With such a space, the concepts of betweeness already makes sense, but so far, the dimensions are not interpretable. So how does one automatically find such directions? In the case of movies, good dimensions may be "scariness", "funniness", "epicness", "family-friendlyness" etc. 



Core assumption then is that 1) words/phrases describing semantically meaningful features appear in the text, and 2)  (a variant of the distributional hypothesis (see Kurs week 2 notes!). 
Linear classifiers have the advantage that their orthogonal can then directly serve as feature axis. 
Thus, if those are given, feature directions can be identified by running such a linear classifier for every single word/phrase that predicts from the embedding whether the word occurs in the descriptions. The performance of the classifier is the extend to which the word describes a simantically meaningful feature, our basic directions.

So, the movies are grouped into those that contain the word often enough vs those that don't. A support-vector-machine subsquently finds a hyperplane that best divides the two groups (eg. scary and non-scary), and its quality is assessed. 

Concretely,  score to assess the performance, comparing not the bare performance but rather if the ranking by distance to decision hyperplane corresponds to ranking of number of occurences of that word.
<!-- (Why is this reasonable? [Wie war das mit stopwords undso..? War das nicht in \cite{Lowe}]) 
For details why this makes sense it is referred to \cite{Lowe}.
Each of the basic features is then associated with the normal vector of the separating hyperplane as feature directions. These are subsequently clustered (reducing the number of features), and the mean direction of that cluster is then one axis of the new coordinate basis of our new conceptual space.

 \q{The learned vectors will be referred to as feature directions [because] only the ordering induced by the dot product $d_i*e$ matters} \cite{Alshaikh2020}



\textbf{Conceptual Space in our Case = Euclidian space with interpretable dimensions}

Am ende soll rauskommen: A \textbf{feature-based representation}


* Important Features: 
    * Unsupervised, data-driven (in contrast to \cite{VISR12})
    * Modular (subcomponents may be exchanged)
    * Optimized to "look good to humans" (no straight-forward metrics or obvious evaluations)


-->

<!-- 

#### Problems with this / CS generally

* Question of how to identify and describe domains not remotely answered
* Reasioning with regions is computationally extremely demanding

-->

