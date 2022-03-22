
<!--
% \begin{figure}[h!]
% 	\begin{center}
% 	  \includegraphics[width=0.9\textwidth]{3dplot_hyperplane_and_orthogonal}
% 	  \caption[Visual representation of the Hyperplane of an SVM splitting a dataset]{ \label{fig:3d_hyperplane_ortho} Visual representation of the Hyperplane of a Support-Vector-Machine splitting a dataset, as well as it's orthogonal and the orthogonal projection of a set of samples onto the plane. For an interactive version of this plot, visit  {\small \url{https://nbviewer.org/github/cstenkamp/derive_conceptualspaces/blob/main/notebooks/text_referenced_plots/hyperplane_orthogonal_3d.ipynb?flush_cache}}}
% 	\end{center}
% \end{figure}


% %Was für Schritte hat der Algo 

% %TODO something along the lines of "Da, based on [source die die accuracy von dem gtranslate algorithm mit denen von menschen vergleicht], a gtranslate translation is as good as the average lecturer, it is assumed that translating the texts to english before using an english model can lead to better results


% \subsection{Extracting Candidate Terms}
% \label{sec:extract_candidates}

% * KeyBERT

% %TODO theoretisch ist es auch möglich bspw nen network mit attention auf gewisse dinge wie fachbereich und anderes zu trainieren und dann rauszusuchen was die wichtigen ausschlaggebenden dinge für das Netzwerk waren

% %TODO extract using TF/IDF as well

% %TODO a source: https://github.com/MaartenGr/KeyBERT#citation

% * After you figure out which candidate term appears in which texts, figure out which other terms are frequent in these texts while infrequent in texts of the other class and then add these to the candidate-term-set (other way may even be to classify the texts according to if the candidateterm appears in them, and then take the misclassified one also as positive samples)

% \begin{figure}[H]
% 	\centering
% 	\includegraphics[width=\figwidth]{graphics/figures/keyphrases_histogram.png}
% 	%plot created with scripts/create_siddata_dataset.py filter-keyphrases /home/chris/Documents/UNI_neu/Masterarbeit/DATA_CLONE --verbose
% 	\caption[Occurences in all Documents per Keyphrase]{
% 		\label{fig:keyphrases_histogram}
% 		Occurences in all Documents per Keyphrase (for all keyphrases that occur $\geq$ 5 times, cut off at the 93th percentile).
% 		7007 of 45295 terms occur at least 5 times.
% 		Most frequent phrases: seminar (4173), course (3722), students (2923), it (2671), language (2071), work (1980), event (1842), research (1731), lecture (1723), law (1719).
% 		}
% \end{figure}


% \subsection{Calculating the distance to the SVMs Separatrix}
% \label{sec:calculate_distance}

% %TODO: before this, explain 
% % * extraction of the candidate term set
% % * how vectors are made from texts
% In order to tell how much a text is prototypical of a category, all texts are split depending on whether they contain words of a set as described in \ref{sec:extract_candidates}, before a linear Support Vector Machine Classifier is trained on the vector-representation of all of the texts, splitting them into two classes: those that contain one of the candidate terms and those that do not. Due to the linear kernel, the SVM finds a hyperplane (\textit{separatrix}) that splits the positive from the negative samples in a way that maximizes the distance between the respective classmembers and the separatrix, using samples close to the margin as \textit{support vectors}. %TODO: what if the data is not linearly seperable?

% Following the SVMs logic, one could argue that the further away a sample is from this separatrix, the more prototypical it is of its class. Thus, the distance of a sample to its \textit{orthogonal projection onto the hyperplane} %TODO explain orthogonal projection
% may serve as metric for how prototypical a sample is for the respective category. 

% Translated into terms relevant to the aim of this thesis, the classes may be those educational resources whose description contains the word "\textit{hard}" as one class vs. those that do not as the other class. Now according to [TODO], one may use the distance of the sample towards the separatrix as a measure of how hard a class is: For all positive samples, a longer distance means a harder class, for all negative samples a longer distance means an easier one, whereas those samples close to the separatrix can be considered average.

% \subsubsection*{How to calculate the distance}

% %TODO mention that I'm in a cartesian coordinate system
% %TODO mention that I'm thinking in euclidian coordinates, see https://en.wikipedia.org/wiki/Plane_(geometry)
% \noindent In the following paragraphs, I will visualize how to calculate the orthogonal distance from a sample to the hyperplane exemplary for the case of three-dimensional text-vectors.

% Generally, the separatrix splitting positive from negative samples for an $n$-dimensional space $\mathds{R}^n$ is an $n-1$-dimensional subspace (called \textit{hyperplane}), which in the case of $\mathds{R}^3$ corresponds to a plane. 
% %https://en.wikipedia.org/wiki/Plane_(geometry)#Representation

% The general form of the equation of a plane is given as the following linear equation, where parameters $a, b, c$ and $d$ encode the position of the plane:

% \begin{equation}
% 	\label{eq:general_plane}
% 	ax + by + cz = d
% 	%TODO source? mein Tafelwerk? :D
% \end{equation}

% This reads as "All points $(x,y,z)$ for which \ref{eq:general_plane} holds are on the plane". 

% In this representation of the plane, the vector $(a,b,c)$ encodes a normal vector orthogonal to this plane, whereas $d$ serves as intercept, encoding the intersection of plane and normal. (specifically: the perpendicular distance you would need to translate the plane along its normal to have the plane pass through the origin) In higher dimensions, the formula for the hyperplane would become $a_1x_1+a_2x_2+a_3x_3+...+a_nx_n = b$, which means that encoding the hyperplane for a space $\mathds{R}^n$ requires $n+1$ parameters.
% % one rough quote in this paragraph from https://stackoverflow.com/a/17661431

% %TODO explain that it's not even harder in higher-dimensional spaces
% %TODO explain that nicely, in python the separatrix is perfectly specified using the normal and the intercept, so we have everything we need 
% %TODO die handschriftlichen notizen aus den beiden notebooks einbauen
% %TODO die plots aus dem notebook einbauen

% % The distance from any point of this $\mathds{R}^n$ to the hyperplane is then calculated as the length of the vector that is the \textit{orthogonal projection} from that point onto the hyperplane. The orthogonal projection from one vector onto another can be calculated as 

% % \begin{equation}
% % 	\label{eq:orthogonal_projection}
% % 	\hat{\vec{a}} = \frac{\vec{a}\cdot\vec{b}}{\vec{b}\cdot\vec{b}}\cdot\vec{b}
% % 	%TODO source https://en.wikipedia.org/wiki/Vector_projection
% % \end{equation}

% % ...as we however have a plane we want to project to, not a vector, what I wrote here is rather useless, isn't it?


% The distance from any point of this $\mathds{R}^n$ to the hyperplane can then be calculated as 
% % As... * dist(point, point_projected_onplane)     						 (`project[1,3]_pre`)
% %       * abs(trafo(point)[0])     										 (`protoypicality_pre`)
% %       * np.dot(plane.normal, point) + plane.d							 (`project2_pre')
% % ...normiert sind die alle gleich, aber for some reason differn die um nen multiplicator..?!
% % And the projections...:
% %       * back_trafo([0, trafo(point)[1], trafo(point)[2]]
% % 		* plane.project(point): k = (ax+by+cz+d)/(a²+b²+c²); result = [x-ka, y-kb, z-kc]
% %       * point - distance * plane.normal  (...aber nur mit protoypicality_pre als distance! )
% % 		...note that second and third are basically equal - both calculate "how much do I need to go into the direction of the orthogonal" and then do so  (point - distance * normal). The difference is that in plane.project the distance is divided by (a²+b²+c²). Originally sagt der typ von SO (https://stackoverflow.com/a/17661431) die distance ist einfach n*p-d, dann fehlt nur der normierungsterm. 
% % TODO: figure out the explanation of the difference from this to the result of using forward and backward??
% % See get_svm_decisionboundary.ipynb, den kram zwischen `#deleteme from here', commit d46a8300dae81adee


% \subsection{Clustering the extracted candidates}

% An analysis of \cite{Carmel2009} showed that a statistical method to extract features from clustered text corpora identified the labels of human annotators as one of the top five most important terms in only 15\% of cases, implying ``that human labels are not necessarily significant from a statistical perspective" \cite[139]{Carmel2009}
% %TODO: die eigentliche Methode (JSD) mehr erklären!!
% %(the JSD method for feature selection identifies human labels as “significant” (appearing in the top five most important terms) for only 15% of the categories. This result implies that human labels are not necessarily significant from a statistical perspective.z)


-->