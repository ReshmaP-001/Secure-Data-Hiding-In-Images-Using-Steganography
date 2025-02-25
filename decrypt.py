import cv2

# Load the encrypted image (lossless PNG format)
img = cv2.imread("encryptedImage.png")
if img is None:
    print("Encrypted image not found!")
    exit()

# Retrieve the stored password from file
try:
    with open("pass.txt", "r") as f:
        correct_pass = f.read().strip()
except FileNotFoundError:
    print("Password file not found!")
    exit()

# Ask user for the decryption passcode
pas = input("Enter passcode for Decryption: ")
if pas != correct_pass:
    print("Incorrect passcode. Access denied!")
    exit()

# Ask user for the secret message length.
# (In this simple example, you need to remember or note the message length.)
try:
    length = int(input("Enter secret message length: "))
except ValueError:
    print("Invalid length input!")
    exit()

message = ""
n = 0  # row index
m = 0  # column index
z = 0  # channel index

# Read the embedded message from the image
for i in range(length):
    # Check if we are within image boundaries
    if n >= img.shape[0] or m >= img.shape[1]:
        print("Reached image boundary before reading the full message.")
        break
    # Read the pixel channel value and convert it back to a character
    message += chr(img[n, m, z])
    n += 1
    m += 1
    z = (z + 1) % 3

print("Decrypted message:", message)
