import re
import requests
from urllib.parse import quote


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
        print("Amazon n'a pas répondu correctement.")
        return

    html = response.text

    titres = re.findall(
        r'<span class="a-size-base-plus a-color-base a-text-normal">(.*?)</span>',
        html,
        re.DOTALL
    )

    prix = re.findall(
        r'<span class="a-price-whole">(.*?)</span>',
        html,
        re.DOTALL
    )

    liens = re.findall(
        r'<a class="a-link-normal s-no-outline" href="([^"]+)"',
        html
    )

    print("=" * 60)
    print("                 AMAZON")
    print("=" * 60)

    if not titres:
        print("Aucun résultat trouvé.")
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
        print("Aucun résultat trouvé.")
        return

    resultats = []

    for titre in titres:
        if titre not in resultats:
            resultats.append(titre)

    for i, titre in enumerate(resultats[:10]):
        print(f"\n{i + 1}. {titre}")


def youtube_searcher():
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
            print("Tu dois entrer une recherche.")
            continue

        if choix == "3":
            recherche_youtube(recherche)

        input("\nAppuie sur Entrée pour continuer...")

if __name__ == "__main__":
    youtube_searcher()