<!--Here: 
*  Anwendungsfall (->e-learning, recommenden von bildungsressourcen, ...). nicht-technisch, aber nötig zum verstehen wo passiert das 
* Explain the Platform and the concept of recommenders
	* That the dataset comes from there as well
	* Dass es ja schon SidBERT gibt welches ja auch schon empfehlungen generiert
-->

This section explains specific usecase (e-learning, recommendation of educational resources) and elaborates what the domain is and why there is the need for recommendation in the domain of educational resources. It further introduces the SIDDATA project and platform and how it relates to this thesis.

TODO: Define "Educational Resource" explicitly
Definition 1: \textbf{Educational Resource} An Education Resource is xyz.

### Overwhelming amounts of resources

Problem that both SIDDATA and this thesis want to solve: 

* e-learning becomes more and more important, and recommendation in the educational section is very helpful.

Users have MANY educational resources but limited time, so the actual problem now is the choice of the right resources. Academics nowadays must engage with a multitude of interconnected, digital and open practices and technologies \cite{Atenas2014}. High-quality \glspl{oer} become more and more widespread, and that's great, as they \q{may ultimately be the genuine equalizer for education and for empowering social inclusion in a pluralistic, multicultural, and imperfect world} \cite[2]{Olcott2012}. However they fundamentally change the landscape of higher education - now there's an overwhelming quantity of high quality  material available, so the new problem is how to find something in this ocean of information. Searching and retreiving \gls{oer} is often challenging as materials are difficult to locate and retrive or to figure out what differentiates from one another \cite{Atenas2014}.

The \emph{Future Skills Report}\footnote{\url{www.nextskills.org}} on the future of learning and higher education \cite{Ehlers2019} suggests that future academic education will look fundamentally different from today, in that it will likely become increasingly multi-institutional with students individually having their own personalized, flexible curriculum selected from a vast set of resources, in constrast to the current rigid available study programmes \cite{Ehlers2019}. 

\cite{Ehlers2019} lists 16 crucial skills regarding individual abilities and development, instrumental skills such as self-organized knowledge acquisition as well as social and cooperation skills. Future is life-long learning and individualization of educational paths, so self-regulatory competencies and being able to find educational pathways is more important, and regarding object-related skills being able to find relevant resources becomes more and more a problem.

<!-- quotes FROM JOHANNES SidBERT Paper:
	* "In German higher education institutions, a pivotal aspect of student learning success is the choice of courses: Aside from compulsory courses, students can choose from the vast offering of courses available at their local university as well as additional material such as books, courses on MOOCs or OER for self-study" 
	* "In German higher education institutions, a pivotal aspect of student learning success is the choice of courses: Aside from compulsory courses, students can choose from the vast offering of courses available at their local university as well as additional material such as books, courses on MOOCs or OER for self-study"
	* "categorizing educational resources into knowledge domains poses an equal challenge, different educational resource repositories use different, sometimes incompatible meta data. Additionally, the inclusion of knowledge domains a course or an OER covers is often only inferable from their title or description."
-->

### SIDDATA

This thesis was started while I worked at the SIDDATA\footnote{As \textsc{Siddata} signifies both the project and the developed digital assistant, the all-upper 'SIDDATA' henceforth refers to the project, while the specific developed software will be denoted 'siddata' or 'DSA'.} project, with the idea to add a recommender to the platform that can generate course recommendations with the user "in the loop"

Problem as before: Data is available but the problem is transparency, target-oriented accessibility, and manageability
Studies have shown (WHICH specified in \cite{Schurz2021} that setting self-set, self-regulated personal educational goals is good, and DSA can help 

* SIDDATA is a joint interdisciplinary project for \q{\emph{Individualization of Studies through Digital, Data-Driven Assistants}}\footnote{\url{https://www.siddata.de/en/}} of the universities Osnabrück, Bremen and Leibniz Universität Hannover, funded by the german \emph{Federal Ministry of Education and Research}\footnote{BMBF. Funding number: 16DHB2124}. 
* The deliverable of the project is a flexible data-driven \gls{dsa}, that supports students in higher education in their invidual learning and achievement of personal study goals by giving hints, reminders and recommendation for their individual study paths \cite{Schurz2021}
* For that, the collaborative project combines unlinked heterogenous data and information (from management systems, offers and resources of other universities and institutions, and data on individual learning and working behavior) in a digital study assistant, integrated into the university's \gls{lms} (Stud.IP \cite{stockmann2005})

The resulting software is a digital data-driven assistant that "aims to compensate the aforementioned weaknesses of human learners in a globalized learning environment". 

* Required is a system architecture that makes heterogenous data source available with a focus on extensibility and flexibility, allowing to include new and different data sources (such as data from \gls{lms} or \gls{oer} sources such as \glspl{mooc}) through simple APIs, and analysis methods for targeted recommendation
* Combines pre-created information recommendation, classical AI (expert systems) and ML
* highly modular extensible architecture designed to support multiple different data sources, clients and recommender modules.
* Design: 
	* Frontent (UI) is a plugin for the LMS Stud.IP (->easy access), that can also get data (courses, talk dates, ..) from Stud.IP through cronjobs, RESTful API to the Django Backend. 
	* Backend is relational ORM database (django & postgres), OO application that Consists of recommender modules with specific purposes each (eg. recommending Academic Contacts that fit an expressed academic interest.)
	* to generate very different recommendations for very different data, the modules must be independent with loose communication (write results to DB is communication), but common ontology for eg. courses and academic interests
	* Backend consists of seperate encapsulated recommender modules in a loosely coupled architecture. These modules generate recommendations towards personal educational goals based on behavioral data from the individual, intra- and extra-organizational data from universities and publicly available educational data from the web
	* What's grouped into a recommender is seen from a user perspective, so each recommender focuses on a topic, like
		* finding peers
		* recommending courses (both rule-based and using modern ML, relating natural language inputs with the datasets)
			* "Classic rule-based Artificial Intelligence, often used in expert systems, combines known facts about the world with rules about these facts to derive new potentially useful knowledge"
			* ANNs "are capable of detecting complex features and patterns in large data sets". More on the "Academic Interests" recommender later.
		* information about scientific career (funding, informationsources)
		* personality-based learning behaviour- and study tips
		* regarding local and remote courses and Open Educational Resources (OER)
* Currently third prototype, evaluated using user data (like which ones were activated and which deactivated) and qualitative data, first insight suggesting that those modules that provide personal recommendtation were most well received \cite{Schurz2021}




The dataset used here was collected through the Siddata platform as well, as mentioned it uses APIs to get courses and events from the three universities as well as other sources (for MOOCs and OERs) through respective APIs. More details in \autoref{sec:dataset_siddata}. It should be noted that the dataset is not artificially generated (unlike \mainalgos) but collected from current courses etc and, well, actually useful, so having an algorithm for this domain can and will directly be incorporated as recommender and is a direct practical contribution.


With the "Academic Interests" recommender there is already a system in place that recommends courses, having seen the same need to aid students in finding educational resources, information about which is only implicit. More details in \autoref{sec:otherwork}.