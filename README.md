# Zadanie_1
## funkcja ZIP()
https://docs.python.org/3/library/functions.html#zip

Tworzy iterator, który łączy elementy z kilku iterowalnych obiektów i tworzy krotkę (tuple), np.:
```
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
lista3 = [10.5, 20.5, 30.5]

for e1, e2, e3 in zip(lista1, lista2, lista3):
    print(e1, e2, e3)
```
Wynik:
```
1 a 10.5
2 b 20.5
3 c 30.5
```
## moduł random
https://docs.python.org/3/library/random.html#module-random

Moduł random służy do generowania liczb pseudolosowych. Przykładowe funkcje:

`random(), randint(), choice(), shuffle()`

## wyjątek ZeroDivisionError
https://docs.python.org/3/library/exceptions.html#ZeroDivisionError

Wyjątek, który występuje, gdy próbujesz podzielić liczbę przez zero.

Dzielenie przez zero jest matematycznie nieprawidłowe, więc Python zgłasza ten błąd, aby poinformować o błedzie. Przykład:

`result = 10 / 0  # To spowoduje ZeroDivisionError`


# Zadanie_2
## Wynik z działania coverage - narzędzia do mierzenia pokrycia kodu
![alt text](https://github.com/Jamptorxes/python-wsb/blob/main/zadanie_2/zadanie2.png)
