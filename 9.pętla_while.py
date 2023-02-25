index = 0
while index < 10:
    print(index)
    '''if index == 2:
        break''' # break kończy pętle
    print("po if")
    index += 1 # lub index = index + 1

index = 0
while index < 10:
    print(index)
    if index == 2:
        continue # jeśli index = 2 pętla zaczyna się od nowa (znowu od 2)
    print("po if")
    index += 1
