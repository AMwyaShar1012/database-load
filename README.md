# File Encryption and Access Control System

This system consists of three Python scripts: `create_db.py`, `admin_program.py`, and `guest_program.py`. It allows for the creation of a database to store files, with access control mechanisms in place.

## Database Creation (`create_db.py`)

This script creates an SQLite database (`files.db`) with a single table `files`. The table has three columns: `id` (primary key), `name` (file name), and `content` (file content).

## Administrator Program (`admin_program.py`)

The administrator program allows for adding and deleting files to/from the database, with encryption applied to the file content. Here's how it works:

1. **Encryption Key Generation**: Generates a unique encryption key using the `get_key()` function from the `cryptography.fernet` library.

2. **File Encryption**: Encrypts the file content using the generated key before inserting it into the database.

3. **File Deletion**: Decrypts the file content using the encryption key before deleting the file from the database.

## Guest Program (`guest_program.py`)

The guest program allows for viewing files stored in the database. Here's how it works:

1. **File Loading**: Loads files from the database without requiring a decryption key.

2. **Viewing Files**: Provides an option to view all files stored in the database. Additionally, it allows for viewing specific files by specifying the file ID.

## Encryption and Decryption

Both the administrator and guest programs use the `cryptography.fernet` library for encryption and decryption. Each file's content is encrypted before insertion and decrypted when retrieved for viewing or deletion.

## Access Control

- **Administrator Access**: The administrator program requires the encryption key to add or delete files. This ensures that only authorized users with access to the key can modify the database.

- **Guest Access**: The guest program allows for viewing files without needing the encryption key. This provides read-only access to the files stored in the database.

## Usage

1. Run `create_db.py` to create the database.
2. Run `admin_program.py` to add or delete files (requires encryption key).
3. Run `guest_program.py` to view files stored in the database.

Ensure that the `cryptography` library is installed before running the scripts (`pip install cryptography`).
