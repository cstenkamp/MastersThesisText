<!-- Johannes 25.3.: das "How to Evaluate" ans ende von "Methods", und "Evaluation Metrics" nennen -->

* Both \cite{Ager2018} and \cite{Alshaikh2020} train shallow decision-trees (depth 1 and depth 3 each), on their feature-based representations (such that the 1 or 3 most distinct interpretable dimensions are used) on a known property of the data (genres for movies, category in some taxonomy for placetypes, fachbereich for mine) - in the assumption that these eg in the movie domain the genre (or rather *terms accurately predicting it*) is among the features.

* warum mich die Ergebnisse die ich in der results-section generiere interessieren schon hier sagen!!
    * "in order to evaluate ... we check inhowfar our algorithm can put educational reasources to fachbereich"


* Subsection: What kinds of results I would LIKE before even looking at the data
    * "A1" and "A2" cluster
    * "math" and "computer" become candidate-directions (corresponding to math-y courses and informatik-y courses)
    * Check if the 3D-embeddings are only a ball -> if so, the SVM may be no good

* Ich kann gucken in welche Richtungen Fachbereiche sich unterscheiden (humanwissenschaften ist mehr psycho als mathe etc)


## What do we expect to see? 

* Mein Datensatz ist anders als deren, so: Der Kappa-Score der rankigns vergleicht ist für mich ne kack metric weil ich ebennicht reviews nehme und more-occurences better-candidate heißen -> gucken wie ich stattdessen gute dimensionen und cluster finde (klingt doch so als sei accuracy/f1/... doch wichtig) => WE EXPECT dass accuracy/f1/... zu besseren ergebnissen führt!
