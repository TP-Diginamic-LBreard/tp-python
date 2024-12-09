from client import Client
from banque import CompteBancaire


if __name__ == '__main__':
    # ⚠ NIR évidemment factices… Bon, ça n'avait peut-être pas besoin d'être dit vu leurs têtes.
    c1 = Client('Nyme', 'Ano', 'quelque part', '000000000000097')
    c2 = Client('Gnito', 'Inco', 'ailleurs', '300000000000044')

    cb1 = CompteBancaire('2024-12-03', c1, 220.)
    cb2 = CompteBancaire('2023-11-09', c2, 220.)

    print(f'ID compte 1: {cb1.identifiant}')
    print(f'ID compte 2: {cb2.identifiant}')
    print(f'compte 1 == compte 2? ⇒ {cb1.__eq__(cb2)}')
    print(f'Total soldes : {CompteBancaire.somme_soldes}')
