# elgamal_test v1

## 1. Potrebno je izraditi kljuceve s "izradi_kljuceve.py"

## 2. Zatim enkriptirati poruku u cjelobrojnom brojcanom obliku koji je manji od vrijednosti P s "kriptiraj.py"

## 3. Nakon enkriptiranja pokušati dekriptirati šifrat(a,b) s "dekriptiraj.py"

Primjer:

(env-dipl) antun@antun-HP:~/Dokumenti/Diplomski_rad/elgamal$ python izradi_kljuceve.py 
unesi mod: 2579
unesi g: 2
unesi tajnu virujednost x: 765
izradjeno

(env-dipl) antun@antun-HP:~/Dokumenti/Diplomski_rad/elgamal$ python kriptiraj.py 
unesi poruku: 1299
{'b': 2454, 'a': 465}

(env-dipl) antun@antun-HP:~/Dokumenti/Diplomski_rad/elgamal$ python dekriptiraj.py 
unesi broj a:465
unesi broj b:2454
rezultat glasi:  465(2454^765)^-1 mod 2579= 1299

# elgamal_test v2

## 1. Potrebno je izraditi kljuceve s "izradi_kljuceve.py"

## 2. Zatim enkriptirati poruku u obliku teksta s "kriptiraj.py", šifrat se sprema u datoteku u JSON obliku.

## 3. Nakon enkriptiranja pokušati dekriptirati s "dekriptiraj.py", rezultat se ispisuje na ekranu.

Primjer:
(env-dipl) antun@antun-HP:~/Dokumenti/Diplomski_rad/elgamal/v2$ python kriptiraj.py

unesi poruku: Bok, ja sam Antun!

(env-dipl) antun@antun-HP:~/Dokumenti/Diplomski_rad/elgamal/v2$ python dekriptiraj.py

Bok, ja sam Antun!

Šifrat u datoteci poruka izgleda ovako:
[{"b": 968, "a": 509}, {"b": 1149, "a": 1423}, {"b": 1271, "a": 1807}, {"b": 968, "a": 1433}, {"b": 1520, "a": 1103}, {"b": 882, "a": 389}, {"b": 291, "a": 1347}, {"b": 282, "a": 1989}, {"b": 1699, "a": 1035}, {"b": 873, "a": 773}, {"b": 549, "a": 309}, {"b": 226, "a": 1225}, {"b": 1293, "a": 1357}, {"b": 2024, "a": 969}, {"b": 160, "a": 89}, {"b": 1377, "a": 1599}, {"b": 836, "a": 551}, {"b": 1243, "a": 31}]
