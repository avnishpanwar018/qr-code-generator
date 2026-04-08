# QR Code Generator

A QR code generator available in two versions — a static website and a Python CLI script.

---

## Versions

### 🌐 Web Version (`web/`)
A browser-based QR code generator built with HTML, CSS, and JavaScript. No installation needed — just open the file.

**Features:**
- Generate QR codes from any URL or text
- Customizable size and color
- Download as PNG
- Works entirely in the browser — no data sent anywhere

**Usage:**
Just open `web/index.html` in any browser.

---

### 🐍 Python CLI Version (`qr_generator.py`)
A simple command-line script that generates QR codes and saves them as a PNG image.

**Features:**
- Generate QR codes from any URL or text
- Saves output as `qrcode.png`
- Lightweight with minimal dependencies

**Requirements:**
- Python 3.x
- `qrcode[pil]` library

**Installation:**
```bash
git clone https://github.com/avnishpanwar018/qr-code-generator.git
cd qr-code-generator
pip install -r requirements.txt
```

**Usage:**
```bash
python qr_generator.py
```

You will be prompted to enter a URL:
```
Enter the URL : https://github.com/avnishpanwar018
```

The QR code will be saved as `qrcode.png` in the same directory.

---

## Tech Stack

- Python, `qrcode`, Pillow (CLI version)
- HTML, CSS, JavaScript (web version)

---

## License

This project is open source and available under the [MIT License](LICENSE).