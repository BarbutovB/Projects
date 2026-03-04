# Custom Encryption Engine (XOR Logic)

## Description
This project is a lightweight symmetric encryption tool developed in Python. It utilizes **XOR (Exclusive OR)** bitwise operations to manipulate data at the binary level. The project serves as a practical demonstration of fundamental cryptography concepts, bitwise logic, and data protection mechanisms.

## Technical Specifications
* **Language:** Python 3.x
* **Algorithm:** Symmetric XOR Cipher
* **Logic:** Each character in the input string is transformed using a secret numeric key via the `^` (XOR) operator. The same key is used for both encryption and decryption.

## How It Works
1. The user provides a plaintext string.
2. The engine iterates through each character, applying an XOR operation to its ASCII value against a predefined secret key.
3. The output is an encrypted string that is unreadable without the specific key.
4. Applying the same function again with the correct key reverts the data to its original form.
