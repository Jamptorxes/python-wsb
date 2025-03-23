import re
from datetime import datetime

# 1. Funkcja sprawdzająca poprawność adresu e-mail
def email_tester(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

# 2. Funkcja dokonująca prostych obliczeń matematycznych (pole koła)
def pole_kola(radius):
    if radius < 0:
        raise ValueError("Promień nie może być ujemny")
    return 3.14159 * radius ** 2

# 3. Funkcja przetwarzająca listę danych (filtracja liczb parzystych)
def filtruj_parzyste(liczby):
    return [x for x in liczby if x % 2 == 0]


# 4. Funkcja konwertująca format dat (z "YYYY-MM-DD" na "DD/MM/YYYY")
def zamien_date(data):
    try: 
        data_obj = datetime.strptime(data, "%Y-%m-%d")
        return data_obj.strftime("%d/%m/%Y")
    except ValueError:
        return "Błędny format daty"
    
# 5. Funkcja sprawdzająca czy podany tekst jest palindromem
def palindrom_test(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]

        