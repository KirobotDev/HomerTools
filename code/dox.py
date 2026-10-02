import requests
import easyjson
from easyjson import core
import time
from sont_selection import son_selection
from colorama import Fore

chemin = "information.json"
easyjson.write(chemin, '{}')

def discord() -> tuple[ str, int, bool ]:
    son_selection()
    id_discord = input("Met l'id discord que tu veux chercher : ")
    page = input("Met combien de page de resultat tu veux recupèrer (1, 20) : ")

    data = {
        "discord_id": id_discord,
        "per_page": page,
    }

    r = requests.post("https://api.brixhub.ru/api/v1/search", json=data)
    resp = r.json()

    try:
        if r.status_code == 200:
            results = resp['data']['results']
            print(results)
            core.write_add(chemin, "discord", results)
            time.sleep(20)

        else:
            print("Error", r.status_code)
            time.sleep(5)

    except (Exception, SyntaxError) as e:
        print(f"Error : {e}")

def perso() -> str:
    son_selection()
    nom = input("Met le nom de la personne que tu veux rechercher : ")
    prenom = input("Met le prénom de la personne que tu veux rechercher : ")
    page = input("Met combien de page de resultat tu veux recupèrer (1, 20) : ")

    data = {
        "nom_famille": nom,
        "prenom": prenom,
        "per_page": page,
    }

    r = requests.post("https://api.brixhub.ru/api/v1/search", json=data)
    resp = r.json()

    try:
        if r.status_code == 200:
            results = resp['data']['results']
            print(results)
            core.write_add(chemin, "perso", results)
            time.sleep(20)

        else:
            print("Error", r.status_code)
            time.sleep(5)

    except (Exception, SyntaxError) as e:
        print(f"Error : {e}")

def email() -> tuple[ str,  int ]:
    son_selection()
    email = input("Met l'id discord que tu veux chercher : ")
    page = input("Met combien de page de resultat tu veux recupèrer (1, 20) : ")

    data = {
        "email": email,
        "per_page": page,
    }

    r = requests.post("https://api.brixhub.ru/api/v1/search", json=data)
    resp = r.json()

    try:
        if r.status_code == 200:
            results = resp['data']['results']
            print(results)
            core.write_add(chemin, "email", results)
            time.sleep(20)

        else:
            print("Error", r.status_code)
            time.sleep(5)

    except (Exception, SyntaxError) as e:
        print(f"Error : {e}")

def dox() -> None:

    choixDox = input(f"""{Fore.RED}
                    ██╗  ██╗ ██████╗ ███╗   ███╗███████╗██████╗     ████████╗ ██████╗  ██████╗ ██╗     ███████╗
                    ██║  ██║██╔═══██╗████╗ ████║██╔════╝██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
                    ███████║██║   ██║██╔████╔██║█████╗  ██████╔╝       ██║   ██║   ██║██║   ██║██║     ███████╗
                    ██╔══██║██║   ██║██║╚██╔╝██║██╔══╝  ██╔══██╗       ██║   ██║   ██║██║   ██║██║     ╚════██║
                    ██║  ██║╚██████╔╝██║ ╚═╝ ██║███████╗██║  ██║       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
                    ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝

                                                            ===== TOOLS DOX =====
                                            1. Discord Lookup

                                            2. Identité Personnel

                                            3. Email lookup
        Choisis un tools de dox : {Fore.RED}{Fore.WHITE}""")

    if choixDox == "1":
        discord()

    elif choixDox == "2":
        perso()

    elif choixDox == "3":
        email()



if __name__ == "__main__":
    dox()
