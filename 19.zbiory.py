pierwszy_zbior = {"Warszawa", "Kraków", "Katowice", "Lodz"}
drugi_zbior = {"Warszawa"}

pierwszy_zbior.add("Kielce")
print(pierwszy_zbior)
pierwszy_zbior.add("Lodz") # nie doda drugi raz "Lodz" tylko elementy unikalne
print(pierwszy_zbior)
'''print(pierwszy_zbior[0])''' # w zbiorach nie ma indeksowania
print(pierwszy_zbior - drugi_zbior)
print(pierwszy_zbior | drugi_zbior) # suma zbiorów
print(pierwszy_zbior & drugi_zbior) # cześć współna zbiorów
print(pierwszy_zbior ^ drugi_zbior) # różnica symatryczna zbiorow 