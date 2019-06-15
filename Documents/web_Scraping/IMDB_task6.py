from IMDB_task5 import *
def analyse_movies_language(movie):
    Language = {}
    for i in movie:
        language = i['language']
        count = 1
        for j in language:
            if j not in Language:
                Language[j] = count
            else:
                Language[j] += 1
            count += 1
    return (Language)

pprint(analyse_movies_language(data))