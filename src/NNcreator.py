""" Creazione di una Rete Neurale"""
import math
import os
import time

import matplotlib.pyplot as plt
import tensorflow as tf
from numpy import genfromtxt
from tensorflow.python.keras.models import load_model
from NN import NeuralNetwork


__author__ = "Matteo Cardano,Stefano Lavaggi"
__version__ = "1.0"
__maintainer__ = "Matteo Cardano, Stefano Lavaggi"
__email__ = "ste.lavaggi@gmail.com matteo.cardano@gmail.com"


class NNcreators():
    """ Classe di operazioni di Rete Neurale 
    
    Attributi
    ---------
    reteNeurale: NeuralNetwork
        Oggetto Rete Neurale
    column_names: string[]
        Nomi di tutte le colonne del dataset
    feature_names: string[]
        Nomi delle colonne riferite alla caratteristiche
    label_name: string
        Nome della colonna riferito alla tipologia
    class_names: string[]
        Tipologie di errori
    """
    
    reteNeurale = NeuralNetwork()

    column_names = ['sensore1', 'sensore2', 'sensore3', 'sensore4', 'tipologia']
    feature_names = column_names[:-1]
    label_name = column_names[-1]
    class_names = ['Nessun Errore', 'Errore non grave', 'Errore']

    def __init__(self, numeroLayer, numeroNodi, percentualeTs, funzione, ModelName, datasetPath):
        """ Inizializzazione degli attributi della reteNeurrale
            
            Parametri
            ---------- 
            numeroLayer: int
                Numero di hidden-layer della Rete Neurale
            numeroNodi: int
                Numero di nodi per layer
            percentualeTs: int
                Percentuale del dataset dedicata al training
            funzione: string
                Funzione di decisione
            ModelName: string
                Nome della rete
            datasetPath: string
                Percorso del dataset
        """
        super().__init__()
        # settaggio delle caratteristiche della rete
        # self.reteNeurale.set__numeroLayer(numeroLayer)
        self.reteNeurale.numeroLayer = numeroLayer
        # self.reteNeurale.set__numeroNodi(numeroNodi)
        self.reteNeurale.numeroNodi = numeroNodi
        # self.reteNeurale.set__percentualeTs(percentualeTs)
        self.reteNeurale.percentualeTs = percentualeTs
        # self.reteNeurale.set__funzione(funzione)
        self.reteNeurale.funzione = funzione
        # self.reteNeurale.set__ModelName(ModelName)
        self.reteNeurale.modelName = ModelName
        # self.reteNeurale.set__datasetPath(datasetPath)
        self.reteNeurale.datasetPath = datasetPath
        # ModelName = self.reteNeurale.get__ModelName()
        # fileDir = self.reteNeurale.get__fileDir()
        fileDir = os.path.dirname(os.path.abspath(__file__))
        self.reteNeurale.fileDir = fileDir

        # settaggio dei vari percorsi utili (salvataggio, trainingdata, testdata)
        pathSave = os.path.join(fileDir, 'modelliSalvati',self.reteNeurale.modelName,self.reteNeurale.modelName)
        self.reteNeurale.pathSave = pathSave

        pathTrain = os.path.join(fileDir, 'dataset', 'signal_training.csv')
        self.reteNeurale.train_dataset_fp = pathTrain

        pathTest = os.path.join(fileDir, 'dataset', 'signal_test.csv')
        self.reteNeurale.test_dataset_fp = pathTest
        
        # calcolo numero righe dataset
        try:
            with open(datasetPath) as f:
                numeroRighe = (sum(1 for line in f))

            # calcolo percentuale di suddivisone del dataset
            # tra il training e il testset
            # self.reteNeurale.set__dimTs(math.ceil(((numeroRighe - 1) / 100) * percentualeTs))
            self.reteNeurale.dimTs = math.ceil(((numeroRighe - 1) / 100) * percentualeTs)
            # self.reteNeurale.set__dimVs((numeroRighe - 1) - self.reteNeurale.get__dimTs())
            self.reteNeurale.dimVs = (numeroRighe - 1) - self.reteNeurale.dimTs
        except:
            print("errore apertura file NNcreator")


    def generazioneFileDatasets(self):
        """ Genera i due file di dataset:
            - uno dedicato per il training della rete
            - l' altro dedicato al testing della rete 
        """
        try:
            dataset = genfromtxt(self.reteNeurale.datasetPath, delimiter = ',')
            f = open(self.reteNeurale.train_dataset_fp, 'w')
            j = 0
            for item in dataset:
                if j == self.reteNeurale.dimTs:
                    break
                for i in range(len(item)):
                    if i == 0:
                        f.write(str(item[i]))
                    elif (i < len(item) - 1):
                        f.write(',' + str(item[i]))
                    elif (i == len(item) - 1):
                        f.write(',' + str(int(item[i])))
                f.write('\n')
                j = j + 1
            f.close()

            f = open(self.reteNeurale.test_dataset_fp,'w')
            j = self.reteNeurale.dimTs + 1
            k = 0
            for item in dataset:
                if k < j:
                    k = k + 1
                    continue
                for i in range(len(item)):
                    if i == 0:
                        f.write(str(item[i]))
                    elif (i < len(item) - 1):
                        f.write(',' + str(item[i]))
                    elif (i == len(item) - 1):
                        f.write(',' + str(int(item[i])))
                f.write('\n')
            f.close()
        except:
            print("errore creazione file Ts e Vs")


    def generazioneDatasets(self):
        """ Generazione dei dataset che vengono utilizzati per training e testing della rete"""
        # dal file csv creo l' effettivo dataset per il training       
        train_dataset = tf.data.experimental.make_csv_dataset(
            self.reteNeurale.train_dataset_fp,
            batch_size=self.reteNeurale.dimTs,
            column_names=self.column_names,
            label_name=self.label_name,
            num_epochs=1)

        def pack_features_vector(features, labels):
            """Inserisce le caratteristiche (features) in un singolo array"""
            features = tf.stack(list(features.values()), axis=1)
            return features, labels

        # dal file csv creo l' effettivo dataset per il testing
        test_dataset = tf.data.experimental.make_csv_dataset(
            self.reteNeurale.test_dataset_fp,
            batch_size=self.reteNeurale.dimVs,
            column_names=self.column_names,
            label_name=self.label_name,
            num_epochs=1,
            shuffle=False)
        
        # reshape dei due dataset e settaggio dei due datasets
        self.reteNeurale.train_dataset = train_dataset.map(pack_features_vector)
        self.reteNeurale.test_dataset = test_dataset.map(pack_features_vector)

        features, labels = next(iter(self.reteNeurale.train_dataset))
        self.reteNeurale.features = features
        self.reteNeurale.labels = labels


    def switch_fun(self,argument):
        """ Funzione di switch per le varie funzioni possibili 
        
        Parametri
        ---------
        argument: string
            Stringa contenente il nome della funzione di decisione scelta
        
        
        Ritorna
        -------
        switcher.get(argument): tf.nn.*
            Funzione di decisione che viene utilizzata nella Rete Neurale
        """

        # creazione dello switch per associare
        # il nome della stringa scelta dall'interfaccia
        # alla funzione vera e propria
        switcher = {
            'relu': tf.nn.relu,
            'sigmoid': tf.nn.sigmoid,
            'softmax': tf.nn.softmax,
            'softplus': tf.nn.softplus,
            'softsign': tf.nn.softsign,
            'tanh': tf.nn.tanh,
            'selu': tf.nn.selu,
            'elu': tf.nn.elu,
        }

        return switcher.get(argument)

    def generazioneModello(self):
        """ Generazione della Rete Neurale con le caratteristiche scelte """

        # salvataggio numero nodi e layers e della funzione di attivazione
        nNodi = self.reteNeurale.numeroNodi
        nLayer = self.reteNeurale.numeroLayer
        model = self.reteNeurale.model
        funzioneAtt = self.switch_fun(self.reteNeurale.funzione)

        # crezione del modello di rete
        model = tf.keras.Sequential(name = self.reteNeurale.modelName)
        
        # aggiunta del layer iniziale
        model.add(tf.keras.layers.Dense(nNodi, activation=funzioneAtt, input_shape=(4,)))

        # aggiunta di 'i' ( numero scelto da interfaccia )  di hidden layer
        for i in range(1, nLayer + 1):
            model.add(tf.keras.layers.Dense(nNodi, activation=funzioneAtt))

        # aggiunta del output layer
        model.add(tf.keras.layers.Dense(3))

        # setto il modello creato all'oggetto reteNeurale
        self.reteNeurale.model = model

    def trainingModello(self):
        """ Training della Rete Neurale """
        # creo la funzione di loss (scelgo la SparseCategoricalCrossentropy per via della
        # presenza di 2 o piu label)
        loss_object = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

        # definisco la funzione 'loss' che confronta la label 
        # letta nel dataset con quella ottentuta dal training
        def loss(model, x, y, training):
            y_ = model(x, training=training)
            return loss_object(y_true=y, y_pred=y_)

        def grad(model, inputs, targets):
            with tf.GradientTape() as tape:
                loss_value = loss(model, inputs, targets, training=True)

            return loss_value, tape.gradient(loss_value, model.trainable_variables)

        # scelgo l' ottimizzatore
        optimizer = tf.keras.optimizers.SGD(learning_rate=0.01)

        # salvo i dati della rete che devo allenare
        model = self.reteNeurale.model
        features = self.reteNeurale.features
        labels = self.reteNeurale.labels
        
        # setto il numero di 'epoch' (epoche) per cui
        # devo riperete il train
        num_epochs = 201

        # training effettivo
        for epoch in range(num_epochs):
            # definisco la loss media e la accuratezza
            epoch_loss_avg = tf.keras.metrics.Mean()
            epoch_accuracy = tf.keras.metrics.SparseCategoricalAccuracy()

            # training loop
            for x, y in self.reteNeurale.train_dataset:
                
                # ottimizzo il modello , salvando la loss
                # e il gradiente
                loss_value, grads = grad(model, x, y)

                optimizer.apply_gradients(zip(grads, model.trainable_variables))
                
                # tengo l' andamento della loss per creare il grafico
                epoch_loss_avg.update_state(loss_value)
                # e anche della accuracy
                epoch_accuracy.update_state(y, model(x, training=True))

            # salvataggio completo delle variabili 
            # contenenti l andamento della loss e della accuracy
            self.reteNeurale.train_loss_results.append(epoch_loss_avg.result())
            self.reteNeurale.train_accuracy_results.append(epoch_accuracy.result())

            if epoch % 50 == 0:
                print("Epoch {:03d}: Loss: {:.3f}, Accuracy: {:.3%}".format(epoch,
                                                                            epoch_loss_avg.result(),
                                                                            epoch_accuracy.result()))

    def salvataggioRisultati(self):
        """ Salva l' andamento della Loss e della Accuracy in una immagine (.png) """
        # salvataggio dell immagine dell' andamento loss e dell' accuratezza
        fig, axes = plt.subplots(2, sharex=True, figsize=(6, 4))
        fig.suptitle('Risultati Training')
        axes[0].set_ylabel("Loss", fontsize=10)
        axes[0].plot(self.reteNeurale.train_loss_results)
        axes[1].set_ylabel("Accuracy", fontsize=10)
        axes[1].set_xlabel("Epoca", fontsize=10)
        axes[1].plot(self.reteNeurale.train_accuracy_results)
        # per creare il nome univoco concateno l'orario corrente
        stringa = str(time.ctime())
        stringa = stringa.replace(" ", "_")
        stringa = stringa.replace(":", "_")
        # salvo l immagine nella cartella img
        pathSaveImg = os.path.join(self.reteNeurale.fileDir, 'img', self.reteNeurale.modelName + stringa)
        try:
            plt.savefig(pathSaveImg)
        except:
            print("errore salvataggio immagine")
        return pathSaveImg

    def testing(self):
        """ Effettua il testing della Rete Neurale """
        self.reteNeurale.test_accuracy = tf.keras.metrics.Accuracy()

        # inizio del testing
        for (x, y) in self.reteNeurale.test_dataset:
            # prendo il modello
            model = self.reteNeurale.model

            logits = model(x, training=False)
            prediction = tf.argmax(logits, axis=1, output_type=tf.int32)

            self.reteNeurale.test_accuracy(prediction, y)

        print("Test set accuracy: {:.3%}".format(self.reteNeurale.test_accuracy.result()))

    def previsione(self,predictionPath):
        """ Effettua la prediction sul file scelto 
        
        Parametri
        ---------
        predictionPath: string
            Percorso del file contenente il dataset su cui si deve
            effettuare la 'prediction'


        Ritorna
        -------
        ris: string[]
            Risultati della 'prediction' nella forma:
            "Riga: " + i +
            "Previsione: " + nomeFiorePredetto + percentualediAccuratezza
        """
        try:
            # leggo il dataset di previsione
            pre_dataset = genfromtxt(predictionPath, delimiter=',')
            # lo converto a tf.tensor per poterlo utilizzare
            predict_dataset = tf.convert_to_tensor(pre_dataset)

            model = self.reteNeurale.model
            predictions = model(predict_dataset, training=False)
            ris = []

            for i, logits in enumerate(predictions):
                class_idx = tf.argmax(logits).numpy()
                funzioneAtt = tf.nn.softmax
                p = funzioneAtt(logits)[class_idx]
                name = self.class_names[class_idx]

                # aggiunta dei valori predetti, con la percentuale di accuracy
                ris.append("Riga: " + str(i) +  "\nPrevisione: " + name +" ("+"{:.3%}".format(p) + ")")

            return ris
        except:
            print("errore definizione file")

    def risultati(self):

        """ Salvataggio della Rete Neurale generata 
        
        Ritorna
        -------
        testAccuracyResult: string[]
            Percentuale di 'Accuracy' del test effettuato
        trainAccuracyResult: strign[]
            Percentuale di 'Accuracy del training effettuato
        """

        # salvo la reteNeurale 
        model = self.reteNeurale.model
        model.save(self.reteNeurale.pathSave)

        testAccuracyResult = "{:.3%}".format(self.reteNeurale.test_accuracy.result())
        trainAccuracyResult = "{:.3%}".format(self.reteNeurale.train_accuracy_results[-1])
        # azzero i suoi valori di train loss e accuracy , cosi da poterli aggiornare
        # con un secondo train
        self.reteNeurale.train_loss_results = []
        self.reteNeurale.train_accuracy_results = []

        return (testAccuracyResult, trainAccuracyResult)

    def setModello(self, percorso):
        """ Caricamento di una Rete Neurale già configurata

        Parametri
        ---------
        percorso: string
            Percorso in cui si trova la Rete Neurale scelta"""
        modelToLoad = load_model(percorso)
        self.reteNeurale.model = modelToLoad

