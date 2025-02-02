
# PdfSnipper
A package to help manage pdf pages, images and their conversions during different NLP, CV or other tasks to avoid repetitive code blocks and give a simple function call to make it happen.

### If you face the error involving `poppler-utlils`
        1. For Google Colab -> !apt-get install -y poppler-utils
        2. Ubuntu/Debian -> sudo apt install poppler-utils

### If still there is an issue in poppler-utils download the latest release from [here](https://github.com/oschwartz10612/poppler-windows/releases)

- Once installation in `/ProgramFiles` is done you can use `os.environ` to set the PATH environment variable 

        # Set the path to the poppler binaries
        os.environ['PATH'] += os.pathsep + r'C:\path\to\poppler\bin'

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

        from PDFSNIPPER import remove_first_pages
        remove_first_pages('/content/input','/content/output',2)


2. Save specific pages
        
        -> Save specific pages of PDFs to a new folder.

           save_specific_pages(input_folder: str, output_folder: str, pages_to_save: list)
->Args:

        input_folder: Path to folder containing PDFs
        output_folder: Path to save modified PDFs
        pages_to_save: List of page numbers (0-indexed) to save

->Usage:

        from PDFSNIPPER import save_specific_pages
        save_specific_pages('content/input','content/output',[0,2,3])

3. Save pages as images

        -> Save specific pages of PDFs as PNG images in another folder.

           save_pages_as_images(input_folder: str, output_folder: str, pages_to_save: list)

->Args:

        input_folder: Path to folder containing PDFs
        output_folder: Path to save PNG images
        pages_to_save: List of page numbers (0-indexed) to save as images

->Usage:

        from PDFSNIPPER import save_pages_as_images
        save_pages_as_images('content/input','content/output',[0,2,4])

4. Split pdf

        -> Splits each page into individual pdf
           split_pdf(input_folder: str, output_folder: str)
->Args:

        Args:
        input_folder: Path to folder containing PDFs
        output_folder: Path to save split PDFs

->Usage:

        from PDFSNIPPER import split_pdf
        split_pdf('content/input','content/output')


