
Research Question: Ich will die Methodik von dem Paper auf educational resources Applien. Das unbedingt in discussion & conclusion aufgreifen.


% Ich habe schon eine eindeutige Fragestelleung ("Kann man X auf educational resources anwenden") -> danach stringent und explizit vorgehen! Das ist meine Hypothese, these are my methods, this my results, this my conclusion! 

\begin{figure}[H]
	\centering
	\includegraphics[width=0.7\textwidth]{graphics/stolenfigures/movietuner.png}
	\slcaption{
		The Movie-Tuner Interface from \cite{VISR12} %TODO: cite exact figure (" … as seen in [8, Fig. 33]")
		\label{fig:movetuner}}
\end{figure}

\subsection{Open Science and Reproducibility}

\label{sec:reproducibility}

% Im Snakemake-Paper https://f1000research.com/articles/10-33/v2 und auf deren startseite https://snakemake.github.io/ hauen sie einige buzzwords raus!
% Mariellas Präsi nochmal angucken
% Explainable AI!! 

from \cite{Molder2021a}: 

\begin{description}
	\item[Reproducibility] allowing validation and regeneration of results on the original or even new data. Requires understandble and well documented code.
	\item[Sustainability] such that the analysis is of lasting impact for the field, not just one research grouped
	\item[Adaptability] i.e. the ability to modify the analysis to anwer extended or slightly different research questions
	\item[Transparency] i.e. the ability for others to understand it well enough to judge if it's technically as well as methodologically valid.
	\item[Scalability] - 
\end{description}

\begin{figure}[H]
	\centering
	\includegraphics[width=0.7\textwidth]{graphics/stolenfigures/snakemake_aspect_hierachy.png}
	\slcaption{
		Hierarchy of aspects to consider for sustainable data analysis. Reproduced from {\cite[Fig.1]{Molder2021a}}. \label{fig:snakemake_aspect_hierachy}
	}
\end{figure}


I think it is absolutely crucial for all branches of science to adhere to the principles of open science and to ensure that all claims that are made in publications are reproducible and testable. This thesis will mostly copy the work of somebody else, but doing so was incredibly tedious, much more so than it would have to be.

Dabei ist mir aufgefallen dass die schon einige DInge machen die ich aus wissenschaftlicher Sicht für ziemlich kritikwürdig halte, zum Beispiel sind die so schwammig in den Formulierungen dass man beim Versuch den Code zu reproduzieren echt viel raten muss, haben geschrieben dass der Code open ist verweisen aber auf ein leeres Repo, haben ihre Daten veröffentlicht aber wenn man damit arbeitet merkt man dass das die selbst definitiv nicht mit dem Datensatz den sie veröffentlicht haben gearbeitet haben könne, sind sehr hart am cherry-picken in ihrer qualitativ  analysis etc etc et

So one main motivation is to reproduce the code for the paper I liked in a way that adheres to the principles of open science, such that others that find it interesting don't have to go through the shit I had to go through.

Principles of open science (TODO: which are: [see thisandthis paper]) are very important to me, so I want to ensure that the claims I am making in this thesis are backed by code that is scalable, reproducible, modular, easily-understood, easily set up and run, well documented, ... . To support this, I will as often as necessary refer to the actual code in this thesis, to allow to understand and reproduce the claims and results, and also highly encourage to critically read everything here and check the respective code (...and let me know if you spot any errors! Just open a Github Issue!)

% TODO: also make the data available somewhere open!



=======================================================================================================================
===================================================== FROM NOTION =====================================================
=======================================================================================================================




Probleme: 

Evaluation? (Non-Qualitative): Entweder ich nutze gewisse Daten (Studiengangs-Zugehörigkeit) nicht zum trainieren sondern nur zum vergleichen, dann hat das ganze wenig praktischen Nutzen, oder ich nutze sie, dann kann es zwar besser sein aber ist Scientifically nicht evaluiert (außer mit ner Big Study which I kinda don't want to do)

Wenige Paper so far (und alle sind halt von Schockeart)


=======================================================================================================================
===================================================== FROM NOTION =====================================================
=======================================================================================================================



RESEARCH QUESTON(s)
Interpretable Dimensions for Courses
* Is the paper any good?
* Can that be done with our data?
* How does it compare to user judgement?


Features
* Be able to enable/disable or select between all components
	Like...
	- [ ]  the contribution of [AGKS18] or [ALBS20]
	- [ ]  which classifier to use to split positives and negatives in step 1 (SVM, logistic regression)
	- [ ]  Cohen's Kappa vs Accuracy vs NDCG
	- [ ]  Kmeans vs [DESC15]'s clustering-algorithm
	- [ ]  how to create semantic space(step 0) (MDS, PCI, Doc2Vec, Average GloVe ([https://nlp.stanford.edu/projects/glove/](https://nlp.stanford.edu/projects/glove/))
* Hyperparameters
	- [x]  #dims of the vector-space (50,100,200)
	- [ ]  #dims as input to the clustering algorithm (500,1000,2000)
	- [ ]  number of clusters (1*inputdimsforclusalgorithm, 2*inputdimsforclusalgorithm)
* Extracting Candiate Terms
	- The way of DESC15
	- The way I'm doing it right now
	- The Tag-LSI-Sim as [VISR12] do it (page 13:15)
	    [[VISR12] have the Tag-LSI-SIM, die brauch ich](https://www.notion.so/VISR12-have-the-Tag-LSI-SIM-die-brauch-ich-0868f6c7a20147f582029163f39c225e)