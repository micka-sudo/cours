#  import pyside 2 avec module pour creation interface graphique
from PySide2 import QtWidgets
import currency_converter


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # creation instance de currency converter
        self.c = currency_converter.CurrencyConverter()
        # commande nom de la fenetre
        self.setWindowTitle("Convertisseur de devises")
        self.config_ui() 
        # instance valeur par defaut
        self.set_default_values()
        # instance config  background
        self.setup_css()
        # instantce setup connection
        self.setup_connections()

    #  Creation methode config ui
    def config_ui(self):
    #  Creation layout pr positionner les widget

        # QHBoxLayout creation layout horizontal
        self.layout = QtWidgets.QHBoxLayout(self)
        # ComBoBox creation
        self.cbb_devisesFrom = QtWidgets.QComboBox()
        # Creation spin box
        self.spn_montant = QtWidgets.QSpinBox()
        self.cbb_devisesTo = QtWidgets.QComboBox()
        self.spn_montantConverti = QtWidgets.QSpinBox()
        # Creation bouton
        self.btn_inverser = QtWidgets.QPushButton("inverser devises")
        # ajout widjet dans notre layout
        self.layout.addWidget(self.cbb_devisesFrom)
        self.layout.addWidget(self.spn_montant)
        self.layout.addWidget(self.cbb_devisesTo)
        self.layout.addWidget(self.spn_montantConverti)
        self.layout.addWidget(self.btn_inverser)
    
    # Cration mehtode valeur par defautl
    def set_default_values(self):
        # Classment et convertion en list du set currencies
        # additems por ajouter plusiuer objet, additem veux des string
        self.cbb_devisesFrom.addItems(sorted(list(self.c.currencies)))
        self.cbb_devisesTo.addItems(sorted(list(self.c.currencies)))
        # devise par defautl.
        self.cbb_devisesFrom.setCurrentText("EUR")
        self.cbb_devisesTo.setCurrentText("EUR")
        # spin box par default
        self.spn_montant.setRange(1, 1000000)
        self.spn_montantConverti.setRange(1, 1000000)
        self.spn_montant.setValue(100)
        self.spn_montantConverti.setValue(100)
    # cration methode setup_connaction
    def setup_connections(self):
        self.cbb_devisesFrom.activated.connect(self.compute)
        self.cbb_devisesTo.activated.connect(self.compute)
        self.spn_montant.valueChanged.connect(self.compute)
        self.btn_inverser.clicked.connect(self.inverser_devise)
    # cration methode setup_css  
    def setup_css(self):
        self.setStyleSheet("""
        background-color: rgb(30,30,30);
        color: rgb(240,240,240);
        border: none;
        """)
       # self.btn_inverser.setStyleSheet("background-color: red;")
    #  Creatin methode changemen de devise ou insversement de devise
    def compute(self):
        montant = self.spn_montant.value()
        devise_from = self.cbb_devisesFrom.currentText()
        devise_to = self.cbb_devisesTo.currentText()
        try:
            resultat =self.c.convert(montant,devise_from,devise_to)
        except currency_converter.currency_converter.RateNotFoundError:
            print("Convertion non trouvé")
        else:
            self.spn_montantConverti.setValue(resultat)

    def inverser_devise(self):
        devise_from = self.cbb_devisesFrom.currentText()
        devise_to = self.cbb_devisesTo.currentText()
        self.cbb_devisesFrom.setCurrentText(devise_to)
        self.cbb_devisesTo.setCurrentText(devise_from)
        self.compute()




# creation Qapllication pour l'ouverture des fenetre
# obligatoirement placer une liste vide dans Qapplication
# cration application

appli = QtWidgets.QApplication([])
#  creation instance win de la class App, utilisation pour creer la fenetre

win = App()
# Affichage du windget
win.show()
appli.exec_()