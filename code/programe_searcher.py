import webbrowser
from urllib.parse import quote_plus

def programme_searcher() -> None:
    try:
        Toolsname = input("Search : ")

        rechercheGit = f"{Toolsname}"

        urlGit = ("https://github.com/search?q=") + quote_plus(rechercheGit)

        print(f"Recherche de : {rechercheGit}")

        webbrowser.open(urlGit)

        print(urlGit)
    except Exception as e:
        print(f"Error {e}")
        raise
    return

if __name__ == "__main__":
    programme_searcher()