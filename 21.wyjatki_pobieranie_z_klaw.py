while True:
    try:
        print("Podaj pierwsa liczbe: ")
        pierwsza_liczba = int(input())
        print(("Podaj druga liczbe: "))
        druga_liczba = int(input())
        print(pierwsza_liczba + druga_liczba)
        break
    except ValueError:
        print("Podałeś błędną wartość")
        print("Spróbuj raz jeszcze")
        continue
