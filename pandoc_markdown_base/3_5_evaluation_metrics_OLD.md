
<!-- Hier: WAS interessiert mich und WARUM -->
<!-- This section explains what kind of results I'm gonna generate in the next chapter and why I'm interested in them. Bc it's not classification, we'll have to think of our own metrics (come up with tricks).  -->

Two goals were stated in this thesis' introduction: To implement a reliable software-architecture that successfully replicates the works of \textcite{Derrac2015}, and figure out if their methodology also works for the domain of educational reasources. Given that there is not one single correct target that the algorithm needs to optimize for, there are also no obvious quantifiable metrics that can be applied straight-forward to test the performance of the algorithm. Instead, one has to rely on qualitative analysis of certain produced features as well as proxy metrics. This section explains what kind of results have been chosen to represent the algorithm's performance as well as why these results are suitable proxies.

<!-- What we can do in order to quantitatively evaluate is to check if the detected features are any good is to check if known qualitative features / categories (as eg the Faculty) can be easily predicted from them. -->

As we also wanted to test the architecture itself, we'll run our code for Placetypes as well and check if our results are consistent with those of the literature.

**Main questions we want to answer:**

(hinleitung vom generellen "thesis goal" zu konkreten measruable sachen)

* Implementation correct?
* Dataset comparisons (features that the algorithm produces)
* Does the Methodik work on the Domain?
* Best Parameters?
(* Architecture blub)

## How do we know what we do is good?  (What are we interested in, whay may good results be?)

* Are (terms acccurately predicting) important human concepts among the detected features? 
    * \cite{Derrac2015} do many different interpretable classifiers (see [THAT SECTION])
        * \cite{Derrac2015} evaluated using a bunch of commonsense reasoning based classifiers (want to show that at least as performant than standard approaches, but can give intuitive explanations) (these reasoning-classifiers can be linked to intuitive explanations: 1-NN is "Y is of the same class as X because X closest to Y", but also more complex ones.) 
        * DESC15 "evaluate the practical usefulness of the considered semantic relations" by checking "their use in commonsense reasoning based classifiers", like interpolation and a fortiori inference (chap 5)
        * Section 6.1: Evaluate whether the derived relations are sufficiently accurate for classification, and 6.2 is then comparison with crowdsourcing experiments (more subjective aspects, the question “are the relations useful explanations?”)
    * Both \cite{Ager2018} and \cite{Alshaikh2020} train shallow decision-trees (depth 1 and depth 3 each), on their feature-based representations (such that the 1 or 3 most distinct interpretable dimensions are used) on a known property of the data (genres for movies, category in some taxonomy for placetypes, fachbereich for mine) - in the assumption that these eg in the movie domain the genre (or rather *terms accurately predicting it*) is among the features, we will do that too. Grains of salt:
        *  GRAIN OF SALT: dass sie nie erwähnen ob sie bei den shallow decision trees one-vs-rest machen --> HOW DID THEY achieve even okay-ish accuracies with the shallow decision-trees? a depth 3 tree has max 2^3 = 8 leaves, so if your to-be-categorized has 100 classes, you'll definitely suck!
            * read https://machinelearningmastery.com/one-vs-rest-and-one-vs-one-for-multi-class-classification/ wegen one-vs-all undso
        * This only checks a subset (like that would be 10 important features, but what about the other 190?) 
        * This doesn't test if the names of the direcitons are good
        * decision tree based on their features, check if it can classify a held out test dataset
        * "To evaluate whether the discovered features are semantically meaningful, we test how similar they are to natural categories, by training depth-1 decision trees"
        * My Argumentation that the way Ager & Alshaikh report their accuracies it must be the case that they did that per class (see also Slack with Johannes!)
        * Faculty
            * does it cluster such that the Faculty is reconizable (->Fig 4.1) (`notebooks/analyze_results/siddata/decisiontrees_bestconfig.ipynb`)
            * Can we get Faculty from shallow decision-trees (like \cite{Ager2018,Alshaik2020}) (->Fig 4.2)
            * is that able to compete with state-of-the-art classification algorithms? "To see if it is possible to extract any kind of structured data from the unstructured course descriptions, a Neural Network classifier was trained on the dataset, classifying courses to the faculty they run under. Accuracy of that: (WO WAR DAS?!)"
        * DDC
            * decision-trees for that (`notebooks/analyze_results/siddata/decisiontrees_bestconfig.ipynb`)
            * TODO: schaff ich's level 2 davon auch zu machen wie \cite{Alshaikh2020}?

* Can we recover courses from the detected direcitons?
    * for that, we train unbounded decision trees without a train/test-split and check if the prediction can recover
    * "Ein anderer Weg zum testen wäre auch ein classifier der nur anhand der most salient generated features versucht den kurs wiederherzustellen (das zeigt natürlich nicht ob es similar to how humans do it but part of it) -> recover_course_from_embeds.ipynb"


## Scientific Qualitative Analysis: Before looking at the data, i I saw what kinds of results I would assume it's doing something right: 

