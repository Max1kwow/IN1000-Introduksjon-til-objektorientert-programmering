steder = []
for i in range(5):
    brukinp = input("Steder: ")
    steder.append(brukinp)
print(steder)

klesplagg = []
avreisedatoer = []

for i in range(5):
    brukinp = input("kles: ")
    klesplagg.append(brukinp)
print(klesplagg)

for i in range(5):
    brukinp = input("datoer: ")
    avreisedatoer.append(brukinp)
print(avreisedatoer)

reiseplan = [steder, klesplagg, avreisedatoer]
print(reiseplan)

for x in reiseplan:
    print(x)

i1 = int(input("skriv forste indeks: "))
i2 = int(input("skriv den andre indeks: "))

if i1 > len(reiseplan)-1 and i1 < 0:
    print("Ugyldig input!")
else:
    if i2 < len(reiseplan[i1]) - 1 and i2 > 0:
        print(reiseplan[i1][i2])
    else:
        print("Ugyldig input!")
