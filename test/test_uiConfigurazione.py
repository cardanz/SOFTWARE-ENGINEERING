import sys
import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from parameterized import parameterized

from configurazione import Configurazione
app = QApplication(sys.argv)

class test_Configurazione(unittest.TestCase):
    
    var = False

    def setUp(self):
        #creo interfaccia
        self.form = Configurazione()

    def test_defaults(self):
         # test dell' interfaccia di default
        assert self.form.ui.nomeRete.text() == ''
        assert self.form.ui.nNodi.value() == 0
        assert self.form.ui.nLayer.value() == 0
        assert self.form.ui.funzione.currentText() == 'relu'
        assert self.form.ui.percentualeTs.value() == 10
        assert self.form.ui.comunicazione.text() == ''
        assert self.form._Configurazione__myNNcreator == None
        assert self.form._Configurazione__sequenza == False
        assert self.form._Configurazione__dataSet == ""
        assert self.form._Configurazione__percentuale == 10

    def test_nome(self):
        self.form.ui.nomeRete.setText("test")
        assert self.form.ui.nomeRete.text() == "test"
        assert type(self.form.ui.nomeRete.text()) is str

    @parameterized.expand([
        [10, 10],
        [-1, 0],
        [25, 20]
    ])
    def test_nLayer(self,input,output):
        self.form.ui.nLayer.setValue(input)
        assert self.form.ui.nLayer.value() == output


    @parameterized.expand([
        [10, 10],
        [-1, 0],
        [55, 50]
    ])
    def test_nNodi(self, input, output):
        self.form.ui.nNodi.setValue(input)
        assert self.form.ui.nNodi.value() == output

    @parameterized.expand([
        ['relu', 0],
        ['sigmoid', 1],
        ['softmax', 2],
        ['softplus', 3],
        ['softsign', 4],
        ['tanh', 5],
        ['selu', 6],
        ['elu', 7]
    ])
    def test_nNodi(self, input, output):
        assert self.form.ui.funzione.findText(input) == output

    def test_testTs(self):
        valore = 20
        self.form.ui.percentualeTs.setValue(valore)
        assert self.form.ui.percentualeTs.value() == valore
        assert type(self.form.ui.percentualeTs.value()) is int
        assert self.form.ui.lab_percentualeTs.text() == 'Definisci partizione TS - VS:20%'

    @parameterized.expand([
        ['test', 'test'],
        ['prrhr532ova','prrhr532ova']
    ])
    def test_comunicazione(self,input,output):
        self.form.ui.comunicazione.setText(input)
        assert self.form.ui.comunicazione.text() == output
        assert type(self.form.ui.comunicazione.text()) is str

    @parameterized.expand([
        ['relu', 'relu'],
        ['sigmoid','sigmoid'],
        ['softmax','softmax'],
        ['softplus','softplus'],
        ['softsign','softsign'],
        ['tanh','tanh'],
        ['selu','selu'],
        ['elu','elu']
    ])
    def test_clickConferma(self, input, output):
        self.form.ui.nomeRete.setText("testoprova")
        var = 10
        self.form.ui.nLayer.setValue(var)
        self.form.ui.nNodi.setValue(var)
        self.form.ui.funzione.setCurrentText(input)
        QTest.mouseClick(self.form.ui.but_convalida,Qt.LeftButton)
        assert self.form._Configurazione__rete == "testoprova"
        assert type(self.form._Configurazione__rete) is str
        assert self.form._Configurazione__layer == var
        assert type(self.form._Configurazione__layer) is int
        assert self.form._Configurazione__nodi == var
        assert type(self.form._Configurazione__nodi) is int
        assert self.form._Configurazione__funzione == output

    def test_clickCaricaDataset(self):
        self.form.ui.but_caricaDataset.clicked.connect(self.click)
        self.form.ui.but_caricaDataset.clicked.disconnect(self.form.caricaDataSet)
        QTest.mouseClick(self.form.ui.but_caricaDataset, Qt.LeftButton)
        assert self.var == True
        self.var = False

    def test_clickCaricaRete(self):
        self.form.ui.but_caricaRete.clicked.connect(self.click)
        self.form.ui.but_caricaRete.clicked.disconnect(self.form.openCaricaNN)
        QTest.mouseClick(self.form.ui.but_caricaRete, Qt.LeftButton)
        assert self.var == True
        self.var = False

    def test_clickTrain(self):
        self.form.ui.but_train.clicked.connect(self.click)
        self.form.ui.but_train.clicked.disconnect(self.form.openVisualizzazione)
        QTest.mouseClick(self.form.ui.but_train, Qt.LeftButton)
        assert self.var == True
        self.var = False

    def click(self):
        self.var = True