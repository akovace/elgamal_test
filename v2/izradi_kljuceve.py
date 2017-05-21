import json

def izradi_kljuceve(p, g, x):
    y = g**x%p
    javni_kljuc = [p, g, y]
    privatni_kljuc = [p, x]

    with open('javni_kljuc', 'w') as outfile:
        json.dump(javni_kljuc, outfile)

    with open('privatni_kljuc', 'w') as outfile:
        json.dump(privatni_kljuc, outfile)
    return("izradjeno")

p = int(input("unesi mod: "))
g = int(input("unesi g: "))
x = int(input("unesi tajnu virujednost x: "))

print(izradi_kljuceve(p,g,x))