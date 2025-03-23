import unittest
from app import *
from parameterized import parameterized

class TestApp(unittest.TestCase):

    # Metoda setUp() do przygotowania środowiska testowego
    def setUp(self):
        self.test_liczby = [1, 2, 3, 4, 5, 6]
        self.test_daty = [
            ("2023-10-05", "05/10/2023"),
            ("2000-01-01", "01/01/2000"),
            ("2025-12-31", "31/12/2025"),
            ("2020-02-29", "29/02/2020"),
            ("2021.02.29", "Błędny format daty"),
        ]   
        self.test_palidromy = [
            ("kajak", True),
            ("oko", True),
            ("python", False),
            ("a to kanapa pana kota", True),
        ]

    # testy dla funkcji sprawdzającej poprawność adresu email
    @parameterized.expand([
        ("dobry_email_1", "test@example.com", True),
        ("dobry_email_2", "jan.kowalski+trash+sort@google.com", True),
        ("zly_email_1", "jan.kowalski@wpemail", False),
        ("zly_email_2", "jan.kowalskiwp.pl", False),
    ])
    def test_email(self, name, email, expected):
        self.assertEqual(email_tester(email), expected)

    # testy dla funkcji obliczającej pole koła
    @parameterized.expand([
        ("dodatni promien", 5, 78.53975),
        ("zerowy promien", 0, 0),
        ("ujemny promien", -1, ValueError),
    ])
    def test_kolo(self, name, promien, expected):
        if expected == ValueError:
            with self.assertRaises(ValueError):
                pole_kola(promien)
        else:
            self.assertAlmostEqual(pole_kola(promien), expected)

    # testy dla funkcji filtrowania liczb parzystych
    def test_filtruj_parzyste(self):
        self.assertEqual(filtruj_parzyste(self.test_liczby), [2, 4, 6])
        self.assertEqual(filtruj_parzyste([]), [])
        self.assertEqual(filtruj_parzyste([1, 3, 5]), [])

    # testy dla funkcji zamieniającej format daty
    def test_zamien_date(self):
        for data in self.test_daty:
            self.assertEqual(zamien_date(data[0]), data[1])

    # testy dla funkcji sprawdzającej palindrom
    def test_palindrom(self):
        for palindrom in self.test_palidromy:
            self.assertEqual(palindrom_test(palindrom[0]), palindrom[1])

if __name__ == "__main__":
    unittest.main()
