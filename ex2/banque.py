# ⚠ alias d'imports précédés de _ pour limiter la transitivité d'exports. (convention)
from datetime import date as _date
import random as _random
import string as _string

from client import Client as _Client
from classproperty import classproperty


class CompteBancaire:
    """
    Représentation d'un compte bancaire.

    Class properties:
        somme_soldes    Somme des soldes de tous les comptes bancaires

    Properties:
        identifiant     Identifiant du compte bancaire
        date            Date de création du compte
        client          Client possédant le compte
        solde           Solde du compte
    """
    __clients: [_Client] = []

    def __init__(self, date: str, client: _Client, solde: float) -> None:
        self.__discriminant_id = "".join(_random.choices(_string.ascii_uppercase, k=4))

        self.date = date
        self.client = client
        self.solde = solde

        CompteBancaire.__clients.append(self)


    # ⚠ __repr__ est préféré à __str__ pour les affichages type debug :)
    def __repr__(self) -> str:
        identifiant = self.identifiant
        date_creation = self.date
        client = self.client
        solde = self.solde
        return f'{type(self).__name__}({identifiant=}, {date_creation}, {client=}, {solde=})'


    def __eq__(self, other: object) -> bool:
        if isinstance(other, CompteBancaire):
            return self.solde == other.solde

        return False


    # ⚠ J'aurais pu travailler avec un attribut statique et une méthode statique (pas une propriété)…
    # Mais le sujet demande une propriété…
    # C'est impossible comme ça mais… Voyez plutôt ;)
    @classproperty
    def somme_soldes(cls) -> float:
        """
        [class property]
        get -> float
            Somme des soldes de tous les comptes bancaires.
        """
        return sum(map(lambda c: c.solde, cls.__clients))


    @property
    def identifiant(self) -> str:
        """
        get -> str
            Identifiant interne du compte bancaire.
        """
        date = self.date.strftime('%d%m%Y')
        return f'{self.__discriminant_id}{date}'

    @property
    def date(self) -> _date:
        """
        get -> date
            Date de création du compte bancaire.

        set(str)
            Réassigner cette valeur se fait via une chaîne de caractères
            représentant une date au format défini par l'ISO-8601.
        """
        return self.__date

    @date.setter
    def date(self, value: str) -> None:
        try:
            self.__date = _date.fromisoformat(value)
        except ValueError:
            raise ValueError('Date entrée erronée (vérifier format)')

    @property
    def client(self) -> _Client:
        """
        get -> Client
        set(Client)
            Client possédant le compte bancaire.
        """
        return self.__client

    @client.setter
    def client(self, value: _Client) -> None:
        self.__client = value

    @property
    def solde(self) -> float:
        """
        get -> float
        set(float)
            Solde du compte bancaire.
        """
        return self.__solde

    @solde.setter
    def solde(self, value: float) -> None:
        self.__solde = value
