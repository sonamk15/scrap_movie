from IMDB_task1 import *
years = []
movie_dic = {}

# Task 2nd
def group_by_year(movies):
    for i in movies:
        if i["year"] not in years:
            years.append(i["year"])
            j = i["year"]
            movie_dic[j] = []
            for i in movies:
                if str(j) == str(i["year"]):
                    movie_dic[j].append(i)

        with open("Group_by_year.json", "w") as file:
            json.dump(movie_dic, file, indent=1)

    return movie_dic


movie_dec = group_by_year(movies)
print (movie_dec)