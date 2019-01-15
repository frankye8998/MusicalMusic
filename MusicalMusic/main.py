import urllib

import bs4
import requests

from .exceptions import *

class MusicalMusic:
  """Musescore actions requiring an account, such as downloading and retrieving scores."""

  def __init__(self, username, password):

    url = "https://musescore.com/user/login"
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text, "html.parser")
    csrf = soup.find("meta", {"name": "csrf-token"})["content"]
    
    url = "https://musescore.com/user/auth/login/process"
    
    cookies = {
        "mu_browser_uni": r.cookies['mu_browser_uni'],
        "_csrf": r.cookies["_csrf"]
    }
   
    data = {
      "username": username,
      "password": password,
      "_csrf": csrf,
      "op" : "Log in"
    }

    try:

      mu_user = requests.post(url,
        data=data,
        cookies=cookies,
        allow_redirects=False
      ).cookies["mu_user"]

    except KeyError:
      raise InvalidCredentials("Please check your username and password!")

    mu_browser_uni = r.cookies['mu_browser_uni']

    self.mu_browser_uni = mu_browser_uni
    self.mu_user = mu_user
    self.musescoreToken = ('cookie',
        f"mu_browser_uni={mu_browser_uni}; mu_user={mu_user}")

  def download(self, id, filename, extension = "mp3"):
    """Downloads Musescore file."""

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

  def retrieve(self, id, extension = "mp3"):
    if extension not in ["mp3", "pdf", "mid", "mxl", "mscz"]:
      raise InvalidFileExtension("Must be mp3, pdf, mid, xml, or mscz.")
    newlink = f"https://musescore.com/score/{id}/download/{extension}"

    cookies = {"mu_browser_uni": self.mu_browser_uni,
        "mu_user": self.mu_user}

    bytes = requests.get(newlink, cookies=cookies)
    if bytes.status_code != 200:
      raise InvalidScoreID(str(bytes.status_code))
    return bytes.content

#79AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
