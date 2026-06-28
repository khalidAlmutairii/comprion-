# Secure File Storage – AES Encryption Project

This is a simple Python program that allows a user to register, log in, and encrypt/decrypt files using AES.  
The program uses a small Tkinter GUI and saves user accounts in a JSON file.

---

## ⚙️ Requirements

Make sure Python 3 is installed.

Install the required library:

```bash
pip install pycryptodome
````

If that doesn't work, try:

```bash
pip3 install pycryptodome
```

or:

```bash
py -m pip install pycryptodome
```

---

## ▶️ How to Run

1. Place the `main.py` file in a folder.
2. Open a terminal/command prompt **inside that folder**.
3. Run the program:

```bash
python main.py
```

or:

```bash
py main.py
```

A GUI window will open.

---

## 🖥️ How to Use the Program

### **1. Register**

* Enter a username and password.
* Click **Register**.
* A new AES key will be created and stored for that user.

### **2. Login**

* Enter the same username and password.
* Click **Login** to access the main screen.

### **3. Encrypt a File**

* Click **Encrypt File**.
* Select any file from your device.
* An encrypted version will be created with the `.enc` extension.

### **4. Decrypt a File**

* Click **Decrypt File**.
* Choose a file ending with `.enc`.
* A decrypted file will be generated with `_dec` added to the name.

---

## 📂 Files Created By The Program

* **users.json** – stores usernames, hashed passwords, and AES keys
* **file.ext.enc** – encrypted file
* **file_dec** – decrypted file

---

## ❗ Notes

* This project is for educational use.
* AES key storage is simplified for assignment purposes.
* GUI is intentionally minimal.

---
