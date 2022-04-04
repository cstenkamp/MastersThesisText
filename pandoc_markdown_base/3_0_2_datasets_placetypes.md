<!-- 
VON JOHANNES: 
"Wo geht mein Argument für diese subsection hin?!"
-> Nutzen das auch zum gucken ob wir fehler in der implentation haben, und wenn wir dann SIDDATA drauf schmeißen können wir sehen wie gut das performt und ob das aussagekräftig ist.

Der Train of thought ist sehr gut, ABER NICHT STIMMIG IN DIESER SECTION
=> workflow section!! (Oder direkt unter methods, ist eine sehr schöne überleitung dazu dann erstmal die datasets zu beschreiben und was die datasets aus der literatur ausmacht ==> Der einleitene Absatz von hier ist vollkommen valide dafür, kann ich stattdessen einfach in 3.0 packen

-->

DATASETS:PLACETYPES SECTION PRE-TEXT

* Didn't do the openCYC taxonomy bc they say that they don't use one level of the taxonomy consistently but also never explain where they go to which level
* The fact that this dataset is created precisely to be good for the respective algorithm, in contrast to mine!
* Ref link for Geonames categories: http://www.geonames.org/export/codes.html
* look/think was die anderen auszeichnet - bei dem placetypedataset ists ja gar kein fließtext sondern direkt ein bag-of-tags
* TODO: link geonames and foursquare and say how many entities have a class


So, infos from \cite{Derrac2015}:
* GeoNames has 667 place-types in 9 categories (403 used)
* Foursquare has 435 place-types in 9 top-level categories (391 used))
* content: tags of Flickr photos. Photos assumed to be of a type if one of the tags is the name of that type (so they queried for photos with that tag), and then all other tags of that picture make up the BoW.
* 22816139 photos, types with less than 1000 photos removed.



Also tried the Plactypes-Dataset used by all main-paper-authors. When doing so I noticed that there are definitely duplicates (which are consistently recognized as closest-terms in embedding):
  abandoned rail road and abandoned railroad
  boat yard and boatyard
  coral reef and reef
  court house and courthouse
  grass land and grassland
  sheep fold and sheepfold
  skate park and skatepark
  steak house and steakhouse
  water fall and waterfall
  wind mill and windmill

Next to that, the embedding however also sees very similar ones as very similar, which is a nice sanity-check, eg.

  abandoned farm and abandoned home
  airfield and airport
  airport and airport terminal
  ancient site and archaeological site
  arch and arch bridge
  art gallery and art museum
  coffee house and coffee shop
  aircraft cabin and airplane cabin
  apartment and apartment building
  bank and bank building
  field hockey field and hockey field

