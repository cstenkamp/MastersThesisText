
Throughout the development of this, the focus shifted strongly from quickly-generating-results to the methodology for a scalable architecture
	* "Meine Ausgangsfrage war ob man die Methoden von diesem einem Paper auf educational resources anwenden kann um regelmäßigkeiten zu finden für recommendations für educational resources. Um das rauszufinden war es wichtig den Algorithmus zu entwickeln, und im verlauf der thesis ist rausgekommen das ein system dafür zu entwickeln sehr komplex ist (...dass dafür halt eine solide Software-Grundlage gegeben sein muss), also ist diese thesis primär dafür da um das system zu beshcreiben um dann mit diesem system prototypisch die fragestellung anzugehen, und die results für die originalfrage sind dann eher als priliminary results zu betrachten"
	* "der Algorithmus den ich da gesehen habe ist ganz nice, das wäre doch cool wenn der so modular und reproduzierbar undundund wäre dass jemand wie ich ankommen kann und den auf andere Datensätze schmeißen kann, aber leider sind die bei open source/open data/details nennen leider nicht so super, so I'm making that instead - the delivarable is a scalable, modular, ... system that makes it easy to exchange components of it, has many analysis-scripts, etc etc etc"
	* This is a Replikationsstudie
		* strong focus on architecture, so I'll also write a lot about the architecture and details that are important for those that really want to work with the algorithm.
		* I'll sanity-check my and their results by also throwing my pipeline on their dataset

But in any case, the two stated goals are thus:

1) Implement a scalable (reproducible, understandable, ..) software-architecture that can be used to easily apply the algorithm to new domains
2) As an exemplary usecase for that, figure out if the Methodik of the paper (the algorithm) works and is useful for the domain of educational resources 
	* ...to find regularities for explainable and smart (based on user input and feedback) recommendation
	* ..and also provide some additions to the algorithm such that it works on datasets that are not specifically curated for this algorithm (my contribution is more than just re-develop something existing exactly)

<!-- Interpretable Dimensions for Courses
* Is the paper any good?
* Can that be done with our data? -->

### (1) would be achieved if


* We can recreate the Results from \mainalgos
	=> So we will: Use their datasets as well.

* We would conduct proper science when creating this, meaning we'll ensure that the pipeline fulfills the criteria for that. These are: <Reproducibility Stuff>


#### Reproducibility and Sustainability
\label{sec:reproducibility}
Or: How I plan to ensure the code I'm writing is good

