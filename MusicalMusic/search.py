import requests
import bs4
import urllib


def search(song):
  """Static search function"""
  
  query = {"text": song}
  search = requests.get(f"https://musescore.com/sheetmusic?{urllib.parse.urlencode(query)}").text
  soup = bs4.BeautifulSoup(search, "html.parser")
  listoftitles = []
  for i in soup.findAll("div", {"class":"col-right"}):
    listoftitles.append(
      {"id": i.find("a")["href"].split("/")[-1],
      "title": i.find("a").text.strip(),
      "instruments": i.find("div", {"class": "instruments"}).text,
      "duration": i.findAll("span")[2].text,
      "pages": int(i.findAll("span")[1].text.split(" ")[0]),
      "views": int(i.findAll("span")[4].text.split(" ")[0].replace(",","")),
      "author": {
        "username": i.find("article").text.split("\n")[1],
        "user_id": i.find("article").find("a")["href"].split("/")[-1]
        },
      "desc":i.find("div", {"class": "expander"}).text}
    )
  return listoftitles
