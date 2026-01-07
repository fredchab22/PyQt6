from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel

class Window2(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setWindowTitle("Fenêtre 2")
        self.setGeometry(150, 150, 300, 200)

        central_widget = QWidget()
        layout = QVBoxLayout()

        label = QLabel("Contenu de la Fenêtre 2")
        layout.addWidget(label)

        btn_back = QPushButton("Retour à la fenêtre principale")
        btn_back.clicked.connect(self.close)

        layout.addWidget(btn_back)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)