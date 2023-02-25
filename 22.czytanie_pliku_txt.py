file = open("wiadomosc.txt")
zawartosc = file.read()
print(zawartosc)
file.close()

file = open("wiadomosc.txt")
zawartosc = file.readlines() # plik w jednej lini ze znakiami specjalnymi python (/n)
print(zawartosc)
file.close()

file = open("wiadomosc.txt")
zawartosc = file.readline() # czyta tylko 1 linie
print(zawartosc)
file.close()

file = open("wiadomosc.txt")

for line in file:
    print(line) # wyświetlanie po 1 lini za pomoca pętlli

file.close()

file = open(r"C:\Users\adamw\OneDrive\Pulpit\zapis.txt") # otwarcie pliktu  po ścieżce
zawartosc = file.readline()
print(zawartosc)
file.close()