

from abc import ABC, abstractmethod


class AlgorithmeTri(ABC):

	@abstractmethod
	def trier(self, publications: list):
        pass
		


class TriChronologique(AlgorithmeTri):
    """Trie par date décroissante."""
    def trier(self, publications: list):
	     return sorted(publications, key=lambda p: p.date, reverse=True)



class FilActualite:
    def __init__(self, algorithme: AlgorithmeTri):
        self.algorithme = algorithme
        

    def trier(self, publications: list) -> list:
        return self.algorithme.trier(publications)
        

    def changer_algorithme(self, nouvel_algorithme: AlgorithmeTri) -> None:
        self.algorithme = nouvel_algorithme
       