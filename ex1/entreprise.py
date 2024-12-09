class Entreprise:
    def __init__(self, nom: str, adresse: str, siret: str) -> None:
        self.nom = nom
        self.adresse = adresse
        self.siret = siret

    def __str__(self) -> str:
        return f"L'entreprise {self.nom}, ayant son siège social au {self.adresse}, possède le numéro de SIRET {self.siret:14d}";


    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, value: str) -> None:
        self.__nom = value

    @property
    def adresse(self) -> str:
        return self.__adresse

    @adresse.setter
    def adresse(self, value: str) -> None:
        self.__adresse = value

    @property
    def siret(self) -> int:
        return self.__siret

    @siret.setter
    def siret(self, value: str) -> None:
        if len(value) == 14 and value.isdigit():
            self.__siret = int(value)
        else:
            raise ValueError('Numéro SIRET erroné')
