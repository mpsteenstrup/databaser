# Databaser


## Tre-lags-arkitektur, (kilde [iftek](http://iftek.dk/leksikon:tre-lags-arkitektur))
I en trelagsarkitur indeles et program i tre lag, hvilket er er nyttigt i implementeringen af programmer, da de tre lag så vidt mulig holdes adskilte og dermed er hele programmet lettere at overskue.

**Præsentationslag:** Det øverste lag der håndterer modtagelse og præsentation af data. Dette lag er kendetegnet ved at være ”tæt” på brugeren af programmet.

**Logiklag:** Det midterste lag der håndterer udvekslingen af data mellem præsentationslaget og datalaget.

**Datalag:** Det nederste lag der opbevarer og håndterer data. Dette lag er også kendetegnet ved at være ”tæt” på computeren.

Vi vil arbejde med hvordan man organiserer data i databaser.

## Introduktion til databaser - Vestfynedu style.
I bruger den glimrende introduktion til databaser [LINK](https://sites.google.com/vestfynedu.dk/informatikdbg/konstruktion-af-it-systemer/databaser?authuser=0).

### Øvelse
* Læs introduktionen og se videoen Introduktion til databaser. 
* Forklar hvad Entiteter, Attributter, primærnøgle og sekundærnøgle er. 

### Øvelse
* Se videoen om normalisering af databaser, start 4 minutter inde [Video](https://youtu.be/22bRAGYB6Is?t=238).
* Normaliser nedenstående database.
![ikke_normaliseret](filer/ikke_normaliseret.png)

## DB Browser
Vi skal arbejde med et databaseprogram. Det vi bruger er DB Browser SQlite.
* Download programmet, [DB Browser SQlite](https://sqlitebrowser.org/dl/).
* Download databasen music, [music.db](filer/music.db).
* Åben music databasen og prøv de forskellige faner.
* Identificer de forskellige Entiteter, Attributter og nøgler. 
* Er databasen normaliseret?


