from setuptools import setup, find_packages

setup(
    name="pdf_snip",  
    version="0.0.2",  # Initial version
    author="Akshay Gokhale",
    author_email="goakshay07@gmail.com",
    description="A package to help manage pdf pages, images and their conversions during different NLP, CV or other tasks to avoid repetitive code blocks and give a simple function call to make it happen",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Aleptonic/PdfSnipper", 
    packages=find_packages(),
    install_requires=[
    "PyPDF2>=3.0.0",       # For PDF reading and writing
    "pdf2image>=1.16.0",   # For converting PDF pages to images
    "Pillow>=9.0.0",       # Required by pdf2image for image handling
    "tqdm>=4.64.0",        # Optional if you plan to add progress bars later
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
