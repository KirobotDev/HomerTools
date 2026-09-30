import webbrowser
import requests
from urllib.parse import quote_plus
from sont_selection import son_selection

def username_lookup() -> str | int:
    son_selection()
    username = input("Username : ")

    recherche = f"{username}"

    url = ("https://github.com/search?q=") + quote_plus(recherche)

    url2 = "https://www.instagram.com/" + quote_plus(recherche)

    url3 = "https://www.tiktok.com/@" + quote_plus(recherche)

    url4 = "https://www.snapchat.com/@" + quote_plus(recherche)

    url5 = "https://www.facebook.com/" + quote_plus(recherche)

    url6 = "https://www.youtube.com/results?search_query=" + quote_plus(recherche)

    url7 = "https://www.twitch.tv/" + quote_plus(recherche)

    print(f"Recherche de : {recherche}")

    webbrowser.open(url)
    webbrowser.open(url2)
    webbrowser.open(url3)
    webbrowser.open(url4)
    webbrowser.open(url5)
    webbrowser.open(url6)
    webbrowser.open(url7)

    print(url)
    print(url2)
    print(url3)
    print(url4)
    print(url5)
    print(url6)
    print(url7)

if __name__ == "__main__":
    username_lookup()