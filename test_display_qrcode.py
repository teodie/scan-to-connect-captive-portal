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

# Set the default data to encode if none is passed via CLI
try:
    qr_data = sys.argv[1]
except IndexError:
    qr_data = "https://example.com"

try:
    display_type = sys.argv[2]
except IndexError:
    display_type = "dhmini"

print("""
qrcode_display.py - Generate and display a QR code on the LCD.

Usage: {} "<text_or_url>" <display_type>

Where <display_type> is one of:
  * square - 240x240 1.3" Square LCD
  * round  - 240x240 1.3" Round LCD (applies an offset)
  * rect   - 240x135 1.14" Rectangular LCD (applies an offset)
  * dhmini - 320x240 2.0" Display HAT Mini 
""".format(sys.argv[0]))

# Create ST7789 LCD display class.

if display_type in ("square", "rect", "round"):
    disp = ST7789(
        height=135 if display_type == "rect" else 240,
        rotation=0 if display_type == "rect" else 90,
        port=0,
        cs=ST7789.BG_SPI_CS_FRONT,  # BG_SPI_CS_BACK or BG_SPI_CS_FRONT
        dc=9,
        backlight=19,               # 18 for back BG slot, 19 for front BG slot.
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

# Generate the QR Code image directly in memory
print(f'Generating QR code for: {qr_data}')
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=2,
)
qr.add_data(qr_data)
qr.make(fit=True)

# Create the Pillow image from the QR structure
qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Resize to fit the hardware specifications while keeping it square
# Using a minimum dimension fallback to prevent stretching on rectangular panels
square_size = min(WIDTH, HEIGHT)
qr_img = qr_img.resize((square_size, square_size), Image.Resampling.NEAREST)

# Create a blank black background canvas matching the display size
final_image = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))

# Center the square QR code onto the canvas
paste_x = (WIDTH - square_size) // 2
paste_y = (HEIGHT - square_size) // 2
final_image.paste(qr_img, (paste_x, paste_y))

# Draw the image on the display hardware
print('Drawing QR Code to screen')
disp.display(final_image)