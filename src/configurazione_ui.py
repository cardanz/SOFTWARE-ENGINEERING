import os

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Configurazione(object):
    def setupUi(self, Configurazione):
        Configurazione.setObjectName("Configurazione")
        Configurazione.resize(510, 400)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Configurazione)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lab_configurazione = QtWidgets.QLabel(Configurazione)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lab_configurazione.setFont(font)
        self.lab_configurazione.setObjectName("lab_configurazione")
        self.verticalLayout_2.addWidget(self.lab_configurazione)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lab_nomeRete = QtWidgets.QLabel(Configurazione)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lab_nomeRete.setFont(font)
        self.lab_nomeRete.setObjectName("lab_nomeRete")
        self.verticalLayout.addWidget(self.lab_nomeRete)
        self.nomeRete = QtWidgets.QLineEdit(Configurazione)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nomeRete.setFont(font)
        self.nomeRete.setObjectName("nomeRete")
        self.verticalLayout.addWidget(self.nomeRete)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lab_nLayer = QtWidgets.QLabel(Configurazione)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lab_nLayer.setFont(font)
        self.lab_nLayer.setObjectName("lab_nLayer")
        self.horizontalLayout.addWidget(self.lab_nLayer)
        self.nLayer = QtWidgets.QSpinBox(Configurazione)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nLayer.setFont(font)
        self.nLayer.setMinimum(0)
        self.nLayer.setMaximum(20)
        self.nLayer.setObjectName("nLayer")
        self.horizontalLayout.addWidget(self.nLayer)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lab_nNodi = QtWidgets.QLabel(Configurazione)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lab_nNodi.setFont(font)
        self.lab_nNodi.setObjectName("lab_nNodi")
        self.horizontalLayout_2.addWidget(self.lab_nNodi)
        self.nNodi = QtWidgets.QSpinBox(Configurazione)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nNodi.setFont(font)
        self.nNodi.setMinimum(0)
        self.nNodi.setMaximum(50)
        self.nNodi.setObjectName("nNodi")
        self.horizontalLayout_2.addWidget(self.nNodi)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.lab_funzione = QtWidgets.QLabel(Configurazione)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lab_funzione.setFont(font)
        self.lab_funzione.setObjectName("lab_funzione")
        self.verticalLayout.addWidget(self.lab_funzione)
        self.funzione = QtWidgets.QComboBox(Configurazione)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.funzione.setFont(font)
        self.funzione.setObjectName("funzione")
        self.funzione.addItem("")
        self.funzione.addItem("")
        self.funzione.addItem("")
        self.funzione.addItem("")
        self.funzione.addItem("")
        self.funzione.addItem("")
        self.funzione.addItem("")
        self.funzione.addItem("")
        self.funzione.addItem("")
        self.verticalLayout.addWidget(self.funzione)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.but_caricaDataset = QtWidgets.QPushButton(Configurazione)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.but_caricaDataset.setFont(font)
        self.but_caricaDataset.setObjectName("but_caricaDataset")
        self.verticalLayout.addWidget(self.but_caricaDataset)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.lab_percentualeTs = QtWidgets.QLabel(Configurazione)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lab_percentualeTs.setFont(font)
        self.lab_percentualeTs.setObjectName("lab_percentualeTs")
        self.verticalLayout.addWidget(self.lab_percentualeTs)
        self.percentualeTs = QtWidgets.QSlider(Configurazione)
        self.percentualeTs.setMinimum(10)
        self.percentualeTs.setOrientation(QtCore.Qt.Horizontal)
        self.percentualeTs.setObjectName("percentualeTs")
        self.verticalLayout.addWidget(self.percentualeTs)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.comunicazione = QtWidgets.QLabel(Configurazione)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.comunicazione.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comunicazione.setFont(font)
        self.comunicazione.setText("")
        self.comunicazione.setObjectName("comunicazione")
        self.verticalLayout.addWidget(self.comunicazione)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.but_caricaRete = QtWidgets.QPushButton(Configurazione)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.but_caricaRete.setFont(font)
        self.but_caricaRete.setObjectName("but_caricaRete")
        self.horizontalLayout_4.addWidget(self.but_caricaRete)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.but_convalida = QtWidgets.QPushButton(Configurazione)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.but_convalida.setFont(font)
        self.but_convalida.setObjectName("but_convalida")
        self.horizontalLayout_3.addWidget(self.but_convalida)

        self.but_salva = QtWidgets.QPushButton(Configurazione)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.but_salva.setFont(font)
        self.but_salva.setObjectName("but_salva")
        self.horizontalLayout_3.addWidget(self.but_salva)

        self.but_train = QtWidgets.QPushButton(Configurazione)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.but_train.setFont(font)
        self.but_train.setObjectName("but_train")
        self.horizontalLayout_3.addWidget(self.but_train)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        currentDir = os.path.dirname(os.path.abspath(__file__))
        pathIcon = os.path.join(currentDir, 'img','icon','configurazione.ico')
        Configurazione.setWindowIcon(QtGui.QIcon(pathIcon))

        self.retranslateUi(Configurazione)

        self.nomeRete.textChanged.connect(Configurazione.listenerModifiche)
        self.nLayer.valueChanged.connect(Configurazione.listenerModifiche)
        self.nNodi.valueChanged.connect(Configurazione.listenerModifiche)
        self.funzione.activated.connect(Configurazione.listenerModifiche)
        self.percentualeTs.valueChanged['int'].connect(Configurazione.listenerModifiche)
        self.but_caricaDataset.clicked.connect(Configurazione.listenerModifiche)

        self.but_convalida.clicked.connect(Configurazione.acquisizioneParametri)
        self.but_salva.clicked.connect(Configurazione.salvaNN)
        self.but_caricaRete.clicked.connect(Configurazione.openCaricaNN)
        self.but_caricaDataset.clicked.connect(Configurazione.caricaDataSet)
        self.percentualeTs.valueChanged['int'].connect(Configurazione.tsVs)
        self.percentualeTs.valueChanged['int'].connect(Configurazione.mostraPercentualeTs)
        self.but_train.clicked.connect(Configurazione.openVisualizzazione)
    
        QtCore.QMetaObject.connectSlotsByName(Configurazione)

    def retranslateUi(self, Configurazione):
        _translate = QtCore.QCoreApplication.translate
        Configurazione.setWindowTitle(_translate("Configurazione", "Configurazione della Rete Neurale"))
        self.lab_configurazione.setText(_translate("Configurazione", "Configurazione Rete Neurale"))
        self.lab_nomeRete.setText(_translate("Configurazione", "Nome Rete"))
        self.lab_nLayer.setText(_translate("Configurazione", "Numero Layer:"))
        self.lab_nNodi.setText(_translate("Configurazione", "Numero Nodi:"))
        self.lab_funzione.setText(_translate("Configurazione", "Funzione decisionale:"))
        self.funzione.setItemText(0, _translate("Configurazione", "relu"))
        self.funzione.setItemText(1, _translate("Configurazione", "sigmoid"))
        self.funzione.setItemText(2, _translate("Configurazione", "softmax"))
        self.funzione.setItemText(3, _translate("Configurazione", "softplus"))
        self.funzione.setItemText(4, _translate("Configurazione", "softsign"))
        self.funzione.setItemText(5, _translate("Configurazione", "tanh"))
        self.funzione.setItemText(6, _translate("Configurazione", "selu"))
        self.funzione.setItemText(7, _translate("Configurazione", "elu"))
        self.funzione.setItemText(8, _translate("Configurazione", "exponential"))
        self.but_caricaDataset.setText(_translate("Configurazione", "carica dataset"))
        self.lab_percentualeTs.setText(_translate("Configurazione", "Definisci partizione TS - VS:10%"))
        self.but_caricaRete.setText(_translate("Configurazione", "carica Rete"))
        self.but_convalida.setText(_translate("Configurazione", "convalida"))
        self.but_salva.setText(_translate("Configurazione", "salva"))
        self.but_train.setText(_translate("Configurazione", "train"))