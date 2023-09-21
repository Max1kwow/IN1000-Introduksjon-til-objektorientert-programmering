liste = [5,7,3]
liste.append(4)

print(liste[0],liste[2])

liste2 = []

for x in range(4):
    liste2.append(input("Skriv et navn: "))
print(liste2)

if "Maksym" in liste2:
    print("Du husket meg!")
elif "maksym" in liste2:
    print("Du husket meg!")
else:
    print("Glemte du meg?")

summen = 0
produkt = 1
# for x in range(len(liste)):
#     summen = summen + liste[x]
# print(summen)
for x in liste:
    summen = summen + x
    produkt = produkt * x
print (summen)
print (produkt)

liste3 = []
liste3.append(summen)
liste3.append(produkt)
print(liste3)

liste4 = liste + liste3
print(liste4)
liste4.pop()
liste4.pop()

print(liste4)
