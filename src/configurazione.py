""" Interfaccia grafica di Configurazione di una Rete Neurale """
import csv
import time
import os
from slugify import slugify

from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget
from configurazione_ui import Ui_Configurazione
from visualizzazione import Visualizzazione

from NNcreator import NNcreators


__author__ = "Matteo Cardano,Stefano Lavaggi"
__version__ = "1.0"
__maintainer__ = "Matteo Cardano, Stefano Lavaggi"
__email__ = "ste.lavaggi@gmail.com matteo.cardano@gmail.com"


class Configurazione(QWidget):
    """ 
        Oggetto utilizzato per definire una interfaccia di Configurazione
        per una Rete Neurale (NN)

        Attributi:
        ----------
        _myNNcreator : NNcreator.NNcreators
            Oggetto per chiamare le funzioni collegate alla Rete Neurale
        __sequenza: Boolean
            Per controllare che sia stato effettuato il click sul tasto 'Salva'
        __convalida: Boolean
            Per controllare che sia stato effettuato il click sul tasto 'Convalida'
        __dataset: string
            Variabile contenente il percorso del dataset
        __percentuale: int
            Variabile contenente la percentuale di suddivisione del dataset in
            training-set e test-set
    """

    __myNNcreator = None
    __sequenza = False
    __convalida = False
    __dataSet = ""
    __percentuale = 10

    def __init__(self):
        super(Configurazione, self).__init__()
        
        self.ui = Ui_Configurazione()
        self.ui.setupUi(self)

    def acquisizioneParametri(self):
        """ Acquisisce i parametri inseriti nei vari campi presenti nell'interfaccia.
            Vengono effettuati anche tutti i controlli richiesti per ottenere dei dati validi per 
            la successiva creazione della Rete Neurale

            Ritorna:
            -------
            True/False: se i dati inseriti rispettano le richieste
        """

        messaggio =''

        try: 
            self.__rete = slugify(self.ui.nomeRete.text())
            # controllo se la lunghezza del nome inserito sia > di 5 caratteri
            if(len(self.__rete) < 5 or len(self.__rete) > 30):

                messaggio = 'err: inserimento Nome'
                raise NameError
                        
            # controllo che il nome scelto sia univoco
            isPresent = self.__NNNameCheck()
            if(isPresent):
                messaggio = 'err: nome già utilizzato'
                raise NameError

            # controlli su numero layer e numero nodi che siano >= 1
            # e che siano rispettivamente <= 20 e <= 50
            self.__layer = int(self.ui.nLayer.text())
            if(self.__layer < 1):
                messaggio = 'err: numero layer < 1'
                raise ValueError
            elif(self.__layer >= 20):
                messaggio = 'err: numero layer > 20'
                raise ValueError

            self.__nodi = int(self.ui.nNodi.text())
            if(self.__nodi < 1):
                messaggio = 'err: numero nodi < 1'
                raise ValueError
            if(self.__nodi >= 50):
                messaggio = 'err: numero nodi > 50'
                raise ValueError

            # salvataggio della funzione scelta
            self.__funzione = self.ui.funzione.currentText()
            
            # controllo che la percentuale di Vs sia < 25%
            # e che la percentuale di Ts sia > 75%
            if(self.__percentuale < 25):
                messaggio = 'err: suddivisione'
                raise ValueError
            if (self.__percentuale > 75):
                messaggio = 'err: suddivisione'
                raise ValueError

            # controllo che sia stato scelto effettivamente un dataset
            if(len(self.__dataSet) == 0):
                messaggio = 'err: dataSet errato'
                raise NameError

            # setto il tasto caricamento di una rete non cliccabile
            self.ui.but_caricaRete.setEnabled(False)

            # cambio nome del tasto convalida
            self.ui.but_convalida.setText('confermato')
            self.ui.comunicazione.setText('')
            #abilito salvataggio
            self.ui.but_salva.setEnabled(True)

            # settandola a True permetto che il training venga effettuato
            # dato che i dati inseriti sono validi
            self.__convalida = True
            return True
        except:
            # in caso di eccezzioni faccio comparire il messaggio
            self.ui.comunicazione.setText(messaggio)
            return False


    def salvaNN(self):
        '''
            Funzione relativa al tasto 'Salva' presente nell'interfaccia, 
            permettendo il salvataggio della Rete Neurale convalidata in precedenza.
        '''
        # solamente se la rete è stata convalidata salvo la rete
        if(self.__convalida == True and self.acquisizioneParametri() == True):
            # salvo il path dove salverò la rete
            currentDir = os.path.dirname(os.path.abspath(__file__))
            pathNNs = os.path.join(currentDir, 'modelliSalvati', self.__rete)
            # scrivo il csv contenente i dati della rete configurata
            try:
                # creo la cartella che conterra il csv e la futura rete
                os.mkdir(pathNNs)

                pathCSV = os.path.join(currentDir, 'modelliSalvati', self.__rete, self.__rete + ".csv")
                f = open(pathCSV, 'w')
                f.write(self.__rete + ',' + str(self.__layer) + ',' + str(self.__nodi) + ',' + str(
                    self.__percentuale) + ',' + str(self.__funzione) + ',' + str(self.__dataSet))
                f.close()
            except:
                messaggio = 'err: lettura file'
                self.ui.comunicazione.setText(messaggio)
            
            # setto il tasto di salvataggio disabilitato e 
            # faccio si che venga mostrato che la rete è stata salvata correttamente
            self.ui.but_salva.setEnabled(False)
            self.ui.but_salva.setText('salvata')

            # genero la rete
            self.generaNN(self.__layer, self.__nodi, self.__percentuale, self.__funzione, self.__rete, self.__dataSet)
            # abilito la possibilità di training
            self.__sequenza = True
            # resetto text pulsante
            self.ui.but_convalida.setText('convalida')
            # permetto il caricamento di una rete salvata
            self.ui.but_caricaRete.setEnabled(True)
            
        else:
            self.ui.comunicazione.setText('err: convalidare la rete')

    def openCaricaNN(self):
        """
            Funzione riferita al pulsante 'Carica' presente nell'interfaccia.
            Permette il caricamento di una Rete Neurale già configurata, tramite
            una finestra
        """

        self.ui.comunicazione.setText(" ")
        try:
            # salvo il path della cartella contenente
            # tutte le reti salvate
            currentDir = os.path.dirname(os.path.abspath(__file__))
            pathNNs = os.path.join(currentDir, 'modelliSalvati')
            # filtro per far scegliere solo file .csv
            filter = "csv(*.csv)"
            # apro il dialog per permettere la scelta della rete da caricare
            nomeFile = QFileDialog.getOpenFileName(None,None,pathNNs,filter)

            
        # controllo che sia stata effettivamente scelta una rete
            if (nomeFile[0] == ''):
                self.ui.comunicazione.setText("err: rete non caricata")
                raise ValueError

            self.caricaNN(nomeFile[0])

        except:
            self.ui.comunicazione.setText("err: errore carica NN")

    def caricaNN(self,percorso):
        """  
            Setta il modello scelto dalla schermata di caricamento 
            aperta in precedenza

            Parametri:
            ---------
            percorso: string
                percorso della Rete Neurale da caricare
        """

        # caricata correttamente la rete permetto il training
        # andato a disabilitare il tasto 'conferma'
        # e permettendo il solo training
        self.__convalida = False
        self.__sequenza = True
        # non rendo cliccabile il tasto 'convalida'
        self.ui.but_convalida.setText('convalida')
        self.ui.but_convalida.setEnabled(False)
        # non rendo cliccabile il tasto di salvataggio
        self.ui.but_salva.setText('salva')
        self.ui.but_salva.setEnabled(False)
        # leggo il file selezionato e genero una rete con le
        # caratteristiche salvate
        try:
            with open(percorso) as f:
                lis = (f.readline().split(','))
                try:
                    self.generaNN(int(lis[1]), int(lis[2]), int(lis[3]), lis[4], lis[0], lis[5])
                except:
                    print("errore")
                    self.ui.comunicazione.setText("err: file non conforme")
                    self.ui.but_convalida.setEnabled(True)
                    self.__sequenza = False
                    self.ui.but_caricaRete.setText('carica Rete')
                    self.ui.but_caricaRete.setEnabled(True)
                    return

            # sovrascrivo la rete creata con quella salvata
            percorso = os.path.split(percorso)
            pathRete = os.path.join(percorso[0], lis[0])
            try:
                self.__myNNcreator.setModello(pathRete)
            except:
                self.ui.comunicazione.setText("war: up modello -> train")

            # mostro l'effettivo caricamento della rete
            # e non rendo cliccabile il tazto di caricamento della rete
            self.ui.but_caricaRete.setText('caricata')
            self.ui.but_caricaRete.setEnabled(False)
        except:
            self.ui.comunicazione.setText("err: percorso errato")

    def generaNN(self, layer, nodi, percentuale, funzione, rete, dataSet):
        
        """ 
        Genera una Rete Neurale utilizzando i parametri inseriti 
        
            Parametri
            ----------
            layer : int
                Numero di hidden-layer 
            nodi : int
                Numero di nodi per layer
            percentuale: int
                Percentuale di suddivisione del dataset in Training-Set e Validation-Set
            rete: string
                Nome della Rete Neurale
            dataSet: string
                Percorso del file utilizzato come dataset
        """
        # salvo i parametri inseriti dall 'interfaccia nell'oggetto
        # reteNeurale della NNcreators
        self.__myNNcreator = NNcreators(layer, nodi, percentuale, funzione, rete, dataSet)
        # creo i due csv contententi i due dataset (training, testing)
        self.__myNNcreator.generazioneFileDatasets()
        # creazione delle strutture dati per l'effettivo 
        # training e per l' effettivo testing
        self.__myNNcreator.generazioneDatasets()
        # genero il modello Keras con le caratteristiche scelte
        self.__myNNcreator.generazioneModello()

    def caricaDataSet(self):
        """ Apre la schermata per effettuare il caricamento del dataset """
        # salvataggio del percorso della cartella contenente i dataset
        currentDir = os.path.dirname(os.path.abspath(__file__))
        pathDataset = os.path.join(currentDir, 'dataset')
        # permetto il solo caricamento di file csv
        filter = "csv(*.csv)"
        try:
            # apro la schermata di caricamento
            nomeFile = QFileDialog.getOpenFileName(None,None,pathDataset,filter)
            percorso = nomeFile[0]
            datafilename = percorso
            d = ','
            f = open(datafilename, 'r')
            reader = csv.reader(f, delimiter=d)
            ncol = len(next(reader))
            if(ncol != 5):
                raise ValueError

        except:
            messaggio = 'err: apertura file'
            self.ui.comunicazione.setText(messaggio)

        # controllo che sia stato caricato il dataset
        try:
            self.__dataSet = percorso

            if(len(self.__dataSet) == 0):
                messaggio = 'err: dataSet non caricato'
                raise NameError
        except:
            # mostro il messaggio di errore
            self.ui.comunicazione.setText(messaggio)

    def tsVs(self):
        """ Salva la percentuale inserita nello slider per la suddivisione del dataset """
        self.__percentuale = self.ui.percentualeTs.value()

    def __NNNameCheck(self):
        """ Controlla che il nome scelto per la Rete Neurale sia univoco """
        # salvo il path della cartella contenente i modelli salvati
        try:
            currentDir = os.path.dirname(os.path.abspath(__file__))
            pathNNs = os.path.join(currentDir,'modelliSalvati')
            # ottengo la lista delle directory presenti all'interno di 'modelliSalvati'
            dirList = os.listdir(pathNNs)
        except:
            print("errore lista directory")
        # setto la var booleana a true se il nome è gia utilizzato
        if self.__rete in dirList:
            isPresent = True
        else:
            isPresent = False

        return isPresent

    def openVisualizzazione(self):
        """ Apertura della schermata per la visualizzazione dei risultati del training """
        # controllo che sia stata creata una rete o che sia stata configurata
        if(self.__sequenza == True):
            self.ui.comunicazione.setText('')
            # inizializzo il cronometro per contare
            # il tempo di esecuzione
            start = time.time()
            # parte il training del modello
            self.__myNNcreator.trainingModello()
            # stoppo il cronometro
            end = time.time()
            # calcolo il lasso di tempo effettivo
            tempo = end-start
            tempo = round(tempo,2)
            # salvo il percorso contenente l'immagine 
            # dell' andamento della loss e della accuracy
            pathImg = self.__myNNcreator.salvataggioRisultati()
            # parte il testing della rete 
            self.__myNNcreator.testing()
            # mi salvo i risultati dei testing e di training
            test, train = self.__myNNcreator.risultati()
            # creo ed apro la interfaccia di visualizzazione
            # per mostrare i risultati
            self.uiVisualizzazione = Visualizzazione()
            self.uiVisualizzazione.setup(test,train,pathImg,self.__myNNcreator,tempo)
            self.uiVisualizzazione.show()

            # rendo il tasto 'convalida' nuovamente cliccabile
            self.ui.but_convalida.setEnabled(True)
            self.ui.but_convalida.setText('convalida')
            # rendo il tasto 'carica' nuovamente cliccabile
            self.ui.but_caricaRete.setEnabled(True)
            self.ui.but_caricaRete.setText('carica rete')
            # rendo il tasto 'salva' nuovamente cliccabile
            self.ui.but_salva.setEnabled(True)
            self.ui.but_salva.setText('salva')
        else:
            self.ui.comunicazione.setText('err: salva/carica una rete')

    def mostraPercentualeTs(self):
        '''
            Metodo che mostra la percentuale(%) scelta per la partizione
            tra training-dataset e test-dataset in tempo reale
        '''
        self.ui.lab_percentualeTs.setText('Definisci partizione TS - VS:' + 
                                            str(self.ui.percentualeTs.value()) + 
                                            '%')

    def listenerModifiche(self):
        """
            Listener sugli elementi dell'interfaccia
            di configurazione che permettono la definizione
            delle caratteristiche della Rete Neurale
        """

        # solo se non è stata caricata una rete
        # ad ogni modifica effettuata 
        if (self.ui.but_caricaRete.isEnabled() or self.__convalida == True) :
            # resetto la convalida della rete
            self.__convalida = False
            self.ui.but_convalida.setText("convalida")
            # resetto la possibilità di effettuare il training
            self.__sequenza = False
            self.ui.but_salva.setEnabled(True)
            self.ui.but_salva.setText('salva')
        
    def setPercentualeTs(self,percentualeTs):
        """ Setter per la percentuale di suddivisione dei dataset"""
        self.__percentuale = percentualeTs

    def setDataset(self,dataset):
        """ Setter per il dataset"""
        self.__dataSet = dataset

    
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    # creo oggetto configurazione
    myapp = Configurazione()
    # mostra la schermata di configurazione
    myapp.show()
    sys.exit(app.exec_())