

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
