import sqlite3
from cryptography.fernet import Fernet

def get_key():
    # Generate a key and store it securely
    return Fernet.generate_key()

def encrypt_file(key, file_content):
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(file_content.encode())

def decrypt_file(key, encrypted_content):
    cipher_suite = Fernet(key)
    return cipher_suite.decrypt(encrypted_content).decode()

def insert_file(key, name, content):
    conn = sqlite3.connect('files.db')
    c = conn.cursor()
    encrypted_content = encrypt_file(key, content)
    c.execute("INSERT INTO files (name, content) VALUES (?, ?)", (name, encrypted_content))
    conn.commit()
    conn.close()

def delete_file(key, file_id):
    conn = sqlite3.connect('files.db')
    c = conn.cursor()
    c.execute("SELECT content FROM files WHERE id=?", (file_id,))
    encrypted_content = c.fetchone()[0]
    decrypted_content = decrypt_file(key, encrypted_content)
    if decrypted_content:
        c.execute("DELETE FROM files WHERE id=?", (file_id,))
        print("File deleted successfully.")
    else:
        print("File not found or unauthorized access.")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    key = get_key()
    print("Encryption key:", key.decode())
    operation = input("Enter 'add' to add a file or 'delete' to delete a file: ").lower()
    if operation == 'add':
        file_name = input("Enter file name: ")
        file_content = input("Enter file content: ")
        insert_file(key, file_name, file_content)
        print("File added successfully.")
    elif operation == 'delete':
        file_id = input("Enter the ID of the file to delete: ")
        delete_file(key, file_id)
    else:
        print("Invalid operation.")
