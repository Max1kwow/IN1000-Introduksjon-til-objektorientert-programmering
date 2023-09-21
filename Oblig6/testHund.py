from hund import Hund

def hovedprogram():
    hund = Hund(10, 15)
    hund.spring()
    print(hund.hentVekt())
    hund.spis(2)
    print(hund.hentVekt())
hovedprogram()
