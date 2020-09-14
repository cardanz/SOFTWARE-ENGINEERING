import os

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Previsione(object):
    def setupUi(self, Previsione):
        Previsione.setObjectName("Previsione")
        Previsione.resize(508, 397)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Previsione)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lab_risultati = QtWidgets.QLabel(Previsione)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lab_risultati.setFont(font)
        self.lab_risultati.setObjectName("lab_risultati")
        self.verticalLayout_2.addWidget(self.lab_risultati)
        self.list_risultati = QtWidgets.QListWidget(Previsione)
        self.list_risultati.setObjectName("list_risultati")
        self.verticalLayout_2.addWidget(self.list_risultati)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        currentDir = os.path.dirname(os.path.abspath(__file__))
        pathIcon = os.path.join(currentDir, 'img','icon','testing.ico')
        Previsione.setWindowIcon(QtGui.QIcon(pathIcon))

        self.retranslateUi(Previsione)
        QtCore.QMetaObject.connectSlotsByName(Previsione)

    def retranslateUi(self, Previsione):
        _translate = QtCore.QCoreApplication.translate
        Previsione.setWindowTitle(_translate("Previsione", "Risultati della Previsione"))
        self.lab_risultati.setText(_translate("Previsione", "Risultati Test "))
