يا هلا فلاح، ما شاء الله تبارك الله! هذا مشروع مادة **ترميز وتعمية (MATH 319 - Coding & Cryptography)** بإشراف الدكتور **عبد الله العبد اللطيف** في **جامعة القصيم**. المشروع قوي وثقيل جداً ومكتمل العناصر الأمنية والسيبرانية.

عشان ترفع هذا المشروع على قيت هاب (GitHub) بشكل احترافي، يثبت جودة شغلك ومجهود الفريق ، جهزت لك ملف الـ **README.md** الكامل والمسبوك على مواصفات السلايدات بالضبط، متضمناً الـ Architecture ، الـ Technology Stack ، وتفاصيل الـ Workflow كاملة.

أول ما تفتح مستودع جديد، اضغط **Add a README** والصق فيه هذا الكلام مباشرة:

```markdown
# Secure File Storage Using AES-256-CBC 🔐

A robust, enterprise-grade cryptographic desktop application designed for temporal and user-authenticated file protection. Developed as a course project for **MATH 319 (Coding & Cryptography)** at **Qassim University**.

The system addresses the fundamental vulnerability of unprotected local storage by ensuring that sensitive documents remain completely unreadable without verified user authorization and compliance with strict temporal boundaries.

---

## ✨ Core Features

* **AES-256-CBC Encryption:** Implements industry-standard symmetric encryption utilizing unique, cryptographically secure 16-byte random Initialization Vectors (IV) per encryption cycle to guard against pattern-based cryptanalysis.
* **Temporal Time-Lock Access Control:** Restricts file decryption using natural language scheduling until a specific, user-defined maturity timestamp has passed.
* **Per-User Cryptographic Identity:** Every registered profile maintains a unique unique SHA-256 cryptographic master key, strictly enforcing cross-user data isolation.
* **Innovative QR Token Recovery:** An alternative password-free rescue path that automatically maps to specific encrypted files for secure, offline extraction while keeping time-lock conditions active.

---

## 🛠️ Technology Stack

* **Core Language:** Python 3
* **Cryptographic Engine:** `PyCryptodome` (AES-256-CBC, SHA-256)
* **User Interface:** `Tkinter` (Custom responsive desktop window layouts)
* **Natural Language Time Parser:** `dateparser`
* **Token Visualizer:** `qrcode` + `PIL` (Pillow)
* **Metadata Management:** `JSON` structure format (`files.json`)

---

## 📐 System Workflow & Implementation Logic

### 1. File Encryption Pipeline
1. **Selection:** User targets any binary file through the OS native Tkinter file browser.
2. **IV Generation:** System injects a high-entropy 16-byte random initialization vector.
3. **Padding & Block Processing:** Applies standard `PKCS7` padding to align variable-sized payloads to mandatory 16-byte cryptographic blocks.
4. **Output Packaging:** Appends the 16-byte raw IV directly to the head of the encrypted stream, outputting a protected `.enc` asset.

### 2. Time-Lock Enforcement Matrix
* Accepts natural text inputs like `"in 5 min"` or `"in 2 hours"`.
* Converts user instructions into relative Unix epoch timestamps via `dateparser`.
* Saves the execution constraint records into the underlying secure tracking register.
* Intercepts immediate decryption requests with a `Time-Locked` constraint alert window if triggered before the expiration timestamp.

---

## 🚀 Execution Lifecycle & Setup

### 1. Install System Dependencies
Ensure you have Python 3 installed on your workstation, then initialize the required module components:
```bash
pip install pycryptodome dateparser qrcode pillow

```

### 2. Run the Application Workspace

Execute the main window layer from your terminal:

```bash
python main.py

```

### 3. Verification Sequence

1. **Register & Login:** Spin up a new secure user profile to establish your distinct SHA-256 identity key.
2. **Encrypt & Lock:** Choose a file target, specify a duration context (e.g., `"in 1 min"`), and execute encryption.
3. **Trigger Validation:** Attempt immediate recovery to verify the operational blocker window.
4. **Decompress/Recover:** Re-extract data seamlessly using either standard login strings after decay or the localized QR rescue token.

