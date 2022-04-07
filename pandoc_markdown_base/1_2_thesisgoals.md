
But in any case, the two stated goals are thus:

1) Implement a scalable (reproducible, understandable, ..) software-architecture that can be used to easily apply the algorithm to new domains
2) As an exemplary usecase for that, figure out if the Methodik of the paper (the algorithm) works and is useful for the domain of educational resources 
	* ...to find regularities for explainable and smart (based on user input and feedback) recommendation
	* ..and also provide some additions to the algorithm such that it works on datasets that are not specifically curated for this algorithm (my contribution is more than just re-develop something existing exactly)
	* we are interested in if the dataset is different and if we have to do things differently (evaluation metrics wird detallierter in diesen Punkten, also wie ist das technisch umgesetzt was ich hier frage, wie kommt man dahin dass man über die fragen ne aussage treffen kann, wie quantifizier ich stuff)

<!-- Interpretable Dimensions for Courses
* Is the paper any good?
* Can that be done with our data? -->

### (1) would be achieved if


* We can recreate the Results from \mainalgos
	=> So we will: Use their datasets as well.

* We would conduct proper science when creating this, meaning we'll ensure that the pipeline fulfills the criteria for that. These are: <Reproducibility Stuff>


<!-- also make the data available somewhere open! -->



### (2) would be achieved if


Fragestellung: "Kann man X auf educational resources anwenden". To answer this question, we'll be stringent and explicit: This is my hypothesis, these are my methods, this my results, this my conclusion! 

* Hard to objectively and quantiatively evaluate without a study, so we'll also need to find good surrogate metrics
* The semantic directions are convincing
	* For example: Stuff like the Faculty would be among the detected semantic directions [->IN RESULTMETHODS: can be shown using shallow decision-trees]
	* For example: <other thing that I show later in the results>
	* For example: <other thing that I show later in the results>
* The semantic directions can be used as basis for explainable recommenders
	* Shallow Decision-Trees achieve a similar performance than ANN techniques when trying to find human categories like faculty or DDC from this [->IN RESULTMETHODS: can be shown by comparing results with classifier]

* Movie Tuner interface? (here or [*])

* We will be able to figure out if the dataset that this algorithm is thrown own must have certain properties in order for it to work -> we must also look at differences in the dataset




<!-- Figure [*]:  -->
\begin{figure}[H]
	\centering
	\includegraphics[width=0.7\textwidth]{graphics/stolenfigures/movietuner.png}
	\slcaption{
		The Movie-Tuner Interface from \cite{VISR12} %TODO: cite exact figure (" … as seen in [8, Fig. 33]")
		\label{fig:movetuner}}
\end{figure}

