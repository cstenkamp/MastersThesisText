
## Ways of quantiative analysis:

* Inter-Cluster and Intra-Cluster-distances
	* Also, are the word-embeddings of words INSIDE cluster significantly closer than those outside?
		* or even significantly close in only certain vector-elements of the embedding?
* does it cluster such that the Faculty is reconizable
* Can we get Faculty from shallow decision-trees
	* Both \cite{Ager2018} and \cite{Alshaikh2020} train shallow decision-trees (depth 1 and depth 3 each), on their feature-based representations (such that the 1 or 3 most distinct interpretable dimensions are used) on a known property of the data (genres for movies, category in some taxonomy for placetypes, fachbereich for mine) - in the assumption that these eg in the movie domain the genre (or rather *terms accurately predicting it*) is among the features.

	* Ich hab ja den Fachbereichs-Classifier gemacht, wenn ich jetzt noch die shallow decision trees mache kann ich ja legit accuracies vergleichen !!
		* To see if it is possible to extract any kind of structured data from the unstructured course descriptions, a Neural Network classifier was trained on the dataset, classifying courses to the faculty they run under. $\rightarrow$ Der FB-Classifier kommt auf $95.33\%$ train, $90.96\%$ Test accuracy nach 10 epochs, that's a lot!!
		==> CORRECTION: auf Siddata2022 kommt er auf $85.19\%$ test, $94.13\%$ train, siehe \todoparagraph{link to notebook}
		* kommt accuracy etc von den shallow decision trees für fachbereich close an die vom fb-classifier?
	* "Here I'll add the results of the low-depth-decision-trees for Fachbereich"
	* notebooks/analyze_results/display_siddata_decisiontrees.ipynb does that 
		* TODO: die BESTE Parameter-kombi dafür rausfinden
		* TODO: für ALLE configs die level-1-decisiontrees machen und die terms des jeweils-entscheidenen-clusters collecten
* Can we get DDC from shallow decision-trees
	* notebooks/analyze_results/display_siddata_decisiontrees.ipynb does that 
		* TODO: write in Dataset-section where these DDCs come from
			* file: Masterarbeit/OTHER/study_behavior_analysis/EducationalResource-2022-01-20.csv
			* TODO: cite Johannes' Siddata/SidBert-Paper !

* die Plots mit den Boxen von display_desc15_top3.ipynb !!
