from IMDB_task5 import *
def analyse_movies_directors(movie):
    Director = {}
    for i in movie:
        director = i['Director']
        count = 1
        for j in director:
            if j not in Director:
                Director[j] = count
            else:
                Director[j] += 1
            count += 1
    return (Director)


pprint(analyse_movies_directors(data))

