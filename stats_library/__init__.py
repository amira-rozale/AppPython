"""
Bibliothèque d'analyse statistique réutilisable.

Ce package implémente les patrons de conception Strategy et Singleton
pour fournir une bibliothèque modulaire d'analyse statistique.
"""

from stats_library.core import MethodeStatistique, JournalCalculs
from stats_library.strategies import (
    Analyseur,
    Moyenne,
    Mediane,
    EcartType,
    Correlation,
    RegressionLineaire
)

__all__ = [
    'MethodeStatistique',
    'JournalCalculs',
    'Analyseur',
    'Moyenne',
    'Mediane',
    'EcartType',
    'Correlation',
    'RegressionLineaire'
]

__version__ = '1.0.0'
