# Directory src

## Cartella dedicata allo sviluppo ("Progettazione")

In questa cartella è disponibile il codice implementato e varie cartelle per la gestione del funzionamento 
tra cui la cartella dei modelli salvati, la cartella contenente alcuni dataset di test, 
le immagini salvate durante l'esecuzione, la documentazione relativa a tutto il codice in formato
standard, cartella 'tools' per la generazione del dataset simile al caso d'uso e inoltre è disponibile la procedura per l'installazione
corretta del simulatore per raspberry nella cartella 'simulatore'.

La struttura della directory risulta:
```
C:.
|   configurazione.py
|   configurazione_ui.py
|   NN.py
|   NNcreator.py
|   previsione.py
|   previsione_ui.py
|   README.md
|   test_connect.py
|   test_NNcreator.py
|   visualizzazione.py
|   visualizzazione_ui.py
|
+---dataset
|   |   sensori.csv
|   |   signal_test.csv
|   |   signal_training.csv
|   |
|   \---previsione
|           sensori_prediction.csv
|
+---doc
|       configurazione.html
|       configurazione.pdf
|       NN.html
|       NN.pdf
|       NNcreator.html
|       NNcreator.pdf
|       previsione.html
|       previsione.pdf
|       visualizzazione.html
|       visualizzazione.pdf
|
+---img
|   |   provaMatteSat_Jul_25_11_48_20_2020.png
|   |
|   \---icon
|           configurazione.ico
|           prediction.ico
|           testing.ico
|
+---modelliSalvati
|   \---provaMatte
|       |   provaMatte.csv
|       |
|       \---provaMatte
|           |   saved_model.pb
|           |
|           +---assets
|           \---variables
|                   variables.data-00000-of-00001
|                   variables.index
|
+---simulatore
|       readme.MD
|
+---tools
|       dataset.csv
|       dataSet.xlsx
|       DatasetCodice.m
|       DataSetGenerator.py
|
+---ui
        configurazione.ui
        previsione.ui
        visualizzazione.ui

```