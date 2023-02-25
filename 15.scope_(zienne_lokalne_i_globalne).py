imie = "Bartek"  # zienna globala


def przedstaw_sie():
    global nazwisko_globalne  # globalna definicja zmiennej wewnątrz metody
    nazwisko_globalne = "Jurek"
    nazwisko = "Kowalski"  # zmienna lokalna
    print(nazwisko)
    print(imie)


print(imie)
'''print(nazwisko)'''  # zmienna lokalna metody przedstaw_sie(), nie możemy się odwołać poza nią
przedstaw_sie()
print(nazwisko_globalne)
