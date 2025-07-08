# 🧾 Tax Form OCR Pipeline

A Python project that demonstrates automated extraction of text from scanned **tax forms**. The solution aligns a scanned form image with a clean template, performs OCR using Tesseract, and post-processes the text to clean and structure the output.

---

## Features

- **Document Alignment**: Aligns scanned forms to a reference template using image processing techniques.
- **OCR with Tesseract**: Uses `pytesseract` to extract text from aligned images.
- **Text Cleanup**: Removes noise, extra whitespace, and performs basic formatting of the extracted text.
- **Visual Debugging**: Optionally saves intermediate steps like aligned forms and bounding boxes.

---

## Technologies Used

- Python 3.x
- OpenCV (for image alignment and preprocessing)
- Pytesseract (Tesseract OCR wrapper)
- NumPy
- PIL (Pillow)

---

## Project Structure

```bash
.
├── assets/                 # Template and scanned form images
├── align_images.py         # Image clean up and alignment
├── extract_text.py         # Extracting text using pytessaract
├── main.py                 # Pipeline script
└── README.md