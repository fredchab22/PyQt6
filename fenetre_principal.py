import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

app= QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Ma Première Fenêtre PyQt6")
window.setGeometry(100, 100, 600, 400)
window.show()
sys.exit(app.exec())