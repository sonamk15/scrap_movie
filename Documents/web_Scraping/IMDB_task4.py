from IMDB_task1 import *
from bs4 import BeautifulSoup
from pprint import pprint
import requests
import os
import json
movies = scrape_top_list(trs)

movie_urls = []
for i in movies:
    movie_urls.append(i["url"])
# print (movie_urls)
store=[]
def scrape_movie_detial(url):
    movies_detial_dic ={}
    for URL in (url[:10]):
        page = requests.get(URL)
        soup = BeautifulSoup(page.text, "html.parser")
        name = soup.find("div", class_="title_wrapper").h1.text.strip()
        movie_name = ' '
        for i in name:
            if "(" not in i:
                movie_name = (movie_name+i).strip()
            else:
                break
        # print (movie_name)
        Director = []
        director = soup.find("div", class_="credit_summary_item").a.text
        Director.append(director)
        # print (Director)

        Gener = []
        gener = soup.find("div", class_="subtext").a.text
        Gener.append(gener)
        # print (Gener)
        runtime = soup.find("div", class_="subtext").time.text.strip()

        run_hour = int(runtime[0])*60
        if 'min' in runtime:
            runmin = int(runtime[3:].strip('min'))
            movie_runtime = run_hour + runmin
        else:
            movie_runtime = run_hour
        # print (movie_runtime)

        bio = soup.find('div', class_="summary_text").text.strip()
        # print (bio)

        poster_link = soup.find('div', class_="poster").a['href']
        image_url = ("https://www.imdb.com"+poster_link)
        # print (image_url')

        lang = soup.find('div', {'id': 'titleDetails'})
        language = []
        for j in lang.find_all('div', {'class': 'txt-block'}):
            if "Country" in (j.text):
                country = j.a.text
            if "Language" in (j.text):
                for i in j.find_all('a'):
                    language.append(i.text)

        movies_detial_dic["name"] = movie_name
        movies_detial_dic["Director"] = Director
        movies_detial_dic["country"] = country
        movies_detial_dic["language"] = language
        movies_detial_dic["poster_image_url"] = image_url
        movies_detial_dic["Bio"] = bio
        movies_detial_dic["movie_runtime"] = movie_runtime
        movies_detial_dic["gener"] = Gener
        store.append(movies_detial_dic)
        with open('movies_detial.json', "w") as file:
            json.dump(store, file, indent=1)

    return store


data=scrape_movie_detial(movie_urls[0])

def  get_movie_list_details(movies):
    scrape_top_list=[]
    for url in movies:
        if url == movies[10]:
            break
        else:
           scrapeMovies = scrape_movie_detial(url)
           scrape_top_list.append(scrapeMovies)
        with open("scrape_top_detial_movie_list.json", "w") as file:
            json.dump(scrape_top_list, file, indent=1)
    return scrape_top_list

pprint(get_movie_list_details(movie_urls))
