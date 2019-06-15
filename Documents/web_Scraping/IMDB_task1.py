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


# Task 1st
def scrape_top_list(trs):
    for i in trs:
        new = {}
        name = i.find('td', class_="titleColumn").a.text

        position = i.find(
            'td', class_="titleColumn").get_text().strip().split()
        position = (position[0].strip("."))

        year = i.find('td', class_="titleColumn").span.get_text()

        rating = i.find("td", class_="ratingColumn").text

        link = i.find("a", href=True)["href"]
        url = "https://www.imdb.com"+link

        new['name'] = name
        new['position'] = int(position)
        new['year'] = (year[1:5])
        new['rating'] = float(rating)
        new['url'] = url

        whole_data.append(new)

        with open("movies_detial.json", "w") as file:
            json.dump(whole_data, file, indent=1)

    return whole_data


# pprint(scrape_top_list(trs))
movies = scrape_top_list(trs)







# pprint(analyse_movies_language(data))



# 1 unic years
# 2. unique year ke same year vale dare data ko ek list me dalna
# 3. unic year ko key banana hai aur list ke data ko value
# [
#     {
#         "name":"Anand",
#         "rating":7.8,
#         "year":1999,

#         "url":"http://www.imdb.com"    return whole_data

#         "potision":1
#     },
# ]
# ek unique year nilalna hai aur us nique year ko key bana hai
# us nique year me uske coursponding year ki sari movie ki detial ko dalna hai
