# 🔏 Invisible Ink - Secure Image Steganography Tool

&#x20;

## 📌 Overview

**Invisible Ink** is a secure **steganography tool** that hides **sensitive data inside images** using the **Least Significant Bit (LSB)** technique. It also **encrypts hidden data** with AES encryption for added security. The tool supports **multiple image formats** and provides both a **command-line interface (CLI) and graphical user interface (GUI)** for ease of use.

---

## ❓ Problem Statement

Traditional encryption is **easily detectable**, making it susceptible to **blocking or interception**. **Invisible Ink** solves this by using **steganography and encryption** to **hide secret messages inside images** securely. This ensures **covert communication** for cybersecurity professionals, journalists, and individuals requiring **data privacy**.

---

## 🚀 Features

✅ **Steganography + Encryption** – Dual-layer security\
✅ **Supports PNG, JPG, GIF, BMP, TIFF** – Works with common image formats\
✅ **Password-Protected Encoding & Decoding** 🔑\
✅ **CLI & GUI Support** – Use it via command-line or graphical interface\
✅ **Lightweight & Efficient** – Optimized for speed and security

---

## 🔧 Technologies Used

- **Programming Language:** Python 🐍
- **Image Processing:** Pillow (PIL) 🖼️
- **Encryption:** Cryptography (AES-based) 🔐
- **CLI Interface:** argparse for professional command-line usage
- **GUI:** PyQt6

---

## 🛠️ Installation

### 1️⃣ **Clone the Repository**

```bash
git clone https://github.com/YashM1234/InvisibleInk.git
cd InvisibleInk
```

### 2️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt
```

---

## 🎯 Usage

### **🔒 Encoding a Message into an Image**

#### **📌 Command Line (CLI)**

```bash
python cli.py encode -i image.png -t "Hidden message here" -p "MySecurePass"
```

✅ **Encodes a message into the image and encrypts it with AES.**\
📸 **CLI Encoding Screenshot:**![](demo\edunetss3.png)


#### **📌 Graphical Interface (GUI)**

```bash
python main.py
```

✅ **Use an intuitive GUI to select images, enter text, and encode.**\
📸 **GUI Encoding Screenshot:**![](demo\edunetss1.png)


---

### **🔓 Decoding a Hidden Message**

#### **📌 Command Line (CLI)**

```bash
python cli.py decode -i encoded_image.png -p "MySecurePass"
```

✅ **Extracts the hidden encrypted message and decrypts it.**\
📸 **CLI Decoding Screenshot:**![](demo\edunetss4.png)


#### **📌 Graphical Interface (GUI)**

✅ **Use the GUI to select an encoded image, enter the password, and decode the message.**\
📸 **GUI Decoding Screenshot:**![](demo\edunetss2.png)


---

## 🎯 Security Features

- **AES Encryption:** Ensures only authorized users can extract hidden messages.
- **Steganography (LSB Method):** Conceals encrypted messages inside images.
- **Password Protection:** Adds an extra layer of security.

---

