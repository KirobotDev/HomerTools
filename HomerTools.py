import webbrowser
from urllib.parse import quote_plus
import os
import requests
import re
from urllib.parse import quote
import winsound
import time
import subprocess
import json



def son_selection():
    winsound.Beep(8000, 250)


os.system("color 0C")

while True:
    os.system("cls")


    def afficher_animation(texte):
        for caractere in texte:
            print(caractere, end="", flush=True)
            time.sleep(0.002)
        print()


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

    """)

    print("===== MENU PRINCIPAL =====")
    print("1. MULTI-TOOLS")
    print("2. BAIZE TA MERE")

    choix = input("Choisis : ")
    son_selection()

    if choix == "2":

        urlHomer = "https://creator.nightcafe.studio/jobs/NzqkZXD3KUbFp4s4CmrZ/NzqkZXD3KUbFp4s4CmrZ--0--elygq.jpg"

        for i in range(100):
            webbrowser.open(urlHomer)
            subprocess.Popen(
                ["cmd.exe", "/k", f"color 0C & echo FORCE WOULAAA "],

                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
            time.sleep(0.2)




    if choix == "1":
        print("\n===== TOOLS =====")
        print("1. USERNAME LOOKUP ")
        print("2. DOX ")
        print("3. Youtube Searcher ")
        print("4. Programe Searcher ")

        choix2 = input("Choisis un tools : ")
        son_selection()

        if choix2 == "1":


            username = input("Username : ")
            son_selection()

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

        if choix2 == "2":
            print("\n===== TOOLS DOX =====")
            print("1.Discord Lookup")
            print("2.Identité Lookup")
            print("3.Email lookup")

            choixDox = input("Choisis un dox : ")

            if choixDox == "1":
                son_selection()
                url = "https://leak.fun/dashboard/searches/discord"
                webbrowser.open(url)
            if choixDox == "2":
                son_selection()
                url = "https://leak.fun/dashboard/searches/breach"
                webbrowser.open(url)
            if choixDox == "3":
                son_selection()
                url = "https://behindtheemail.com/"
                webbrowser.open(url)

        if choix2 == "3":
            def recherche_amazon(recherche):

                print("\n🔎 Recherche sur Amazon...\n")

                url = "https://www.amazon.fr/s?k=" + quote(recherche)

                headers = {
                    "User-Agent": (
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/131.0 Safari/537.36"
                    )
                }

                response = requests.get(url, headers=headers, timeout=10)

                if response.status_code != 200:
                    print("❌ Amazon n'a pas répondu correctement.")
                    return

                html = response.text

                # Titres
                titres = re.findall(
                    r'<span class="a-size-base-plus a-color-base a-text-normal">(.*?)</span>',
                    html,
                    re.DOTALL
                )

                # Prix
                prix = re.findall(
                    r'<span class="a-price-whole">(.*?)</span>',
                    html,
                    re.DOTALL
                )

                # Liens
                liens = re.findall(
                    r'<a class="a-link-normal s-no-outline" href="([^"]+)"',
                    html
                )

                print("=" * 60)
                print("                 AMAZON")
                print("=" * 60)

                if not titres:
                    print("❌ Aucun résultat trouvé.")
                    return

                for i, titre in enumerate(titres[:10]):

                    titre = re.sub(r"<.*?>", "", titre)
                    titre = titre.replace("&amp;", "&")

                    if i < len(prix):
                        prix_produit = re.sub(r"<.*?>", "", prix[i])
                        prix_produit = prix_produit.strip()
                        prix_produit += " €"
                    else:
                        prix_produit = "Prix inconnu"

                    if i < len(liens):
                        lien = "https://www.amazon.fr" + liens[i]
                    else:
                        lien = "Lien indisponible"

                    print(f"\n{i + 1}. {titre}")
                    print(f"   💰 {prix_produit}")
                    print(f"   🔗 {lien}")


            # ==========================================
            # YOUTUBE
            # ==========================================

            def recherche_youtube(recherche):

                print("\n🔎 Recherche sur YouTube...\n")

                url = "https://www.youtube.com/results?search_query=" + quote(recherche)

                headers = {
                    "User-Agent": (
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/131.0 Safari/537.36"
                    )
                }

                response = requests.get(url, headers=headers, timeout=10)

                if response.status_code != 200:
                    print("❌ YouTube n'a pas répondu correctement.")
                    return

                html = response.text

                titres = re.findall(
                    r'"title":{"runs":\[{"text":"(.*?)"}',
                    html
                )

                print("=" * 60)
                print("                 YOUTUBE")
                print("=" * 60)

                if not titres:
                    print("❌ Aucun résultat trouvé.")
                    return

                resultats = []

                for titre in titres:
                    if titre not in resultats:
                        resultats.append(titre)

                for i, titre in enumerate(resultats[:10]):
                    print(f"\n{i + 1}. {titre}")


            # ==========================================
            # MENU PRINCIPAL
            # ==========================================

            while True:

                print("\n")
                print("=" * 40)
                print("          🔎 Youtube Searcher ")
                print("=" * 40)

                print("3. YouTube")
                print("4. Menu Principal")

                choix = input("\nChoix : ")

                if choix == "4":
                    print("\nTu retournes au menu principal.")
                    break

                if choix not in ["4", "3"]:
                    print("\n Choix invalide.")
                    continue

                recherche = input("\n🔎 Recherche : ")

                if recherche.strip() == "":
                    print("❌ Tu dois entrer une recherche.")
                    continue

                if choix == "3":
                    recherche_youtube(recherche)

                input("\nAppuie sur Entrée pour continuer...")

        if choix2 == "4":
            Toolsname = input("Search : ")

            rechercheGit = f"{Toolsname}"

            urlGit = ("https://github.com/search?q=") + quote_plus(rechercheGit)

            print(f"Recherche de : {rechercheGit}")

            webbrowser.open(urlGit)

            print(urlGit)




