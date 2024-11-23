# ismed2024Z_Kuna - Program do anonimizacji plików DICOM

Program do anonimizacji plików DICOM. W każdym z plików dane osobowe pacjenta muszą zostać zastąpione wartościami generowanymi według zadanego schematu (np. pacjent01, pacjent02, …) lub losowymi. Program powinien zapewniać użytkownikowi możliwość wyboru listy plików źródłowych (lub katalogu, w którym się one znajdują), docelowego katalogu oraz listy tagów, które podlegać będą anonimizacji. 

## Wymagania

- Python 3.x
- Pakiet `pydicom` (zainstaluj za pomocą `pip install -r requirements.txt`)

## Jak uruchomić?

1. Sklonuj repozytorium.
2. Zainstaluj zależności: `pip install -r requirements.txt`
3. Uruchom program:

```bash
python main.py
```

### Podsumowanie

1. Program umożliwia anonimizację plików DICOM na podstawie wskazanych tagów.
2. Używa biblioteki `pydicom` do manipulacji plikami DICOM.
3. Anonimizacja danych polega na zastępowaniu wartości tagów tekstowych (np. imię pacjenta) fikcyjnymi danymi wygenerowanymi losowo.
4. Program pozwala na interaktywne określenie katalogu wejściowego, katalogu wyjściowego, plików do anonimizacji oraz listy tagów do anonimizacji za pomocą komunikacji z wiersza poleceń.

## chceck_anonymizer.py
Plik służy do odczytu zawartości tagów z danych plików w celu weryfikacji, czy tagi pliku .dcm zostały zanimizowane poprawnie.
