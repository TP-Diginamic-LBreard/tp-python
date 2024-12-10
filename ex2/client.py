class Client:
    """
    Représentation d'un client de la banque.

    Properties:
        nom             Nom·s du client
        prenom          Prénom·s du client
        adresse         Adresse du client
        nir             Numéro de sécurité sociale / NIR
    """
    def __init__(self, nom: str, prenom: str, adresse: str, nir: int) -> None:
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.nir = nir


    # ⚠ __repr__ est préféré à __str__ pour les affichages type debug :)
    def __repr__(self) -> str:
        nom = self.nom
        prenom = self.prenom
        adresse = self.adresse
        nir = self.nir
        return f'{type(self).__name__}({nom=}, {prenom=}, {adresse=}, {nir=:015d})'


    @property
    def nom(self) -> str:
        """
        get -> str
        set(str)
            Nom·s du client.
        """
        return self.__nom

    @nom.setter
    def nom(self, value: str) -> None:
        self.__nom = value

    @property
    def prenom(self) -> str:
        """
        get -> str
        set(str)
            Prénom·s du client.
        """
        return self.__prenom

    @prenom.setter
    def prenom(self, value: str) -> None:
        self.__prenom = value

    @property
    def adresse(self) -> str:
        """
        get -> str
        set(str)
            Adresse du client.
        """
        return self.__adresse

    @adresse.setter
    def adresse(self, value: str) -> None:
        self.__adresse = value

    @property
    def nir(self) -> int:
        """
        get -> int
            Numéro de sécurité sociale / NIR du client.

        set(str)
            Réassigner cette valeur se fait via une chaîne de 15 caractères,
            représentant le NIR *et* la clef de validation (13+2 caractères).
            Le NIR et sa clef de validation sont vérifiés avant réassignation.
        """
        return self.__nir

    # Bien que ce soit une procédure rare, le NIR *peut* être modifié.
    @nir.setter
    def nir(self, value: str) -> None:
        if len(value) == 15 and value.isdigit():
            num   = int(value)
            clef  = num % 100
            nir   = num // 100
            valid = 97 - (nir % 97) == clef

            if valid:
                self.__nir = num

                # Retour anticipé pour éviter de tomber sur l'erreur.
                return

        raise ValueError('Le NIR renseigné est erroné.')
