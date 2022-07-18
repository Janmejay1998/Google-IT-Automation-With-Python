#!/usr/bin/env python3
from os import listdir
from PIL import Image

# Set source and target dirs:
# NOTE: lab calls for new images to be stored to system root
source_dir = "images/"
new_dir = "/opt/icons/"

# Set reprocess vars:
r_90dg = -90
r_size = (128, 128)
# NOTE: The required output format results in black images because the source
# TIFF files have transparent backaground which original JPG format doesn't
# support. PNG would be a more suitable option, but the lab calls for JPEG.
r_format = "JPEG"

# Gather list of image files:
img_files = [f for f in listdir(source_dir) if f.startswith("ic_")]

# Reprocess images:
for file in img_files:
    source_img = Image.open(source_dir + file)

    # Rotate & resize image:
    new_img = source_img.rotate(r_90dg).resize(r_size)

    # NOTE: We need to convert to RGB here to avoid error:
    new_img = new_img.convert("RGB")

    # Save new output file:
    new_img.save(new_dir + file, r_format)
