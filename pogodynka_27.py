
def pogoda_krakow():
    return "Słonecznie"

def pogoda_szczecin():
    return "Pochmurno"

def pogoda_wroclaw():
    return "Upal"

if __name__ == '__main__': # __name__ to zmienna specjalna jej wartość będzie wypisywana
                            #tylko przy bepośrednim odpaleniu pogodynka_27.py aby użyć wpisujemy main
    print(pogoda_krakow())
    print(pogoda_szczecin())
    print(pogoda_wroclaw())