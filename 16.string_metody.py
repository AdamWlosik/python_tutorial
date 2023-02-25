imie = 'Bartek'
nazwisko = "Kowalski 'Nowak'"
adres = '''kwiatowa 28c/1
            warszawa 00-001'''

print(nazwisko)
print('Czytam książke "Władce Pierścieni"')
print('Czytam\t książke\n \"Władce Pierścieni\"') # \n nowa linia, \t tab, \ wprowadzenie znaku specjalnego
print("małe litery".upper()) # zamiana na małe litery
print("DUZE LITERY".lower()) # zamiana na duże litery

print(imie.islower()) # sprawdze czy litery w zmiennej sa małe
print(nazwisko.islower()) # sprawdza czy litery w zmiennej sa duze

for litery in "Bartek":
    print(litery) #iteracja po wszystkich literach

print(imie[0]) # wypisujemy 0 litere
print(imie[0:4]) # wypisujemy litery  0-4
print(imie.index("a")) # wypisujemy index danej litery
print("Ala" in "Ala ma kota") # sprawdzamy czy dany wyraz znajduje sie w wyrażeniu
print(" ".join(["Ala", "ma", "kota"])) # w konsoli Ala ma kota
print(" OK ".join(["Ala", "ma", "kota"])) # w konsoli Ala OK ma OK kota
print("Ala ma kota split i psa".split("split")) # w konsoli ['Ala ma kota', ' i psa']
print(imie.startswith("Ba")) # sprawdza czy imie zaczyna sie od Ba
print(imie.endswith("tek")) # sprawdza czy imie konczy sie na tek
