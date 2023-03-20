#what to watch next program

import spacy

nlp = spacy.load('en_core_web_md')

planet_hulk = "Will he save the their world or destroy it? When the Hulk becomes too dangerous for the Earth, the illuminati trick Hulk into a shuttle and launch him into space to a planet where Hulk can live in peace. unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
films_list = []

with open('movies.txt', 'r') as file:
    for item in file:
        films = item.replace('\n',',')
        films_list.append(films)


def best_film():
    max_similarity = 0
    best_film = ""

    model_sentence = nlp(planet_hulk)
    for film in films_list:
        similarity = nlp(film).similarity(model_sentence)


        if similarity > max_similarity:
            max_similarity = similarity
            best_film = film[:7] 
    print("I really think you will like",best_film)

best_film()
 


