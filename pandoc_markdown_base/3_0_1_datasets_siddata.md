
#### What's inside & Where the data is from 

see \autoref{sec:discuss_datasetdiffs} \todoparagraph{the fact that we mitigate smaller dataset size by only taking those entities with at least 80 words etc}
* dass man ja sieht das gerade beim thresholden nicht mehr viel von nicht-kursen übrig bleibt 


    * Problems / Besonderheiten / Whackities:: 
        * Often short 
            * \ref{fig:sid_wordsperdesc}
            * Especially Informatik-Department often has links to longer descriptions but there's no straightforward way to follow them
        * Often useless 
            * "Tutoren: Willi Wacker Susi Sorglos"
            * "Findet statt in Raum XYZ"
        * Often repeating 
            * Sprachkurse-Example: Fast alle haben die gleiche description (beispiel. `....len([i for i in descriptions._descriptions if "kompetenzen entwickelt befahigen akademischen berufstypischen" in i.processed_as_string()]) == 25`  ... weil es genau 25 exakt gleiche Beschreibungen gibt, für die Fremdsprachkurse. Deswegen ist up to jede 5-wort-kombination davon ein extracted keyword`) (und das obwohl sie verschiedene Namen haben! merging them doesn't make sense but they are almost equal)

        * Sample Shitty descriptions: (all from data_exploration_Siddata2021)
            * "BA/MA Hauptmodul"
            * "Bestandteile:Vorlesung + Übung"
            * "Dozent  Dr. Michael Wicke"
            * "Siehe Gruppe A"
            * "s. Modulbeschreibung"
            * "Literatur:wird noch bekannt gegeben"





#### Size & Distributions

\todoparagraph{A lot of this has already been said in the general dataset section}

* Distribution of what's inside, where it's from and its languages 
    * \ref{tab:siddata_metadata}
        * und dahinter noch was haben was für all die auch noch average length listet (geht erst in running)
    * \ref{fig:sid_statistics}
    * Ref the sunburst-plot
    * It was started to be translated using gtranslate such that everything is english but that was dropped with the 2022 data
* Distribution of lengths & words
    * Description-Lengths
        * Verhältnis von #descriptions zu average length
        * \ref{fig:sid_wordsperdesc}
        * Backref \ref{tab:corpussizes}
    * "Preliminary experiments have shown that including short ones led to worse results than excluding, so we excluded."
        * Again \ref{tab:siddata_metadata} (lists number of entities for different word-limits) 
    * That it's REALLY small compared to the others
        * Bei keinem sonderlichen min-word-per-desc threshold hab ich halt XXX samples, bei 50 schon nur noch YYY, das ist wirklich little
        * How I would need to calculate the candidate-word-threshold to have the same one as DESC15 to demonstrate HOW MUCH SMALLER it is
            * how irrelevant the extract-candidtes step of the alrorithm is for my dataset because there are only XXX [was "6k"] unique x-grams anyway so just taking all is the best thing to do anyway

    * Regarding Candidate Words:
            => auch in groß ist mein datensatz ja noch deutlich kleiner als placetypes, die haben immerhin 22k candidates
            --> n-docs: 7596
            --> 1-grams >= 25 times: 5054, 1-5-grams >= 25 times: 6717
            --> unique 1-grams: 106235
            bei placetypes sind es 
            * unique 1-grams: 746180, davon 41320 >= 25 mal und 21833 >= 50 mal (their threshold)
            --> das verhältnis Anzahl Texte zu Länge Texte ist bei mir halt komplett off 
        * ausrechnen "um so gut zu sein wie die, müsste der datensatz größe xyz haben"


#### How I created it

* Preliminary analysis 
    * ref data_exploration_Siddata2021 
    * "if I delete all that are shorter than X, it are |Y|"
    * Preprocessing in kurzem Fließtext beschreiben - "After throwing out all descriptions shorter than xyz chars, 2323 courses where left. 223 of these were ..."
* ref Preprocess_Siddata2022_new
* dass der weg von rehct viel pre-preprocessen zu ZERROOO prepreprocessen geführt hat^^
    * Meine Pre-Preprocessing Schritte die da ja auch noch gut rumfiltern und rummergen beschreiben
    * Mir ist bewusst wie viele Kurse auch nach dem bisschen preprocessing was ich mache drin sind deren Beschreibung schlicht lautet “Tutoren: Susi Sorglos und Willi Wacker”
