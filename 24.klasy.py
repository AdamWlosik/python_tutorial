class Pies:

    gatunek = "pies domowy"

    def __init__(self, rasa, imie, wiek): # metoda specjalna __init__ wywoływana podczas tworzenia nowego obiaktu z klasy
        print("Wewnatrz metody init")
        self.rasa = rasa
        self.imie = imie
        self.wiek = wiek

    def szczekaj(self):
        return "Hau Hau "

    def zaprezentuj_psa(self):
        print("Rasa:", self.rasa)
        print("Imie:", self.imie)
        print("Wiek:", self.wiek)

reksio = Pies("kundelek", "reksio", 2)
print(reksio.wiek) # odowłanie do wiek z poziomu obiektu
'''print(Pies.wiek)''' # nie można sie odwołac do wiek z poziomu Classy tylko z poziomu obiektu
print(reksio.gatunek)
print(Pies.gatunek)
reksio.wiek = 3
print(reksio.wiek) # w konsoli: 3
reksio.gatunek = "Ptak"
print(reksio.gatunek)

print(reksio.szczekaj())
print(reksio.zaprezentuj_psa())