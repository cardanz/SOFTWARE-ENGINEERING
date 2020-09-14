import numpy as np
import os
import math

# TODO: mettere tutti i commenti e spiegazione del file ! come i javadoc ma in python

# funzione per la creazione del dataset 
vDisponibile = [0.135, 0.155, 0.11, 0.0025, 0.12, 0.002, 0.01, 0.79, 0.18, 0.16]

# gaussiana centrata sul valor medio 
mu = 0.1664 

# varianza
R = [0.067, 0.044, 0.032, 0.06, 0.067, 0.024, 0.011, 0.056,0.054, 0.043]

dataSet = np.zeros((2,10000))
count = 0

for i in range(0,999):
    var = R[int(i/100)]
    csi = np.random.normal(mu,math.sqrt(var),10)
    for j in range(0,10):
        if(csi[j] < 0):
            dataSet[0,i*10 + j] = - csi[j]
        else:
            dataSet[0,i*10 + j] = csi[j]

        if(csi[j] > 0.2):
            randomN = np.random.randint(0,2)
            dataSet[1,i + j] = int(randomN)
dataSet = dataSet.transpose()

my_dir = os.path.dirname(os.path.abspath('DataSetGenerator.py'))
file_name = 'dataset.csv'
fname = os.path.join(my_dir, file_name)

np.savetxt(fname, dataSet, delimiter=",", fmt='%1.3f')
