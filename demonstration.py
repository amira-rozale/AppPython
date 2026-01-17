"""
ÉTAPE 6 : DÉMONSTRATION COMPLÈTE
=================================

Ce script démontre toutes les fonctionnalités de la bibliothèque d'analyse statistique :
- Chargement de fichiers CSV
- Toutes les méthodes statistiques disponibles
- Journal de calculs (Singleton)
- Changement de stratégie à la volée
- Gestion des erreurs
"""

import csv
import time
from stats_library.strategies import (
    Analyseur,
    Moyenne,
    Mediane,
    EcartType,
    Correlation,
    RegressionLineaire
)
from stats_library.core import JournalCalculs


def charger_donnees(filepath):
    """Charge les données depuis un fichier CSV."""
    donnees = []
    try:
        with open(filepath, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)  # ignorer en-tête si présent
            for row in reader:
                if not row or all(not cell.strip() for cell in row):
                    continue
                if len(row) >= 2:
                    try:
                        donnees.append((float(row[0]), float(row[1])))
                    except ValueError:
                        continue
                elif len(row) == 1 and row[0].strip():
                    try:
                        donnees.append(float(row[0]))
                    except ValueError:
                        continue
    except FileNotFoundError:
        print(f" Fichier '{filepath}' introuvable.")
        return None
    except Exception as e:
        print(f" Erreur lors du chargement : {e}")
        return None
    
    if not donnees:
        print(f" Aucune donnée valide dans '{filepath}'.")
        return None
    
    return donnees


def afficher_separateur(titre):
    """Affiche un séparateur visuel."""
    print("\n" + "=" * 70)
    print(f"  {titre}")
    print("=" * 70)


