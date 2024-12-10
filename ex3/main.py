import csv


def solutions_procedurales(data):
    print('⚠ SOLUTIONS PROCÉDURALES ⚠')
    # Moyenne d'âge
    somme = 0
    total = 0
    for i in data:
        # Vérification validité nombres
        age = str(i.get('age', ''))
        # Filtrage des valeurs non numériques
        if age.replace('.', '', 1).isdigit():
            somme += float(age)
            total += 1

    print(f"Moyenne d'âge des passagers : {somme / total:.1f} ans")

    # Pourcentage de survie par classe
    sommes = [0, 0, 0]
    totaux = [0, 0, 0]
    for i in data:
        classe = str(i.get('pclass', ''))
        survie = str(i.get('survived', ''))
        if classe.isdigit() and survie.isdigit():
            c = int(classe)
            s = int(survie)
            sommes[c - 1] += 1 if s == 1 else 0
            totaux[c - 1] += 1

    print(f'Pourcentage de survie en 1ère classe : {sommes[0] / totaux[0] * 100:.2f}%')
    print(f'Pourcentage de survie en 2nde classe : {sommes[1] / totaux[1] * 100:.2f}%')
    print(f'Pourcentage de survie en 3e classe   : {sommes[2] / totaux[2] * 100:.2f}%')

    # Bateaux de sauvetage
    bateaux = {}
    for i in data:
        bateau = str(i.get('boat', ''))
        bateaux[bateau] = bateaux.get(bateau, 0) + 1

    # ⚠ Suppression compte valeurs manquantes
    del bateaux['']

    bateau_max = ''
    for bateau, sauvetages in bateaux.items():
        if sauvetages > bateaux.get(bateau_max, 0):
            bateau_max = bateau

    print(f'Le bateau de sauvetage ayant sauvé le plus de passagers est le bateau n°{bateau_max} avec {bateaux[bateau_max]} passagers sauvés')


def solutions_fonctionnelles(data):
    print('⚠ SOLUTIONS FONCTIONNELLES ⚠')
    # Moyenne d'âge, édition FP (programmation fonctionnelle)
    a_raw = list(map(lambda i: float(i),
                     filter(lambda i: i.replace('.', '', 1).isdigit(),
                            map(lambda i: i.get('age', ''),
                                data))))
    somme, total = sum(a_raw), len(a_raw)

    print(f"Moyenne d'âge des passagers : {somme / total:.1f} ans")

    # Pourcentage de survie par classe, édition FP
    s_raw = list(map(lambda cs: (int(cs[0]), int(cs[1])),
                     filter(lambda cs: cs[0].isdigit() and cs[1].isdigit(),
                            map(lambda i: (i.get('pclass', ''), i.get('survived', '')),
                                data))))
    classes = set(map(lambda c_: c_[0], s_raw))
    survivants = list(filter(lambda _s: _s[1] == 1, s_raw))

    sommes = {classe: len(list(filter(lambda c_: c_[0] == classe, survivants))) for classe in classes}
    totaux = {classe: len(list(filter(lambda c_: c_[0] == classe, s_raw))) for classe in classes}

    for classe in classes:
        print(f'Pourcentage de survie en classe {classe} : {sommes[classe] / totaux[classe] * 100:.2f}%')

    # Bateaux de sauvetages, édition FP
    b_raw = list(filter(lambda i: i.isdigit(),
                        map(lambda i: i.get('boat', ''),
                            data)))
    bateaux = {b: b_raw.count(b) for b in set(b_raw)}
    bateau_max = max(bateaux, key=bateaux.get)

    print(f'Le bateau de sauvetage ayant sauvé le plus de passagers est le bateau n°{bateau_max} avec {bateaux[bateau_max]} passagers sauvés')


if __name__ == '__main__':
    data = []
    with open('titanic_survival.csv') as f:
        data.extend(csv.DictReader(f))

    solutions_procedurales(data)
    solutions_fonctionnelles(data)
