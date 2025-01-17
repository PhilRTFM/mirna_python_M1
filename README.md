# Analyse et Visualisation de Données de microARN

## Description du Projet
Ce projet Python permet d'analyser des données de microARN issus de la base de données mirbase, afin de calculer les pourcentages de bases nucléiques (A, C, G, U) pour chaque espèce, et de générer des graphiques sous forme de camemberts. L'objectif est de fournir une visualisation claire des compositions nucléotidiques par espèce et globalement (sur l'ensemble du jeu de données).

---

## Fonctionnalités

1. **Extraction des espèces :**
   - Identification et extraction des noms d'espèces uniques depuis un fichier `mirna.txt`.
   - Résultat enregistré dans un fichier `species.txt`.

2. **Traitement des données :**
   - Lecture et traitement des données de `mirna.txt` pour associer des espèces à leurs séquences nucléotidiques.

3. **Visualisation des bases nucléotidiques :**
   - Calcul des pourcentages de chaque base (`A`, `C`, `G`, `U`) pour chaque espèce d'intérêt.
   - Génération de graphiques camemberts individuels pour chaque espèce.
   - Création d’un graphique global montrant la composition moyenne.

---

## Structure du Projet

```
.
├── main.py               # Script principal pour exécuter l'analyse et générer les graphiques.
├── functions.py          # Fonctions utilitaires pour le traitement des données et la génération des graphiques.
├── extract_species.py    # Outil annexe pour extraire les noms  d'espèces uniques depuis le fichier mirna brut
├── input/ # Répertoire contenant les fichiers d'entrées.
└──  species.txt           # Liste des espèces d'intérêt (généré par extract_species.py).
└──  mirna.txt             # Fichier contenant les données de microARN.
├── output/               # Répertoire contenant les graphiques générés.
└── README.md             # Documentation du projet.
```

---

## Prérequis

### Logiciels nécessaires
- **Python 3**
- Bibliothèques Python :
  - `matplotlib`
  - `unittest` pour les tests unitaires
### Installation des dépendances

```bash
pip install matplotlib
```

---

## Utilisation

### 0. (Optionnel) Extraction des noms d'espèces
   - Exécutez `extract_species.py` pour extraire les noms d'espèces depuis le fichier `mirna.txt` :

     ```bash
     python extract_species.py
     ```
   - Fournissez les chemins d'accès aux fichiers demandés (ex. `mirna.txt`) et un nom de fichier de sortie (ex. `species.txt`).

### 1. Programme principal : Analyse et visualisation

   - Lancez le script principal `main.py` :

     ```bash
     python main.py
     ```
   - Fournissez les chemins des fichiers nécessaires (`mirna.txt`, `species.txt`) et le dossier de sortie pour les graphiques.

---

## Fonctionnement des Scripts

### `extract_species.py`
- **Objectif :** Extraire les noms d'espèces en identifiant les séquences nucléotidiques et en utilisant leur position dans `mirna.txt`.
- **Résultat :** Écrit les espèces uniques dans `species.txt`.

### `main.py`
1. Lit `species.txt` pour obtenir la liste des espèces d'intérêt.
2. Traite `mirna.txt` pour associer des séquences nucléotidiques à chaque espèce.
3. Calcule les pourcentages de bases nucléotidiques et génère des graphiques pour chaque espèce et globalement.

### `functions.py`
- Contient les fonctions suivantes :
  - **`is_nucleotide_sequence`** : Vérifie si une chaîne est une séquence nucléotidique valide.
  - **`is_valid_species_name`** : Vérifie si un mot correspond au format d’un nom d’espèce.
  - **`process_data`** : Traite les données pour associer des espèces à leurs séquences.
  - **`calculate_base_rates_and_draw_charts`** : Calcule les pourcentages de bases et génère des graphiques pour chaque espèce.
  - **`mean_overall_chart`** : Génère un graphique global des compositions moyennes.

---

## Résultats

- Les graphiques camemberts sont sauvegardés dans le dossier spécifié lors de l'exécution de `main.py`.
- Chaque graphique est nommé selon le format `<nom_espece>_base_composition.png`.
- Un graphique global est enregistré sous le nom `overall_base_composition.png`.

---

## Tests unitaires

Ce projet inclut des tests unitaires dans `tests.py` avec la bibliothèque `unittest` pour valider les fonctions du fichier `functions.py`.
---

## Auteur

- **Philippe Stocker**  
  Étudiant en Master 1 de Bioinformatique à l'Université de Rouen.

---

## Licence

Ce projet est sous licence libre GPL V.3. Consultez le fichier `LICENSE` pour plus d'informations.
