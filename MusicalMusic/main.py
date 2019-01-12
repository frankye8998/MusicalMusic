import urllib
import bs4
import requests

from .exceptions import *

class MusicalMusic:

  def __init__(self, username, password):

    url = "https://musescore.com/user/login"
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text, "html.parser")
    csrf = soup.find("meta", {"name": "csrf-token"})["content"]
    
    url = "https://musescore.com/user/auth/login/process"
    cookies = {"mu_browser_uni": r.cookies['mu_browser_uni'], "_csrf": r.cookies["_csrf"]}
    data = {"username": username, "password": password, "_csrf": csrf, "op" : "Log in"}

    try:
      mu_user = requests.post(url, data=data, cookies=cookies, allow_redirects=False).cookies["mu_user"]
    except KeyError:
      raise InvalidCredentials("Please check your username and password!")
    mu_browser_uni = r.cookies['mu_browser_uni']

    self.musescoreToken = ('cookie', f"mu_browser_uni={mu_browser_uni}; mu_user={mu_user}")
  def search(self, song):
    query = {"text": song}
    search = requests.get("https://musescore.com/sheetmusic?" + urllib.parse.urlencode(query)).text
    soup = bs4.BeautifulSoup(search, "html.parser")
    listoftitles = []
    for i in soup.findAll("div", {"class":"col-right"})[:10]:
      listoftitles.append({i.find("a")["href"].split("/")[-1]: [i.find("a").text.strip(), i.find("div", {"class": "instruments"}).text, i.findAll("span")[2].text]})
    return listoftitles


  def download(self, id, filename, extension = "mp3"):
    if extension not in ["mp3", "pdf", "mid", "mxl", "mscz"]:
      raise InvalidFileExtension("Must be mp3, pdf, mid, xml, or mscz.")
    newlink = f"https://musescore.com/score/{id}/download/{extension}"
    opener = urllib.request.build_opener()
    opener.addheaders = [self.musescoreToken]
    urllib.request.install_opener(opener)
    try:
      urllib.request.urlretrieve(newlink, filename)
    except urllib.error.HTTPError:
      raise InvalidScoreID("The ID of the score is invalid!")
