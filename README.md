# benjaminths.github.io

Site du développeur, servi par GitHub Pages sur `https://benjaminths.github.io/`.

## Pourquoi cette structure

```
/                       page d'accueil Enami  ->  https://benjaminths.github.io/
app-ads.txt             validation AdMob      ->  https://benjaminths.github.io/app-ads.txt
padel-idle-site/        site du jeu           ->  https://benjaminths.github.io/padel-idle-site/
build.py                génère padel-idle-site/ dans les six langues
```

Le dépôt s'appelle `benjaminths.github.io` — et pas autrement — pour une raison précise :
GitHub Pages ne sert la **racine** du domaine que depuis un dépôt portant exactement le nom
d'utilisateur. Un dépôt nommé `padel-idle-site` serait servi sous `/padel-idle-site/`, et rien
de ce qu'il contient ne pourrait jamais répondre sur `/app-ads.txt`.

Or le crawler AdMob part de l'URL du site développeur déclarée dans la fiche App Store — côté
Apple, le champ **URL marketing**, pas l'URL d'assistance — puis **ignore le chemin** et lit
`/app-ads.txt` à la racine du domaine. Comme `github.io` est un domaine public, la racine ici
est bien `benjaminths.github.io`.

Donc : `https://benjaminths.github.io/padel-idle-site/app-ads.txt` ne sera **jamais** lu.
`https://benjaminths.github.io/app-ads.txt` l'est.

Le sous-dossier `padel-idle-site/` porte le nom de l'ancien dépôt pour que les URLs déjà
publiées (App Store, moteurs de recherche, liens dans le jeu) répondent à l'identique.

Ne pas renommer le dépôt ni déplacer `app-ads.txt` : la validation AdMob de Padel Idle,
et donc la monétisation du jeu, en dépendent.

## Modifier le site du jeu

Les pages de `padel-idle-site/` sont générées, ne pas les éditer à la main :

```
python3 build.py     # réécrit les 18 pages dans padel-idle-site/
```

Les textes des six langues sont dans le dictionnaire `T` de `build.py`.
La feuille de style `padel-idle-site/style.css` sert aussi à la page d'accueil.

## Modifier app-ads.txt

Une ligne par régie autorisée à vendre l'inventaire du jeu. Format IAB : UTF-8 **sans BOM**,
fins de ligne LF. Si tu ajoutes de la médiation (LevelPlay / ironSource, Unity…), chaque
partenaire fournit ses propres lignes, à ajouter ici en plus de celle d'AdMob.
