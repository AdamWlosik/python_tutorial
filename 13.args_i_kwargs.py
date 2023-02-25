def rzeczy(pierwsza_rzecz, *args):
    print(pierwsza_rzecz)
    print(args[0])
    for i in args:
        print(i)

rzeczy("lampa", "koc", "lozko", "telefon")
print("")

def dziennik(klasa, **kwargs):
    print("klasa" + klasa)
    for nazwisko in kwargs.keys():
        print(nazwisko)
    print(kwargs.get("Kowalski"))

    for index in kwargs.values():
        print("index= ", index)


dziennik("3c", Kowalski = 1, Nowak = 2, Wiśniewski = 3)

def parametr_domyslny(rocznik = 1996):
    print(rocznik)

parametr_domyslny()

