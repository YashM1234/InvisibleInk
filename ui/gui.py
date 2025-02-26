import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
    QTextEdit, QFileDialog, QLineEdit, QMessageBox, QProgressBar,
    QHBoxLayout, QRadioButton, QGroupBox
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from core.steganography import encode_image, decode_image
from core.encryption import encrypt_data, decrypt_data


class SteganographyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Invisible Ink - Steganography Tool")
        self.setGeometry(300, 200, 600, 500)
        self.setStyleSheet("""
            QWidget { background-color: #1e1e1e; color: #FFFFFF; font-size: 14px; }
            QPushButton { background-color: #007ACC; color: white; padding: 10px; border-radius: 5px; }
            QPushButton:hover { background-color: #005F99; }
            QLineEdit, QTextEdit { background-color: #2E2E2E; color: white; border: 1px solid #444; padding: 5px; }
            QLabel { font-weight: bold; }
            QProgressBar { border: 1px solid #333; background: #2E2E2E; height: 10px; }
            QProgressBar::chunk { background: #00FF7F; }
            QGroupBox { border: 1px solid #444; border-radius: 5px; padding: 10px; }
        """)

        main_layout = QVBoxLayout()

        # Header Label
        self.header_label = QLabel("🔏 Invisible Ink - Secure Steganography")
        self.header_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        self.header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.header_label)

        # Encode/Decode Toggle
        mode_layout = QHBoxLayout()
        self.encode_radio = QRadioButton("Encode")
        self.encode_radio.setChecked(True)
        self.encode_radio.toggled.connect(self.toggle_mode)
        mode_layout.addWidget(self.encode_radio)

        self.decode_radio = QRadioButton("Decode")
        self.decode_radio.toggled.connect(self.toggle_mode)
        mode_layout.addWidget(self.decode_radio)

        main_layout.addLayout(mode_layout)

        # File Selection
        file_group = QGroupBox("Select Image")
        file_layout = QVBoxLayout()

        self.image_label = QLabel("Selected Image: None")
        self.image_label.setStyleSheet("color: #00FF7F; font-weight: bold;")
        file_layout.addWidget(self.image_label)

        self.select_file_btn = QPushButton("📂 Select Image")
        self.select_file_btn.clicked.connect(self.select_file)
        file_layout.addWidget(self.select_file_btn)

        file_group.setLayout(file_layout)
        main_layout.addWidget(file_group)

        # Text Input (Only for Encoding)
        self.text_group = QGroupBox("Enter Text to Hide")
        text_layout = QVBoxLayout()

        self.text_input = QTextEdit()
        text_layout.addWidget(self.text_input)

        self.text_group.setLayout(text_layout)
        main_layout.addWidget(self.text_group)

        # Password Input (Required for Both)
        pass_group = QGroupBox("Enter Password")
        pass_layout = QVBoxLayout()

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        pass_layout.addWidget(self.password_input)

        pass_group.setLayout(pass_layout)
        main_layout.addWidget(pass_group)

        # Progress Bar
        self.progress = QProgressBar()
        self.progress.setValue(0)
        main_layout.addWidget(self.progress)

        # Encode & Decode Buttons
        self.encode_btn = QPushButton("🔒 Encode")
        self.encode_btn.clicked.connect(self.encode)
        main_layout.addWidget(self.encode_btn)

        self.decode_btn = QPushButton("🔓 Decode")
        self.decode_btn.clicked.connect(self.decode)
        main_layout.addWidget(self.decode_btn)

        self.setLayout(main_layout)

        self.image_path = None
        self.toggle_mode()  # Ensure UI updates on launch

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg)")
        if file_path:
            self.image_path = file_path
            self.image_label.setText(f"📄 {os.path.basename(file_path)}")

    def toggle_mode(self):
        """ Show/Hide text input based on Encode/Decode selection """
        if self.encode_radio.isChecked():
            self.text_group.show()
            self.encode_btn.show()
            self.decode_btn.hide()
        else:
            self.text_group.hide()
            self.encode_btn.hide()
            self.decode_btn.show()

    def encode(self):
        if not self.image_path:
            QMessageBox.warning(self, "Error", "Please select an image file!")
            return

        text = self.text_input.toPlainText().strip()
        password = self.password_input.text().strip()

        if not text or not password:
            QMessageBox.warning(self, "Error", "Please enter text and a password!")
            return

        save_path, _ = QFileDialog.getSaveFileName(self, "Save Encoded Image", "", "PNG Images (*.png)")
        if not save_path:
            QMessageBox.warning(self, "Error", "No save location selected!")
            return

        self.progress.setValue(30)

        encrypted_text = encrypt_data(text, password)
        self.progress.setValue(60)

        try:
            encode_image(self.image_path, encrypted_text, save_path)
            self.progress.setValue(100)
            QMessageBox.information(self, "Success", f"Data successfully encoded! Saved at:\n{save_path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Encoding failed: {str(e)}")
            self.progress.setValue(0)

    def decode(self):
        if not self.image_path:
            QMessageBox.warning(self, "Error", "Please select an image file!")
            return

        password = self.password_input.text().strip()
        if not password:
            QMessageBox.warning(self, "Error", "Please enter a password!")
            return

        self.progress.setValue(30)

        try:
            extracted_data = decode_image(self.image_path)
            self.progress.setValue(60)

            decrypted_data = decrypt_data(extracted_data, password)
            self.progress.setValue(100)
            QMessageBox.information(self, "Decoded Message", decrypted_data)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Decoding failed: {str(e)}")
            self.progress.setValue(0)
