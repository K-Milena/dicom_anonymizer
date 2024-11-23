import pydicom

def list_dicom_tags(file_path):
    """
    Wyświetla wszystkie czytelne tagi w pliku DICOM
    """
    try:
        dataset = pydicom.dcmread(file_path)
        print("\nLista tagów w pliku DICOM:")
        print("-" * 50)
        for elem in dataset:
            if elem.VR == "SQ":  # ignorujemy sekwencje
                print(f"{elem.keyword} ({elem.tag}): <->")
            elif isinstance(elem.value, bytes):  # ignorujemy dane binarne
                print(f"{elem.keyword} ({elem.tag}): <->")
            else:
                print(f"{elem.keyword} ({elem.tag}): <->")
                #print(f"{elem.keyword} ({elem.tag}): {elem.value}")
        print("-" * 50)
    except Exception as e:
        print(f"Błąd podczas wczytywania pliku DICOM: {e}")

file_path = "./input/example1.dcm"  
list_dicom_tags(file_path)
