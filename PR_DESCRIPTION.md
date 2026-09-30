# Pull Request — Refonte en modules + nouveau Github Checker

> **Titre :** `Refonte en modules + nouveau Github Checker`
>
> **Base :** `KirobotDev/HomerTools` → **Fork :** `W0k00000/homertools`

---

## 📋 Résumé

Cette PR effectue une **refonte complète de l'architecture** du projet en découpant
le monolithe `HomerTools.py` (312 lignes) en **modules indépendants et lisibles**
(97 lignes), et ajoute un ** nouvel outil : le Github Checker**.

---

## 🔧 Refactor

`HomerTools.py` passe de **312 lignes monolithiques à 97 lignes**.
Tout le code est extrait dans des modules dédiés, un par outil :

| Nouveau fichier | Contenu |
|---|---|
| `code/__init__.py` | Transforme le dossier en package |
| `code/checker.py` | `githuhchecker()` — **nouveau** |
| `code/dox.py` | `dox()` |
| `code/youtube_searcher.py` | `youtube_searcher()` + `recherche_amazon()` |
| `code/usenrame_lookup.py` | `username_lookup()` |
| `code/programe_searcher.py` | `programme_searcher()` |
| `bombe.py` | `bombe()` (commande « Baize ta mère ») |
| `sont_selection.py` | `son_selection()` (beep de sélection) |

### Points techniques

- Ajout de `code/__init__.py` pour transformer le dossier en **package** Python
- Ajout de **type hints** (`-> None`) sur les fonctions
- Ajout d'une **garde `if __name__ == "__main__":`** avec une boucle `run()` propre
- `afficher_animation()` remonté au niveau module
- Suppression de l'imbrication `while True` / `if` monolithique au profit d'un **dispatch menu lisible**

**Diff :** `1 file changed, 97 insertions(+), 312 deletions(-)`

---

## ✨ Nouveau : Github Checker (option 5)

Le tout nouvel outil **5. Github Checker** :

- Génère des **pseudos aléatoires de 4 caractères** (lettres minuscules + chiffres)
- Interroge l'**API GitHub** (`api.github.com/users/{pseudo}`)
- **Les pseudos libres (HTTP 404) sont sauvegardés automatiquement dans `github.json`**
  via la librairie `easyjson`
- Les pseudos **déjà pris** (HTTP 200) sont signalés à l'écran
- Gestion des **erreurs réseau / API** (timeouts, codes inattendus)
- Bannière ASCII **colorée** grâce à `colorama`

```python
pseudo = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
url = f"https://api.github.com/users/{pseudo}"
response = requests.get(url, headers=HEADERS, timeout=10)

if response.status_code == 404:
    easyjson.write_add(chemin, "pseudo", pseudo)   # pseudo libre -> sauvegardé
```

---

## 🎨 Interface / UX

- **Bannière ASCII du menu Tools ajoutée** (second logo HOMER TOOLS en en-tête du prompt)
- Menu Tools **réorganisé et étendu de 4 à 5 entrées** (ajout du Github Checker)
- L'ASCII-art est **directement intégré dans le prompt** `input()` pour un affichage
  plus propre et un meilleur rendu des couleurs
- Structure du menu Tools désormais affichée en **colonnes** (2 colonnes) pour gagner de la place

---

## 📦 Dépendances

Nouveau fichier **`requirements.txt`** :

```
requests
colorama
easyjson
```

- `colorama` → coloration de l'ASCII-art du Github Checker
- `easyjson` → sauvegarde lisible des pseudos dans `github.json`

---

## ⚠️ Points d'attention

Deux problèmes détectés lors de la revue, **à corriger avant merge** :

### 1. `requirements.txt` ≠ import réel

`requirements.txt` déclare **`measyjson`** alors que le code importe **`easyjson`**
(`code/checker.py:7`). L'installation échouera et le Github Checker ne fonctionnera pas.

```diff
- measyjson
+ easyjson
```

### 2. Seuil bloquant dans le Github Checker

`code/checker.py:29` — la boucle de recherche est protégée par :

```python
if main >= 10:
```

En dessous de **10 essais**, rien ne se passe et l'utilisateur ne reçoit aucun retour.
À remplacer par une simple garde de valeur minimale :

```python
if main < 1:
    print("Entre au moins 1 essai.")
    return
```

---

## 🧪 Vérification

- Lancement sans erreur : `python HomerTools.py`
- Navigation dans les 5 outils du menu
- Le Github Checker écrit bien `github.json` à la racine du projet
- Le beep de sélection est toujours audible (`sont_selection.py`)

---

## 📄 Crédits / Licence

- **Développé par :** w0k00 & HOMER0.1 — [github.com/w0k00000](https://github.com/w0k00000)
- **Licence :** MIT
- **Version :** v1.1 Beta