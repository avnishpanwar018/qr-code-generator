# QR Code Generator

A simple Python script that generates QR codes from any URL or text and saves them as an image.

---

## Features

- Generate QR codes from any URL or text
- Saves output as a `.png` image
- Lightweight with minimal dependencies

---

## Requirements

- Python 3.x
- `qrcode[pil]` library

---

## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/avnishpanwar018/qr-code-generator.git
   cd qr-code-generator
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

```bash
python qr_generator.py
```

You will be prompted to enter a URL:

```
Enter the URL : https://github.com/avnishpanwar018
```

The QR code will be saved as `qrcode.png` in the same directory.

---

## Example

| Input | Output |
|-------|--------|
| `https://github.com/avnishpanwar018` | `qrcode.png` |

---

## Tech Stack

- Python
- [qrcode](https://pypi.org/project/qrcode/) library
- Pillow (PIL)

---

## License

This project is open source and available under the [MIT License](LICENSE).