Dir Scanner

A simple Python tool for directory enumeration on websites, built for authorized security testing and pentesting practice.

⚠️ Legal Disclaimer

This tool was developed strictly for educational purposes and authorized security testing. Using it against systems, websites, or applications without explicit permission from the owner is illegal in most countries.

The author is not responsible for any misuse of this tool. Only use it on:

Systems you own
Training platforms like TryHackMe, HackTheBox
Systems with explicit written authorization (e.g. a pentest contract)
What it does

Tests a list of common directories/paths against a target URL and reports which ones exist, based on the returned HTTP status code.

Requirements
Python 3 installed on your machine
The requests library (installation steps below)
How to run this project (step by step)
1. Download the project

Click the green Code button on this repository's GitHub page, then Download ZIP. Extract the ZIP file somewhere on your computer.

(Alternatively, if you use Git: git clone this repository's URL.)

2. Open the folder in VSCode
Open VSCode
Go to File > Open Folder
Select the dir-scanner folder you just extracted
3. Open the integrated terminal
In VSCode, go to the top menu: Terminal > New Terminal
(or use the shortcut Ctrl + `)

This opens a terminal already pointed at your project folder — you don't need to type cd or navigate anywhere manually.

4. Install the required library

In that terminal, type:

bash
pip install requests

and press Enter. This only needs to be done once.

5. Run the script

Still in the same terminal, type:

bash
python main.py

If that gives an error like "command not found," try:

bash
python3 main.py

(this is common on Mac/Linux, where python3 is used instead of python)

6. Follow the prompt

The script will ask you to enter a target URL. Type it and press Enter.

Example output
Directory exists and was found | http://mysite.local/admin | Status Code: 200
Access denied / protected | http://mysite.local/config | Status Code: 403
Tech stack
Python 3
requests library
Roadmap / upcoming improvements
 Support for external wordlist files (.txt)
 Multithreading for faster scanning
 Configurable delay between requests
 Export results to a file (.txt / .json)
 Command-line arguments (argparse)
License

This project is licensed under the MIT License — see the LICENSE file for details.