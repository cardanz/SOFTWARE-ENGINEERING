""" Classe di una Rete Neurale """
import os

import tensorflow as tf

__author__ = "Matteo Cardano,Stefano Lavaggi"
__version__ = "1.0"
__maintainer__ = "Matteo Cardano, Stefano Lavaggi"
__email__ = "ste.lavaggi@gmail.com matteo.cardano@gmail.com"


class NeuralNetwork():
    """ Oggetto Rete Neurale (NN)
        
        Attributi
        ----------
        __numeroLayer : int
            Numero di hidden-layer 
        __numeroNodi : int
            Numero di nodi per layer
        __percentualeTs: int
            Percentuale di suddivisione del dataset in Training-Set e Validation-Set
        __funzione: string
            Funzione di decisione scelta
        __modelName: string
            Nome della Rete Neurale
        __datasetPath: string
            Percorso del file utilizzato come dataset
        __fileDir: string
            Percorso in cui è presente il file python
        __pathSave: string
            Percorso in cui dovrà esser salvata la Rete Neurale
        __train_dataset_fp: string
            Percorso del dataset di training
        __test_dataset_fp: string
            Percorso del dataset di test
        __dimTs: int
            Numero di righe del dataset dedicate al training-dataset
        __dimVs: int
            Numero di righe del dataset dedicate al validation-dataset (test-dataset)
        __train_dataset: tf.Tensor
            Dataset utilizzato per il training
        __test_dataset: tf.Tensot
            Dataset utilizzato er il testing
        __features: tf.Tensor
            Dati riferiti alle caratteristiche del dataset
        __labels: tf.Tensor
            Dati riferiti alla tipologia
        __model: tf.keras.Sequential
            Modello di Rete Neurale
        train_loss_results: tf.Tensor
            Andamento della Loss nel training
        train_accuracy_results: tf.Tensor
            Andamento della Accuracy nel training
        test_accuracy: tf.keras.metrics.Accuracy()
            Accuracy del testing
    """

    def __init__(self):
        """ Inizializzazione degli attributi della classe """
        self.__numeroLayer = 0
        self.__numeroNodi = 0
        self.__percentualeTs = 0
        self.__funzione = ''
        self.__modelName = ''
        self.__datasetPath = ''

        self.__fileDir = os.path.dirname(os.path.abspath(__file__))
        self.__pathSave = ''

        self.__train_dataset_fp = ''
        self.__test_dataset_fp = ''

        self.__dimTs = 0
        self.__dimVs = 0

        self.__train_dataset = None
        self.__test_dataset = None
        self.__features = None
        self.__labels = None

        self.__model = None


        # tipologia di oggetto c'è all interno della lista
        self.train_loss_results = [] # type: tf.Tensor
        self.train_accuracy_results = [] # type: tf.Tensor

        self.test_accuracy = None

    @property
    def numeroLayer(self):
        return self.__numeroLayer

    @numeroLayer.setter
    def numeroLayer(self ,numeroLayer):
        self.__numeroLayer = numeroLayer

    @property    
    def numeroNodi(self):
        return self.__numeroNodi

    @numeroNodi.setter
    def numeroNodi(self, numeroNodi):
        self.__numeroNodi = numeroNodi
    
    @property
    def percentualeTs(self):
        return self.__percentualeTs

    @percentualeTs.setter
    def percentualeTs(self, percentualeTs):
        self.__percentualeTs = percentualeTs

    @property
    def funzione(self):
        return self.__funzione

    @funzione.setter
    def funzione(self, funzione):
        self.__funzione = funzione

    @property
    def modelName(self):
        return self.__modelName
    
    @modelName.setter
    def modelName(self, modelName):
        self.__modelName = modelName

    @property
    def datasetPath(self):
        return self.__datasetPath

    @datasetPath.setter
    def datasetPath(self, datasetPath):
        self.__datasetPath = datasetPath

    @property
    def fileDir(self):
        return self.__fileDir
 
    @fileDir.setter
    def fileDir(self, fileDir):
        self.__fileDir = fileDir

    @property
    def pathSave(self):
        return self.__pathSave

    @pathSave.setter
    def pathSave(self, pathSave):
        self.__pathSave = pathSave

    @property
    def train_dataset_fp(self):
        return self.__train_dataset_fp

    @train_dataset_fp.setter
    def train_dataset_fp(self, train_dataset_fp):
        self.__train_dataset_fp = train_dataset_fp

    @property
    def test_dataset_fp(self):
        return self.__test_dataset_fp

    @test_dataset_fp.setter
    def test_dataset_fp(self, test_dataset_fp):
        self.__test_dataset_fp = test_dataset_fp

    @property
    def dimTs(self):
        return self.__dimTs
        
    @dimTs.setter
    def dimTs(self, dimTs):
        self.__dimTs = dimTs

    @property
    def dimVs(self):
        return self.__dimVs

    @dimVs.setter
    def dimVs(self, dimVs):
        self.__dimVs = dimVs

    @property
    def train_dataset(self):
        return self.__train_dataset

    @train_dataset.setter
    def train_dataset(self, train_dataset):
        self.__train_dataset = train_dataset

    @property
    def test_dataset(self):
        return self.__test_dataset

    @test_dataset.setter
    def test_dataset(self, test_dataset):
        self.__test_dataset = test_dataset
        
    @property
    def features(self):
        return  self.__features

    @features.setter
    def features(self, features):
        self.__features = features
    
    @property
    def labels(self):
        return  self.__labels
     
    @labels.setter
    def labels(self, labels):
        self.__labels = labels

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model