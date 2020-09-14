import sys
import os
import pytest
import unittest
import numpy
import tensorflow as tf

from NN import NeuralNetwork

class Test_NeuralNetwork(unittest.TestCase):

    def setUp(self):
        self.NN = NeuralNetwork()

    def test_NN(self):
        self.NN.numeroLayer = 10
        assert self.NN.numeroLayer == 10

        self.NN.numeroNodi = 10
        assert self.NN.numeroNodi == 10

        self.NN.percentualeTs = 10
        assert self.NN.percentualeTs == 10

        self.NN.funzione = 'relu'
        assert self.NN.funzione == 'relu'

        self.NN.modelName = 'test'
        assert self.NN.modelName =='test'

        self.NN.datasetPath = '/path/to/test'
        assert self.NN.datasetPath =='/path/to/test'

        self.NN.fileDir = '/path/to'
        assert self.NN.fileDir =='/path/to'

        self.NN.pathSave = '/path/to/test'
        assert self.NN.pathSave =='/path/to/test'

        self.NN.train_dataset_fp = '/path/to/test/dataset_training'
        assert self.NN.train_dataset_fp =='/path/to/test/dataset_training'

        self.NN.test_dataset_fp = '/path/to/test/dataset_test'
        assert self.NN.test_dataset_fp =='/path/to/test/dataset_test'

        self.NN.dimTs = 70
        assert self.NN.dimTs == 70

        self.NN.dimVs = 30
        assert self.NN.dimVs == 30

        A = numpy.ones((5, 5)) 

        self.NN.train_dataset = A
        assert numpy.array_equal(self.NN.train_dataset, A) == True

        self.NN.test_dataset = A
        assert numpy.array_equal(self.NN.test_dataset, A) == True

        self.NN.features = ['sensore1', 'sensore 2', 'sensore 3', 'sensore 4']
        assert self.NN.features == ['sensore1', 'sensore 2', 'sensore 3', 'sensore 4']
        assert len(self.NN.features) == 4

        self.NN.labels = ['Nessun errore','Errore non grave','Errore']
        assert self.NN.labels == ['Nessun errore','Errore non grave','Errore']
        assert len(self.NN.labels) == 3

        model = tf.keras.Sequential(name = self.NN.modelName)
        self.NN.model = tf.keras.Sequential(name = self.NN.modelName)
        assert model.get_config() == self.NN.model.get_config()





