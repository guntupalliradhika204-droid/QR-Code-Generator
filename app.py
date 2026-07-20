import qrcode

print("========== QR Code Generator ==========")

# Get text or URL from the user
data = input("Enter text or URL: ")

# Get file name from the user
filename = input("Enter file name (without .png): ")

# Create QR Code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create QR image with custom colors
img = qr.make_image(
    fill_color="darkgreen",   # QR code color
    back_color="white"        # Background color
)

# Save the image
img.save(f"{filename}.png")

print("\n===================================")
print("✅ QR Code Generated Successfully!")
print(f"📁 File Name : {filename}.png")
print("===================================")