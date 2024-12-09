from entreprise import Entreprise


if __name__ == '__main__':
    ent = Entreprise('Diginamic', '40 rue Louis Lepine—34470—Pérols', '81824197800050')

    print(ent)

    ent.nom = 'Tecken'
    ent.siret = '91974496100013'

    print(ent)
