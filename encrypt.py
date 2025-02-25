import cv2
import os

# Cover Image
img = cv2.imread("images.jpg")  # Ensure this image exists in the same folder
if img is None:
    print("Cover image to encrypt message is not found!")
    exit()

# Input secret message and password
msg = input("Enter secret message you want to encrypt: ")
password = input("Enter a password: ")

# Save the password to a file (for demonstration purposes only)
with open("pass.txt", "w") as f:
    f.write(password)

# Embed the message into the image.
# We will write each character’s ASCII value into a pixel channel.
n = 0  # row index
m = 0  # column index
z = 0  # channel index (0=Blue, 1=Green, 2=Red in OpenCV)

for char in msg:
    # Check if we are within image boundaries
    if n >= img.shape[0] or m >= img.shape[1]:
        print("Message is too long for the image!")
        break
    # Write the ASCII value of the character into the chosen pixel channel
    img[n, m, z] = ord(char)
    n += 1
    m += 1
    z = (z + 1) % 3  # Cycle through the three channels

# Save the encrypted image as PNG to avoid lossy compression
cv2.imwrite("encryptedImage.png", img)
os.system("start encryptedImage.png")  # For Windows; on macOS use 'open' and on Linux 'xdg-open'
print("Secret message embedded into image!")
