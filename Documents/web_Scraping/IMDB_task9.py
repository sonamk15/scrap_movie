from IMDB_task1 import *
import random
import time 
movie_urls = []
for i in movies:
    movie_urls.append(i["url"])
# print (movie_urls)

store = []
def impleimentCaching(url):
    movies_detial_dic = {}

    for i in url:
        URL= i
        link = URL[27:]
        link_url = ' '
        for i in link:
            if '/' in i:
                break
            else:
                link_url+=i
        cach_file = link_url+".json"

        if os.path.exists('./movie_details/'+cach_file):
            with open('./movie_details/'+cach_file,"r") as file:
                data_read = file.read()
                return(data_read)

        sec_time = random.randint(1,3)
        time.sleep(sec_time) 
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
        # store.append(movies_detial_dic)
        with open('./movie_details/'+cach_file, "w") as file:
            json.dump(movies_detial_dic, file, indent=1)

    return movies_detial_dic
    
pprint(impleimentCaching(movie_urls))

# IMDB_task9.py