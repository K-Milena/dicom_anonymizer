# ismed2024Z_Kuna - DICOM File Anonymization Program  

A program for anonymizing DICOM files. In each file, the patient's personal data must be replaced with values generated according to a specified scheme (e.g., patient01, patient02, …) or random values. The program should allow the user to select a list of source files (or the directory containing them), the target directory, and the list of tags to be anonymized. 

## Requirements  

- Python 3.x 
- `pydicom` package (install via `pip install -r requirements.txt`) 

## How to Run?  

1. Clone the repository. 
2. Install dependencies: `pip install -r requirements.txt` 
3. Run the program: 

```bash
python main.py
```

### Summary  

1. The program enables the anonymization of DICOM files based on specified tags. 
2. It uses the `pydicom` library to manipulate DICOM files. 
3. Data anonymization involves replacing text-based tag values (e.g., patient name) with randomly generated fictitious data. 
4. The program allows interactive selection of the input directory, output directory, files to be anonymized, and the list of tags to anonymize via command-line interaction. 

## check_anonymizer.py  

This file is used to read the contents of tags in given files to verify whether the tags in the `.dcm` file have been correctly anonymized.
