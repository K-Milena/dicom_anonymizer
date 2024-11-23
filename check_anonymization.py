import pydicom

def check_anonymization(file_path, tags_to_check):
    """
    Funkcja do sprawdzenia wyników anonimizacji.
    Wypisuje wartości tagów po anonimizacji.
    Wystarczy uruchomić z terminala.
    """
    dataset = pydicom.dcmread(file_path)

    for tag in tags_to_check:
        tag_name = dataset.get(tag, "Brak tagu")
        print(f"Tag: {tag}, Wartość: {tag_name}")

# Przykład użycia
tags_to_check = [0x00100010, 0x00100020, 0x00100030]  # przykładowe tagi: PatientName,PatientID,PatientBirthDate
check_anonymization("input/example1.dcm", tags_to_check)
check_anonymization("output/example1.dcm", tags_to_check)
