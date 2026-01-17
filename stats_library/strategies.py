import math
from stats_library.core import MethodeStatistique, JournalCalculs

class Moyenne(MethodeStatistique):
    def calculer(self, donnees):
        if not donnees: return 0
        return sum(donnees) / len(donnees)

class Mediane(MethodeStatistique):
    def calculer(self, donnees):
        if not donnees: return 0
        sorted_data = sorted(donnees)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid-1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

class EcartType(MethodeStatistique):
    def calculer(self, donnees):
        if len(donnees) < 2: return 0
        avg = sum(donnees) / len(donnees)
        variance = sum((x - avg)**2 for x in donnees) / (len(donnees) - 1)
        return math.sqrt(variance)

class Correlation(MethodeStatistique):
    """Corrélation entre 2 listes de valeurs."""
    def calculer(self, donnees):
        if len(donnees) < 2: return 0
        try:
            x = [d[0] for d in donnees]
            y = [d[1] for d in donnees]
        except (TypeError, IndexError):
            raise ValueError("Les données doivent être des tuples (x, y)")
        n = len(donnees)

        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(xi*yi for xi, yi in zip(x, y))
        sum_x2 = sum(xi**2 for xi in x)
        sum_y2 = sum(yi**2 for yi in y)

        numerator = n*sum_xy - sum_x*sum_y
        denominator = math.sqrt((n*sum_x2 - sum_x**2)*(n*sum_y2 - sum_y**2))
        if denominator == 0: return 0
        return numerator / denominator

class RegressionLineaire(MethodeStatistique):
    """Régression Linéaire (retourne pente, intercept)."""
    def calculer(self, donnees):
        if len(donnees) < 2: return (0,0)
        try:
            x = [d[0] for d in donnees]
            y = [d[1] for d in donnees]
        except (TypeError, IndexError):
            raise ValueError("Les données doivent être des tuples (x, y)")
        n = len(donnees)

        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(xi*yi for xi, yi in zip(x, y))
        sum_x2 = sum(xi**2 for xi in x)

        denominator = n*sum_x2 - sum_x**2
        if denominator == 0:
            return (0, sum_y/n)

        slope = (n*sum_xy - sum_x*sum_y) / denominator
        intercept = (sum_y - slope*sum_x) / n
        return slope, intercept

class Analyseur:
    """Classe principale qui utilise la stratégie choisie."""
    def __init__(self, methode: MethodeStatistique = None):
        self._methode = methode
        self._journal = JournalCalculs()

    def set_methode(self, methode: MethodeStatistique):
        self._methode = methode

    def executer_analyse(self, donnees):
        if self._methode is None:
            raise ValueError("Aucune méthode définie")

        resultat = self._methode.calculer(donnees)
        self._journal.enregistrer(
            self._methode.__class__.__name__,
            resultat,
            status="SUCCES"
        )
        return resultat
