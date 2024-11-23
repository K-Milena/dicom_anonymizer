import pydicom

def list_dicom_tags(file_path):
    """
    Wyświetla wszystkie czytelne tagi w pliku DICOM, ignorując dane binarne.
    """
    try:
        dataset = pydicom.dcmread(file_path)
        tags = []
        for elem in dataset:
            if elem.VR == "SQ":  # ignorowanie sekwencji
                tags.append(f"{elem.keyword} ({elem.tag}): <SEKWENCJA>")
            elif isinstance(elem.value, bytes):  # ignorowanie danych binarnych
                tags.append(f"{elem.keyword} ({elem.tag}): <DANE BINARNE>")
            else:
                tags.append(f"{elem.keyword} ({elem.tag}): {elem.value}")
        return tags
    except Exception as e:
        print(f"Błąd podczas wczytywania pliku DICOM: {e}")
        return []  # Zwracamy pustą listę w przypadku błędu


# przykladowe uzycie
#file_path = "./input/example1.dcm"  #wlasna sciezka do pliku
#list_dicom_tags(file_path)
