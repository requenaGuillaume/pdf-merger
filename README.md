# PDF merger/splitter

## Dependencies
pip install PyPDF2

## Merge command

py main.py merge<br>
Be sure to have few pdf files in the folder named "pdf_files".

## Split commands

py main.py split_classic<br>
py main.py split_pack<br>
Be sure to name the pdf file to split "to_split.pdf", and located in "pdf_files" folder.<br>
Classic option will split all files separated.<br>
Pack option will split files and pack them as the original files before merge (a pdf file that include itself few pdf files, so they will be packed)
