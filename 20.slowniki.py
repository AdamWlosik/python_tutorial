dziennik = {1 : "Kowalski", 2 : "Nowak", 3 : "Lewandowski"}

print(dziennik.get(1))
print(dziennik[1]) # drugi sposób odwołania sie po indeksie
dziennik[4] = "Mucha"
print(dziennik[4])

for i in dziennik.keys():
    print(i) # wypisujemy indexy

for wartosci in dziennik.values():
    print(wartosci) # wypisujemy wszystkie wartosci

del dziennik[1] # usuwanie z dziennika

dziennik[2] = "Nowy uczen"
print(dziennik[2])
