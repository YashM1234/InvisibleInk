import os
from PIL import Image


def encode_image(image_path, data, output_path):
    """Hides data within an image using LSB steganography and allows user-defined storage location."""
    if not os.path.isfile(image_path):
        raise FileNotFoundError("Image file not found.")

    image = Image.open(image_path)
    encoded_image = image.copy()
    binary_data = ''.join(format(ord(char), '08b') for char in data)
    binary_data += '1111111111111110'  # EOF marker

    pixels = list(encoded_image.getdata())
    new_pixels = []
    data_index = 0

    for pixel in pixels:
        new_pixel = list(pixel)
        for i in range(3):
            if data_index < len(binary_data):
                new_pixel[i] = (new_pixel[i] & ~1) | int(binary_data[data_index])
                data_index += 1
        new_pixels.append(tuple(new_pixel))

    encoded_image.putdata(new_pixels)
    encoded_image.save(output_path)
    return f"Data encoded successfully! Saved as {output_path}"


def decode_image(image_path):
    """Extracts hidden data from an image."""
    if not os.path.isfile(image_path):
        raise FileNotFoundError("Image file not found.")

    image = Image.open(image_path)
    binary_data = ""
    pixels = list(image.getdata())

    for pixel in pixels:
        for i in range(3):
            binary_data += str(pixel[i] & 1)

    all_bytes = [binary_data[i: i + 8] for i in range(0, len(binary_data), 8)]
    decoded_data = "".join(chr(int(byte, 2)) for byte in all_bytes)
    return decoded_data.split("\xFE", 1)[0]  # Stop at EOF marker
