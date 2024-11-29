# s24110 Jan Cieślak: Prognozowanie wieku krabów

## Opis projektu

Ten projekt skupia się na przewidywaniu wieku krabów na podstawie ich cech morfometrycznych. Wiedza na temat wieku krabów jest istotna zarówno w badaniach biologicznych, jak i w sektorze rybołówstwa. Może to pomóc w lepszym zarządzaniu populacjami krabów, co przyczynia się do zrównoważonego rozwoju środowiska oraz do efektywnego zarządzania zasobami morskimi.

### Problem biznesowy/techniczny
Główne wyzwanie polega na opracowaniu modelu predykcyjnego, który dokładnie oszacuje wiek krabów na podstawie dostarczonych danych. Kluczowe zastosowania to:
- Lepsze zrozumienie populacji krabów i ich dynamiki.
- Wspieranie decyzji w zakresie ochrony zasobów naturalnych.
- Optymalizacja procesu hodowli i połowu krabów dla sektora rybołówstwa.

## Źródło i charakterystyka danych

### Źródło danych
Dane pochodzą z https://www.kaggle.com/datasets/shalfey/extended-crab-age-prediction. Zbiór danych zawiera pomiary fizyczne krabów oraz informacje o ich wieku.

### Charakterystyka danych
Zbiór danych zawiera następujące atrybuty:
- `Sex`: Płeć kraba (`M` - samiec, `F` - samica, `I` - inny).
- `Length`, `Diameter`, `Height`: Wymiary fizyczne kraba w milimetrach.
- `Weight` (Shell, Viscera, Meat): Wagi różnych części ciała kraba w gramach.
- `Shucked weight`: Waga po usunięciu skorupy.
- `Age`: Cel predykcji, liczba pierścieni wzrostu, która wskazuje wiek kraba.

### Uzasadnienie wyboru
Zbiór danych został wybrany ze względu na jego kompleksowość oraz zastosowanie w problemach rzeczywistych. Ponadto, jest to dobrze udokumentowany i dostępny zbiór, co ułatwia jego analizę i implementację modeli uczenia maszynowego.

## Cele projektu
1. Przeprowadzenie eksploracyjnej analizy danych (EDA), aby lepiej zrozumieć ich strukturę i rozkład.
2. Przygotowanie danych do modelowania (czyszczenie danych, kodowanie kategorii, skalowanie cech).
3. Opracowanie i przetestowanie modelu predykcyjnego w celu oszacowania wieku krabów.
4. Ocena wyników wytworzonego modelu predykcyjnego.
5. Przygotowanie wniosków końcowych.

## Struktura pracy nad modelem

Ogólna struktura pracy przedstawia się następująco:

1. Import danych
2. Eksploracja i analiza danych (EDA)
   - Analiza rozkładu zmiennych
   - Analiza korelacji
3. Przygotowanie danych
   - Czyszczenie danych
   - Kodowanie i skalowanie danych
4. Podział danych na zestawy treningowe i testowe oraz
   wytrenowanie modelu
5. Walidacja modelu
   - Sprawdzenie skuteczności modelu na danych testowych
6. Wnioski i raport końcowy
