```
def create_conceptual_space(entities):
    entities = preprocess(entities)
    dtm = create_dtm(entities)
    candidates = dtm.get_words(min_df=25)
    embeddings = mds(dtm)
    good_phrases = []
    for phrase in candidates:
        target = [doc.count(phrase) > 0 for doc in dtm]
        svm.fit(embeddings, target)
        if compare(svm, dtm) > threshold:
            good_phrases.add(svm)
    clusters = cluster_phrases(svm)
    clusters = postprocess(clusters)
    return cs_embedding(entities, clusters)


def preprocess(entities, options):
    for entity in entities:
        # depending on options:
        entity.prepend_title()
        entity.lemmatize()
        # ...
        entity.create_bow()
    return entities

def compare(svm, dtm):
    distances = [svm.distance_to_hyperplane(doc) for doc in dtm]
    counts = [doc.quantification(phrase) 0 for doc in dtm]
    return kappa_score(rank(distances), rank(counts))
        
def cluster_phrases(svm):
    ...

def cs_embedding(entities, clusters):
    new_embed = [cluster.distance(entity) 
                    for cluster in clusters 
                        for entity in entities]
    new_embed = rank(new_embed)
    return new_embed
```