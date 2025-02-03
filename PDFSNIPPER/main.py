import os
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
import logging
from pdf2image import convert_from_path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

#REMOVE FIRST N PAGES
def remove_first_pages(input_folder: str, output_folder: str, pages_to_remove: int):
    """
    Args:
        input_folder: Path to folder containing PDFs
        output_folder: Path to save modified PDFs
        pages_to_remove: Number of pages to remove from start 
    """
    try:
        # Create output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        # Get all PDF files from input folder
        pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.pdf')]

        if not pdf_files:
            logger.warning(f"No PDF files found in {input_folder}")
            return

        logger.info(f"Found {len(pdf_files)} PDF files to process")

        for pdf_file in pdf_files:
            input_path = os.path.join(input_folder, pdf_file)
            output_path = os.path.join(output_folder, f"{pdf_file}")

            try:
                logger.info(f"Processing {pdf_file}")

                # Read PDF
                reader = PdfReader(input_path)
                writer = PdfWriter()

                # Check if PDF has enough pages
                total_pages = len(reader.pages)
                if total_pages <= pages_to_remove:
                    logger.warning(
                        f"Skipping {pdf_file}: Has only {total_pages} pages, "
                        f"cannot remove {pages_to_remove} pages"
                    )
                    continue

                # Add all pages except the first N pages
                for page_num in range(pages_to_remove, total_pages):
                    writer.add_page(reader.pages[page_num])

                # Save modified PDF
                with open(output_path, 'wb') as output_file:
                    writer.write(output_file)

                logger.info(
                    f"Successfully processed {pdf_file}: Removed first {pages_to_remove} pages, "
                    f"saved to {output_path}"
                )

            except Exception as e:
                logger.error(f"Error processing {pdf_file}: {e}")
                continue

    except Exception as e:
        logger.error(f"Error in main execution: {e}")
        raise

#SAVE SPECIFIC PAGES
def save_specific_pages(input_folder: str, output_folder: str, pages_to_save: list):
    """
    Save specific pages of PDFs to a new folder.

    Args:
        input_folder: Path to folder containing PDFs
        output_folder: Path to save modified PDFs
        pages_to_save: List of page numbers (0-indexed) to save
    """
    try:
        os.makedirs(output_folder, exist_ok=True)
        pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.pdf')]

        if not pdf_files:
            logger.warning(f"No PDF files found in {input_folder}")
            return

        logger.info(f"Found {len(pdf_files)} PDF files to process")

        for pdf_file in pdf_files:
            input_path = os.path.join(input_folder, pdf_file)
            output_path = os.path.join(output_folder, f"{pdf_file}")

            try:
                logger.info(f"Processing {pdf_file}")
                reader = PdfReader(input_path)
                writer = PdfWriter()

                total_pages = len(reader.pages)
                valid_pages = [p for p in pages_to_save if 0 <= p < total_pages]

                if not valid_pages:
                    logger.warning(f"No valid pages to save for {pdf_file}")
                    continue

                for page_num in valid_pages:
                    writer.add_page(reader.pages[page_num])

                with open(output_path, 'wb') as output_file:
                    writer.write(output_file)

                logger.info(f"Saved specific pages {valid_pages} of {pdf_file} to {output_path}")

            except Exception as e:
                logger.error(f"Error processing {pdf_file}: {e}")
                continue

    except Exception as e:
        logger.error(f"Error in main execution: {e}")
        raise

#SAVE PAGES AS IMAGES
def save_pages_as_images(input_folder: str, output_folder: str, pages_to_save: list):
    """
    Save specific pages of PDFs as PNG images in another folder.

    Args:
        input_folder: Path to folder containing PDFs
        output_folder: Path to save PNG images
        pages_to_save: List of page numbers (0-indexed) to save as images
    """
    try:
        os.makedirs(output_folder, exist_ok=True)
        pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.pdf')]

        if not pdf_files:
            logger.warning(f"No PDF files found in {input_folder}")
            return

        logger.info(f"Found {len(pdf_files)} PDF files to process")

        for pdf_file in pdf_files:
            input_path = os.path.join(input_folder, pdf_file)
            pdf_name = os.path.splitext(pdf_file)[0]

            try:
                logger.info(f"Processing {pdf_file}")
                images = convert_from_path(input_path)
                total_pages = len(images)
                valid_pages = [p for p in pages_to_save if 0 <= p < total_pages]

                if not valid_pages:
                    logger.warning(f"No valid pages to save as images for {pdf_file}")
                    continue

                for page_num in valid_pages:
                    image_path = os.path.join(output_folder, f"{pdf_name}_page_{page_num + 1}.png")
                    images[page_num].save(image_path, 'PNG')
                    logger.info(f"Saved page {page_num + 1} of {pdf_file} as image to {image_path}")

            except Exception as e:
                logger.error(f"Error processing {pdf_file}: {e}")
                continue

    except Exception as e:
        logger.error(f"Error in main execution: {e}")
        raise

