from motorsykkel import Motorsykkel

def hovedprogram():
    motorsykkel = Motorsykkel("Bmw", "fbv123", 5)
    motorsykkel1 = Motorsykkel("Yamaha", "dfgr45423", 500)
    motorsykkel2 = Motorsykkel("Suzuki", "no15234", 100)
    motorsykkel2.kjor(10)
    motorsykkel.hentKilometerstand()

    motorsykkel.skrivUt()
    motorsykkel1.skrivUt()
    motorsykkel2.skrivUt()
hovedprogram()
