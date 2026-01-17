import csv
from stats_library.strategies import (
    Analyseur,
    Moyenne,
    Mediane,
    EcartType,
    Correlation,
    RegressionLineaire
)
from stats_library.core import JournalCalculs


# ==========================
# Chargement des données CSV
# ==========================
def charger_donnees(filepath):
    donnees = []
    try:
        with open(filepath, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)  # ignorer en-tête si présent
            for row in reader:
                if len(row) >= 2:
                    donnees.append((float(row[0]), float(row[1])))
                elif len(row) == 1:
                    donnees.append(float(row[0]))
    except Exception as e:
        print(f"[ERREUR] Problème lors du chargement : {e}")
        return None
    return donnees


# ==========================
# Affichage des menus
# ==========================
def afficher_menu():
    print("\n" + "=" * 60)
    print("BIBLIOTHEQUE D'ANALYSE STATISTIQUE")
    print("=" * 60)
    print("1. Charger CSV")
    print("2. Choisir méthode et calculer")
    print("3. Afficher données")
    print("4. Consulter journal")
    print("5. Quitter")
    print("=" * 60)


def afficher_methodes():
    print("\nMéthodes statistiques disponibles :")
    print("1 - Moyenne")
    print("2 - Médiane")
    print("3 - Écart-Type")
    print("4 - Corrélation (2 colonnes)")
    print("5 - Régression Linéaire (2 colonnes)")


def choisir_methode():
    afficher_methodes()
    choix = input("Votre choix : ").strip()
    methodes = {
        "1": Moyenne(),
        "2": Mediane(),
        "3": EcartType(),
        "4": Correlation(),
        "5": RegressionLineaire()
    }
    return methodes.get(choix), choix


# ==========================
# Programme principal
# ==========================
def main():
    analyseur = Analyseur()
    journal = JournalCalculs()

    donnees_chargees = None
    donnees_simples = None
    donnees_paires = None
    fichier_actuel = None

    print("Bienvenue dans la Bibliotheque d'Analyse Statistique !")

    while True:
        afficher_menu()
        choix = input("Votre choix : ").strip()

        # -------- 1. Charger CSV --------
        if choix == "1":
            fichier = input("Nom du fichier CSV (Entrée = data.csv) : ").strip()
            if not fichier:
                fichier = "data.csv"

            donnees = charger_donnees(fichier)
            if donnees is None:
                continue

            donnees_chargees = donnees
            fichier_actuel = fichier

            if isinstance(donnees[0], tuple):
                donnees_paires = donnees
                donnees_simples = [d[0] for d in donnees]
                print(f"[OK] {len(donnees)} paires chargées depuis '{fichier}'")
            else:
                donnees_simples = donnees
                donnees_paires = None
                print(f"[OK] {len(donnees)} valeurs chargées depuis '{fichier}'")

            print("✔️ Données chargées avec succès.")
            print("➡️ Vous pouvez maintenant choisir les options 2, 3, 4 ou 5.")

        # -------- 2. Choisir méthode --------
        elif choix == "2":
            if donnees_chargees is None:
                print("Charger d'abord des données.")
                continue

            methode, num_methode = choisir_methode()
            if methode is None:
                print("Choix de méthode invalide.")
                continue

            # ⚠️ Cas méthodes nécessitant (X,Y)
            if num_methode in ["4", "5"] and donnees_paires is None:
                message = "Cette méthode nécessite des paires (X,Y)"
                print(f"[ERREUR] {message}")

                journal.enregistrer(
                    methode.__class__.__name__,
                    message,
                    status="ECHEC"
                )
                continue

            donnees_a_utiliser = (
                donnees_paires if num_methode in ["4", "5"] else donnees_simples
            )

            try:
                analyseur.set_methode(methode)
                resultat = analyseur.executer_analyse(donnees_a_utiliser)

                print(f"[RESULTAT] {methode.__class__.__name__} : {resultat}")

                if num_methode == "5":
                    a, b = resultat
                    print(f"Équation : y = {a:.4f}x + {b:.4f}")

            except Exception as e:
                print(f"[ERREUR] {e}")

        # -------- 3. Afficher données --------
        elif choix == "3":
            if donnees_chargees is None:
                print("Aucune donnée chargée.")
            else:
                print(f"Données depuis '{fichier_actuel}' :")
                print(donnees_chargees[:10], "...")

        # -------- 4. Journal --------
        elif choix == "4":
            logs = journal.consulter()
            if not logs:
                print("Journal vide.")
            else:
                print("\nJournal des calculs :")
                print("-" * 60)
                for i, log in enumerate(logs, 1):
                    print(
                        f"{i}. [{log['date']}] {log['methode']} "
                        f"| {log['status']} → {log['resultat']}"
                    )
                print("-" * 60)

        # -------- 5. Quitter --------
        elif choix == "5":
            print("Au revoir !")
            break

        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
