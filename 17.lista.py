imiona = ["Bartek", "Tomek", "Andrzej", 1, 2, 3, 4]
print(imiona[0])
print(imiona[6])
print(imiona[-1]) # w konsoli 4 wyswyetla elementy licząc od konca
print(imiona[1:5])
print(imiona.index("Bartek"))

imiona.append("Wojtek") # dodaje Wojtek do listy jako ostatni element
imiona.insert(3,"Grzegorz") # dodaje do listy w wybrane miejsce
print(imiona)
print(len(imiona)) # długośc listy
imiona.remove("Bartek") # usuwanie z listy
del imiona[0] # usuwanie po indeksie

pierwsza_lista = ["lampa", "koc", "krzesło"]
print(pierwsza_lista * 3) # każdy element * 3
druga_lista = ["auto", "młotek", 1, 2, 3, 4]
print(pierwsza_lista + druga_lista)
pierwsza_lista.sort() # sortowanie alfabetyczne
posortowana = sorted(pierwsza_lista) # tworzy nową posotrowana liste
print(pierwsza_lista)
zmienna1, zmienna2, zmienna3 = pierwsza_lista # przypisujemy zmienne1 zerowy element listy pierwsza_lista itd
print(zmienna1) # w konsoli koc
