import sqlite3
from cryptography.fernet import Fernet

def decrypt_file(key, encrypted_content):
    cipher_suite = Fernet(key)
    return cipher_suite.decrypt(encrypted_content).decode()

def load_files():
    conn = sqlite3.connect('files.db')
    c = conn.cursor()
    c.execute("SELECT * FROM files")
    files = c.fetchall()
    conn.close()
    return files

def view_file_by_id(file_id, key):
    conn = sqlite3.connect('files.db')
    c = conn.cursor()
    c.execute("SELECT * FROM files WHERE id=?", (file_id,))
    file_data = c.fetchone()
    if file_data:
        file_id, file_name, encrypted_content = file_data
        decrypted_content = decrypt_file(key, encrypted_content)
        print(f"File ID: {file_id}, Name: {file_name}, Content: {decrypted_content}")
    else:
        print("File not found.")
    conn.close()

if __name__ == "__main__":
    files = load_files()
    for file in files:
        file_id, file_name, _ = file
        print(f"File ID: {file_id}, Name: {file_name}")
    
    option = input("Enter 'view' to view a file by ID: ").lower()
    if option == 'view':
        file_id = input("Enter the ID of the file to view: ")
        view_file_by_id(file_id)
