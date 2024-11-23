
#import argparse
import os
import re
from dicom_anonymizer import process_dicom_files
from list_dicom_tags import list_dicom_tags

def get_dicom_files(input_dir):
    """Zwraca listę plików DICOM z podanego katalogu."""
    dicom_files = [
        os.path.join(input_dir, f) for f in os.listdir(input_dir)
        if os.path.isfile(os.path.join(input_dir, f)) and f.lower().endswith('.dcm')
    ]
    return dicom_files

def select_files(files):
    """Pozwala użytkownikowi wybrać pliki do przetworzenia."""
    print("Znalezione pliki DICOM:")
    for i, file in enumerate(files):
        print(f"{i + 1}: {file}")

    selection = input("Wybierz numery plików oddzielone przecinkami (lub wpisz 'all' aby wybrać wszystkie): ")
    if selection.strip().lower() == 'all':
        return files

    selected_indices = map(int, selection.split(','))
    selected_files = [files[i - 1] for i in selected_indices if 0 < i <= len(files)]
    return selected_files

def select_tags(tags):
    """Wyświetla tagi w pliku DICOM i pozwala użytkownikowi wybrać te do anonimizacji."""
    print(f"Tagi w pliku {tags}:")
    tags = list_dicom_tags(tags)
    
    if not tags:
        print("Brak tagów do anonimizacji.")
        return []

    for i, tag in enumerate(tags):
        print(f"{i + 1}: {tag}")

    selection = input("Wybierz numery tagów do anonimizacji oddzielone przecinkami: ")
    
    selected_indices = map(int, selection.split(','))
    preprocessed_tags = [tags[i - 1] for i in selected_indices if 0 < i <= len(tags)]
    pattern = r'^[a-zA-Z]+(?:[A-Z][a-z]+)*' #wyrażenie regularne - wyłuskiwanie nazw
    selected_tags = [re.match(pattern, item).group() for item in preprocessed_tags]
    return selected_tags

def main():

    input_dir = input("Podaj ścieżkę do katalogu wejściowego: ")
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)
    
    if not os.path.exists(input_dir):
        print(f"Błąd: Katalog {input_dir} nie istnieje.")
        return

    dicom_files = get_dicom_files(input_dir)
    if not dicom_files:
        print("Brak plików DICOM w podanym katalogu.")
        return
    
    selected_files = select_files(dicom_files)
    if not selected_files:
        print("Nie wybrano żadnych plików.")
        return
    
    selected_tags = select_tags(selected_files[0])
    if not selected_tags:
        print("Nie wybrano żadnych tagów do anonimizacji.")
        return
    
    output_dir = input("Podaj ścieżkę do katalogu wyjściowego: ")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    print("Wybrane tagi to: ", ', '.join(selected_tags))

    process_dicom_files(input_dir, output_dir, selected_tags)

if __name__ == "__main__":
    main()
    