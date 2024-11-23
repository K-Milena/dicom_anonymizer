
import argparse
import os
from dicom_anonymizer import process_dicom_files

def main():
    parser = argparse.ArgumentParser(description="Program do anonimizacji plików DICOM.")
    parser.add_argument('input_dir', type=str, help="Ścieżka do katalogu z plikami DICOM")
    parser.add_argument('output_dir', type=str, help="Ścieżka do katalogu docelowego")
    parser.add_argument('tags', type=str, help="Lista tagów DICOM do anonimizacji (oddzielona przecinkami)")
    
    args = parser.parse_args()

    #czy input istnieje check
    if not os.path.exists(args.input_dir):
        print(f"Błąd: Katalog {args.input_dir} nie istnieje.")
        return

    tags_to_anonymize = args.tags.split(",")  # Rozdzielamy tagi po przecinkach

    # Przetwarzanie plików DICOM
    process_dicom_files(args.input_dir, args.output_dir, tags_to_anonymize)

if __name__ == "__main__":
    main()
    