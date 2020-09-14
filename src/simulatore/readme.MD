Directory simulatore

## Cartella dedicata al simulatore

In questa cartella è elencata la procedura per la corretta simulazione del RaspBerry Pi one su Windows con le seguenti caratteristiche:
```
CPU	700 MHz single-core ARM1176JZF-S

GPU	Broadcom VideoCore IV,[18] OpenGL ES 2.0, 1080p30 H.264 high-profile decoder ed encoder[2] 250 MHz per BCM2835 e BCM2836. 400 MHz dual core per BCM2837 (1080p60)

Memoria (SDRAM)	256 MB (condivisa con la GPU)
```


1) download di QEMU al seguente link https://www.qemu.org/download/  
2) download del kernel linux al seguente link https://github.com/dhruvvyas90/qemu-rpi-kernel  
3) download iso Raspbian os https://www.raspberrypi.org/downloads/raspberry-pi-os/
4) estrarre i file e posizionare il kernel nella stessa cartella contenente l'immagine .iso.  
5) tramite editor di testo creare file.bat (es. start.bat)  inserire le seguenti linee (settare opportunamente la versione secondo i download effettuati , vedi kernel e versione SO).
```
"c:\Program Files\qemu\qemu-system-arm.exe" ^
-kernel kernel-qemu-4.4.34-jessie ^
-cpu arm1176 ^
-m 256 ^
-M versatilepb ^
-serial stdio ^
-append "root=/dev/sda2 rootfstype=ext4 rw" ^
-hda 2019-06-20-raspbian-buster.img ^
-net nic ^
-net user,hostfwd=tcp::5022-:22 ^
-no-reboot

```
6) aprire prompat dei comandi nella cartella contenente kernel e iso
7) avviare la simulazione (es start.bat)

di default la memeoria di dispotivo risulta limitata a 256 MB (insufficiente per l'installazione di tensorflow) per estenderla occorre effettuare in seconda battuta il resize. Per un corretto funzionamento eseguire i seguenti comandi: 
 
 - aprire un terminale nella cartella contenente il file .is 
 - digitare qemu-img.exe resize 2020-06-02-raspbian-buzer.img +4G
 (inserire l'opportuna versione scaricata e la dimensione di memoria desiderata per l'estensione)
 - una corretta esecuzione presenterà un warning relativo al resize 

 al seguente link https://drive.google.com/file/d/15ID7Q6RVmdS56RjzudnA0IUNc-4wqGCh/view?usp=sharing è disponibile una file .zip contenente un simulatore correttamente inizializzato e con installato tensorflow (versione 2020-02-13-raspbian-buster.img , kernel-qemu-4.4.34-jessie, 8G)
