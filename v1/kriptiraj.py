import json

from v2.slucajni_broj import sample

poruka = int(input('unesi poruku: '))

def citaj_dat():
    with open('javni_kljuc', 'r') as f:
        array = json.load(f)
    return(array)

def slucajni_broj():
    sl_br = sample(range(citaj_dat()[0] - 1), k=1)
    return sl_br[0]

def kriptiraj():
    javni_kljuc = citaj_dat()
    p = javni_kljuc[0]
    g = javni_kljuc[1]
    y = javni_kljuc[2]
    k = slucajni_broj()
    a = g**k%p
    b = (y**k)*poruka%p
    sifrat = {
        "a": a,
        "b": b
    }
    return sifrat

print(kriptiraj())