import json

a = int(input("unesi broj a:"))
b = int(input("unesi broj b:"))

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

def dektipt(a,b):
    privatni_kljuc = citaj_dat()
    pot = (a**privatni_kljuc[1])%privatni_kljuc[0]
    inv = modinv(pot,privatni_kljuc[0])
    rez = (b*inv)%privatni_kljuc[0]
    gl_rez = str(a)+"("+str(b)+"^"+str(privatni_kljuc[1])+")^-1 mod "+str(privatni_kljuc[0])+"= "+str(rez)
    return gl_rez

print("rezultat glasi: ", dektipt(a,b))

