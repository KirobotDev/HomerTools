import os
import time

"""

Tout les contributeur metez les import en desous merci :)

"""

from code.checker import githuhchecker
from code.youtube_searcher import youtube_searcher
from sont_selection import son_selection
from code.usenrame_lookup import username_lookup
from bombe import bombe
from code.dox import dox
from code.programe_searcher import programme_searcher


os.system("color 0C")


def afficher_animation(texte) -> None:
    for caractere in texte:
        print(caractere, end="", flush=True)
        time.sleep(0.002)
    print()


def menu() -> None:
    afficher_animation("""
    ██╗  ██╗ ██████╗ ███╗   ███╗███████╗██████╗     ████████╗ ██████╗  ██████╗ ██╗     ███████╗
    ██║  ██║██╔═══██╗████╗ ████║██╔════╝██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
    ███████║██║   ██║██╔████╔██║█████╗  ██████╔╝       ██║   ██║   ██║██║   ██║██║     ███████╗
    ██╔══██║██║   ██║██║╚██╔╝██║██╔══╝  ██╔══██╗       ██║   ██║   ██║██║   ██║██║     ╚════██║
    ██║  ██║╚██████╔╝██║ ╚═╝ ██║███████╗██║  ██║       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
    ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝

                                        BY W0K00 & HOMER

                                    https://discord.gg/mPEFRA3e
                                https://www.tiktok.com/@homer0.1

                                        ===== MENU PRINCIPAL =====

                                    1. Multi Tools
                                    2. Baize Ta mère

    """)

    choix = input("Met ton choix : ")
    son_selection()

    if choix == "2":
        bombe()

    if choix == "1":
        choix2 = input("""
                        ██╗  ██╗ ██████╗ ███╗   ███╗███████╗██████╗     ████████╗ ██████╗  ██████╗ ██╗     ███████╗
                        ██║  ██║██╔═══██╗████╗ ████║██╔════╝██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
                        ███████║██║   ██║██╔████╔██║█████╗  ██████╔╝       ██║   ██║   ██║██║   ██║██║     ███████╗
                        ██╔══██║██║   ██║██║╚██╔╝██║██╔══╝  ██╔══██╗       ██║   ██║   ██║██║   ██║██║     ╚════██║
                        ██║  ██║╚██████╔╝██║ ╚═╝ ██║███████╗██║  ██║       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
                        ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝

                                                                ===== TOOLS =====

                                            1. USERNAME LOOKUP      4. Programe Searcher

                                            2. DOX                  5. Github Checker

                                            3. Youtube Searcher
                Choisis un tools : """)

        if choix2 == "1":
            username_lookup()

        elif choix2 == "2":
            dox()

        elif choix2 == "3":
            youtube_searcher()

        elif choix2 == "4":
            programme_searcher()

        elif choix2 == "5":
            githuhchecker()


def run() -> None:
    while True:
        os.system("cls")
        menu()


if __name__ == "__main__":
    run()
