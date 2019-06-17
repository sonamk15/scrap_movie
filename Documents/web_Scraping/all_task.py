from bs4 import BeautifulSoup
import requests
import os
import json
from pprint import pprint
URL = "https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
page = requests.get(URL)
soup = BeautifulSoup(page.text, "html.parser")
tbody = soup.find('tbody', class_="lister-list")
trs = tbody.find_all("tr")
whole_data = []
# i=trs[0]
# link=i.find("a",href=True)["href"]
# print link
# url=  "https://www.imdb.com"+link
# print url
# Task 1


def scrape_top_list(trs):
    i = 0
    for i in trs:
        new = {}

        name = i.find('td', class_="titleColumn").a.text

        position = i.find(
            'td', class_="titleColumn").get_text().strip().split()
        position = int(position[0].strip("."))

        year = i.find('td', class_="titleColumn").span.get_text()

        rating = i.find("td", class_="ratingColumn").text

        link = i.find("a", href=True)["href"]
        url = "https://www.imdb.com"+link

        new['name'] = name
        new['position'] = (position)
        new['year'] = (year[1:5])
        new['rating'] = float(rating)
        new['url'] = url

        whole_data.append(new)

        with open("movies_detial.json", "w") as file:
            json.dump(whole_data, file, indent=1)

    return whole_data


# pprint(scrape_top_list(trs))


movies = scrape_top_list(trs)

years = []
movie_dic = {}


def group_by_year(movies):
    for i in movies:
        if i["year"] not in years:
            years.append(i["year"])
            j = i["year"]
            movie_dic[j] = []
            for i in movies:
                if str(j) == str(i["year"]):
                    movie_dic[j].append(i)

        # with open("Group_by_year.json", "w") as file:
            # json.dump(movie_dic, file, indent=1)

    return movie_dic


movie_dec = group_by_year(movies)
# pprint(movie_dec)


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
        # with open("Decade_by_year.json", "w") as file:
            # json.dump(movie_all_dec, file, indent=1)

    return (movie_all_dec)


# pprint(group_by_decade(movies))
movie_urls = []
for i in movies:
    movie_urls.append(i["url"])
# print (movie_urls)


# task 12th
def  scrape_movie_cast(url):
    cast=[]
    page=requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    table=soup.find('table',class_="cast_list")
    trs=table.find_all('tr')
    for tr in trs:
        td=tr.find_all('td',class_='')
        cast_movie={}
        for actor in td:
            name=actor.find('a').get_text().strip()
            imdb_id=actor.find('a',href=True)["href"]
            imdb_id = (imdb_id[6:15])
            cast_movie['imdb_id']=imdb_id
            cast_movie['name']=name
            cast.append(cast_movie)

            
    return cast
        


def scrape_movie_detial(url):
    # 13th task
    cast=scrape_movie_cast(url) 
    page = requests.get(url)
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
    movies_detial_dic = {}

    movies_detial_dic["name"] = movie_name
    movies_detial_dic["Director"] = Director
    movies_detial_dic["country"] = country
    movies_detial_dic["language"] = language
    movies_detial_dic["poster_image_url"] = image_url
    movies_detial_dic["Bio"] = bio
    movies_detial_dic["movie_runtime"] = movie_runtime
    movies_detial_dic["gener"] = Gener
    movies_detial_dic['cast']=cast


    # with open("per_movie_detials.json", "w") as file:
        # json.dump(movies_detial_dic, file, indent=1)

    return movies_detial_dic


# scrape_movie_detial(movie_urls[0])

# pprint(scrape_movie_detial(movie_urls[0]))
# task 5
def  get_movie_list_details(movies):
    scrape_top_list=[]
    for url in movies:
        if url == movies[10]:
            break
        else:
           scrapeMovies = scrape_movie_detial(url)
           scrape_top_list.append(scrapeMovies)
        with open("scrape_top_movie.json", "w") as file:
            json.dump(scrape_top_list, file, indent=1)

    return scrape_top_list

# task 10
data=(get_movie_list_details(movie_urls))

def analyse_language_and_directors(movies):
    language_and_directors={}
    c=1
    for i in movies:
        language=i['language']
        director = i['Director']
        for key in director:
            if key not in language_and_directors:
                language_and_directors[key]={}
            for v in language:
                if v not in language_and_directors[key]:
                    language_and_directors[key][v]=c
                else:
                    language_and_directors[key][v]+=1
    return (language_and_directors)

# pprint(analyse_language_and_directors(data))

# task 11
def  analyse_movies_genre(movies):
    genre_dictionary={}
    for i in movies[:5]:
        genre=i['gener']
        # print (genre)
        count=1
        for j in genre:
            if j not in genre_dictionary:
                genre_dictionary[j]=count
            else:
                genre_dictionary[j]+=1
    return genre_dictionary
    # analyse_movies_genre(data)


# pprint(analyse_movies_genre(data))
# movie_list=get_movie_list_details(movie_urls)
# def  analyse_co_actors(movie_list):
#     actors_dict = {}
# 	for movie in movies_list:
# 		actors_dict[movie['cast'][0]['imdb_id']] = {
# 		'name':movie['cast'][0]['name'],'frequent_co_actors':[]}
# 	    co_actors_dict = {'imdb_id':'','name':'','num_movies':0}
    # return actors_dict

# 14th task
# movie_list=get_movie_list_details(movie_urls)
def  analyse_co_actors(movie_list):
    dic={}
    actors=[]
    for i in movie_list:
        co_actor=[]
        cast=i['cast']
        count=0
        for j in cast:
            if count==0:
                id=j['imdb_id']
                dic[id]={}
                name=j['name']
                dic[id]['name']=name
                dic[id]['frequent_co_actors']=[]
            else:
                co_actor.append(j['name'])
            count+=1
            if count==6:
                break
      
        for i in co_actor:
            c=0
            dic1={}
        
            for j in movie_list:
                cast1=j['cast']
                for k in cast1:
 				    if (dic[id]['name'] and i) in k['name']:
                        dic1['imdb_id'] = k['imdb_id']
			    		dic1['name'] = k ['name']

            dic[id]['movies_num']=c
            dic[id]['frequent_co_actors'].append(dic1)
            dic1={}
        actors.append(dic)
        dic={}
            
    return actors


pprint(analyse_co_actors(movie_list))
#     actors_dic={}
#     for cast in movie_list:
#         movie_cast=cast['cast']
#         main_id=movie_cast[0]['imdb_id']
#         actors_dic[main_id]={}
#         dict1={}
#         count=1
#         for i in movie_cast[:2]:
#             if i == movie_cast[0]:
#                 name=i['name']
#                 dict1['name']=name
#             else:
#                 co_actor_name=i['name']
#                 co_actor_id=i['imdb_id']
#                 dict1['frequent_co_actors']=[{'name':co_actor_name,'imdb_id':co_actor_id,"num_movies":count}]
#             actors_dic[main_id]=dict1
#         count+=1


#     return actors_dic
# pprint(analyse_co_actors(movie_list))
