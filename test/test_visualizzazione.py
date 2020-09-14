import sys
import os
import pytest
import unittest
from parameterized import parameterized

from PyQt5.QtWidgets import QApplication
from visualizzazione import Visualizzazione
from NNcreator import NNcreators

app = QApplication(sys.argv)

class Test_Visualizzazione(unittest.TestCase):

    def setUp(self):

        self.form = Visualizzazione()

        self.currentDir = os.path.dirname(os.path.abspath(__file__))
        splitDir = os.path.split(self.currentDir)

        test_risultato = 'test'
        train_risultato = 'train'
        pathImg = os.path.join(splitDir[0],'src','img','test','test.jpg')
        
        myNNcreator = NNcreators(0,0,0,'funzione','test','')
        pathModel = os.path.join(splitDir[0],'src','modelliSalvati','test','test')
        myNNcreator.setModello(pathModel)
        
        tempo = 9.8

        self.form.setup(test_risultato,train_risultato,pathImg,myNNcreator,tempo)

    @parameterized.expand([
                            ['signal_prediction.csv',''],
                            ['test_except','errore previsione'],
                            ['signal_dataset.csv','file non conforme'],
                            ['','Dataset non caricato']
                        ])
    def test_openPrevisione(self,nomeFile,errore):

        splitDir = os.path.split(self.currentDir)
        PathNomeFile = os.path.join(splitDir[0],'src','dataset','previsione',nomeFile)

        if (nomeFile == ''):
            self.form.openPrevisione(nomeFile)
        elif(nomeFile == 'signal_dataset.csv'):
            PathNomeFileErrato = os.path.join(splitDir[0],'src','dataset',nomeFile)
            self.form.openPrevisione(PathNomeFileErrato)
        else:
            self.form.openPrevisione(PathNomeFile)


        assert self.form.ui.comunicazione.text() == errore
