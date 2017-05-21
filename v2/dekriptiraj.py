import json

# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
# ----
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
# ----

def citaj_dat():
    with open('privatni_kljuc', 'r') as f:
        array = json.load(f)
    return(array)

def citaj_poruku():
    with open('poruka', 'r') as f:
        array = json.load(f)
    return(array)

def dektipt(a,b):
    privatni_kljuc = citaj_dat()
    pot = (a**privatni_kljuc[1])%privatni_kljuc[0]
    inv = modinv(pot,privatni_kljuc[0])
    rez = (b*inv)%privatni_kljuc[0]
    return rez

def main():
    por = citaj_poruku()
    poruka = []
    for znak in por:
        poruka.append(chr(dektipt(znak["a"],znak["b"])))
    poruka1 = ""
    for p in poruka:
        poruka1 = poruka1 + p
    return poruka1

print(main())