def demonstration():
    """Démonstration complète de toutes les fonctionnalités."""
    
    print("\n" + "*" * 35)
    print(" " * 20 + "DÉMONSTRATION COMPLÈTE")
    print(" " * 15 + "Bibliothèque d'Analyse Statistique")
    print("*" * 35)
    
    # Initialisation
    analyseur = Analyseur()
    journal = JournalCalculs()
    
    # ========================================================================
    # DÉMONSTRATION 1 : Chargement de fichiers CSV
    # ========================================================================
    afficher_separateur("DÉMONSTRATION 1 : Chargement de fichiers CSV")
    
    print("\n Chargement de data.csv (1 colonne)...")
    donnees_simples = charger_donnees("data.csv")
    if donnees_simples:
        print(f" {len(donnees_simples)} valeurs chargées")
        print(f"   Premières valeurs : {donnees_simples[:5]}...")
    
    print("\n Chargement de data2.csv (2 colonnes)...")
    donnees_paires = charger_donnees("data2.csv")
    if donnees_paires:
        print(f" {len(donnees_paires)} paires chargées")
        print(f"   Premières paires : {donnees_paires[:3]}...")
        # Extraire les valeurs simples pour les méthodes univariées
        donnees_simples_2 = [d[0] for d in donnees_paires]
    
    time.sleep(1)
    
    # ========================================================================
    # DÉMONSTRATION 2 : Méthodes statistiques univariées
    # ========================================================================
    afficher_separateur("DÉMONSTRATION 2 : Méthodes statistiques univariées")
    
    if donnees_simples:
        print(f"\n Analyse des données : {donnees_simples}")
        print(f"   Nombre de valeurs : {len(donnees_simples)}\n")
        
        # Moyenne
        print("1️  MOYENNE")
        analyseur.set_methode(Moyenne())
        resultat = analyseur.executer_analyse(donnees_simples)
        print(f"   Résultat : {resultat:.4f}")
        print(f"   Formule : Σ(xi) / n = {sum(donnees_simples)} / {len(donnees_simples)}")
        time.sleep(0.5)
        
        # Médiane
        print("\n2️  MÉDIANE")
        analyseur.set_methode(Mediane())
        resultat = analyseur.executer_analyse(donnees_simples)
        print(f"   Résultat : {resultat:.4f}")
        donnees_triees = sorted(donnees_simples)
        print(f"   Données triées : {donnees_triees}")
        if len(donnees_triees) % 2 == 0:
            mid = len(donnees_triees) // 2
            print(f"   Calcul : ({donnees_triees[mid-1]} + {donnees_triees[mid]}) / 2")
        else:
            mid = len(donnees_triees) // 2
            print(f"   Valeur centrale : {donnees_triees[mid]}")
        time.sleep(0.5)
        
        # Écart-Type
        print("\  ÉCART-TYPE")
        analyseur.set_methode(EcartType())
        resultat = analyseur.executer_analyse(donnees_simples)
        print(f"   Résultat : {resultat:.4f}")
        moyenne = sum(donnees_simples) / len(donnees_simples)
        variance = sum((x - moyenne)**2 for x in donnees_simples) / (len(donnees_simples) - 1)
        print(f"   Variance : {variance:.4f}")
        print(f"   Écart-type : √{variance:.4f} = {resultat:.4f}")
        time.sleep(0.5)
    
    # ========================================================================
    # DÉMONSTRATION 3 : Méthodes statistiques bivariées
    # ========================================================================
    afficher_separateur("DÉMONSTRATION 3 : Méthodes statistiques bivariées")
    
    if donnees_paires:
        print(f"\n Analyse des paires : {donnees_paires}")
        print(f"   Nombre de paires : {len(donnees_paires)}\n")
        
        # Corrélation
        print("  CORRÉLATION DE PEARSON")
        analyseur.set_methode(Correlation())
        resultat = analyseur.executer_analyse(donnees_paires)
        print(f"   Résultat : {resultat:.4f}")
        if resultat > 0.7:
            print("    Forte corrélation positive")
        elif resultat > 0.3:
            print("    Corrélation positive modérée")
        elif resultat > -0.3:
            print("     Corrélation faible")
        elif resultat > -0.7:
            print("    Corrélation négative modérée")
        else:
            print("    Forte corrélation négative")
        time.sleep(0.5)
        
        # Régression Linéaire
        print("\n  RÉGRESSION LINÉAIRE")
        analyseur.set_methode(RegressionLineaire())
        resultat = analyseur.executer_analyse(donnees_paires)
        pente, intercept = resultat
        print(f"   Pente (a) : {pente:.4f}")
        print(f"   Intercept (b) : {intercept:.4f}")
        print(f"   Équation : y = {pente:.4f}x + {intercept:.4f}")
        
        # Exemple de prédiction
        if donnees_paires:
            x_exemple = donnees_paires[0][0]
            y_pred = pente * x_exemple + intercept
            print(f"\n   💡 Exemple de prédiction :")
            print(f"      Pour x = {x_exemple}, y prédit = {y_pred:.4f}")
            print(f"      Valeur réelle : {donnees_paires[0][1]}")
        time.sleep(0.5)
    
    # ========================================================================
    # DÉMONSTRATION 4 : Changement de stratégie à la volée
    # ========================================================================
    afficher_separateur("DÉMONSTRATION 4 : Changement de stratégie à la volée")
    
    if donnees_simples:
        print("\n Démonstration du patron Strategy")
        print(f"   Données : {donnees_simples[:5]}... (total: {len(donnees_simples)} valeurs)\n")
        
        methodes = [
            ("Moyenne", Moyenne()),
            ("Médiane", Mediane()),
            ("Écart-Type", EcartType())
        ]
        
        for nom, methode in methodes:
            analyseur.set_methode(methode)
            resultat = analyseur.executer_analyse(donnees_simples)
            print(f"   {nom:15} : {resultat:.4f}")
        print("\n    Changement de méthode sans recréer l'analyseur !")
        time.sleep(0.5)
    
    # ========================================================================
    # DÉMONSTRATION 5 : Patron Singleton (Journal)
    # ========================================================================
    afficher_separateur("DÉMONSTRATION 5 : Patron Singleton (Journal)")
    
    print("\n Vérification du patron Singleton :")
    journal1 = JournalCalculs()
    journal2 = JournalCalculs()
    journal3 = JournalCalculs()
    
    print(f"   journal1 is journal2 : {journal1 is journal2}")
    print(f"   journal2 is journal3 : {journal2 is journal3}")
    print(f"   Toutes les instances pointent vers le même objet !\n")
    
    print(f" Nombre total de calculs enregistrés : {len(journal.consulter())}")
    time.sleep(0.5)
    
    # ========================================================================
    # DÉMONSTRATION 6 : Consultation du journal
    # ========================================================================
    afficher_separateur("DÉMONSTRATION 6 : Consultation du journal")
    
    logs = journal.consulter()
    if logs:
        print(f"\n Historique complet des calculs ({len(logs)} entrées) :\n")
        print("-" * 70)
        print(f"{'N°':<4} {'Date':<20} {'Méthode':<20} {'Statut':<10} {'Résultat'}")
        print("-" * 70)
        
        for i, log in enumerate(logs, 1):
            resultat_str = str(log['resultat'])
            if isinstance(log['resultat'], tuple):
                resultat_str = f"({log['resultat'][0]:.4f}, {log['resultat'][1]:.4f})"
            elif isinstance(log['resultat'], (int, float)):
                resultat_str = f"{log['resultat']:.4f}"
            
            # Tronquer si trop long
            if len(resultat_str) > 30:
                resultat_str = resultat_str[:27] + "..."
            
            print(f"{i:<4} {log['date']:<20} {log['methode']:<20} {log['status']:<10} {resultat_str}")
        
        print("-" * 70)
        
        # Statistiques du journal
        succes = sum(1 for log in logs if log['status'] == 'SUCCES')
        echecs = sum(1 for log in logs if log['status'] == 'ECHEC')
        print(f"\n Statistiques :")
        print(f"    Succès : {succes}")
        print(f"    Échecs : {echecs}")
    else:
        print("   Journal vide.")
    
    time.sleep(1)
    
    # ========================================================================
    # DÉMONSTRATION 7 : Gestion des erreurs
    # ========================================================================
    afficher_separateur("DÉMONSTRATION 7 : Gestion des erreurs")
    
    print("\n Test avec données insuffisantes :")
    
    # Test avec liste vide
    print("\n   1. Liste vide :")
    try:
        analyseur.set_methode(Moyenne())
        resultat = analyseur.executer_analyse([])
        print(f"      Résultat : {resultat}")
    except Exception as e:
        print(f"       Erreur : {e}")
        journal.enregistrer("Moyenne", str(e), status="ECHEC")
    
    # Test avec une seule valeur (écart-type)
    print("\n   2. Écart-type avec 1 seule valeur :")
    try:
        analyseur.set_methode(EcartType())
        resultat = analyseur.executer_analyse([10])
        print(f"      Résultat : {resultat}")
    except Exception as e:
        print(f"       Erreur : {e}")
        journal.enregistrer("EcartType", str(e), status="ECHEC")
    
    # Test avec méthode bivariée sur données univariées
    print("\n   3. Corrélation avec données univariées :")
    try:
        analyseur.set_methode(Correlation())
        resultat = analyseur.executer_analyse([10, 20, 30])
        print(f"      Résultat : {resultat}")
    except Exception as e:
        print(f"       Erreur : {e}")
        journal.enregistrer("Correlation", str(e), status="ECHEC")
    
    print("\n    Toutes les erreurs sont enregistrées dans le journal !")
    time.sleep(1)
    
    # ========================================================================
    # RÉSUMÉ FINAL
    # ========================================================================
    afficher_separateur("RÉSUMÉ FINAL")
    
    print("\n Démonstration terminée avec succès !\n")
    print(" Fonctionnalités démontrées :")
    print("   ✓ Chargement de fichiers CSV (1 et 2 colonnes)")
    print("   ✓ Calcul de la moyenne")
    print("   ✓ Calcul de la médiane")
    print("   ✓ Calcul de l'écart-type")
    print("   ✓ Calcul de la corrélation")
    print("   ✓ Calcul de la régression linéaire")
    print("   ✓ Patron Strategy (changement de méthode à la volée)")
    print("   ✓ Patron Singleton (journal unique)")
    print("   ✓ Journalisation de tous les calculs")
    print("   ✓ Gestion des erreurs")
    
    print(f"\n Total de calculs effectués : {len(journal.consulter())}")
    print("\n" + "=" * 70)
    print(" Merci d'avoir suivi cette démonstration !")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    try:
        demonstration()
    except KeyboardInterrupt:
        print("\n\n  Démonstration interrompue par l'utilisateur.")
    except Exception as e:
        print(f"\n\n Erreur inattendue : {e}")
        import traceback
        traceback.print_exc()
