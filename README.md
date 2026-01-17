# Bibliothèque d'Analyse Statistique

Une bibliothèque Python réutilisable pour l'analyse statistique, implémentant les patrons de conception **Strategy** et **Singleton**.

## Table des matières

- [Objectifs pédagogiques](#objectifs-pédagogiques)
- [Architecture](#architecture)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Structure du projet](#structure-du-projet)
- [Patrons de conception](#patrons-de-conception)
- [Méthodes statistiques](#méthodes-statistiques)
- [Exemples](#exemples)
- [Démonstration complète](#démonstration-complète)

##  Objectifs pédagogiques

- **Patron Strategy** : Permet de changer d'algorithme statistique à la volée
- **Patron Singleton** : Assure une instance unique du journal de calculs
- **Programmation orientée objet** : Architecture modulaire et extensible
- **Modularité** : Séparation claire des responsabilités

## Architecture

Le projet est organisé en modules séparés :

```
AppPython-main/
├── stats_library/
│   ├── __init__.py          # Point d'entrée du package
│   ├── core.py              # Interface et Singleton
│   └── strategies.py        # Implémentations des stratégies
├── main.py                  # Interface utilisateur principale
├── demonstration.py         # Script de démonstration (Étape 6)
├── data.csv                 # Fichier CSV exemple (1 colonne)
├── data2.csv               # Fichier CSV exemple (2 colonnes)
└── README.md               # Ce fichier
```

##  Installation

### Prérequis

- Python 3.7 ou supérieur
- Aucune dépendance externe requise (utilise uniquement la bibliothèque standard)

### Installation

1. Clonez ou téléchargez le projet
2. Assurez-vous d'être dans le répertoire du projet :
   ```bash
   cd AppPython-main
   ```

3. Le projet est prêt à être utilisé !

##  Utilisation

### Interface interactive

Lancez le programme principal :

```bash
python main.py
```

Le menu interactif vous permet de :
1. **Charger un fichier CSV** : Importez vos données depuis un fichier CSV
2. **Choisir une méthode et calculer** : Sélectionnez une méthode statistique et exécutez le calcul
3. **Afficher les données** : Visualisez les données chargées
4. **Consulter le journal** : Affichez l'historique de tous les calculs effectués
5. **Quitter** : Fermer l'application

### Format des fichiers CSV

Le programme accepte deux formats de CSV :

**Format 1 colonne** (pour Moyenne, Médiane, Écart-Type) :
```csv
valeur
10
30
31
25
```

**Format 2 colonnes** (pour Corrélation, Régression Linéaire) :
```csv
valeur1,valeur2
15,20
15,23
22,30
25,35
```

**Note** : La première ligne est considérée comme en-tête et est ignorée.

### Démonstration automatique

Pour voir toutes les fonctionnalités en action :

```bash
python demonstration.py
```

##  Structure du projet

### `stats_library/core.py`

Contient les éléments fondamentaux :

- **`MethodeStatistique`** : Interface abstraite (ABC) définissant le contrat `calculer(donnees)`
- **`JournalCalculs`** : Singleton qui enregistre tous les calculs avec date, méthode, résultat et statut

### `stats_library/strategies.py`

Implémentations concrètes des stratégies statistiques :

- **`Moyenne`** : Calcule la moyenne arithmétique
- **`Mediane`** : Calcule la médiane
- **`EcartType`** : Calcule l'écart-type (échantillon)
- **`Correlation`** : Calcule le coefficient de corrélation de Pearson
- **`RegressionLineaire`** : Calcule la régression linéaire (pente et intercept)
- **`Analyseur`** : Classe contextuelle qui utilise une stratégie et enregistre dans le journal

### `main.py`

Interface utilisateur en ligne de commande avec menu interactif.

### `demonstration.py`

Script de démonstration automatique montrant toutes les fonctionnalités.

##  Patrons de conception

### Patron Strategy

Le patron Strategy permet de définir une famille d'algorithmes, de les encapsuler et de les rendre interchangeables. Ici, chaque méthode statistique est une stratégie concrète.

**Avantages** :
- Extensibilité : Ajouter une nouvelle méthode statistique est simple
- Séparation des responsabilités : Chaque stratégie est indépendante
- Flexibilité : Changement de méthode à la volée via `set_methode()`

**Exemple d'utilisation** :
```python
from stats_library import Analyseur, Moyenne, Mediane

analyseur = Analyseur()
donnees = [10, 20, 30, 40, 50]

# Utiliser la moyenne
analyseur.set_methode(Moyenne())
resultat = analyseur.executer_analyse(donnees)  # 30.0

# Changer pour la médiane
analyseur.set_methode(Mediane())
resultat = analyseur.executer_analyse(donnees)  # 30.0
```

### Patron Singleton

Le patron Singleton garantit qu'une classe n'a qu'une seule instance et fournit un point d'accès global à cette instance. Ici, `JournalCalculs` est un Singleton.

**Avantages** :
- Instance unique : Tous les calculs sont enregistrés dans le même journal
- Accès global : N'importe où dans le code, on obtient la même instance
- Persistance : L'historique est conservé pendant toute l'exécution

**Exemple d'utilisation** :
```python
from stats_library import JournalCalculs

journal1 = JournalCalculs()
journal2 = JournalCalculs()

# journal1 et journal2 sont la même instance
print(journal1 is journal2)  # True
```

##  Méthodes statistiques

### 1. Moyenne (`Moyenne`)

Calcule la moyenne arithmétique d'un ensemble de valeurs.

**Formule** : `moyenne = Σ(xi) / n`

**Données requises** : Liste de nombres (1 dimension)

**Exemple** :
```python
donnees = [10, 20, 30, 40, 50]
moyenne = 30.0
```

### 2. Médiane (`Mediane`)

Calcule la valeur médiane (valeur centrale) d'un ensemble de valeurs.

**Données requises** : Liste de nombres (1 dimension)

**Exemple** :
```python
donnees = [10, 20, 30, 40, 50]
mediane = 30.0
```

### 3. Écart-Type (`EcartType`)

Calcule l'écart-type d'un échantillon (formule avec n-1).

**Formule** : `σ = √(Σ(xi - μ)² / (n-1))`

**Données requises** : Liste de nombres (1 dimension), minimum 2 valeurs

**Exemple** :
```python
donnees = [10, 20, 30, 40, 50]
ecart_type ≈ 15.81
```

### 4. Corrélation (`Correlation`)

Calcule le coefficient de corrélation de Pearson entre deux variables.

**Formule** : `r = (nΣxy - ΣxΣy) / √((nΣx² - (Σx)²)(nΣy² - (Σy)²))`

**Données requises** : Liste de tuples (x, y) - 2 dimensions

**Valeurs** : Entre -1 (corrélation négative parfaite) et +1 (corrélation positive parfaite)

**Exemple** :
```python
donnees = [(15, 20), (15, 23), (22, 30), (25, 35), (30, 41)]
correlation ≈ 0.99
```

### 5. Régression Linéaire (`RegressionLineaire`)

Calcule la régression linéaire simple (y = ax + b).

**Formule** :
- Pente : `a = (nΣxy - ΣxΣy) / (nΣx² - (Σx)²)`
- Intercept : `b = (Σy - aΣx) / n`

**Données requises** : Liste de tuples (x, y) - 2 dimensions

**Retour** : Tuple (pente, intercept)

**Exemple** :
```python
donnees = [(15, 20), (15, 23), (22, 30), (25, 35), (30, 41)]
pente, intercept = (1.23, 2.45)
# Équation : y = 1.23x + 2.45
```

##  Exemples

### Exemple 1 : Utilisation basique

```python
from stats_library import Analyseur, Moyenne, JournalCalculs

# Créer un analyseur
analyseur = Analyseur()

# Définir la méthode
analyseur.set_methode(Moyenne())

# Calculer
donnees = [10, 20, 30, 40, 50]
resultat = analyseur.executer_analyse(donnees)
print(f"Moyenne : {resultat}")  # 30.0

# Consulter le journal
journal = JournalCalculs()
logs = journal.consulter()
for log in logs:
    print(f"{log['date']} - {log['methode']} : {log['resultat']}")
```

### Exemple 2 : Changement de stratégie

```python
from stats_library import Analyseur, Moyenne, Mediane, EcartType

analyseur = Analyseur()
donnees = [10, 20, 30, 40, 50]

# Moyenne
analyseur.set_methode(Moyenne())
print(f"Moyenne : {analyseur.executer_analyse(donnees)}")

# Médiane
analyseur.set_methode(Mediane())
print(f"Médiane : {analyseur.executer_analyse(donnees)}")

# Écart-type
analyseur.set_methode(EcartType())
print(f"Écart-type : {analyseur.executer_analyse(donnees)}")
```

### Exemple 3 : Analyse bivariée

```python
from stats_library import Analyseur, Correlation, RegressionLineaire

analyseur = Analyseur()
donnees = [(15, 20), (15, 23), (22, 30), (25, 35), (30, 41)]

# Corrélation
analyseur.set_methode(Correlation())
corr = analyseur.executer_analyse(donnees)
print(f"Corrélation : {corr:.4f}")

# Régression linéaire
analyseur.set_methode(RegressionLineaire())
pente, intercept = analyseur.executer_analyse(donnees)
print(f"Équation : y = {pente:.4f}x + {intercept:.4f}")
```

##  Démonstration complète

Le fichier `demonstration.py` contient une démonstration automatique de toutes les fonctionnalités :

- Chargement de fichiers CSV (1 et 2 colonnes)
- Calcul de toutes les méthodes statistiques
- Affichage des résultats formatés
- Consultation du journal de calculs
- Gestion des erreurs

Pour lancer la démonstration :

```bash
python demonstration.py
```

## 🔧 Extension de la bibliothèque

### Ajouter une nouvelle méthode statistique

1. Créez une nouvelle classe héritant de `MethodeStatistique` :

```python
from stats_library.core import MethodeStatistique

class Variance(MethodeStatistique):
    def calculer(self, donnees):
        if len(donnees) < 2:
            return 0
        avg = sum(donnees) / len(donnees)
        return sum((x - avg)**2 for x in donnees) / (len(donnees) - 1)
```

2. Importez et utilisez-la :

```python
from stats_library.strategies import Analyseur
from votre_module import Variance

analyseur = Analyseur()
analyseur.set_methode(Variance())
resultat = analyseur.executer_analyse([10, 20, 30, 40, 50])
```

##  Notes importantes

- **Gestion des erreurs** : Toutes les erreurs sont enregistrées dans le journal avec le statut "ECHEC"
- **Données vides** : Les méthodes retournent 0 ou (0, 0) pour les données vides
- **Données insuffisantes** : L'écart-type nécessite au moins 2 valeurs
- **Format CSV** : Les lignes vides sont automatiquement ignorées
- **Journal** : Le journal persiste pendant toute l'exécution du programme

##  Auteur

Projet réalisé dans le cadre d'un cours sur les patrons de conception.

##  Licence

Ce projet est fourni à des fins éducatives. par leila et amira 

---

**Version** : 1.0.0  
**Dernière mise à jour** : 2024
