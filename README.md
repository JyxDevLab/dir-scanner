# Dir Scanner

A lightweight Python security toolkit for directory enumeration, subdomain discovery, reconnaissance, and automated security testing.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-2.0-purple)

## About

**Dir Scanner** is a Python-based security toolkit created by **JyxDevLab**.

The project started as a simple directory enumeration tool and has evolved into a collection of lightweight security scanners and automated bots designed to assist with reconnaissance and authorized security testing.

The main goal is to provide simple, fast, and easy-to-use tools directly from the terminal.

---

## Features

### Directory Scanner

The Directory Scanner is designed to discover directories and files on authorized web targets.

- Directory enumeration
- File enumeration
- Custom wordlist support
- HTTP status code detection
- Fast HTTP requests
- Target URL scanning
- Result filtering
- Scan result output
- Results saved to a file
- Colored terminal output
- Progress indicators
- Error handling

### Subdomain Scanner

The Subdomain Scanner is designed to discover subdomains associated with an authorized target domain.

- Subdomain enumeration
- Custom subdomain wordlists
- HTTP/HTTPS checking
- Response status detection
- Fast requests
- Result filtering
- Subdomain result collection
- Scan results output
- Colored terminal interface
- Error handling

### Security Bots

The project also includes automated security bots designed to assist with reconnaissance and repetitive security tasks.

The bots can help automate:

- Reconnaissance
- Target analysis
- Subdomain discovery
- Directory discovery
- HTTP response analysis
- Automated scanning
- Result collection
- Security testing workflows

Each bot is designed for a specific purpose and can be used independently depending on the testing scenario.

---

## What's New

### v2.0

The project has received a major update with new scanning capabilities, automation features, and security bots.

### New

- Subdomain Scanner
- New security bots
- Additional reconnaissance capabilities
- Expanded automation
- Improved scanning workflow
- New terminal interface
- Additional scanning functionality

### Improvements

- Improved HTTP request handling
- Improved error handling
- Cleaner terminal output
- Better colored output
- Improved result organization
- Improved scanning performance
- More organized project structure
- Better user experience
- More reliable scanning process

---

## Installation

```bash
git clone https://github.com/JyxDevLab/dir-scanner.git
cd dir-scanner
```

Install dependencies:

```bash
pip install requests
```

## Usage

```bash | directory-scanner
python main.py
```


```bash | subdomains-scanner
python domains.py
```


## Example

```text | directory-scanner
Target: https://example.com

[200] https://example.com/admin
[200] https://example.com/login
[403] https://example.com/backup
[404] https://example.com/test
```

```text | subdomains-scanner
Target: example.com

[200] https://www.example.com
[200] https://mail.example.com
[200] https://api.example.com
[403] https://admin.example.com
[404] https://dev.example.com

Scan completed.

Results saved to: results.txt
```

## Disclaimer

This project is intended for educational purposes and authorized security testing only.

The author is not responsible for any misuse of this software.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

**JyxDevLab**

GitHub: https://github.com/JyxDevLab
