class Osoba: # klasa główna rodzic

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "Nazywam sie " + self.imie + " " + self.nazwisko

class Student(Osoba): # klasa dziecko dziediczy po rodzicu

    def __init__(self, imie, nazwikso, numer_indeksu):
        super().__init__(imie, nazwikso) # lub Osoba.__init__(self, imie, nazwikso)
        self.indeks = numer_indeksu

    def podaj_numer_indeksu(self):
        return self.indeks

    def przedstaw_sie(self): # nadpisanie metody przedstaw_sie w klasie dziecka
        return "Jestem studentem i mam na imie " + self.imie

student = Student("Tomasz", "Kot", 123456)
print(student.przedstaw_sie()) # odwołujemy się do nadpisanej metody przedstaw_sie
print(student.podaj_numer_indeksu())

osoba = Osoba("Tomasz", "Kot")
print(osoba.przedstaw_sie()) # odwołujemy się do "podstawowej" metody przedstaw_sie
