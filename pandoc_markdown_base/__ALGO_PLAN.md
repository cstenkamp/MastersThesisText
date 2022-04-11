ALGORITHM

# Pay Attention to when reading \mainalgos:
	* which params were optimal
	* didn't somebody say that cohen's kappa sucks!?!
		* Is that the same paper that used the algo for wikipedia-pages? 
		* Was kommt dabei raus? Does it supprort my thinkings?

==========================

# Algorithm
	## General Remarks
			* Allgemeiner Kram, kürzen, das was besser nach vorne passt nach vorne
			* drauf eingehen dass ich halt meine implementation beschreib
			* I may have up to FOUR SECTIONS with the same content
				* Algorithm. Short & Nothing Superflous
				* Implementation Details
				* What-Configs-Are-Available-Where (TABLE??)
				* What-other-things-one-could-have-done-thereandthere

		### Contributions from Ager & Alshaikh
			* MDFILE: 3_1_1_ageralshaikh
			* reference yamls
			* doc2vec nicht implementiert weil schlechter bei ager.
    		* Finetuning nicht drin weil nur marginal besser bei ager (ref tabelle im anhang)
    		* ...ähnliche gründe für alshaikh finden

		### Core Idea Again I guess

	## Steps (SHORTLY say if future work possible in the steps)
		* Dependency-Graph
		### Preprocessing
			* Remove stopwrods, 
			* tokenize und 
			* Lemmatize näher beschreiben
		### extract candidates               (Generate Candidate Words for Feature Directions)
			* Ensure consistency with dataset section and results
			* MARKDOWN: Extract Candidates (Steps 4, 5 and 6: Extracting Candidate Terms, Postprocessing them, creating the Doc-Term-Matrix for the Candidate-Terms and filtering it)
		### create embedding    			 (Generate Vector Spaces (Embeddings) from Descriptions)
			* MARKDOWN: "Create Dissimilarity Matrix & Quantify" 
			* MARKDOWN: Embed
		### candidate SVM & Filter           (Filter Candidate Feature Directions)   
			* MARKDOWN: Creating Candidate SVMs & Filter Candidates
			* PLOT: Beispiel für "faithful" induced ranking vs "not faithful" one ---- "wann ist ein induziertes ranking faithful pos/neg example" (grafische Darstellung von "if the ranking induced by the SVM corresponds to the count/PPMI, we see it as faithful measure", also ein beispiel wo's passt und ein Beispiel wo's nicht passt)
		### Cluster & Calculate directions   (Merge Feature Directions)
			* MARKDOWN: Cluster 
		### (optional) post-process clusters (Post-Processing)
			* MARKDOWN: Post-processing
		### Calculate distances 			 (RATHER CALL RE-EMBED?!)
			* MARKDOWN: Embed with Semantic Directions (includes find cluster names)
			* MDFILE: 2_7_separatrixidstance

		* MARKDOWN: Make decision-trees


	## Whatelse 
		### Features and Contributions / Differences to \mainalgos
			* MDFILE: 3_features_differences
			* Algorithm-Compare-Table
			* All important configs
			* reference yamls
			* TABELLE which parameter-combis were USED, with optimal ones MARKED for \mainalgos (-> also into yaml!)

		### Temporal & Spatial Complexity
		    * MDS hat quadratic complexity
		    * Didn't find a way to have PPMI without quadratic space req, so we're talking >24GB RAM
		    

	## POSSIBLY SPÄTER (WORKFLOW)
		* MDFILE: 3_4_workflow

		### Reasonable Params (??)
			* MDFILE: 3_reasonableparams

		### Problems of the algo 
			* The property
			* Fundamental Information Retrieval Problem

		* Snakemake-Graph mit Configs wie für DESC15