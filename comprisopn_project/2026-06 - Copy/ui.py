import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import os



from Crypto.Random import get_random_bytes

from auth import load_users, save_users, hash_pw
from crypto import encrypt_file, decrypt_file
from storage import ensure_folders, make_encrypted_output_path, make_decrypted_output_path
from tk_store import new_token, save_token, get_token


class App:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Secure File Storage")
        self.users = load_users()
        self.key = None
        self.username = None

        ensure_folders()
        self.show_login()

    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()

    def show_login(self):
        self.clear()

        tk.Label(self.root, text="Login").pack(pady=5)

        tk.Label(self.root, text="Username").pack()
        self.u_entry = tk.Entry(self.root)
        self.u_entry.pack()

        tk.Label(self.root, text="Password").pack()
        self.p_entry = tk.Entry(self.root, show="*")
        self.p_entry.pack()

        tk.Button(self.root, text="Login", command=self.login).pack(pady=5)
        tk.Button(self.root, text="Register", command=self.register).pack()
        tk.Button(self.root, text="Recover (Token)", command=self.recover_without_login).pack(pady=10)


    def register(self):
        u = self.u_entry.get().strip()
        p = self.p_entry.get()

        if len(u) == 0 or len(p) == 0:
            messagebox.showerror("Error", "Username/Password must not be empty")
            return

        if u in self.users:
            messagebox.showerror("Error", "User exists")
            return

        hashed = hash_pw(p)
        aes_key = get_random_bytes(32)  # AES-256

        self.users[u] = {"pw": hashed, "key": aes_key.hex()}
        save_users(self.users)
        messagebox.showinfo("OK", "User registered")

    def login(self):
        u = self.u_entry.get().strip()
        p = self.p_entry.get()

        if u not in self.users:
            messagebox.showerror("Error", "User not found")
            return

        if self.users[u]["pw"] != hash_pw(p):
            messagebox.showerror("Error", "Wrong password")
            return

        self.username = u
        self.key = bytes.fromhex(self.users[u]["key"])
        self.show_main()

    def show_main(self):
        self.clear()

        tk.Label(self.root, text=f"Welcome {self.username}").pack(pady=10)
        tk.Button(self.root, text="Encrypt File", command=self.encrypt_gui).pack(pady=5)
        tk.Button(self.root, text="Decrypt File", command=self.decrypt_gui).pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.logout).pack(pady=10)

    def logout(self):
        self.key = None
        self.username = None
        self.show_login()

    def encrypt_gui(self):
        file_path = filedialog.askopenfilename()
        if not file_path:
            return

        out_path = make_encrypted_output_path(file_path)

        try:
            encrypt_file(file_path, self.key, str(out_path))
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed:\n{e}")
            return

        token = new_token()
        qr_path = save_token(token, str(out_path), self.key.hex())

        messagebox.showinfo(
            "Done",
            f"Encrypted saved to:\n{out_path}\n\nToken:\n{token}\nQR:\n{qr_path}"
        )


    def decrypt_gui(self):
        file_path = filedialog.askopenfilename(filetypes=[("Encrypted files", "*.enc")])
        if not file_path:
            return

        out_path = make_decrypted_output_path(file_path)

        ok = decrypt_file(file_path, self.key, str(out_path))
        if ok:
            messagebox.showinfo("Done", f"Decrypted saved to:\n{out_path}")
        else:
            messagebox.showerror("Error", "Failed to decrypt (wrong key or corrupted file).")
    def recover_without_login(self):
        token = simpledialog.askstring("Recover", "Enter token:")
        if not token:
            return

        rec = get_token(token.strip())
        if not rec:
            messagebox.showerror("Error", "Token not found")
            return

        enc_path, thekey = rec

        if not os.path.exists(enc_path):
            messagebox.showerror("Error", "Encrypted file missing")
            return

        out_path = make_decrypted_output_path(enc_path)

        ok = decrypt_file(enc_path, bytes.fromhex(thekey), str(out_path))

        if ok:
            messagebox.showinfo("Done", f"Recovered:\n{out_path}")
        else:
            messagebox.showerror("Error", "Failed to decrypt")

        


def start_app():
    root = tk.Tk()
    root.geometry("260x350")
    App(root)
    root.mainloop()
