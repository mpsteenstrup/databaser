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

## SQL kommandoer
Hvis man arbejder med rigtigt store databaser er det ikke praktisk at bruge regnearksrepresentationen til at hente data ud. Den mest udbredte sprog til at arbejde med databaser er SQL, Structured Query Language. Vi bruger SQL fanen i BD Browser,
![SQL](filer/SQL.ong)

### Øvelse
* Prøv de nedenstående kommandoer
```
SELECT * FROM albums
SELECT count(*) FROM albums
SELECT * FROM albums WHERE ArtistId = 2   
```
* Lav om i sidste linje for at finde ud af hvilken kunstner der har ArtistId=2

INNER JOIN er en måde at sætte tabeller sammen.
### Øvelse
* Kør koden og forklar hvad der sker ved INNER JOIN
```
SELECT artists.Name, albums.Title
from artists
INNER JOIN albums ON artists.ArtistId =albums.ArtistId
```
Her er et [cheat sheet](https://res.cloudinary.com/dyd911kmh/image/upload/v1675360372/Marketing/Blog/SQL_Basics_For_Data_Science.pdf).


Pas på med hvad I beder om!
![DROP TABLE](https://imgs.xkcd.com/comics/exploits_of_a_mom.png)

### Øvelse
* Undersøg andre dele af music databasen.


## Egen relationel database
Vi vil lave tabellerne med biler om til en database.

### Øvelse
* Vælg Ny database, giv tabellen et navn, add de forskellige søjler og vælg primærnøgle.
Den generere selv SQL koden,
```
CREATE TABLE "kunder" (
	"kunde_id"	INTEGER,
	"navn"	TEXT,
	"email"	TEXT,
	"tlf"	INTEGER,
	PRIMARY KEY("kunde_id")
);
```
* Brug koden til at lav en tabel for bilmærker
* Brug nedenstående kode til at udfylde tabellen
```
INSERT INTO kunder VALUES (1,"Hans","hans@gmail.com","54783219")
```
* Join de to tabellers så I kan finde ud af hvilke bilen der hører til hvilke personer.

## E/R diagram
Endnu en fin video, nu om E/R diagrammer, [E/R diagrammer](https://youtu.be/wIR-SXl86KY).

### Øvelse
* se filemn.
* Brug [draw.io](https://app.diagrams.net/) til at lave et E/R diagram over kunde/bil databasen.

### Øvelse - egen database.
I skal lave jeres egen database. I må selv vælge hvad databasen skal indeholde men her er et par forslag,
* Spillere, resultater og turneringer i den lokale skakklub.
* Toppings og isvarianter i den lokale isbar.
* Kunder og varer i en online shop.
* Deltagere på musik-festeivaller til sommer.

Som altid er det smart at starte simpelt så,
* Beskriv kort hvad indeholdet af en simpel version af jeres database er.
* Skitser den som én tabel i regneark.
* Normaliser databasen, stadigt i regneark.
* Lav et E/R diagram og vurder graden af relationerne.
* Hvis I har en mange til mange relation så lav den simplere.
* Implementer databasen I DB browser.
