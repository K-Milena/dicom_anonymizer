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
python main.py <ścieżka_do_katalogu_wejściowego> <ścieżka_do_katalogu_docelowego>  <tagi_do_anonimizacji>

## Przykład
python main.py ./input ./output "PatientName,PatientID"


### Podsumowanie

1. Program umożliwia anonimizację plików DICOM na podstawie wskazanych tagów.
2. Używa biblioteki `pydicom` do manipulacji plikami DICOM.
3. Anonimizacja danych polega na zastępowaniu wartości tagów tekstowych (np. imię pacjenta) fikcyjnymi danymi.
4. Program pozwala na określenie katalogu wejściowego, katalogu wyjściowego oraz listy tagów do anonimizacji za pomocą argumentów wiersza poleceń.

## Linki do edytowania i wyświetlania dokumentacji w LaTeX

Anyone with this link can edit this project: https://www.overleaf.com/9926597754gnfznmnrvzrb#2933db

Anyone with this link can view this project: https://www.overleaf.com/read/rfypkgwqfqjq#170fba
