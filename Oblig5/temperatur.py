def les_inn_temperaturer(filnavn):
    ordbok = {}
    openfil = open(filnavn, "r")
    for elem in openfil:
        liste = elem.strip().split(",")
        maaned = liste[0]
        temp = liste[1]
        ordbok[maaned] = float(temp)
    openfil.close()
    return ordbok

mineOrdbok = les_inn_temperaturer("max_temperatures_per_month (1).csv")
print(mineOrdbok)

def finn_varmerekord(ordbok, filnavn):
    openfil = open(filnavn, "r")
    for linje in openfil:
        liste = linje.strip().split(",")
        maaned = liste[0]
        daag = liste[1]
        temp = float(liste[2])
        if ordbok[maaned] < temp:
            ordbok[maaned] = temp
            print(f"Ny varmerekord på {daag} {maaned}: {temp} grader Celsius (Gammel varmerekord var {ordbok[maaned]} grader Celcius)")
    return ordbok

mineOrdbok = finn_varmerekord(mineOrdbok, "max_daily_temperature_2018 (1).csv")
print(mineOrdbok)

def skrivifill(ordbok, filnavn):
    openfil = open(filnavn, "w")
    for key in ordbok:
        openfil.write(f"{key},{ordbok[key]} \n")
    openfil.close()

skrivifill(mineOrdbok, "ny_max_temp.csv")
