# elgamal_test

## 1. Potrebno je izraditi kljuceve s "izradi_kljuceve.py"

## 2. Zatim enkriptirati poruku u cjelobrojnom brojcanom obliku s "kriptiraj.py"

## 3. Nakon enkriptiranja pokušati dekriptirati s "dekriptiraj.py"

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