* Qualitative Analysis in this case means "looking at stuff". Such a qualitative analysis is always to be taken with a grain of salt, because it is very prone to cherry-picking (both on purpose and not on purpose, the stuff you're looking at just doesn't need to be representative!). However it does help a lot and provides a lot of insights (and often helped me in the debugging process).
* Are the words in clusters similar 
	* if things you know to be similar are actually in the same clusters
	* in the "scary" cluster, is there also often something like "horror" or "gore"?
	* in courses that would be "A1" and "A2", both hinting at langauge courses 
		* OLD RESULTS didn't show that => Distance-threshold small: no clusters at all; threshold high: "A1" is in a cluster with "course", which makes it useless
    * "A1" and "A2" cluster
    * Gibt's ne Direction für Corona-Kurse? "FÄLLT AUS"?? 
        * Kann ich nicht doch das Jahr benutzen? Und daran erkennen was die 202Xer sind ob "FÄLLT AUS" drin vorkommt?
* Are words that I would LIKE to be semantic directions actually semantic directions? ("computer", "mathe", ..)  (corresponding to math-y courses and informatik-y courses)
* Check if the 3D-embeddings are only a ball -> if so, the SVM may be no good
* Inter-Cluster and Intra-Cluster-distances
	* Also, are the word-embeddings of words INSIDE cluster significantly closer than those outside?
		* or even significantly close in only certain vector-elements of the embedding?



* If descriptions you know to be semantically similar are actually close in the embedding
    * You can do the whole thing for only three dimensions instead of the 50/100/200 because there you can plot the stuff and interpret it  (->Refer to the section BEFORE if in 3D close stuff is supposed to be close)
* Sanity Checks
	* dass ich ja in 3D gucken kann (und auch in höher-D ausrechnen) ob eben dinge like "airplane cabin" und "aircraft cabin" im Embedding nah sind, und ob die SVM Dinge schön trennt ("howto_embed.ipynb")
	* Check if the 3D-embeddings are only a ball -> if so, the SVM may be no good
* Spezielles
	* Ist "Codierungstheorie und Kryptographie" - mathe = "Kryptographische Methoden in der Informatik"?
	* Does the continuation thingy which they have (backtothefuture:backtothefutureII::terminator:terminator2) hold for courses as well - Verhält sich Informatik A zu Informatik B wie Mathe für Anwender 1 zu Mathe für Anwender 2?  Info B zu Info A genau wie Statistik 2 zu Statisik 1? 
* Neben den Clustern die ich mir anzeigen lassen kann und qualitativ analysieren kann, kann ich mir auch die distances to the origins of the respective dimensions (induced by the clusters), what induces the respective rankings! (see DESC15 p.24u, proj2 of load_semanticspaces.load_projections) anzeigen lassen - da kann ich sagen "term xyz ist bei "nature" am höchsten".
	* FRAGE: sind dafür ÜBERHAUPT IRGENDWIE die cluster relevant??! Ich meine es wird nur die distance zur hyperplane vom main-term considered, so why the hell even cluster?!



## What else can we look at/test? 

* Check in which direction Faculties differ (humanwissenschaften ist mehr psycho als mathe etc)
* What are the most often detected / most often occuring keywords/keyphrases (see THROWN OUT)
    * When we make a histogram counting for every keyword how many documents it appears in, we see an exponential decrease (plot: "Docs per Keyword")
* Are PPMI & tf-idf good measures to extract/detect important terms in entities? -> Look at maximums:
    * `term_doc_matrix.index[np.unravel_index(term_doc_matrix.to_numpy().argmax(), term_doc_matrix.to_numpy().shape)[0]], term_doc_matrix.columns[np.unravel_index(term_doc_matrix.to_numpy().argmax(), term_doc_matrix.to_numpy().shape)[1]]` → 'Information Systems (Wirtschaftsinformatik) M III: IT-Risikomanagement (Übung)' und 'risk'
* Inter-Cluster and Intra-Cluster-distances
	* Also, are the word-embeddings of words INSIDE cluster significantly closer than those outside?
		==> or even significantly close in only certain vector-elements of the embedding?
	    (Sowohl für MEINE embeddings, als auch einfach mal für word2vec testen)


## What do we expect in Terms of Parameters?

* Mein Datensatz ist anders als deren, so: Der Kappa-Score der rankigns vergleicht ist für mich ne kack metric weil ich ebennicht reviews nehme und more-occurences better-candidate heißen -> gucken wie ich stattdessen gute dimensionen und cluster finde (klingt doch so als sei accuracy/f1/... doch wichtig) => WE EXPECT dass accuracy/f1/... zu besseren ergebnissen führt!
* What parameter-combinations and algorithm-components are the best 
	* What are optimal parameters for Siddta-dataset
	* What are optimal parameters for placetypes-dataset
		* COMPARISON-Table mit \mainalgos
	* Der Plot wie viele candidate-words wir für welchen Kappa-Weighting-Paramter haben (backref auf meinen complain in der intro)
	* Evaluate choices of \mainalgos:
		* Regarding "binary" as quantification: As soon as "course" is in a cluster, the cluster becomes useless if you're binary  (clar.1) => Bad choice (zeigt sich das auch in den Daten)
		* Derrac2015 sagen nie warum sie PPMI over tf-idf wählen, kann ich bestätigen dass das okay so war oder performt tf-idf mindestens so gut wie ppmi?



## Sort-Me

* Explain why we care for the number-of-goodkappas in the next section argh