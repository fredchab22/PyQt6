from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PyQt6.QtCore import pyqtSignal
from window1 import Window1
from window2 import Window2

class MainWindow(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setWindowTitle("Fenêtre Principale")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        layout = QVBoxLayout()

        btn_open1 = QPushButton("Ouvrir Fenêtre 1")
        btn_open1.clicked.connect(self.open_window1)

        btn_open2 = QPushButton("Ouvrir Fenêtre 2")
        btn_open2.clicked.connect(self.open_window2)

        layout.addWidget(btn_open1)
        layout.addWidget(btn_open2)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_window1(self):
        self.window1 = Window1(self.db)
        self.window1.show()

    def open_window2(self):
        self.window2 = Window2(self.db)
        self.window2.show()