"""
    Napisz prosta funkcje "szyfrujaca". Jej zadaniem jest zamiana
    co trzeciego znaku w hasle na znak gwiazdki (*).
    Przyklad:
    >> x = hide_password("moje_super_tajne_haslo123")
    >> print(x)
    "mo*e_*up*r_*aj*e_*as*o1*3"
    Pamietaj, ze dlugosc napisu nie musi byc podzielna przez 3.
    Ukrywa co trzecia litere w hasle password.
    :param password: haslo z gwiazdkami co trzecia litere.
    :return: napis z czesciowo ukrytym haslem.
"""


def hide_password(password):
    lp = list(password)
    for i, password in enumerate(password):
        if i > 1 and (i + 1) % 3 == 0:
            lp[i] = "*"
    return "".join(lp)



# password = "password1234"
#
# hide_password(password)
