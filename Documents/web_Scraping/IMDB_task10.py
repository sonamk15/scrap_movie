from IMDB_task4 import *

data=scrape_movie_detial(movie_urls)

def analyse_language_and_directors(movies):
    language_and_directors={}
    for i in movies:
        language=i['language']
        director = i['Director']
        for key in director:
            language_and_directors[key]={}
            c=1
            for v in language:
                if v not in language_and_directors[key]:
                    language_and_directors[key][v]=c
                else:
                    language_and_directors[key][v]+=1
            
    return (language_and_directors)

pprint(analyse_language_and_directors(data))