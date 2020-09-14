""" Interfaccia grafica di Previsione su una Rete Neurale """

from PyQt5.QtWidgets import  QWidget
from previsione_ui import Ui_Previsione

__author__ = "Matteo Cardano,Stefano Lavaggi"
__version__ = "1.0"
__maintainer__ = "Matteo Cardano, Stefano Lavaggi"
__email__ = "ste.lavaggi@gmail.com matteo.cardano@gmail.com"


class Previsione(QWidget):
    """ Oggetto utilizzato per definire una interfaccia di Previsione
    utilizzando una Rete Neurale (NN) """

    def __init__(self, risultati):
        super(Previsione, self).__init__()
        
        self.ui = Ui_Previsione()
        self.ui.setupUi(self)

        self.riempiListView(risultati)

    def riempiListView(self,risultati):
        """Riempe l'elemento listView presente con i risultati della previsione
        
        Parametri
        ---------
        risultati:string[]
            Lista contenente i risultati della previsione 
            effettuata sulla Rete Neurale"""
        # calcolo la lunghezza della lista 'risultati'
        length = len(risultati)
        # mostro i risultati della previsione nella listView
        self.ui.list_risultati.insertItems(length, risultati)