file = open("zapis.txt", "w") # "w" tekst się nadpisuje za każdym razem
file.write("To jest jakis tekst")
file.close()

file = open("zapis.txt", "a") # "a" tekst dodany do pliku
file.write("To jest jakis tekst")
file.close()