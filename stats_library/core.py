import datetime
from abc import ABC, abstractmethod

class JournalCalculs:
    """Singleton pour journaliser tous les calculs."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(JournalCalculs, cls).__new__(cls)
            cls._instance.logs = []
        return cls._instance

    def enregistrer(self, methode, resultat, status="SUCCES"):
            log_entry = {
                  "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                  "methode": methode,
                  "resultat": resultat,
                  "status": status
                }
            self.logs.append(log_entry)


    def consulter(self):
        return self.logs

class MethodeStatistique(ABC):
    """Interface pour les stratégies statistiques."""
    @abstractmethod
    def calculer(self, donnees):
        pass
