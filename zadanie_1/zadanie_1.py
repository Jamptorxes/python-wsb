from random import randint

lista1 = [1, 2, 3]
lista2 = ["a", "b", "c"]

lista3 = list(zip(lista1, lista2)) # scalenie dwóch list za pomocą zip() - opis w pliku README.md
print(lista3)

print("Losowa liczba z zakresu od 1 do 100: ", randint(1, 100)) # losowa liczba z zakresu od 1 do 100 - opis w pliku README.md

try:
    print(50 / 0)
except ZeroDivisionError: # obsługa błędu dzielenia przez zero - opis w pliku README.md
    print("Nie można podzielić przez zero")