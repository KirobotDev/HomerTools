import random
import os
import string
import requests
from colorama import Fore
# Install with - pip install measyjson
import easyjson
from easyjson import core

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

chemin = "github.json"

def githuhchecker():
        os.system("cls")
        main = int(input(f"""{Fore.BLUE}
             ██████╗ ██╗████████╗██╗  ██╗██╗   ██╗██████╗      ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗
            ██╔════╝ ██║╚══██╔══╝██║  ██║██║   ██║██╔══██╗    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
            ██║  ███╗██║   ██║   ███████║██║   ██║██████╔╝    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
            ██║   ██║██║   ██║   ██╔══██║██║   ██║██╔══██╗    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
            ╚██████╔╝██║   ██║   ██║  ██║╚██████╔╝██████╔╝    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
             ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝      ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

            Met le nombre d'essaye a fair : """))
        os.system("cls")
        try:
            if main >= 10:
                easyjson.write(chemin, "{}")
                for i in range(main):
                    try:
                        pseudo = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
                        url = f"https://api.github.com/users/{pseudo}"
                        response = requests.get(url, headers=HEADERS, timeout=10)

                        if response.status_code == 404:
                            easyjson.write_add(chemin, "pseudo", pseudo)

                        elif response.status_code == 200:
                            print("Le pseudo est deja pris", pseudo)
                        else:
                            print(f"Erreur GitHub ({response.status_code})", pseudo)
                            continue
                    except Exception as e:
                        print(f"Error {e}")
                        raise
        except Exception as e:
            print(f"Error {e}")
            raise

if __name__ == "__main__":
    githuhchecker()