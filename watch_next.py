import spacy

def check_films(sentence) :    
    films = []
    films_titles = []
    with open("C:\\Education\\watch_next\\movies.txt", "r+") as item_file:
        lines = item_file.readlines()
        for item in lines :
            line = item.split(':');
            films.append(line[1])
            films_titles.append(line[0])

    nlp = spacy.load('en_core_web_md')
    model_sentence = nlp(sentence_to_compare)
    max_similarity = 0
    max_index = 0
    for index, film in enumerate (films):
        similarity = nlp(film).similarity(model_sentence)
        if similarity > max_similarity :
            max_similarity = similarity
            max_index = index
        print("sm model " + films_titles[index] + " - ", similarity)
    return films_titles[max_index] 

sentence_to_compare = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
next_film = check_films (sentence_to_compare)
print(f"Probably next film will be {next_film}")