
% ich hätte gerne sowas wie könig - mann + frau = königin \cite{Mikolov:Regularities}, nur halt mit mann und frau als einer achse

% * wie schlecht der amazon-approach wirklich ist! I mean ja, similarity-based reasoning haben sie mittlerweile sehr gut hinbekommen, aber similarity-based reasoning is the absolute basic reasoning/classification you can think of!

Dass die paar leute die in dem Bereich veröffentlichen echt aktiv sind and all und coole Ideen haben, dass die aber immer nur sich selbst zitieren (und alle auf DESC15 basieren und einen der autoren als co-author haben), und das es sinnvoll ist da mal nen sanity-check reinzubringen und als externe person die validität vom DESC15 algorithmus zu prüfen (...und dass sie ja auch alle die selben 2 datensätze nutzen und dass man eben da auch mal prüfen sollte ob deren kram so sinnvoll ist BEYOND this one dataset) - also in kurz "If this algorithm is as good as they claim, that would be great, but we have reasons to not trust their claim so we're checking them." Im Prozess dafür soll halt auch eine Pipeline rauskommen die es future research leichter macht ebengenau das zu tun was ich hier tu und die validiät der claims zu prüfen etc.

Es gibt auch arbeiten bei denen die formulierte These ein Beispiel-Anwendungsfall für die Software-Grundlage ist

in meinem Fall "Meine Ausgangsfrage war ob man die Methoden von diesem einem Paper auf educational resources anwenden kann um regelmäßigkeiten zu finden für recommendations für educational resources. Um das rauszufinden war es wichtig den Algorithmus zu entwickeln, und im verlauf der thesis ist rausgekommen das ein system dafür zu entwickeln sehr komplex ist (...dass dafür halt eine solide Software-Grundlage gegeben sein muss), also ist diese thesis primär dafür da um das system zu beshcreiben um dann mit diesem system prototypisch die fragestellung anzugehen, und die results für die originalfrage sind dann eher als priliminary results zu betrachten - fokus-shift von results zu methodik".

Das ist eine Motivation für die Thesis ganz klar ist "der Algorithmus den ich da gesehen habe ist ganz nice, das wäre doch cool wenn der so modular und reproduzierbar undundund wäre dass jemand wie ich ankommen kann und den auf andere Datensätze schmeißen kann, aber leider sind die bei open source/open data/details nennen leider nicht so super, so I'm making that instead - the delivarable is a scalable, modular, ... system that makes it easy to exchange components of it, has many analysis-scripts, etc etc etc" 
% * One of the main goals of this thesis was to create a better architecture than the shit that was available from the papers I tried to re-do here 
	% * DESC15 didn't have any code, 
	% * one of the others has a link to the repo but it's empty
	% * the last one has >40 unnamed command-line-args!)
	% * good way to bash the original paper who either didn't publish their sourcecode or link a github-repo in their paper that is fucking empty, or did at least opensource their code but have just one fucking file in there that expects >40 unnamed command-line-args

Das was ich mache ist ja eine Replikationsstudie -> Dann darf ich auch gerne diese Dinge über die Architektur undso schreiben. "Ist ja schon irgendwie ingeneurwissenschaft", dazu gehört also auch mal mehr detail wie man das gemacht hat - hängt natürlich von der gewünschten seitenzahl und dem raum den ich hab ab. In der Arbeit sollte alles drinstehen was man für die Beurteilung braucht, also quellcode oder so darf auch gerne mal im Hauptteil stehen

feature directions allow us to rank objects according to how much they have the corresponding feature, and can thus play an important role in interpretable classifiers, recommendation systems, or entity-oriented search engines, among others  [AGKS18] has many sources for these!!
	* Recommender systems (gerade critique-based ones thanks to the keyword-extraction etc)
		-> see example of [VIGSR12]
	* Semantic Search Engines (can use directions in case of gradual and possibly ill-defined features, like "popular holiday destinations")
	* Represent examples in classification tasks
	* Rule-Based Classifiers from the rankings

TODO: direkt repeatability problems ansprechen, see \url{https://cs.carleton.edu/cs_comps/1920/replication/index.php} (the paper states there is problem X, makes a claim that algorithm Y may be good at problem X, create datasets Z for X, and then test the code on these datasets. " In that test of performance, the goal is typically to identify how well the proposed algorithm works versus alternative approaches and additionally to explore what kinds of examples one's algorithm can successfully classify versus what examples it makes errors on  Future research and applications often build on these experiments, relying on their results when deciding what algorithm is most appropriate for a new task or determining whether a new algorithm is better than existing work. For instance, based on the paper above, one might conclude that to test if one has a better sarcasm detector, one need only compare against the new algorithm, since the older approach performed less well in their experiments. Yet, it's rare that people directly try to replicate other's work to confirm that the results are valid and evaluate whether the trends in the results hold in other datasets. In psychology, there has been concern in recent years that many purported psychological phenomena may be overblown, as some attempts to replicate them have been unsuccessful. While computer science experiments are not the same as psychology experiments, there is still reason to be concerned about the lack of work focused on replicating computer science experiments. Often, the details of experiments in published work are opaque, and sometimes important information for reproducing the work in not included. Replicating previous work offers the opportunity to better understand that work, and to investigate the robustness of the algorithm to changes in parameters or dataset. If the exact parameters used have major impacts on the results or the same approach on a different dataset produces very different results, it suggests that caution should be used in generalizing the results and adding nuance to the original conclusions." [quote from webpage])


Motivation of \textcite{Derrac2015} (and thus also mine, I mean I picked this bc I found what they do interesting and their idea promising): Explainable AI but data-driven (They want to get "commonsense reasoning such as interpolation and a fortiori inference", but learned automatically. As they claim, "commonsense reasoning" <=> "how different concepts and entities are semantically related" <=> CS, because "CS qualitative spatial relations" <=> "required semantic relations for reasoning"
So why do we need structured knowledge bases you ask? [Chapter 1 of DESC15]. Many CL tasks rely on structured  knowledge bases, but getting them in symbolic form occupied (computational) linguists for dozens of years without significant progress, so finding it automatically is a good idea.


* Ganz konkret ist diese Arbeit halt im Rahmen von SIDDATA entstanden, und die Idee ist ja für die existierende Platform einen Recommender hinzuzufügen der kurs-empfehlungen nach wunsch generieren kann. 
	* Cite SIDDATA main paper
	* Explain the Platform and the concept of recommenders
	* That the dataset comes from there as well
	* Dass es ja schon SidBERT gibt welches ja auch schon empfehlungen generiert (another cite)