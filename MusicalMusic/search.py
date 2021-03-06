import requests
import bs4
import urllib
from .exceptions import *


def search(song, sort="relevance"):
    """Static search function"""
    if sort not in ["relevance", "date_uploaded", "comment_count", "view_count"]:
        raise InvalidSearchSort("Results must be sorted by either \"relevance\", \"date_uploaded\", \"comment_count\", or \"view_count\"")
    query = {"text": song, "sort": sort}
    search = requests.get(f"https://musescore.com/sheetmusic?"
                          f"{urllib.parse.urlencode(query)}").text
    soup = bs4.BeautifulSoup(search, "html.parser")
    listoftitles = []
    for i in soup.findAll("div", {"class": "col-right"}):
        listoftitles.append({
            "id": i.find("a")["href"].split("/")[-1],
            "title": i.find("a").text.strip(),
            "instruments": i.find("div", {"class": "instruments"}).text,
            "duration": i.findAll("span")[2].text,
            "pages": int(i.findAll("span")[1].text.split(" ")[0]),
            "views": int(i.findAll("span")[4].text.split(" ")[0]
                         .replace(",", "")),
            "author": {
                "username": i.find("article").text.split("\n")[1],
                "user_id": i.find("article").find("a")["href"].split("/")[-1]
            },
            "desc": i.find("div", {"class": "expander"}).text}
        )
    return listoftitles
