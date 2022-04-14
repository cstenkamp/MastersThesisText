## "Workflow", also wie ich mich voran gearbeitet habe

\todoparagraph{The calculation how to find the best threshold for candidates}

PLOTS HERE:
* why kappa_weights=None is bad 
* Plots/Tables mit set-overlaps von meinen placetypes zu deren (und auch die big_21222.yml ergebnisse danach auswerten)

* Very first: explore if there are enough courses in the Database (data_exploration.ipynb)
* Obvious first choice sind die Derrac & Schockhaed Paper, das aktuellste von denen von dem der Code avaiable ist ist Hierachical Linear Disentanglement [ALBS20] -> [https://github.com/rana-alshaikh/Hierarchical_Linear_Disentanglement](https://github.com/rana-alshaikh/Hierarchical_Linear_Disentanglement)
    * Code schwer zu verstehen und ohne Daten. Gibt's vielleicht andere Paper auf denen es aufbaut die Code haben?
        * [DESC15]?
        * [AGKS18]? JA, auch uncleaned [https://github.com/ThomasAger/Modelling-Salient-Features-as-Directions-in-Fine-Tuned-Semantic-Spaces](https://github.com/ThomasAger/Modelling-Salient-Features-as-Directions-in-Fine-Tuned-Semantic-Spaces)
    - Auch wenn er angeblich die Daten zur Verfügung stellen wollte hat ers nicht. Das einzige was man an Daten so kriegt sind die vom vorherigem Paper [Inducing semantic relations] [DESC15], available at [http://www.cs.cf.ac.uk/semanticspaces/](http://www.cs.cf.ac.uk/semanticspaces/)
* ...versuchen, die [AGKS18] und [ALBS20] zu verwenden, deren code ist aber absoluter Bockmist
* dazu übergehen es doch selbst zu machen. Angefangen bei [DESC15], das ist der "basic algorithm". Von vorne bis hinten durchimplementeiren was die da Beschreiben.
    * Ganz viel deren Claims aus den Tabellen etc asserten ob ich auf das selbe Ergebnis komme mit den daten von [http://www.cs.cf.ac.uk/semanticspaces/](http://www.cs.cf.ac.uk/semanticspaces/), ganz viel testen
    * ...den Siddata-Datensatz muss ich dann auf die selbe Weise wie die erstellen und hoffen dass das selbe rauskommt → ganz viel plotten

* modularity, an möglist vielen stellen gucken können ob's klappt oder nicht
* workflow mit grid und yamls für kombis und runterladen wie johannes gesagt 
	* Grundlage: Das Gelöt ist in Schritte einteilbar, an gewissen Schritten werde gewisse Params relevant
	* Um dann den Algorithmus auf einem Dataset laufen zu lassen muss man sich dann, informedly, mögliche parameter-spaces überlegen (also teilweise schlichte hyperparamter, teilweise halt komplette austauschbare komponenten wie "MDS in schritt 2"). Informedly bspw weil * verhältnisse wie datasetgröße zu threshold ähnlich wie bei den daten der originalautoren wählbar sind, * die verschiedenen paper optimal results für verschiedene parameterkombinationen reporten (siehe tabe xyz), * datensätze schlicht verschieden sind und man schon wissen über das dataset hat (siehe den teil in section dataset wo ich bspw schreibe dass bei mir ja "öfter vorkommen" nicht "relevanter" heißt), etc etc  [Auf dataset & algorithm tabellen verweisen]
	* Dann macht man sich halt nen yaml dass fixwerte und listen für parameter-spaces hat [ein config-file beispielhaft zeigen]
	* Dank snakemake und meinem Code kann man dann mit einem Kommando sämtlihce Kombinationen (maximal efficiently, orchestrated, auf dem Grid, mit zig maschinen gleichzeitig, remote) laufen lassen  [screenshot davon wie zig kombis auf dem grid laufen, both mit `analyse` and `check`, screenshot von snakemake's tabelle was-wie-oft die es immer am Anfang anzeigt, screenshot von snakemake dependency-graph für die original DESC15-config]
	* dann zieht man sich die für-bis-schritt-x-relevanten zwischenergebnisse wieder auf seine maschine (nicht mal das) und führt die analyse-skripte aus um zu gucken was für ergebnisse die jeweiligen parameterkombis dann so haben und sich zig metriken für sämtliche kombis anschauen und vergleichen [auf analyse_svm_metrics verweisen und screenshot von den 60*12 plots und dem dataframe unten]


* Relativ früh  in the process I of course tried the placetypes-dataset as sanity-check to find errors - for that dataset, stuff like the good-candidates is known so as long as I don't reach their performances for that dataset I know my code is the problem, but as soon as I reach their performance I can savely say that the actual algorithm is correct and if it's still bad on the Siddata-dataset it's just not applicable to this kind of data (dass ich halt das jetzt erstmal auf den Originaldatensätzen laufen lasse und sehe ob ungefähr das gleiche rauskommt wie bei den autoren um zu gucken ob's an meinen Daten oder an meinem Code liegt)
	* Dass ich smarterweise meinen Kram auf deren dataset hab laufen lassen und mir set set-overlaps angucken kann
* often I had to guess parameters bc the original papers were not specific about it, but because I had some numbers from them I could work with that
	* In deren T^0.5 sind mindestens n_dims*2 Terms -> solange ich das nicht hab mach ich was falsch
	* Der Workflow-Teil "erst guck ich mir nur die Anzahl Candidates an, und nur mit den paramkombis wo das nicht viel zu wenige sind mach ich überhaupt weiter"
	* meta-workflow wie ich dann Parameter-kombis rausfiltern kann anhand der condition "so viele candidates sollten es mindestens sein", sodass ich nicht die totale combinatorical explosion habe... (also pre-analysis und main analysis),
		* Soll heißen: Bis schritt 7 muss man sich einfach keine Daten angucken - man weiß man möchte mindestens X feature directions, probiert dann in preliminary tests erste parameter-kombis durch und kann die rausfiltern die unter diesem threshold liegen. 
		* Dafür hab ich ja auch plots - beispielhaft sieht man hier dass mit kappa-weights=None nicht die gewünschte Anzahl directions bei rumkommt. So I know from now on for the next steps I don't need even need to consider that. 
		* Die guten parameter kann ich dann mit mehr details betrachten (also nach dem motto "200d und 100d waren gut, let's also try 150d") und den ganzen bums zurück aufs grid werfen! 
		* und dann halt einen weiteren schritt hab wo ich mir qualitativ die cluster angucken muss und quanitativ shallow decision trees machen kann (mit ebenweniger params) um davon das "beste" zu finden
	* (ref kappa-weights-plot) (wie ich das klug tun kann anhand vergleich zu DESC15 )
	* dass mein Debugging-Workflow ja auch klasse ist, von wegen dass ich halt die ganzen Plots gleichzeitig anzeigen kann und sehen kann wie das so qualitativ aussieht
	* Ne shitton an Parameter-Kombis ausführen (besonders da wo im Text nicht eindeutig ist bspw ob sie mit dem PPMI-Ranking oder dem Count-Embedding vergleichen)
* Many Sanity-Checks I could do
	* Look at close [dissimiliarity-matrix und emedding], are they semantically related and do similar ones cluster
	* Embedding und die SVM in 3 Dimensionen plotten
		* does the SVM divide useful (\ref{fig:mds_3d_hyperplane})
		* Daran hab ich bspw erkannt dass das MDS fehlerhaft war (...weil die sklearn-implementation buggy ist). 
		* ...daran sieht man dann aber auch, dass die SVM eigentlich super aussieht, OBWOHL die darauffolgenden Metriken (also die ganzen kappas) immernoch crap sind -> ich hab nicht nur die Bugs in meinem Code erkannt, sondern ebenauch dass mein Code richtig ist und TROTZDEM schlechte Sachen bei rumkommen, und in letzterem Fall ist die interpretation dann ja eher dass die Metriken die DESC15 vorschlägt gar nicht funktionieren...?!

* Ich kann an jedem einzelnem Schritt der Pipeline gucken ob ich die selben Ergebnisse hab wie deren Zwischenergebnisse, dass das teil des workflows war 
	* Ich kann gucken ob die Clustercenters von denen (die ja kappa >= 0.5 haben) auch bei mir hohe kappa-werte haben 