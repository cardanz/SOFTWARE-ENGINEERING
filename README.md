# FMECA - On the Edge
## Installazione software 
Per la corretta installazione delle software occorre:

1) Installare python ( versioni utilizzate 3.7.0 - 3.7.7) 
    https://www.python.org/downloads/ 

2) ``` pip install --upgrade pip  ```
(I programmi di installazione di Python per Windows includono pip)
nel caso si utilizzi linux o macOS si può utilizzare la versione pip fornita dalla distribuzione Linux, eventualmente consulta il seguente link
https://packaging.python.org/guides/installing-using-linux-tools/

3) ```pip install --user virtualenv``` 
Installare virtualenv ,(nel caso On macOS and Linux:
python3 -m pip install --user virtualenv) 

4) Creare un virtual environment (denominato 'env'):
    - ```python -m venv env```

    Attivare il virtual env appena creato:
    - ```.\env\Scripts\activate``` ( linux :source env/bin/activate )

    Installare tutte le librerie richieste (presenti nel file):

    - ```pip install -r requirements.txt ``` disponibile nella repository contenente tutte le dipendenze necessarie)

    Nota: ```requirements.txt``` deve essere "allo stesso livello" dell'environment come indicato sotto.

    ``` 
    +---path/...
        +---env
        |   requirements.txt
    ```   
    Per confermare di essere nell'ambiente virtuale si può verificare la posizione dell'interprete Python (dovrebbe puntare alla directory env).
    ```Windows:```
    ```where python```
    ```
    .../env/bin/python.exe
    ``` 

    ```macOS and Linux: ```
    ```which python```
    ```
    .../env/bin/python
    ```

5) ```python configurazione.py ``` per eseguire il software.


## Testing software

Per il corretto testing del software occorre:

1) eseguire il comando     ```pytest -v``` in   
```
...\se20-project-22 
``` 
(nell'environment precedentemente realizzato, dove sono già installate le librerie di testing), è possibile visualizzare il coverage complessivo, ottenuto in fase di testing durante la progettazione, nella cartella ``` htmlcov ``` , file ```index.html```




(Nota: la procedura è stata correttamente testata su Windows 10 Home, i comandi linux/macOS riportarti dovrebbero garantire comunque una corretta installazione).

## Struttura Directory del progetto:
```
+---docs
|   |   README.md
|   |   
|   +---drs
|   |   |   DRS -document.docx
|   |   |   README.md
|   |   |   
|   |   +---images
|   |   |       AD_configurazione.jpeg
|   |   |       AD_configurazione.png
|   |   |       AD_simulazione.jpeg
|   |   |       AD_simulazione.png
|   |   |       CD.png
|   |   |       configurazione_Ui.png
|   |   |       dati.PNG
|   |   |       diagramma_generale.jpeg
|   |   |       h1.PNG
|   |   |       h2.PNG
|   |   |       h3.PNG
|   |   |       risulati_Ui.jpeg
|   |   |       SD_simulazione.jpg
|   |   |       SD_simulazione.png
|   |   |       simulazione_Ui.jpg
|   |   |       uses_cases.jpeg
|   |   |       visualizzazione_Ui.png
|   |   |       
|   |   +---ui-files
|   |   |       configurazione.ui
|   |   |       previsione.ui
|   |   |       visualizzazione.ui
|   |   |       
|   |   \---uml-diagrams
|   |           AD_configurazione.dia
|   |           AD_simulazione.dia
|   |           CD.dia
|   |           CD.dia~
|   |           diagramma_generale.dia
|   |           SD_simulazione.dia
|   |           uses_cases.dia
|   |           
|   \---urs
|       |   README.md
|       |   URS - document.docx
|       |   
|       \---images
|               struttura.PNG
|               
|       
+---src
|   |   configurazione.py
|   |   configurazione_ui.py
|   |   NN.py
|   |   NNcreator.py
|   |   previsione.py
|   |   previsione_ui.py
|   |   README.md
|   |   test_connect.py
|   |   visualizzazione.py
|   |   visualizzazione_ui.py
|   |   
|   +---dataset
|   |   |   signal.csv
|   |   |   signal_test.csv
|   |   |   signal_training.csv
|   |   |   
|   |   \---previsione
|   |           signal_prediction.csv
|   |           
|   +---doc
|   |       configurazione.html
|   |       NN.html
|   |       NNcreator.html
|   |       previsione.html
|   |       visualizzazione.html
|   |       
|   +---img
|   |   |   
|   |   +---icon
|   |   |       configurazione.ico
|   |   |       prediction.ico
|   |   |       testing.ico
|   |   |       
|   |   \---test
|   |           testimg.ico
|   |           
|   +---modelliSalvati
|   |       stefano.csv
|   |       test_dati_corretti2.csv
|   |   
|   |               
|   +---simulatore
|   |       readme.MD
|   |       
|   +---tools
|   |       dataset.csv
|   |       dataSet.xlsx
|   |       DatasetCodice.m
|   |       DataSetGenerator.py
|   |       
|   +---ui
|           configurazione.ui
|           previsione.ui
|           visualizzazione.ui
|          
|           
+---test
        README.md.txt
        test_configurazione.py
        test_uiConfigurazione.py
        test_uiVisualizzazione.py
      

```
