bruker_ordbok = {}

def lag_brukernavn(navn):
    navn = navn.lower()
    brukernavn = navn.split()
    fornavn = brukernavn[0]
    etternavn = brukernavn[1][0]
    brukernavn = fornavn + etternavn
    return brukernavn

#print(lag_brukernavn("Kari Nordmann"))

def lag_epost(brukernavn, epost_suffix):
    e_postadressen = brukernavn + "@" + epost_suffix
    return e_postadressen

#print(lag_epost(lag_brukernavn("Kari Nordmann"), "UiO.no"))

def print_eposter(ordbok):
    for element in ordbok:
        print(lag_epost(element, ordbok[element]))

#print_eposter({"olan": "ifi.uio.no", "karian": "student.matnat.uio.no"})

def main():
    inp = input("Skriv inn i bokstav: ")
    while inp != "s":
        if inp == "i":
            navn = input("Skriv inn navn: ")
            suffix = input("Skriv inn suffix: ")
            bruk_navn = lag_brukernavn(navn)
            bruker_ordbok[bruk_navn] = suffix
        elif inp == "p":
            print_eposter(bruker_ordbok)
        else:
            print("Skriv inn på nytt: ")
        inp = input("Skriv inn i bokstav: ")
main()
