import requests
import bs4
import urllib


def search(song):
  query = {"text": song}
  search = requests.get(f"https://musescore.com/sheetmusic?{urllib.parse.urlencode(query)}").text
  soup = bs4.BeautifulSoup(search, "html.parser")
  listoftitles = []
  for i in soup.findAll("div", {"class":"col-right"}):
    listoftitles.append({"id": i.find("a")["href"].split("/")[-1], "title": i.find("a").text.strip(), "instruments": i.find("div", {"class": "instruments"}).text, "duration": i.findAll("span")[2].text})
  return listoftitles
