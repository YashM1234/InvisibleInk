import argparse
import os
import sys

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import core modules
from core.steganography import encode_image, decode_image
from core.encryption import encrypt_data, decrypt_data

VALID_IMAGE_FORMATS = (".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff")


def banner():
    """Display the Invisible Ink CLI Banner."""
    print("""
╔══════════════════════════════════════════════════════╗
║  🔐         ██████████        ██████████         🔐  ║
║  🔐             ██                ██             🔐  ║
║  🔐             ██      ████      ██             🔐  ║
║  🔐             ██                ██             🔐  ║
║  🔐         ██████████        ██████████         🔐  ║
╠══════════════════════════════════════════════════════╣
║ 🔏 Invisible Ink - Secure Steganography CLI          ║
║ ✨ Hide & extract messages secretly inside images    ║
║ 🔒 Strong encryption for added security              ║
║ 📂 Supports PNG, JPG, JPEG, GIF, BMP, TIFF formats   ║
║ 🖥️ Easy command-line interface                       ║
║ 🔑 Password-protected encoding & decoding            ║
║ 📌 Created with ❤️ | GitHub: github.com/YashM1234    ║
╚══════════════════════════════════════════════════════╝
    """)


def validate_image_file(file_path):
    """Ensure the file exists and is a supported image format."""
    if not os.path.isfile(file_path):
        print(f"\n❌ Error: File '{file_path}' not found!\n")
        sys.exit(1)

    if not file_path.lower().endswith(VALID_IMAGE_FORMATS):
        print(f"\n❌ Error: Invalid file format! Supported formats: {VALID_IMAGE_FORMATS}\n")
        sys.exit(1)


def main():
    banner()

    parser = argparse.ArgumentParser(
        description="Invisible Ink - Hide and Extract Secret Messages Securely",
        epilog="For more information, visit: https://github.com/YashM1234/InvisibleInk",
        formatter_class=argparse.RawTextHelpFormatter
    )

    # Define subcommands for encode and decode
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")

    # Encoding Command
    encode_parser = subparsers.add_parser("encode", aliases=["-e"], help="🔒 Hide a secret message inside an image")
    encode_parser.add_argument("-i", "--image", required=True, metavar="FILE", help="Path to the original image file")
    encode_parser.add_argument("-t", "--text", required=True, metavar="MESSAGE", help="Secret message to hide inside "
                                                                                      "the image")
    encode_parser.add_argument("-o", "--output", required=True, metavar="FILE", help="Path to save the encoded image")
    encode_parser.add_argument("-p", "--password", required=True, metavar="PASSWORD", help="Password for encrypting "
                                                                                           "the text")

    # Decoding Command
    decode_parser = subparsers.add_parser("decode", aliases=["-d"], help="🔓 Extract hidden text from an encoded image")
    decode_parser.add_argument("-i", "--image", required=True, metavar="FILE", help="Path to the encoded image file")
    decode_parser.add_argument("-p", "--password", required=True, metavar="PASSWORD", help="Password for decrypting "
                                                                                           "the hidden text")

    # If no arguments are provided, show help
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    if args.command in ["encode", "-e"]:
        validate_image_file(args.image)

        try:
            print("\n🔑 Encrypting message...")
            encrypted_data = encrypt_data(args.text, args.password)
            print("🖼️ Encoding data into image...")

            # Validate output file format
            if not args.output.lower().endswith(VALID_IMAGE_FORMATS):
                print(f"\n⚠️ Warning: Output format should match a valid image format. Saving as 'encoded_output.png' "
                      f"instead.\n")
                args.output = "encoded_output.png"

            encode_image(args.image, encrypted_data, args.output)
            print(f"\n✅ Data successfully hidden! Saved at: {args.output}\n")
        except Exception as e:
            print(f"\n❌ Error: {str(e)}\n")

    elif args.command in ["decode", "-d"]:
        validate_image_file(args.image)

        try:
            print("\n🖼️ Extracting hidden data from image...")
            extracted_data = decode_image(args.image)

            print("🔑 Decrypting message...")
            decrypted_data = decrypt_data(extracted_data, args.password)

            if not decrypted_data.strip():
                print("\n❌ Error: Incorrect password or no hidden message found!\n")
                sys.exit(1)

            print(f"\n✅ Decoded Message: {decrypted_data}\n")
        except Exception as e:
            print(f"\n❌ Error: {str(e)}\n")


if __name__ == "__main__":
    main()
