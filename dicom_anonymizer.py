import pydicom
from pydicom.dataelem import DataElement
import os
import random
import string

STR_LENGTH =   8

def generate_random_string(length=STR_LENGTH):
    """
    Generuje losowy ciąg znaków o długości STR_LENGTH.
    """
    characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9 -
    return ''.join(random.choices(characters, k=length))


def anonymize_dicom(file_path, tags_to_anonymize):
    """
    Anonimizuje dane w pliku DICOM, zastępując wartości wybranych tagów losowymi ciągami.
    """
    # wczytanie DICOM
    dataset = pydicom.dcmread(file_path)

    for tag in tags_to_anonymize:
        if tag in dataset:
            anon = generate_random_string()
            dataset[tag] = DataElement(tag, 'ST', anon)  # 'ST' to typ danych dla stringa

    anonymized_path = file_path.replace("input", "output")
    dataset.save_as(anonymized_path)

    return dataset

def process_dicom_files(input_dir, output_dir, tags_to_anonymize):
    """
    Procesuje pliki DICOM w podanym katalogu wejściowym i zapisuje zanonimizowane pliki w katalogu wyjściowym.
    
    :param input_dir: Katalog z plikami DICOM do anonimizacji.
    :param output_dir: Katalog, do którego zostaną zapisane zanonimizowane pliki.
    :param tags_to_anonymize: Lista tagów do anonimizacji.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_name in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file_name)
        if file_path.endswith(".dcm"):
            anonymized_dataset = anonymize_dicom(file_path, tags_to_anonymize)
            output_file_path = os.path.join(output_dir, file_name)
            anonymized_dataset.save_as(output_file_path)
            print(f"Zanonimizowano: {file_name}")
