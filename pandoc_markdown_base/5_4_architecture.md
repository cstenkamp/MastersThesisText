## Results regarding the Implementation and Goals for the architecture (in terms of architecture quality)
<!-- Eine meiner 2 research questions ja war "wie sieht eine gute architecture aus", so if the architecture is good and how it (and thus a good architecture) looks are results!! -->

First of all, we wanted to show that 

* this implementation works
* the results of \mainalgos are not a fluke (that the algorithm works at all)

The results on placetypes have shown that that's the case.


We remember, we also wanted to build a good architecture and set goals for that, such as adaptability to new datasets etc. We said a good architecture would show in adaptability, scability, ..., so we wanna show that these are achieved. 

* We are scalable and can run massively parallel (that you'll have to believe me, it's one command to run on the grid and I would say that's pretty noice).
* Keep in mind when reading the other sections of the results that all plots and tables you'll see are explictly linked and easily re-creatable and runnable
* We ran the stuff on other datasets\footnote{See Table with datasets and the respective notebooks and the quick datasets section} and it ran through, so we're adaptable.
    *  wie schnell es geht den bums auf neue datasets zu werfen (100k coursera, 90k short stories, ...) und dass ich damit schon angefangen hab 

* dass sowohl die architektur hierfür, als auch meine Grid-solutions eine major contribution sind die sich sehen lassen können!
* Development was really easy as soon as the architecture did what it should so yes, future work will be made a lot easier, our goal of "Make a good architecture" (see \autoref{sec:goals_research_questions} is fulfilled.)

* Adding new param-kombis including stuff from ager was really easy, add the code, add the config to the yaml, run ` MA_ENV_FILE=siddata.env submit -kwr by_config --configfile config/derrac2015_edited.yml --keep-going`, kabams.

* It was SUCH a pain to bring snakemake where it is now, but now its really helping

IN 3_3_architecture is a section "My workflow to generate results", darauf nochmal eingehen und sagen dass das wirklich wunderbar funktioniert, dass es am ende nur ein wenig chaotisch ist weil man darauf achten muss dass man consistent ist in den conditions für best-config (random seed für die decision trees undso)

## Soo lets look at our success conditions

* The results of \cite{Derrac2015} and its follow-up works \cite{Ager2018,Alshaikh2020} can be replicated for at least one of their original datasets
* The architecture sucessfully runs on the compute grid, indicating scalability and modularity.
* The criteria for software quality as specified in \textbf{ISO 25010} and open science are fulfilled.
* The code is open-sourced, well-documented and understandable.