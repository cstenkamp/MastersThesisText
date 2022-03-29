* Ganz konkret ist diese Arbeit halt im Rahmen von SIDDATA entstanden, und die Idee ist ja für die existierende Platform einen Recommender hinzuzufügen der kurs-empfehlungen nach wunsch generieren kann. 
	* Cite SIDDATA main paper
	* Explain the Platform and the concept of recommenders
	* That the dataset comes from there as well
	* Dass es ja schon SidBERT gibt welches ja auch schon empfehlungen generiert (another cite)



Nicht vergessen was zu e-learning und education zu schreiben.


% Anwendungsfall (->e-learning, recommenden von bildungsressourcen, ...) -> nicht-technisch, aber nötig zum verstehen wo passiert das 

% TALK ABOUT that actually, in CS concepts (=types) are regions, BUT we have only one-instance-per, so TOKENS, so it's kiiinda reasonable that we have points! IF we would have the collection of "ALL Computer Science 1 Courses" it would be different


* auch schreiben warum recommendation im educational bereich SINNVOLL ist.


* kein künstlich erzeugter datensatz (like the one for Derrarc2015), but actually useful, so if we have a good algorithm that can make sense of it, great


SIDDATA 

From the website:
	* Joint, interdisciplinary project for \q{\emph{Individualization of Studies through Digital, Data-Driven Assistants}}\footnote{\url{https://www.siddata.de/en/}} of Universität Osnabrück, Universität Bremen and Leibniz Universität Hannover, funded by the Federal Ministry of Education and Research
	* Examines how students can be supported in achieving individual study goals by combining previously unlinked data and information (from management systems, offers and resources of other universities and institutions, and data on individual learning and working behavior) in a digital study assistant, accessible over the university's [campus/learning] management system (osnabrück: Stud.IP) (-> Data-driven!)
	* Core Product: flexible, individually einstellbarer Digital Study Assistant that encourages sutdents  to define their own study goals and to follow them consistently. 
	* The data-driven environment will be able to give hints, reminders and recommendations [...] regarding local and remote courses and Open Educational Resources (OER). These tips and recommendations should help students to make informed decisions for their own individual study path.
	* Interdisciplinary research: Higher Education Research, Cognitive Science, Information Systems as well as Software Development - ML part from coxi duh
	* Heterogenous data
	* collaborative project


From "TOWARDS A USER FOCUSED DEVELOPMENT OF A DIGITAL STUDY ASSISTANT THROUGH A MIXED METHODS DESIGN"
	* DSA - help individual learning by appropriate recommendations
	* SIDDATA DSA = prototype of a DSA for students in higher education, integrated into the LMS . Consists of recommender modules with specific purposes each (eg. recommending Academic Contacts that fit an expressed academic interest.)
	* Classical AI + ML 
	* Current Prototype evaluated by mixed methods design approach with concurrently collected user data and qualitative data.
		* "A first insight in the user data suggests that recommender modules providing personalized recommendations are more likely to be used by students."

	* Users have MANY educational resources but limited time, so the actual problem now is the choice of the right resources.
	* studies show mixed results when it comes to integrating technology into the learning process 
	* studies have shown that setting self-set, self-regulated personal educational goals  is good, and DSA can help. Also finding peers
	* Frontent is a plugin for the LMS Stud.IP, that can also get stuff from Stud.IP, REST to the Django Backend. 
	* Software modular, seppearte encapsulated recommender modules, each focusing on something (contacts, courses (rulebased+ANN-based (relating natural language inputs with the dataset)), information about scientific career/personality-based-studytips/dataethics/OERs...)
	* Used my plots^^

FROM "A Data-Driven Study Assistant Architecture for Universities"
	* The extensible architecture is designed to support multiple different data sources, clients and recommender modules. These modules generate recommendations towards personal educational goals based on behavioral data from the individual, intra- and extra-organizational data from universities and publicly available educational data from the web [...] loosely coupled architecture
	* "Future Skills Report" [EK19] on the future of learning and higher education lists 16 crucial skills
		* First group "Subject and individual development related skills" essential for life-long learning and the individualization of educational paths. This requires a high degree of self-regulatory competencies for finding individual educational pathways. 
		* Second group "Object-related skills": educational envrionment has manymany resources, but choice becomes problematic
	* digital data-driven assistant "aims to compensate the aforementioned weaknesses of human learners in a globalized learning environment". Data is available but the problem is transparency, target-oriented accessibility, and manageability
	* Required is a system architecture that makes heterogenous data source avaible focus on extensibility and flexibility. It must be possible to include new and very different sources of individual and public data, incorporate a wide range of data analysis methods to deduce targeted recommendations on different levels. The protoype we present here collects data from Learning Management Systems (LMS)...
	* Requirements/Challenges/DesignDecisions:
		* Easy Access (Stud.IP integration)
		* API to gather data from various sources
		* relational ORM database , OO application
		* to generate very different recommendations for very different data, the modules must be independent with loose communication (write results to DB is communication), but common ontology for eg. courses and academic interests
		* safe & async	
    * frontend 
		* UI in the LMS as plugin that visualizes any kind of data from the backend & reacts to input
		* also has cronjobs to regularly get data from the LMS (courses, talk dates, etc) & let user gift data
	* backend (connected using RESTful API)
		* based on django & postgres, encapsulated into recommenders. Recommender logic from user perspective, eg one for recommending accademic contacts. Many different methods
			* "Classic rule-based Artificial Intelligence, often used in expert systems, combines known facts about the world with rules about these facts to derive new potentially useful knowledge"
			* ANNs "are capable of detecting complex features and patterns in large data sets"
			* scientific career (funding, informationsources), dataethics, personality module (measures memory & ability to task-switch, gives learning behaviour recommendations based on that), contacts, learn about OERs, 
				* Academic Interests, an AI-based application that categories courses and ohter learning materials into knowledge categories. Deep ANN that classifies courses and user requests to DDC [source], "a categorization system commonly deployed in libraries around the globe" based on title and description, matching DDCs of searches and courses

From "Opening Teaching Landscapes: The Importance of Quality Assurance in the Delivery of Open Educational Resources"
	* "Academics today are expected to engage not only with the traditional classroom technologies but also with a kaleidoscope of interconnected digital, open and social practices."
	* "Open Educational Practices (OEP) are defined by the International Council for Open and Distance Education (ICDE) as “practices which support the production, use and reuse of high quality Open Educational Resources (OER) through institutional policies, which promote innovative pedagogical models, and respect and empower learners as co-producers on their lifelong learning path”"
	* “OER may ultimately be the genuine equalizer for education and for empowering social inclusion in a pluralistic, multicultural, and imperfect world” (Olcott, 2012, p. 2).
	* Ferguson & Shum (2012): "while OERs greatly improve the quality of material available online to learners, this wealth of resources can leave learners adrift in an ocean of information, struggling to solve ill-structured problems, with little clear idea of how to approach them [...]"
	* we have noticed that searching and retrieving OER from repositories can be a challenging task as materials are difficult to locate, retrieve
	* For Misra (2013, p. 25), “there are literally millions of open education resources currently available on the Internet. But what differentiates them from one another? How can educators determine whether the resources are high quality?”

FROM A Neural Natural Language Processing System for Educational Resource Knowledge Domain Classification
	* "Information on the content discussed in the scope of the educational resources, however, is implicit and must be inferred by the user by reading the resource title or through contextual information"
	* maps onto the 905 DDC classes
	* "In German higher education institutions, a pivotal aspect of student learning success is the choice of courses: Aside from compulsory courses, students can choose from the vast offering of courses available at their local university as well as additional material such as books, courses on MOOCs or OER for self-study"...
	* "When using traditional pattern-matching search, these search queries may yield no results or return courses within another domain that by chance contain the same words but are otherwise unrelated to the domain the student is looking for."
	* "categorizing educational resources into knowledge domains poses an equal challenge, different educational resource repositories use different, sometimes incompatible meta data. Additionally, the inclusion of knowledge domains a course or an OER covers is often only inferable from their title or description."
	* DDC has hierachical tree stucture with 10 childs at each level. Childs are subtopics of thir parents, things can have multiple DDCs.
	* BERT - based on transfomer (text doesn't need to be added sequentially). 12 stacked self-attention+feedforward encoder layers to create deep phrase embeddings, trained with masked-token inference tasks where the hidden word must be preicted
	* SidBERT trained on 1.3m book titles & descriptions (uni/hannover/bremen uni + german national libray) 3-4 level
	* SidBERT is BERT-base model + custom classification head, from Huggingface-transformers. 
	* 62.2% recall, 45.2% accuracy for 905 classes (chance would be 0.11)
	* Hierachical clustering with agglomerative hierachical clustering using Ward's minimum variance method (iteratively creating superclusters based on their relative euclidian distance)
	* analyze misclassifications to draw conclusions about the internal representation of the model. observe a cluster retention rate of 74,47% for clusters at DDC level 3. This means that classes that are closer within the original DDC tree structure are also closer in the learned representation of SidBERT.
	* Potential future stuff: one could make use of the DDC structure as additional information for model training. This may be achieved through the application of Graph Neural Networks (GNNs) in the classification head of model