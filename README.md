# PdfSnipper

A package to help manage PDF pages, images, and their conversions during different **NLP, CV, or other tasks** to avoid repetitive code blocks and provide a simple function call for operations.

---

## **Installation**

To install PdfSnipper, use:

```bash
pip install -i https://test.pypi.org/simple/ pdf-snip
```

---

## **Dependencies**

### **If you face an error involving `poppler-utils`**
1. **For Google Colab:**  
   ```bash
   !apt-get install -y poppler-utils
   ```
2. **For Ubuntu/Debian:**  
   ```bash
   sudo apt install poppler-utils
   ```
3. **For Windows:**  
   Download the latest release from [here](https://github.com/oschwartz10612/poppler-windows/releases).
   After installation in `/ProgramFiles`, set the PATH environment variable:

   ```python
   import os
   os.environ['PATH'] += os.pathsep + r'C:\path\to\poppler\bin'
   ```

---

## **Features**

### **1. Remove First N Pages**
Removes the first `N` pages from all PDFs in a folder.

```python
remove_first_pages(input_folder: str, output_folder: str, pages_to_remove: int)
```

#### **Arguments**
- `input_folder`: Path to the folder containing PDFs.
- `output_folder`: Path to save modified PDFs.
- `pages_to_remove`: Number of pages to remove from the start.

#### **Usage**
```python
from PDFSNIPPER import remove_first_pages
remove_first_pages('/content/input', '/content/output', 2)
```

---

### **2. Remove Last N Pages**
Removes the last `N` pages from all PDFs in a folder.

```python
remove_last_pages(input_folder: str, output_folder: str, pages_to_remove: int)
```

#### **Arguments**
- `input_folder`: Path to the folder containing PDFs.
- `output_folder`: Path to save modified PDFs.
- `pages_to_remove`: Number of pages to remove from the end.

#### **Usage**
```python
from PDFSNIPPER import remove_last_pages
remove_last_pages('/content/input', '/content/output', 3)
```

---

### **3. Remove Pages Outside a Specified Range**
Keeps only the pages within a specified range `[start_page, end_page]` inclusive, removing all others.

```python
remove_pages_outside_range(input_folder: str, output_folder: str, start_page: int, end_page: int)
```

#### **Arguments**
- `input_folder`: Path to the folder containing PDFs.
- `output_folder`: Path to save modified PDFs.
- `start_page`: First page to keep (0-indexed).
- `end_page`: Last page to keep (0-indexed).

#### **Usage**
```python
from PDFSNIPPER import remove_pages_outside_range
remove_pages_outside_range('/content/input', '/content/output', 2, 5)
```

---

### **4. Save Specific Pages**
Saves only specific pages from PDFs into a new folder.

```python
save_specific_pages(input_folder: str, output_folder: str, pages_to_save: list)
```

#### **Arguments**
- `input_folder`: Path to the folder containing PDFs.
- `output_folder`: Path to save modified PDFs.
- `pages_to_save`: List of page numbers (0-indexed) to keep.

#### **Usage**
```python
from PDFSNIPPER import save_specific_pages
save_specific_pages('/content/input', '/content/output', [0, 2, 3])
```

---

### **5. Save Pages as Images**
Saves specific pages as **PNG images** in a new folder.

```python
save_pages_as_images(input_folder: str, output_folder: str, pages_to_save: list)
```

#### **Arguments**
- `input_folder`: Path to the folder containing PDFs.
- `output_folder`: Path to save PNG images.
- `pages_to_save`: List of page numbers (0-indexed) to save as images.

#### **Usage**
```python
from PDFSNIPPER import save_pages_as_images
save_pages_as_images('/content/input', '/content/output', [0, 2, 4])
```

---

### **6. Split PDF**
Splits each page of a PDF into individual PDF files.

```python
split_pdf(input_folder: str, output_folder: str)
```

#### **Arguments**
- `input_folder`: Path to the folder containing PDFs.
- `output_folder`: Path to save split PDFs.

#### **Usage**
```python
from PDFSNIPPER import split_pdf
split_pdf('/content/input', '/content/output')
```

