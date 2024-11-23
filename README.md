# ismed2024Z_Kuna - Program do anonimizacji plików DICOM

Program do anonimizacji plików DICOM. W każdym z plików dane osobowe pacjenta muszą zostać zastąpione wartościami generowanymi według zadanego schematu (np. pacjent01, pacjent02, …) lub losowymi. Program powinien zapewniać użytkownikowi możliwość wyboru listy plików źródłowych (lub katalogu, w którym się one znajdują), docelowego katalogu oraz listy tagów, które podlegać będą anonimizacji. 

Program anonimizuje dane osobowe wprowadzając dane wygenerowane losowo.

## Wymagania

- Python 3.x
- Pakiet `pydicom` (zainstaluj za pomocą `pip install -r requirements.txt`)

## Jak uruchomić?

1. Sklonuj repozytorium.
2. Zainstaluj zależności: `pip install -r requirements.txt`
3. Uruchom program:

```bash
python main.py <ścieżka_do_katalogu_wejściowego> <ścieżka_do_katalogu_docelowego>  <tagi_do_anonimizacji>
```
## Przykład
```
python main.py ./input ./output "PatientName,PatientID"
```
Gdy przykładowy kagtalog wyjściowy nie istnieje, zostaje automatycznie stworzony.

### Podsumowanie

1. Program umożliwia anonimizację plików DICOM na podstawie wskazanych tagów.
2. Używa biblioteki `pydicom` do manipulacji plikami DICOM.
3. Anonimizacja danych polega na zastępowaniu wartości tagów tekstowych (np. imię pacjenta) fikcyjnymi danymi.
4. Program pozwala na określenie katalogu wejściowego, katalogu wyjściowego oraz listy tagów do anonimizacji za pomocą argumentów wiersza poleceń.

## chceck_anonymizer.py
Plik służy do odczytu tagów z danych plików w celu weryfikacji, czy tagi pliku .dcm zostały zanimizowane poprawnie.
