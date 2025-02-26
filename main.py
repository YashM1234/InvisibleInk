import sys
from PyQt6.QtWidgets import QApplication
from ui.gui import SteganographyApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SteganographyApp()
    window.show()
    sys.exit(app.exec())
