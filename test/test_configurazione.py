import shutil
import sys
import os
import time

import pytest

from PyQt5.QtWidgets import QApplication, QFileDialog, QInputDialog, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets

from configurazione import Configurazione

from visualizzazione import Visualizzazione

app = QApplication(sys.argv)

# def setUp(self):
@pytest.fixture(scope='module')
def form():
    form = Configurazione()
    yield form

@pytest.mark.parametrize(['nome' ,'numeroLayer' ,'numeroNodi' ,'funzione' ,'dataset' ,'percentualeTs' ,'risultato'],
                        [
                        ('',0,0,'','','','err: inserimento Nome'),
                        ('stefano',0,0,'','','','err: nome già utilizzato'),
                        ('test-dati-errati',0,0,'','','','err: numero layer < 1'),
                        ('test-dati-errati',20,0,'','','','err: numero layer > 20'),
                        ('test-dati-errati',1,0,'','','','err: numero nodi < 1'),
                        ('test-dati-errati',1,50,'','','','err: numero nodi > 50'),
                        ('test-dati-errati',1,1,'relu','',80,'err: suddivisione'),
                        ('test-dati-errati',1,1,'relu','',20,'err: suddivisione'),
                        ('test-dati-errati',1,1,'relu','',70,'err: dataSet errato')
                        ]
                    )
def test_dati_errati(form,nome,numeroLayer,numeroNodi,funzione,dataset,percentualeTs,risultato):

    form.ui.nomeRete.setText(nome)
    form.ui.nLayer.setValue(numeroLayer)
    form.ui.nNodi.setValue(numeroNodi)
    form.setPercentualeTs(percentualeTs)
    form.setDataset(dataset)

    form.acquisizioneParametri()

    assert form.ui.comunicazione.text() == risultato


@pytest.mark.parametrize(['nome' ,'numeroLayer' ,'numeroNodi' ,'funzione' ,'dataset' ,'percentualeTs' ,'risultato'],
                        [
                            ('test-dati-corretti2',1,10,'relu','signal_dataset.csv',70,'prova')
                        ]
                        )
def test_acquizione_correto(form,nome,numeroLayer,numeroNodi,funzione,dataset,percentualeTs,risultato):

    form.ui.nomeRete.setText(nome)
    form.ui.nLayer.setValue(numeroLayer)
    form.ui.nNodi.setValue(numeroNodi)
    form.setPercentualeTs(percentualeTs)

    currentDir = os.path.dirname(os.path.abspath(__file__))
    splitPath = os.path.split(currentDir)
    datasetPath= os.path.join(splitPath[0],'src','dataset',dataset)
    form.setDataset(datasetPath)

    ritorno = form.acquisizioneParametri()
    assert ritorno == True
    assert form.ui.comunicazione.text() == ''


@pytest.mark.parametrize(['bool','s'],
                        [
                            (True,""),
                            (False,"")
                        ]
                        )
def test_salva(form,bool,s):
    if(bool == True):
        assert form._Configurazione__sequenza == False
        form.salvaNN()
        assert form._Configurazione__sequenza == True

    else:
        form._Configurazione__convalida = False
        form.salvaNN()
        assert form.ui.comunicazione.text() == "err: convalidare la rete"
        assert type(form.ui.comunicazione.text()) is str


@pytest.mark.parametrize(['bool', 's'],
                        [
                             (True, ""),
                             (False, "")
                        ]
                        )

def test_visualizzazione(form,bool,s):
    form.ui.comunicazione.setText("")
    if (bool == True):
        form._Configurazione__sequenza = True
        assert form.ui.comunicazione.text() == ""
        form.openVisualizzazione()
        assert type(form.uiVisualizzazione) is Visualizzazione
        
    else:
        form._Configurazione__sequenza = False
        form.openVisualizzazione()
        assert form.ui.comunicazione.text() == 'err: salva/carica una rete'



@pytest.mark.parametrize(['number', 's'],
                        [
                             (0, ""),
                             (1, ""),
                             (2, "")
                        ]
                        )
def test_caricaRete(form,number,s):
    form.ui.comunicazione.setText("")
    form.uiVisualizzazione.close()
    currentDir = os.path.dirname(os.path.abspath(__file__))
    splitPath = os.path.split(currentDir)
    reteEl = os.path.join(splitPath[0], 'src', 'modelliSalvati', 'test-dati-corretti2')
    rete = os.path.join(splitPath[0], 'src', 'modelliSalvati','test-dati-corretti2','test-dati-corretti2.csv')
    if(number == 0):
        reteErr = os.path.join(splitPath[0],'src','dataset','previsione','signal_prediction.csv')
        form.caricaNN(reteErr)
        assert form.ui.comunicazione.text() == 'err: file non conforme'
    elif (number == 1):
        form.caricaNN(rete)
        assert form.ui.comunicazione.text() == ''
        shutil.rmtree(reteEl)
    elif(number == 2):
        form.caricaNN("ajeje")
        assert form.ui.comunicazione.text() == 'err: percorso errato'
