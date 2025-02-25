# Image Steganography using Python

Image steganography is the technique of hiding a secret message within an image in such a way that the original image remains unaltered to the human eye.

## Overview

This project involves creating a Python-based steganography tool that allows users to securely embed text messages within cover images. Using a user-provided password, the tool encrypts and hides the message, producing an encrypted image named "EncryptedImage.png." A separate decryption program will retrieve the hidden message using the correct password. This solution ensures confidential communication via image-based steganography.

## 🚀Features

   - Secure Embedding: The tool allows users to securely embed text messages within cover images. 
   - Encryption: Utilizes a user-provided password to encrypt and hide the message within the cover image `images.jpg`.
   - Output Image: Generates an encrypted image named `EncryptedImage.png`.
   - Decryption Program: A separate program accepts the encrypted image and correct password to retrieve and display the hidden message.
   - Confidential Communication: Ensures that the message remains confidential and accessible only to individuals with the correct decryption password.

## 🔧Requirements

   - Python 3.x
   - OpenCV
     
# 📦 Installation

Ensure you have Python 3.x installed, then install the required library:

     pip install opencv-python

Clone the repository:

    https://github.com/ReshmaP-001/Secure-Data-Hiding-In-Images-Using-Steganography.git

# ⚡ Usage

### 🔒 Encrypt a Message into an Image
    
    python3 encrypt.py
   + python3 encrypt.py

   - Enter the image path (supports .png, .jpg, .jpeg).
   - Enter the output file name (must be .png).
   - Provide the secret message to hide.
   - Set a passcode for protection.
   - The encrypted image is saved!

### 🔑 Decrypt a Hidden Message

    python3 decrypt.py

   - Enter the path of the encrypted image.
   - Enter the correct passcode.
   - Enter the message length (starts from 1)
   - The secret message is revealed!

## ⚠️ Notes & Warnings

   - You can use Python IDLE or Visual Studio Code to execute.
   - Ensure that the cover image exists in the same folder as the programs.
   - The output image must be saved in PNG format to preserve the hidden data.
   - If the passcode is incorrect, the message cannot be retrieved.
   - Large messages may not fit in small images—use a high-resolution image.










 

 

