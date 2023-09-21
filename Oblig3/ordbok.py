ordbok = {"melk":14.90, "brød":24.90, "yoghurt":12.90, "pizza":39.90}
print (ordbok)
for x in ordbok:
    print(x)
print(ordbok["pizza"])
varenavn = input("Skriv inn varenavn: ")
pris = input("Skriv inn pris: ")


ordbok[varenavn] = float(pris)
print(ordbok)
