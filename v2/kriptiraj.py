import json
from slucajni_broj import sample

poruka = str(input('unesi poruku: '))


def citaj_dat():
    with open('javni_kljuc', 'r') as f:
        array = json.load(f)
    return (array)


def pisi_dat(poruka):
    with open('poruka', 'w') as outfile:
        json.dump(poruka, outfile)
    return ("upisano")


def slucajni_broj():
    sl_br = sample(range(citaj_dat()[0] - 1), k=1)
    return sl_br[0]


def kriptiraj(znak):
    javni_kljuc = citaj_dat()
    p = javni_kljuc[0]
    g = javni_kljuc[1]
    y = javni_kljuc[2]
    k = slucajni_broj()
    a = g ** k % p
    b = (y ** k) * znak % p
    sifrat = {
        "a": a,
        "b": b
    }
    return sifrat


def poruka_u_broj(poruka):
    por = list(poruka)
    por_ord = []
    for znak in por:
        por_ord.append(ord(znak))
    return por_ord


def main():
    poruka_broj = poruka_u_broj(poruka)
    kript = []
    for znak in poruka_broj:
        kript.append(kriptiraj(znak))
    return pisi_dat(kript)


main()
