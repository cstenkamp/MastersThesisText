
* Qualitative Analysis in this case means "looking at stuff". Such a qualitative analysis is always to be taken with a grain of salt, because it is very prone to cherry-picking (both on purpose and not on purpose, the stuff you're looking at just doesn't need to be representative!). However it does help a lot and provides a lot of insights (and often helped me in the debugging process).

## Ways of qualitative analysis ("What can you look at for such a qualitative analysis?"):

* Are the words in clusters similar 
	* if things you know to be similar are actually in the same clusters
	* in the "scary" cluster, is there also often something like "horror" or "gore"?
	* in courses that would be "A1" and "A2", both hinting at langauge courses
		* OLD RESULTS didn't show that => Distance-threshold small: no clusters at all; threshold high: "A1" is in a cluster with "course", which makes it useless
* Are words that I would LIKE to be semantic directions actually semantic directions? ("computer", "mathe", ..)

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


## MY QUALITATIVE ANALYSIS:

* doc-cand-matrix
	* the term-frequencies for terms that I WOULD LIKE are really low
		`for term in ["computer", "mathe", "mathematik", "wissenschaft"]: print(f"TF of `{term}`: {filtered_dcm.term_freq(term, relative=True):.2%}")`: 1.0%, 0%, 0.8%, 3.3%
* embedding & dissim-mat
	* 3D-Embedding & t-SNE on (veryveryhigh-dim) dissim-mat, colored by Fachbereich 
		* shows that, at least regarding this feature, okay-ish
		* TODO: show one of Placetypes and compare!!!
	* Show 10 courses that are close according to the embedding and manually look if they are similar
		* Look at courses that I KNOW to be similar and check if their embedding is close
			* Language Courses, Mathe für Anwender 1 & 2, Info A & B
* Final Embeddings	
	* Is there a direction for "more advanced course"? 
		* Language Courses, Mathe für Anwender 1 & 2, Info A & B


\begin{figure}[H]
	\centering
	\includegraphics[width=\figwidth]{svm_mathematik_highlight_infoAB.png}
	\caption[3D-Plot with an SVM for the term "Mathematik"]{
		\label{fig:3dplot_mathe_infoab}
		3D-Plot with an SVM for the term "Mathematik", also highlighting the courses "Informatik A" and "Informatik B"
	}
\end{figure}

In \autoref{fig:3dplot_mathe_infoab} we see a 3D-Embedding for courses, splitting courses which contain the term "mathematics" from those that don't, also hightlighting the terms "Informatik A" and "Informatik B". We see they are close we see the SVM is not to bad, and even though neiher Info A nor Info B contains the word "mathematik", thy are both on the "mathematical side" of courses. Negative samples are hidden for better visibility, and entities that contain the word more-often-than-the 75th (???) percentile have bigger markers.


Look how good "reclassify" algo is!!

Highest-ranking descriptions per dimension:
	------------------------ reclassify --- main ------------
	isawyoufirst           : beach          beach
	workspace              : office
	nutrition              : restaurant     deli
	goalie                 : stadium		football stadium
	pumper                 : building 		county
	starwoodhotels         : hotel room 	pool
	interstate10           : highway 		mongolian restaurant
	urban                  : interior 		movie theater
	tuolumne               : creek 			national forest
	cabs                   : downtown
	investment             : school 		stock exchange
	stripmall              : downtown 		department store
	michiganstateuniversity: school 		campus
	ews                    : railroad 		train
	anchored               : boat 			pier
	a10                    : airport
	wc2                    : restaurant 	square
	airbase                : airport 		airbase
	joshuatreenationalpark : canyon 
	clinker                : building
-> WE SEE HERE that using the respectively best-fitting DOCUMENT (without LSI or anything, just the one with the highest ranking!)  is often even the MUCH BETTER direction!!!


Top 3 Features by Importance (TODO: Link notebook)

Mathematik/Informatik            programmiersprache, menge, szene
Rechtswissenschaften             juristisch, einfuhrung allgemein, bgb
Erziehungs-/Kulturwissenschaften erziehungswissenschaft, religionsunterrichts, berufsbildend schule
Physik                           neu entwicklung, regelmassig aktiv teilnahme ubernahme, unterrichtsforschung
Sprach-/Literaturwissenschaften  deutsch literaturwissenschaft, sprache, partie
Wirtschaftswissenschaften        center betriebswirtschaftlich kompetenz, zitat, religionsunterrichts
Humanwissenschaften              psychologie, metaphysik, exposes
Sozialwissenschaften             arbeitsmarkt, regieren, multiple
Biologie/Chemie                  aktivierung studierend, brd, madchen
Kultur-/Geowissenschaften        tourismus, gi, stadtgeographie