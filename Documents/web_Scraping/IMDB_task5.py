from IMDB_task1 import*
movie_urls = []
for i in movies:
    movie_urls.append(i["url"])
def get_movie_list_details(movies):
    scrape_top_list = []
    for url in movies:
        if url == movies[10]:
            break
        else:
            scrapeMovies = scrape_movie_detial(url)
            scrape_top_list.append(scrapeMovies)
        with open("scrape_top_detial_movie_list.json", "w") as file:
            json.dump(scrape_top_list, file, indent=1)

    return scrape_top_list


# data = get_movie_list_details(movie_urls)
pprint(get_movie_list_details(movie_urls))
