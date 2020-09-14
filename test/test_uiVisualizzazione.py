import sys
import unittest
import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from parameterized import parameterized

from visualizzazione import Visualizzazione
app = QApplication(sys.argv)

class test_Visualizzazione(unittest.TestCase):

    var = False

    def setUp(self):
        #creo interfaccia
        self.form = Visualizzazione()

    def test_defaults(self):

        assert self.form.ui.lab_precisioneTest.text() == 'Precisione del Test:'
        assert self.form.ui.lab_precisioneTraining.text() == 'Precisione del training:'
        assert self.form.ui.precisioneTest.text() == 'TextLabel'
        assert self.form.ui.precisioneTraining.text() == 'TextLabel'
        assert self.form.ui.tempo.text() == 'TextLabel'
        assert self.form.ui.comunicazione.text() == ''
        assert self.form.ui.img_graph.text() == ''
        assert type(self.form.ui.but_previsione) == QtWidgets.QPushButton

    @parameterized.expand([
        ['90%', '90%', '',None, 20.5]
    ])
    def test_postSetup(self,test_risultato,train_risultato,pathImg,myNNcreator,tempo):

        currentDir = os.path.dirname(os.path.abspath(__file__))
        pathImg = os.path.join(currentDir, 'img','test','testimg')

        self.form.setup(test_risultato,train_risultato,pathImg,myNNcreator,tempo)
        
        assert self.form.ui.precisioneTest.text() == test_risultato
        assert self.form.ui.precisioneTraining.text() == train_risultato
        assert type(self.form.ui.tempo.text()) is str
        assert self.form.ui.tempo.text() == 'Tempo di training: ' + str(tempo) + ' (s)'
        assert self.form.ui.comunicazione.text() == ''
        assert type(pathImg) is str

        pass

    def test_clickPrevisione(self):
        self.form.ui.but_previsione.clicked.connect(self.click)
        self.form.ui.but_previsione.clicked.disconnect(self.form.previsione)
        QTest.mouseClick(self.form.ui.but_previsione, Qt.LeftButton)
        assert self.var == True
        self.var = False
        pass

    def click(self):
        self.var = True