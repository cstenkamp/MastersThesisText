
%TODO:
% * reference yamls again
% * Im Text link zu binder bei results section der auf die notebooks/analyze_results/analyze_pipeline_results.ipynb referenziert, und für die tables auch!
% * Schreiben dass ich einige Claims oder nonclaims von denen prüfe, bspw nutzen sie immer PPMI ohne je tf-idf zu testen
% * Wie lange der ganze Kram dauert - MDS hat quadratic complexity etc
% * Das mit dem Koordinatensystem drehen passiert gar nicht so wie ich dachte dass es passiert...?!
% * Tabelle
% 	* Einduetig rausschreiben welche der 3 paper [DESC15] [AGKS18] [RaZb20] welche parameter-werte verlangen und !!welche optimal waren!! angucken welche Kombi die Beste Performance hatte und die entsprechend markieren (und im yaml haben!)!


% 	* POSSIBLE EXTRA-STEPS FOR ALGORITHM
% 		* BOOTSTRAP MORE CANDIDATES (AFTER EXTRACT CANDIDATES)
% 			* [VISR12]: LSI
% 				* Options:
% 					* What to take for the term-document-matrix
% 						* [VISR12]: 
% 							* tag-applied
% 							* tag-count
% 							* tag-share (the number of times tag t has been applied to item i, divided by the number of times any tag has been applied to item i)
% 						* relative-tag-count (tag-count / text-len) or tag-count / distinct-words-in-text
% 						* See also: https://en.wikipedia.org/wiki/Latent_semantic_analysis#Term-document_matrix
% 				* Parameters:
% 					#dims for the rank reduction (see https://en.wikipedia.org/wiki/Latent_semantic_analysis#Rank-reduced_singular_value_decomposition)

% * Schritte des Algorithmus bewerten:
% 	* "that the better Ht separates entities to which t applies from the others in S,the better \vec{v_t} models the term t." --> wie sinnvoll ist diese measure wenn das verhältnis literally 14.900 zu 100 ist, dann haben halt 99.33% der Daten einen rank von 0 ?!
% 	* DESC15 write they select Kappa "due to its tolerance to class imbalance." -> Does that mean I have to set the weight?! Außerdem weiß ich ja superviel ebennicht, like which weighting they use! I don't like
% 	* Der letzte Schritt mit dem Clustern der good-kappa-ones ist wirklich very basic und hat very much room for improvement



%TODO: maybe describe shortly what the improvements from  Ager2018 Alshaikh2020 were? 

% * Regarding DESC15 vs AGKS18 vs Alshaikh2020:
% 	* didn't somebody say that cohen's kappa sucks!?!
% 	* Alshaikh2020: 
% 		* use affinity propagation "for getting rid of the clusters of informative words", similar to how they did it in their 2019 paper
% 			-> affinity propagation has a so-called preference parameter, den als config lassen - usual, this parameter is chosen relative to the median µ of the affinity scores. For the methods Sub and Or- tho, we considered values from {0.7µ, 0.9µ, µ, 1.1µ, 1.3µ}
% 		* do kappa ON BINARY!!!
% 		* say that for them, the binary "does the word occur in the description" is the only sensible signal, no ppmi or anything! (page 2, footnote 1 of RaZb20)
% 		* "When representing a particular entity in a conceptual space, we need to specify which domains it belongs to, and for each of these domains we need to provide a corresponding vector." 
% 		* then they show their example of something that is not seperable with a hyperplane unless we specify subdomains, maybe just steal their plot that explains their one contribution to 99%
% 	* DESC15: 
% 		* "Here we use the assumption that the better Ht separates entities to which t applies from the others in S,the better \vec{v_t} models the term t." --> allein von der aussage muss man das mit den induzierten rankings echt nicht machen, sondern halt nur auf classification quality (-> metrics like accuracy) gucken, bzw kappa anhand der binären klasse berechnen --> the ranking induced by count, or the baremetal count?
% * The "Disentangled" from their title means "feature-based"
