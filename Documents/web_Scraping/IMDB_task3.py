from IMDB_task2 import *



def group_by_decade(movie_decade):

    strating_year = 1950
    dec_years = []
    list_of_years = []
    movie_all_dec = []

    for i in movie_decade:
        list_of_years.append(int(i['year']))
        list_of_years.sort()
    for i in range(strating_year, list_of_years[-1], 10):
        dec_years.append(i)
        dec_years.sort(reverse=True)

    for i in dec_years:
        movie_store_in_dict = {}
        # Creating keys of the decades in which the movies were released
        movie_store_in_dict[i] = []
        for j in movie_decade:
            # print(j)
            if int(j["year"]) >= i and int(j["year"]) <= i+9:
                # Appending all movies of same decades in a list
                movie_store_in_dict[i].append(j)
        movie_all_dec.append(movie_store_in_dict)
        with open("Decade_by_year.json", "w") as file:
            json.dump(movie_all_dec, file, indent=1)

    return (movie_all_dec)


# pprint(group_by_decade(movies))
movie_urls = []
for i in movies:
    movie_urls.append(i["url"])
# print (movie_urls)