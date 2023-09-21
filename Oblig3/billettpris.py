def billettpris():
    alder = int(input("Skriv alder på kjøperen: "))
    billettpris = 0

    if alder < 17:
        billettpris = 30
    elif alder >= 63:
        billettpris = 35
    elif alder > 17:
        billettpris = 50
    print(billettpris)

billettpris()