Reproducibility is the pinnacle of open Science - while there's no single definition of the term, it's almost part of the definition\footnote{See for example \url{https://www.talyarkoni.org/blog/2019/07/13/i-hate-open-science/}, accessed at date{2022}{03}{25}}. And \q{Open Science is just science done right}\footnote{Quote from John Tennant, see \eg https://soundcloud.com/tidningen-curie/jon-tennant-open-science-is-just-science-done-right}, accessed at date{2022}{03}{25}}. Reproducibility means the Ability to reproduce - computationally or experimentally - the methods used to produce a given result, by virtue of being accessible and understandible.

Reproducibility a hot topic since the reproducibility crisis\footnote{Baker M: 1,500 scientists lift the lid on reproducibility. Nature. 2016; 533(7604): 452–4. \url{https://www.nature.com/articles/533452a}}, but the topic is just es relevant in research revolving around computer science \footnote{Mesirov JP: Computer science. Accessible reproducible research. Science. 2010; 327(5964): 415–6. \url{https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3878063/}}. In that realm, Reproducibility may be seen as sub-goal of (the more fundamental) Sustainability, as \eg by \textcite{Molder2021a}\footnote{\q{reproducibility alone is not enough to sustain the hours of work that scientists invest in crafting data analyses}, \cite{Molder2021a}}, whose hierarchy of aspects to consider for sustainable data analysis is reprinted as \autoref{fig:snakemake_aspect_hierachy}.

\begin{figure}[H]
	\centering
	\includegraphics[width=0.7\textwidth]{graphics/stolenfigures/snakemake_aspect_hierachy.png}
	\slcaption{
		Hierarchy of aspects to consider for sustainable data analysis. Reproduced from {\cite[Fig.1]{Molder2021a}} (Creative Commons Attribution License) \label{fig:snakemake_aspect_hierachy}
	}
\end{figure}

Some important aspects to conduct proper (computer) science and data analysis that allows for \textbf{Sustainability} (such that the analysis is of lasting impact), may thus be \cite{Molder2021}:

\begin{description}
	\item[Reproducibility] \ie allowing validation and regeneration of results on the original or even new data. Requiring understandable and well documented code.
	\item[Adaptability] \ie the ability to modify the analysis to answer extended or slightly different research questions.
	\item[Transparency] \ie the ability for others to understand it well enough to judge if it's technically as well as methodologically valid.
	\item[Scalability] \ie enabling the scalable execution of the algorithm and each involved step, including deployment on complex compute clusters, grids or clouds. 
\end{description}

Important subgoal to achieve these: Modularization and allowing components of the pipeline to easily be exchanged and extended



#### How to replicate

<!-- Ja, das hier sollte drin sein, ich geh in methods:datasets drauf ein -->

\label{sec:howtoreplicate}

See \url{https://cs.carleton.edu/cs_comps/1920/replication/index.php}: The paper states there is problem X, makes a claim that algorithm Y may be good at problem X, create datasets Z for X, and then test the code on these datasets. 
* In that test we...
	* compare it to alternative approaches to see if it's a good choice
	* explore if we can see regularities from our algorithm (like what kinds of samples we are good at vs which we are not good yet) 
		* this yields future research opportunity, showing for which other domains the algorithm may also be a good choice 

What we want to do just that: apply an existing algorithm to another domain.
* Replicating other's work and seeing if its results are valid and it works on multiple (and, importantly, on non-artificial and non-specifically-created-and-curated-just- to-test-this-algorithm ones) datasets is important! See Repeatability Crisis in Psychology!
* Often, the details of experiments in published work are opaque, and sometimes important information for reproducing the work in not included. 
  => Repeating helps
  	* investigating the robustness of the algorithm to changes in parameters or dataset: If the exact parameters used have major impacts on the results or the same approach on a different dataset produces very different results, it suggests that caution should be used in generalizing the results!




It is absolutely crucial for science to ensure that all claims that are made are reproducible and testable. This thesis mostly replicates existing research, and doing so should not have been as much work as it was. Also, while replicating, some Questionable Research Practices came apparent, such as the authors neither publishing their code\footnote{Or referencing a repository that is empty since it's creation in 20XX (\todoparagraph{URL})}, nor being unambiguous about details of their algorithm in their description\footnote{Such as the question about which kappa, and which kappa-weights, and also the \q{MDS trained with the angular differences between the PPMI weighted BoW Vectors}, vs (whatever other thing) elsewhere}, which required a lot of unnecessary trial and error. Or, even opening their data, only doing that only in a form that does not allow for comparison (see datasets-section), or cherry-picking their qualitative analysis (See \todoparagraph{Ich hab irgendwo aufgeschrieben das wievielte Beispiel einer ihrer plots war} (hing es zusammen mit "Paperlesen und den cluster von "pub" für placetypes angucken"?))


So one main motivation is to reproduce the code for the paper I liked in a way that adheres to the aforementioned principles, such that others that find it interesting don't have to go through the shit I had to go through.

Principles of open science are very important to me, so I want to ensure that the claims I am making in this thesis are backed by code that is scalable, reproducible, modular, easily-understood, easily set up and run, well documented, ... . To support this, I will as often as necessary refer to the actual code in this thesis, to allow to understand and reproduce the claims and results, and also highly encourage to critically read everything here and check the respective code (...and let me know if you spot any errors! Just open a Github Issue!)


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

