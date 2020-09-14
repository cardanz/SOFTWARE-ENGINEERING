import sys
import unittest
import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from parameterized import parameterized

from previsione import Previsione

app = QApplication(sys.argv)

class Test_Previsione(unittest.TestCase):

    def setUp(self):
        risultati = ['1: prova','2: test','3: lavaggi','4: cardano']
        assert risultati == risultati
        self.form = Previsione(risultati)
    
    def test_ui(self):
        assert self.form.ui.lab_risultati.text() == 'Risultati Test '
        assert self.form.ui.list_risultati.takeItem(0).text() == '1: prova'
        assert self.form.ui.list_risultati.takeItem(0).text() == '2: test'
        assert self.form.ui.list_risultati.takeItem(0).text() == '3: lavaggi'
        assert self.form.ui.list_risultati.takeItem(0).text() == '4: cardano'

        self.form.ui.list_risultati.addItem('1: prova')
        assert self.form.ui.list_risultati.count() == 1

        
