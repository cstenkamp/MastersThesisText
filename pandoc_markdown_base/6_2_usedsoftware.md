% * Meckern über used software:
% * nltk's sent_tokenize(*, language=german) trennt sogar "...am Ende des 2. Semesters", oder, even worse, "Relevante Probleme wie z.B. Lautierungsregeln", like seriously?!
% * MDS has bugs
% * Regarding PPMI: DESC15 say it's divided py p_e* = sum_t'(pet'), whereas here [https://stackoverflow.com/questions/58701337/how-to-construct-ppmi-matrix-from-a-text-corpus] they say it's the product
% dass PPMI und auch viele andere Sachen von der größe des Datasets abhängen und exporbitant RAM verbrauchen
% DESC15 nutzt ja "the part-of-speech tagger and chunker from the Open NLP Project [http://opennlp.apache.org/], um Phrases zu finden
