import qrcode

# Data you want to encode
data = "https://example.com"

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save it to a file
img.save("qrcode.png")