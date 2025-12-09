import sys
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget


class FenetreAvecLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.init_Ui()
        
    def init_Ui(self):

        layout = QVBoxLayout()
        

        # Créer un QVBoxLayout
        layout = QVBoxLayout()

        # Ajouter des boutons au layout
        bouton1 = QPushButton("Bouton 1")
        bouton2 = QPushButton("Bouton 2")
    

        layout.addWidget(bouton1)
        layout.addWidget(bouton2)
        

        # Définir le layout pour la fenêtre
        self.setLayout(layout)
        self.setWindowTitle("Exemple de QVBoxLayout")
        
# creer QApplication
app = QApplication(sys.argv)

# instenciation de la fenetre
window = FenetreAvecLayout()
window.setWindowTitle("Exemple de QVBoxLayout")
window.setGeometry(100, 100, 600, 400)

#qafficher la fenetre
window.show()

#boucle principale
sys.exit(app.exec())
