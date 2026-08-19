# Dir Scanner

Simple Python tool for directory enumeration on websites.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## Features

* Directory and file enumeration
* Custom wordlist support
* Fast HTTP requests
* Simple command-line interface
* Lightweight and easy to use

## Installation

```bash
git clone https://github.com/JyxDevLab/dir-scanner.git
cd dir-scanner
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Example

```text
Target: https://example.com

[200] /admin
[200] /login
[403] /backup
[404] /test
```

## Disclaimer

This project is intended for educational purposes and authorized security testing only.

The author is not responsible for any misuse of this software.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

**JyxDevLab**

GitHub: https://github.com/JyxDevLab
