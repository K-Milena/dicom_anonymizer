import pydicom

def list_dicom_tags(file_path):
    """
    Zwraca listę wszystkich czytelnych tagów w pliku DICOM
    """
    tags = []
    try:
        dataset = pydicom.dcmread(file_path)
        for elem in dataset:
            if elem.VR == "SQ":  # ignorujemy sekwencje
                tags.append(f"{elem.keyword} ({elem.tag})")
            elif isinstance(elem.value, bytes):  # ignorujemy dane binarne
                tags.append(f"{elem.keyword} ({elem.tag})")
            else:
                tags.append(f"{elem.keyword} ({elem.tag})")
    except Exception as e:
        print(f"Błąd podczas wczytywania pliku DICOM: {e}")
    return tags  # Zwracamy pustą listę, jeśli wystąpi błąd
