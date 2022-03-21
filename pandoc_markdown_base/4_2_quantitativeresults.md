
% Schreiben was die paper denen ich mostly folge zur evaluation gemacht haben! ("To evaluate whether the discovered features are semantically meaningful, we test how similar they are to natural categories, by training depth-1 decision trees")
% Ein anderer Weg zum testen wäre auch ein classifier der nur anhand der most salient generated features versucht den kurs wiederherzustellen (das zeigt natürlich nicht ob es similar to how humans do it but part of it)

Here I'll add the results of the low-depth-decision-trees for Fachbereich, and also compare the results of throwing my code onto their placetypes-dataset and how my results compare to theirs 
(set overlap of candidate terms!)

To see if it is possible to extract any kind of structured data from the unstructured course descriptions, a Neural Network classifier was trained on the dataset, classifying courses to the faculty they run under. 
$\rightarrow$ Der FB-Classifier kommt auf $95.33\%$ train, $90.96\%$ Test accuracy nach 10 epochs, that's a lot!!


Both \cite{Ager2018} and \cite{Alshaikh2020} train shallow decision-trees (depth 1 and depth 3 each), on their feature-based representations (such that the 1 or 3 most distinct interpretable dimensions are used) on a known property of the data (genres for movies, category in some taxonomy for placetypes, fachbereich for mine) - in the assumption that these eg in the movie domain the genre (or rather *terms accurately predicting it*) is among the features.


TODO die Plots mit den Boxen von display_desc15_top3.ipynb !!!

\begin{itemize}
	\item result: set overlap of my extracted candidates for placetypes and theirs (und auch die big_21222.yml ergebnisse danach auswerten) (nicht nur overlap, ich kann auch verhältnis set intersect zu set union machen, und die als true/false positive/negative deklarieren und dann accuracy, f1 etc analysieren und halt anhand dessen "die hyperparam kombi die am closesten zu deren ergebnissen ist" rausbekommen)
	\item result: kommt accuracy etc von den shallow decision trees für fachbereich close an die vom fb-classifier?
\end{itemize}