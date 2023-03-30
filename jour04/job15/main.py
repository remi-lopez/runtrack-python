"""
    Écrire un programme qui demande à l’utilisateur de fournir une première chaîne de
    caractères, puis une seconde. Le programme affiche 1 si les 2 chaines sont identiques
    ou 0 si les chaînes ne sont pas identiques. Les chaînes ne sont constituées que de
    lettres minuscules. La deuxième chaîne de caractères peut contenir un ou plusieurs ‘ * ‘.
    Chaque ‘ * ‘ peut remplacer 0 ou plusieurs caractères. Par exemple, si la chaîne 1 est
    “laplateforme” et la chaine 2 “lap*”, le programme affiche 1 car l’ ‘ * ‘ remplace ‘
    lateforme ‘. Si la chaîne 1 est “laplateforme” et la chaîne 2 “l*a*pla*te*form***e” le
    programme renvoie 1 car les ‘ * ‘ ne remplace rien.
"""


def inputs():
    a = str(input("Saisir une 1ere chaine de caractères : ").lower())
    b = str(input("Saisir une 2eme chaine de caractères : ").lower())

    if a != '' and b != '':
        if '*' in a:
            print('La première chaine de caratères ne peut contenir de *')
            inputs()
        else:
            compare_str(a, b)


def compare_char(c1, c2):
    if c1 == c2:
        return True
    else:
        if c2 == '*':
            return True

        print('Not good for %s %s' % (c1, c2))
        return False


def compare_str(str1, str2):
    new_str1 = []
    new_str2 = []

    for s in str1:
        new_str1.append(s)

    for s in str2:
        if s == '*':
            new_str2.append(s)
            break
        else:
            new_str2.append(s)

    print(new_str1)
    print(new_str2)

    for x, y in zip(new_str1, new_str2):
        res = compare_char(x, y)

        if res:
            compare_char(x, y)
        else:
            break

    print(res)


if __name__ == "__main__":
    inputs()
