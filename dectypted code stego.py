import cv2

# Reading the encrypted image
img = cv2.imread("encryptedImage.jpg")  # Replace with the correct image path
if img is None:
    print("Error: Image not found or unable to load.")
    exit()

# Creating dictionaries for ASCII conversions
c = {}
for i in range(255):
    c[i] = chr(i)

# Decryption process
message = "hello"
n = 0
m = 0
z = 0

password = input("Enter the original passcode used for encryption: ")
try:
    msg_length = int(input("Enter the length of the original message (numeric value): "))
except ValueError:
    print("Error: Please enter a valid numeric value for the message length.")
    exit()

pas = input("Enter passcode for Decryption: ")
if password == pas:
    for i in range(msg_length):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT authorized")
