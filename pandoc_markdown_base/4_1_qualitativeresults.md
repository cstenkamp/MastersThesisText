
Qualitative Analysis in this case means "looking at stuff". Such a qualitative analysis is always to be taken with a grain of salt, because it is very prone to cherry-picking (both on purpose and not on purpose, the stuff you're looking at just doesn't need to be representative!). However it does help a lot and provides a lot of insights (and often helped me in the debugging process).
What can you look at for such a qualitative analysis?
\begin{itemize}
	\item The clusters, checking if things you know to be similar are actually in the same clusters
	\item If descriptions you know to be semantically similar are actually close in the embedding
	\item You can do the whole thing for only three dimensions instead of the 50/100/200 because there you can plot the stuff and interpret it
\end{itemize}

\begin{itemize}
	\item  Man kann ja schon nach dem Embedding anhand der nächsten Entities sehen ob das was werden kann - bei 100D sind dann halt "airplane cabin" und "aircraft cabin" die nächsten entities, bei 3D dann halt eher kram wie "area" and "moor", was schon eindeutig zeigt dass 3D offensichtlich nicht so der Hit ist
	\item Die vielen Sanity Checks die man machen kann, bspw dass ich ja in 3D gucken kann (und auch in höher-D ausrechnen) ob eben diese dinge (von item 1) im Embedding nah sind, und ob die SVM Dinge schön trennt ("howto_embed.ipynb")
	\item "placetypes_origconf.ipynb", was einfach von vorne bis hinten die original-config (ist ja auch im yaml) von DESC15 ausführt und interpretiert	
\end{itemize}

\begin{itemize}
	\item Ist "Mathe" ein Keyword, clustern "a1" und "a2", ...
	\item Ist "Codierungstheorie und Kryptographie" - mathe = "Kryptographische Methoden in der Informatik"?
	\item Question: Does the continuation thingy which they have (backtothefuture:backtothefutureII::terminator:terminator2) hold for courses as well - Verhält sich Informatik A zu Informatik B wie Mathe für Anwender 1 zu Mathe für Anwender 2?  Info B zu Info A genau wie Statistik 2 zu Statisik 1? 
	\item Paperlesen und den cluster von "pub" für placetypes angucken
\end{itemize}


\begin{figure}[H]
	\centering
	\includegraphics[width=\figwidth]{svm_mathematik_highlight_infoAB.png}
	\caption[3D-Plot with an SVM for the term "Mathematik"]{
		\label{fig:3dplot_mathe_infoab}
		3D-Plot with an SVM for the term "Mathematik", also highlighting the courses "Informatik A" and "Informatik B"
	}
\end{figure}

In figure \ref{fig:3dplot_mathe_infoab} we see a 3D-Embedding for courses, splitting courses which contain the term "mathematics" from those that don't, also hightlighting the terms "Informatik A" and "Informatik B". We see they are close we see the SVM is not to bad, and even though neiher Info A nor Info B contains the word "mathematik", thy are both on the "mathematical side" of courses. Negative samples are hidden for better visibility, and entities that contain the word more-often-than-the 75th (???) percentile have bigger markers.


\begin{itemize}
	\item In 3D ists immer ne Kugel, und ich würde behaupten in höheren Dimensionen ist es nicht extrem viel besser. dadrin ne SVM zu machen bringt echt wenig bis gar nix (Ich hab ja sogar Plots die zeigen dass die Movies viel besser clustern - TODO: die einbringen)
\end{itemize}