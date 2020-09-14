""" Interfaccia grafica di Visualizzazione del Test di una Rete Neurale"""
import csv
import os

from PyQt5.QtWidgets import QFileDialog, QWidget
from PyQt5 import QtCore, QtGui
from visualizzazione_ui import Ui_Visualizzazione
from previsione import Previsione


__author__ = "Matteo Cardano,Stefano Lavaggi"
__version__ = "1.0"
__maintainer__ = "Matteo Cardano, Stefano Lavaggi"
__email__ = "ste.lavaggi@gmail.com matteo.cardano@gmail.com"


class Visualizzazione(QWidget):
    """ Oggetto utilizzato per definire una interfaccia di Visualizzazione
    per il training effettuato su una Rete Neurale (NN) 
    
    Attributo
        ----------
        __myNNcreator : tf.keras.Model
            Modello della Rete Neurale su cui è stato effettuato il training """

    __myNNcreator = None

    def __init__(self):
        super(Visualizzazione, self).__init__()
        
        self.ui = Ui_Visualizzazione()
        self.ui.setupUi(self)

    def setup(self, test_risultato, train_risultato, pathImg, myNNcreator, tempo):

        """ 
            Settaggio della schermata per visualizzare il risultato del 
            training con gli effettivi dati calcolati
            
            Parametri:
            ----------
            test_risultato: string
                Percentuale di Accuracy del test
            train_risultato: string
                Percentuale di Accuracy del train
            pathImg: string
                Percorso dell'immagine dei risultati di training
                della Loss e della Accuracy
            myNNcreator: NNcreators
                Oggetto NNcreators utile per la previsione
            tempo: float
                tempo di esecuzione del training
        """
        self.__myNNcreator = myNNcreator

        _translate = QtCore.QCoreApplication.translate
        self.ui.precisioneTraining.setText(_translate("Visualizzazione", train_risultato))
        self.ui.precisioneTest.setText(_translate("Visualizzazione", test_risultato))
        self.ui.tempo.setText("Tempo di training: " + str(tempo) + " (s)")
        self.ui.img_graph.setPixmap(QtGui.QPixmap(pathImg))



    def previsione(self):
        """ Apertura della schermata per visualizzare la previzione """
        # salvo il percorso della cartella
        # contenente il dataset per la previsione
        currentDir = os.path.dirname(os.path.abspath(__file__))
        pathDatasetPrevisione = os.path.join(currentDir, 'dataset','previsione')
        # permetto solo i file csv
        filter = "csv(*.csv)"
        # apro la schermata per il caricamento
        try:
            nomeFile = QFileDialog.getOpenFileName(None, None, pathDatasetPrevisione, filter)

        except:
            print("errore caricament file visual")
            self.ui.comunicazione.setText("errore apertura")
            
        self.ui.comunicazione.setText("")
        # apro la schermata di previsione
        self.openPrevisione(nomeFile[0])

        
    def openPrevisione(self, nomeFile):
        """
            Apertura della schermata di previsione
            
            Parametri:
            ---------

            nomeFile: string
                Percorso del dataset utilizzato per la previsione

        """

        # controllo che sia stato caricato un dataset
        if(nomeFile == ''):
            self.ui.comunicazione.setText("Dataset non caricato")
        else:
            try:
                datafilename = nomeFile
                d = ','
                f = open(datafilename, 'r')
                reader = csv.reader(f, delimiter=d)
                # conto il n di colonne del file csv, per 
                # esser corretto deve averne 4
                ncol = len(next(reader))
                try:
                    # controllo che il dataset caricato sia di previsione
                    if (ncol != 4):
                        raise ValueError
                    # salvo i risultati della previsione
                    risultati = self.__myNNcreator.previsione(nomeFile)
                except:
                    print("file non conforme")
                    self.ui.comunicazione.setText("file non conforme")
                    return
                # apro la schermata di previsione
                self.uiPrevisione = Previsione(risultati)
                self.uiPrevisione.show()
            except:
                print("errore calcolo previsione")
                self.ui.comunicazione.setText("errore previsione")

