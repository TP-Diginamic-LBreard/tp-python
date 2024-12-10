class Entreprise:
    """
    Représentation d'une entreprise.

    Properties:
        nom             Nom de l'entreprise
        adresse         Adresse du siège de l'entreprise
        siret           Numéro de SIRET de l'entreprise (set: str)
    """
    def __init__(self, nom: str, adresse: str, siret: str) -> None:
        self.nom = nom
        self.adresse = adresse
        self.siret = siret

    def __str__(self) -> str:
        return f"L'entreprise {self.nom}, ayant son siège social au {self.adresse}, possède le numéro de SIRET {self.siret:14d}";


    @property
    def nom(self) -> str:
        """
        get -> str
        set(str)
            Nom de l'entreprise.
        """
        return self.__nom

    @nom.setter
    def nom(self, value: str) -> None:
        self.__nom = value

    @property
    def adresse(self) -> str:
        """
        get -> str
        set(str)
            Adresse du siège de l'entreprise.
        """
        return self.__adresse

    @adresse.setter
    def adresse(self, value: str) -> None:
        self.__adresse = value

    @property
    def siret(self) -> int:
        """
        get -> int
            Numéro de SIRET de l'entreprise.

        set(str)
            Réassigner cette valeur se fait via une chaîne de 14 caractères,
            représentant le numéro de SIRET.
        """
        return self.__siret

    @siret.setter
    def siret(self, value: str) -> None:
        if len(value) == 14 and value.isdigit():
            self.__siret = int(value)
        else:
            raise ValueError('Numéro SIRET erroné')
