#!/usr/bin/env python3
import sys
import os
import qrcode
from PIL import Image
from OrangePi_ST7789 import ST7789

SPI_PORT = 0
SPI_CS = 0
SPI_DC = 27    # PA0
SPI_RES = 17   # PA1
BACKLIGHT = 22 # PA3

print(f"Current working directory: {os.getcwd()}")

# Configure your Wi-Fi credentials here or pass them via command line
try:
    wifi_ssid = sys.argv[1]
except IndexError:
    wifi_ssid = "Teddy"  # Replace with your Wi-Fi name

try:
    wifi_password = sys.argv[2]
except IndexError:
    wifi_password = "Theodoulos26"  # Replace with your Wi-Fi password

try:
    display_type = sys.argv[3]
except IndexError:
    display_type = "dhmini"

# Format string strictly adhering to the universal Wi-Fi QR code standard
qr_data = f"WIFI:S:{wifi_ssid};T:WPA;P:{wifi_password};;"

print(f"""
wifi_qr_display.py - Generate and display a Wi-Fi login QR code on the LCD.

Usage: {sys.argv[0]} "<ssid>" "<password>" <display_type>

Current Target Network: {wifi_ssid}
""")

# Create ST7789 LCD display class.

if display_type in ("square", "rect", "round"):
    disp = ST7789(
        height=135 if display_type == "rect" else 240,
        rotation=0 if display_type == "rect" else 90,
        port=0,
        cs=ST7789.BG_SPI_CS_FRONT,
        dc=9,
        backlight=19,
        spi_speed_hz=80 * 1000 * 1000,
        offset_left=0 if display_type == "square" else 40,
        offset_top=53 if display_type == "rect" else 0
    )

elif display_type == "dhmini":
    disp = ST7789(
        height=240,
        width=320,
        rotation=0,
        port=SPI_PORT,
        cs=SPI_CS,
        dc=SPI_DC,
        rst=SPI_RES,
        backlight=BACKLIGHT,
        spi_speed_hz=60 * 1000 * 1000,
        offset_left=0,
        offset_top=0
   )

else:
    print("Invalid display type!")

WIDTH = disp.width
HEIGHT = disp.height

# Initialize display.
disp.begin()

# Generate the QR Code image
print('Generating Wi-Fi QR code...')
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=2,
)
qr.add_data(qr_data)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Keep the QR code square based on the shortest screen dimension
square_size = min(WIDTH, HEIGHT)
qr_img = qr_img.resize((square_size, square_size), Image.Resampling.NEAREST)

# Create a black background canvas matching the display size
final_image = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))

# Center the square QR code onto the canvas
paste_x = (WIDTH - square_size) // 2
paste_y = (HEIGHT - square_size) // 2
final_image.paste(qr_img, (paste_x, paste_y))

# Draw the image on the display hardware
print('Drawing Wi-Fi QR Code to screen')
disp.display(final_image)