import sys
from PyQt6.QtWidgets import QApplication
from main_window import MainWindow
from database import Database

def main():
    app = QApplication(sys.argv)

    # Initialisation de la base de données
    db = Database()

    # Création et affichage de la fenêtre principale
    window = MainWindow(db)
    window.show()

    # Nettoyage à la fermeture
    app.aboutToQuit.connect(db.close)

    sys.exit(app.exec())

if __name__ == "__main__":
    main()