#SPLIT PDFs
def split_pdf(input_folder: str, output_folder: str):
    """
    Split each page of a PDF into separate PDF files.

    Args:
        input_folder: Path to folder containing PDFs
        output_folder: Path to save split PDFs
    """
    try:
        os.makedirs(output_folder, exist_ok=True)
        pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.pdf')]

        if not pdf_files:
            logger.warning(f"No PDF files found in {input_folder}")
            return

        logger.info(f"Found {len(pdf_files)} PDF files to process")

        for pdf_file in pdf_files:
            input_path = os.path.join(input_folder, pdf_file)
            pdf_name = os.path.splitext(pdf_file)[0]

            try:
                logger.info(f"Processing {pdf_file}")
                reader = PdfReader(input_path)

                for page_num, page in enumerate(reader.pages):
                    writer = PdfWriter()
                    writer.add_page(page)

                    output_path = os.path.join(output_folder, f"{pdf_name}_page_{page_num + 1}.pdf")
                    with open(output_path, 'wb') as output_file:
                        writer.write(output_file)

                    logger.info(f"Saved page {page_num + 1} of {pdf_file} to {output_path}")

            except Exception as e:
                logger.error(f"Error processing {pdf_file}: {e}")
                continue

    except Exception as e:
        logger.error(f"Error in main execution: {e}")
        raise

# CODE TO REMOVE LAST N PAGES
def remove_last_pages(input_folder: str, output_folder: str, pages_to_remove: int):
    """
    Remove the last N pages from PDFs.

    Args:
        input_folder (str): Path to folder containing PDFs.
        output_folder (str): Path to save modified PDFs.
        pages_to_remove (int): Number of pages to remove from the end.
    """
    try:
        os.makedirs(output_folder, exist_ok=True)

        pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.pdf')]
        if not pdf_files:
            logger.warning(f"No PDF files found in {input_folder}")
            return

        logger.info(f"Found {len(pdf_files)} PDF files to process")

        for pdf_file in pdf_files:
            input_path = os.path.join(input_folder, pdf_file)
            output_path = os.path.join(output_folder, pdf_file)

            try:
                logger.info(f"Processing {pdf_file}")

                reader = PdfReader(input_path)
                writer = PdfWriter()

                total_pages = len(reader.pages)
                if total_pages <= pages_to_remove:
                    logger.warning(
                        f"Skipping {pdf_file}: Has only {total_pages} pages, cannot remove {pages_to_remove} pages"
                    )
                    continue

                for page_num in range(total_pages - pages_to_remove):
                    writer.add_page(reader.pages[page_num])

                with open(output_path, 'wb') as output_file:
                    writer.write(output_file)

                logger.info(
                    f"Successfully processed {pdf_file}: Removed last {pages_to_remove} pages, saved to {output_path}"
                )

            except Exception as e:
                logger.error(f"Error processing {pdf_file}: {e}")
                continue

    except Exception as e:
        logger.error(f"Error in main execution: {e}")
        raise

# CODE TO REMOVE PAGES OUTSIDE A RANGE
def remove_pages_outside_range(input_folder: str, output_folder: str, start_page: int, end_page: int):
    """
    Remove pages outside the specified range from PDFs.

    Args:
        input_folder (str): Path to folder containing PDFs.
        output_folder (str): Path to save modified PDFs.
        start_page (int): The first page to keep (0-indexed).
        end_page (int): The last page to keep (0-indexed).
    """
    try:
        os.makedirs(output_folder, exist_ok=True)

        pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.pdf')]
        if not pdf_files:
            logger.warning(f"No PDF files found in {input_folder}")
            return

        logger.info(f"Found {len(pdf_files)} PDF files to process")

        for pdf_file in pdf_files:
            input_path = os.path.join(input_folder, pdf_file)
            output_path = os.path.join(output_folder, pdf_file)

            try:
                logger.info(f"Processing {pdf_file}")

                reader = PdfReader(input_path)
                writer = PdfWriter()

                total_pages = len(reader.pages)
                if start_page >= total_pages or end_page >= total_pages or start_page > end_page:
                    logger.warning(
                        f"Skipping {pdf_file}: Invalid page range ({start_page}-{end_page}) for {total_pages} pages"
                    )
                    continue

                for page_num in range(start_page, end_page + 1):
                    writer.add_page(reader.pages[page_num])

                with open(output_path, 'wb') as output_file:
                    writer.write(output_file)

                logger.info(
                    f"Successfully processed {pdf_file}: Kept pages {start_page}-{end_page}, saved to {output_path}"
                )

            except Exception as e:
                logger.error(f"Error processing {pdf_file}: {e}")
                continue

    except Exception as e:
        logger.error(f"Error in main execution: {e}")
        raise
