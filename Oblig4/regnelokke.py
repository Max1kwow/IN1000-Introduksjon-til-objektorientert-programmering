inputtall = input("Skriv inn tall: ")
tallListe = []
while inputtall != "0":
    tallListe.append(int(inputtall))
    inputtall = input("Skriv inn tall: ")

print(tallListe)

for x in tallListe:
    print(x)

minSum = 0
for x in tallListe:
    minSum += x
print(minSum)

maxTall = tallListe[0]
for x in tallListe:
    if x > maxTall:
        maxTall = x
print(maxTall)

minstTall = tallListe[0]
for x in tallListe:
    if x < minstTall:
        minstTall = x
print(minstTall)
