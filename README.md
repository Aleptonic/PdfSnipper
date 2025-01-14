
# PdfSnipper
A package to help manage pdf pages, images and their conversions during different NLP, CV or other tasks to avoid repetitive code blocks and give a simple function call to make it happen.

### If you face the error involving `poppler-utlils`
        1.For Google Colab -> !apt-get install -y poppler-utils
        2. Ubuntu/Debian -> sudo apt install poppler-utils

## Installation
        pip install -i https://test.pypi.org/simple/ pdf-snip
## Features
1. Remove First N pages

        remove_first_pages(input_folder: str, output_folder: str, pages_to_remove: int)

->Args:

        input_folder: Path to folder containing PDFs
        output_folder: Path to save modified PDFs
        pages_to_remove: Number of pages to remove from start 
-> Usage:

        remove_first_pages('/content/input','/content/output',2)


2. Save specific pages
        
        -> Save specific pages of PDFs to a new folder.

           save_specific_pages(input_folder: str, output_folder: str, pages_to_save: list)
->Args:

        input_folder: Path to folder containing PDFs
        output_folder: Path to save modified PDFs
        pages_to_save: List of page numbers (0-indexed) to save

->Usage:

        save_specific_pages('content/input','content/output',[0,2,3])

3. Save pages as images

        -> Save specific pages of PDFs as PNG images in another folder.

           save_pages_as_images(input_folder: str, output_folder: str, pages_to_save: list)

->Args:

        input_folder: Path to folder containing PDFs
        output_folder: Path to save PNG images
        pages_to_save: List of page numbers (0-indexed) to save as images

->Usage:

        save_pages_as_images('content/input','content/output',[0,2,4])

4. Split pdf

        -> Splits each page into individual pdf
           split_pdf(input_folder: str, output_folder: str)
->Args:

        Args:
        input_folder: Path to folder containing PDFs
        output_folder: Path to save split PDFs

->Usage:

        split_pdf('content/input','content/output')


