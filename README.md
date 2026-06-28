# Secure File Storage System 🔐

A desktop application built in Python using **Tkinter** that provides a secure interface for encrypting and decrypting files, ensuring sensitive data remains protected from unauthorized access.

## ✨ Features
* **AES-256 Encryption:** Utilizes strong Advanced Encryption Standard (AES) in CBC mode to secure files.
* **SHA-256 Hashing:** Implements password hashing and verification to ensure cryptographic integrity.
* **Secure Key Management:** Safe handling of cryptographic keys and initialization vectors (IV).
* **User-friendly GUI:** Interactive desktop interface for easy file selection, encryption, and decryption.

## 🛠️ Project Structure
The repository contains the project files structured as follows:
* `comprisopn_project/2026-06 - Copy/`
  * `SecureStorage.py` — Main UI controller and Tkinter layout interface.
  * `crypto_engine.py` — Core cryptographic functions handling AES-256 encryption and decryption processes.

## 🚀 How to Run

### 1. Install Dependencies
Make sure you have Python installed, then install the required cryptographic library by running:
```bash
pip install pycryptodome

2. Clone the Repository
Clone this repository to your local machine:

Bash
git clone [https://github.com/khalidAlmutairii/comprion-.git](https://github.com/khalidAlmutairii/comprion-.git)
3. Run the Application
Navigate to the project folder and execute the main interface file:

Bash
python "comprisopn_project/2026-06 - Copy/SecureStorage.py"
