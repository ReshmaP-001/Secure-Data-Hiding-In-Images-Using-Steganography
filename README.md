# Image Steganography using Python
Image steganography is the technique of hiding information within an image. 

## Overview
This project involves creating a Python-based steganography tool that allows users to securely embed text messages within cover images. Using a user-provided password, the tool encrypts and hides the message, producing an encrypted image named "EncryptedImage.png." A separate decryption program will retrieve the hidden message using the correct password. This solution ensures confidential communication via image-based steganography.

## 🚀Features
   - Secure Embedding: The tool allows users to securely embed text messages within cover images. 
   - Encryption: Utilizes a user-provided password to encrypt and hide the message within the cover image `images.jpg`.
   - Output Image: Generates an encrypted image named `EncryptedImage.png`.
   - Decryption Program: A separate program accepts the encrypted image and correct password to retrieve and display the hidden message.
   - Confidential Communication: Ensures that the message remains confidential and accessible only to individuals with the correct decryption password.

## Requirements
   - Python 3.x
   - OpenCV
     
# 📦 Installation

Ensure you have Python 3.x installed, then install OpenCV:

     pip install opencv-python

Clone the repository:

    https://github.com/ReshmaP-001/Secure-Data-Hiding-In-Images-Using-Steganography.git

# ⚡ Usage

### 🔒 Encrypt a Message into an Image
    
    python3 encryption.py

   - Enter the image path (supports .png, .jpg, .jpeg).
   - Enter the output file name (must be .png).
   - Provide the secret message to hide.
   - Set a passcode for protection.
   - The encrypted image is saved!






 

 

