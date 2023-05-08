#!/usr/bin/env python 

# Michael Doornbos
# mike@imapenguin.com
# 2023-05-08 

# This script will create a QR code with a logo in the middle.
import qrcode
from PIL import Image
import os

# Function to create a QR code and add a logo in the middle
def create_qr_with_logo(data, logo_path, output_file, border_ratio=0.1):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,  # Change error correction level to Q
        box_size=12,  # Increase box_size from 10 to 12
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

    logo = Image.open(logo_path).convert("RGBA")
    img_w, img_h = img.size
    logo_w, logo_h = logo.size
    scale_factor = min(img_w * 2 // 5, img_h * 2 // 5)
    new_logo_w = logo_w if logo_w < scale_factor else scale_factor
    new_logo_h = int(new_logo_w * (logo_h / logo_w))

    logo = logo.resize((new_logo_w, new_logo_h), Image.LANCZOS)

    # Add border to the logo
    border_w = int(new_logo_w * border_ratio)
    border_h = int(new_logo_h * border_ratio)
    logo_with_border = Image.new("RGBA", (new_logo_w + border_w * 2, new_logo_h + border_h * 2), (255, 255, 255, 255))
    logo_with_border.paste(logo, (border_w, border_h), mask=logo)

    logo_w, logo_h = logo_with_border.size

    img.paste(logo_with_border, ((img_w - logo_w) // 2, (img_h - logo_h) // 2), mask=logo_with_border)
    img.save(output_file)



# Create a vcf file
vcf_data = '''BEGIN:VCARD
VERSION:3.0
N:Teel;Theresa;;;
FN:Theresa Teel
ORG:Morrison Racing Stables
TEL;TYPE=work,voice:+1-909-239-8232
TITLE:Bookkeeper
EMAIL:racing@usamorrison.com
URL:https://morrisonracing.com
END:VCARD
'''

# Create a vcf file
vcf_data = '''BEGIN:VCARD
VERSION:3.0
N:;Smith; Joe;;;
FN:Joe Smith
ORG:Company, Inc.
TITLE:CEO
TEL;TYPE=work,voice:+1-703-555-1212
EMAIL:namen@email.com
URL:https://mycompany.com
END:VCARD
'''

# Path to your logo image file
logo_path = "logo.jpg"

# Output QR code image file
output_file = "user_qr_code_with_logo.png"

create_qr_with_logo(vcf_data, logo_path, output_file)
