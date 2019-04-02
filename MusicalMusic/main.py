import urllib

import bs4
import requests

from .exceptions import *


class MusicalMusic:
    """Musescore actions requiring an account."""

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
          "op": "Log in"
        }
        try:
            mu_user = requests.post(url,
                                    data=data,
                                    cookies=cookies,
                                    allow_redirects=False,
                                    ).cookies["mu_user_new"]
        except KeyError as e:
            raise InvalidCredentials(
                "Please check your username and password!") from e

        mu_browser_uni = r.cookies['mu_browser_uni']

        self.mu_browser_uni = mu_browser_uni
        self.mu_user = mu_user

    def retrieve(self, id, format="pdf"):
        """Retrieves Musescore data in bytes"""

        if format not in ["mp3", "pdf", "mid", "mxl", "mscz"]:
            raise InvalidFileExtension("Must be mp3, pdf, mid, mxl, or mscz.")
        newlink = f"https://musescore.com/score/{id}/download/{format}"
        cookies = {"mu_browser_uni": self.mu_browser_uni,
                   "mu_user_new": self.mu_user}
        bytes = requests.get(newlink, cookies=cookies, verify=False)
        if bytes.status_code != 200:
            raise InvalidScoreID(str(bytes.status_code))
        return bytes.content

    def download(self, id, filename, format="mp3"):
        if format not in ["mp3", "pdf", "mid", "mxl", "mscz"]:
            raise InvalidFileExtension("Must be mp3, pdf, mid, mxl, or mscz.")
        newlink = f"https://musescore.com/score/{id}/download/{format}"
        opener = urllib.request.build_opener()
        cookieString = f"mu_browser_uni={self.mu_browser_uni};" \
                        f"mu_user_new={self.mu_user}"
        opener.addheaders = [("cookie", cookieString)]
        urllib.request.install_opener(opener)
        try:
            urllib.request.urlretrieve(newlink, filename)
        except urllib.error.HTTPError:
            raise InvalidScoreID("The ID of the score is invalid!")

