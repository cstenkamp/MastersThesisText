Uhhhm ist es nicht scheißegal ob der ursprüngliche space metrisch (MDS) ist oder nicht, wenn letztlich EBENNICHT nur das koordinatensystem gedreht wird sondern die rankings für die einzelnen word-directions genutzt werden?! weil ob das metrisch ist oder nicht ist doch komplett unabhängig davon obs ursprünglisch metrisch war?!

We're always concerned with points, not with vectors!!! gucken was das für auswirkungen hat!!! (AUCH: points, not convex regions (like CS SHOULD be))

* WHY do they always calculate with cosine-distances (eg in my `select_salient_terms`) - I thought the important thing is that we are talking about POINTS, NOT VECTORS  (also - param-combi for closeness by euclidian distance isntead of that)


* über deren algo
    * dass sie nie erwähnen ob sie bei den shallow decision trees one-vs-rest machen --> HOW DID THEY achieve even okay-ish accuracies with the shallow decision-trees? a depth 3 tree has max 2^3 = 8 leaves, so if your to-be-categorized has 100 classes, you'll definitely suck!
    * dass sie, wenn sie die orthogonalen der decision-planes averagen, definitiv auch den intercept berücksichtigen müssten!
            (...would they? I mean they are only concerned with direction and ranking, so there it's just an added, irrelevant, constant)
    * Dass over all n-dims (20, 50, 100, 200) einfach 21832 (literally alle bis auf einen!) candidates in T^0.1 sind (ALSO FAST ALLE), und T^0.5 könnte schlechtestenfalls 740 (400+200+100+40) werte haben, bestenfalls 400, und hat 697 - soll heißen WELCHE ausgewählt werden ist kraass abhängig von der #dimensions, which is bad
        ==> I would really like to say somthing about the robustness of this algorithm for multiple runs. For that I can either take my own runs which I don't know if they are okay or theirs across dimensions. (Maybe some 2d-plot looking like a confusion matrix showing the overlap of T^0.5 terms, also intersection over union, for different runs (and also for the 4 n-dims in orig desc15))