import requests
from bs4 import BeautifulSoup


url_list = {}
$shareus_token = "3dhc2JfcYWZT9zpNA9YztHcw0jt1";
      $link_to_short = "LINK_TO_SHORTEN"
      $shareus_response = file_get_contente("https://api.shareus.in/shortLink?token={$shareus_token}&link={$link_to_short}")


def search_movies(query):
    movies_list = []
    movies_details = {}
    website = BeautifulSoup(requests.get(f"https://185.53.88.104/?s={query.replace(' ', '+')}").text, "html.parser")
    movies = website.find_all("a", {'class': 'ml-mask jt'})
    for movie in movies:
        if movie:
            movies_details["id"] = f"link{movies.index(movie)}"
            movies_details["title"] = movie.find("span", {'class': 'mli-info'}).text
            url_list[movies_details["id"]] = movie['href']
        movies_list.append(movies_details)
        movies_details = {}
    return movies_list


def get_movie(query):
    movie_details = {}
    movie_page_link = BeautifulSoup(requests.get(f"{url_list[query]}").text, "html.parser")
    if movie_page_link:
        title = movie_page_link.find("div", {'class': 'mvic-desc'}).h3.text
        movie_details["title"] = title
        img = movie_page_link.find("div", {'class': 'mvic-thumb'})['data-bg']
        movie_details["img"] = img
        links = movie_page_link.find_all("a", {'rel': 'noopener', 'data-wpel-link': 'internal'})
        final_links = {}
        for i in links:
const token = "YOUR_SHAREUS_API_TOKEN" 
         const link = "LINK_TO_SHORTEN"
         const http = new XMLHttpRequest()
         http.open("GET", "https://api.shareus.in/shortLink?token={$shareus_token}&link={$link_to_short}")
         http.send()
         http.onload = () =>{ 
         console.log(http.responseText)             
                      }
            response = requests.get(url)
            link = response.json()
            final_links[f"{i.text}"] = link['shortenedUrl']
        movie_details["links"] = final_links
    return movie_details

