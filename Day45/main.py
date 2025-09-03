import requests
from bs4 import BeautifulSoup

request = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
data = request.text

soup = BeautifulSoup(data, "html.parser")
movie_headers = soup.find_all(name="h3", class_ = "title")
movie_list = []
for movie in movie_headers:
    movie_list.append(movie.get_text())

movie_list.reverse()

with open(file="./movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movie_list:
        file.write(movie + "\n")