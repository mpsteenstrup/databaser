# Databaser og hjemmesider
Vi skal bruge vores viden om databaser til at strukturere indholdet i en hjemmeside. Vi skal bruge javaScript til at loade data og for at kunne bruge det. JavaScript er godt hvis man vil lave interaktive hjemmesider.

Her er en hjemmeside hvor informationen om de forskellige FN verdensmål er gemt som en kommasepareret fil, csv. [https://mpsteenstrup.github.io/databaser/javascript/FN_goals_loaddata.html](https://mpsteenstrup.github.io/databaser/javascript/FN_goals_loaddata.html)

### Øvelse
* Hvorfor er det en god ide at adskille indhold fra strukturen og layoutet i en hjemmeside?
* Beskriv hvad de tre formater, ```html, css, javaScript``` bruges til på en hjemmeside.

## Introduktion til javaScript
Vi bruger w3schools javaScript tutorial til at komme i gang.

### Eksempel
Første eksempel er en knap som kan vise tid og dato, [https://mpsteenstrup.github.io/databaser/javascript/ex1.html](https://mpsteenstrup.github.io/databaser/javascript/ex1.html).

Koden ser sådan ud

```
<!DOCTYPE html>
<html>
<body>

<h2>Ex 1</h2>

<button type="button" onclick="getDate()"> Tid og dato</button>
<p id="demo"></p>

</body>
</html> 

<script>
    function getDate(){
        document.getElementById('demo').innerHTML = Date();
    }
    </script>
```
De første 3 linjer er html setup og så en overskrift Ex 1. Det ny er at vi laver en knap
```
<button type="button" onclick="getDate()"> Tid og dato</button>
```
typen er sat med ```type="button"``` og den kalder funktionen ```getDate()``` ved kommandoen ```onclick="getDate()"````.

JavaScript delen er i ```script``` tags og kan placeres nederst på siden. Funktionen bliver defineret med ```function detDate() { } ``` og har kun én linje kode.

```document.getElementById('demo').innerHTML = Date();````
finder det element på siden med ``ìd="dem0"```og sætter det lig ```Date()```som er en indbygget funktion i javaScript til at give tid og dato.

### Øvels
* Kopier koden ind i et Bracket dokument og kør den. Det er også muligt at bruge w3schools online editor,[https://www.w3schools.com/tryit/tryit.asp?filename=tryhtml_hello](https://www.w3schools.com/tryit/tryit.asp?filename=tryhtml_hello).
* Prøv at lav om i koden så den i stedet fortæller en joke når man trykker på knappen, husk at tekst skal i gåseøjne " ".

## Data og hjemmesiden
Vi skal nu bruge vores nyvundne JS skills til at loade data. Data skal være gemt som csv fil og have overskrift på alle kolonner.

### eksempel 2, load biler databasen
Vil loade databasen ```biler.csv```som indeholder
```
bilID,type,mærke
1,Octavia,Skoda
2,Fabia,Skoda
3,Ceed,Kia
```
Hjemmesiden kan ses her [https://mpsteenstrup.github.io/databaser/javascript/ex2.html](https://mpsteenstrup.github.io/databaser/javascript/ex2.html). Hvis man bruger Google Chrome kan man se javaScript konsollen ved at gå ind under ```Vis->Udvikler->JavaScript-konsol```. So I kan ligger data i et lidt sjovt format kaldet en ```dictionary```
```
0:{bilID: '1', type: 'Octavia', mærke: 'Skoda'}
1:{bilID: '2', type: 'Fabia', mærke: 'Skoda'}
2: {bilID: '3', type: 'Ceed', mærke: 'Kia'}
```
For at få fat i informationen om mærket i første linje skal man skrive ```data[0]["mærke"]```. Som før indsætter vi informationen i dokumentet med koden ```document.getElementById('biler').innerHTML = data[0]["mærke"] + " "+ data[0]["type"];```

For at kunne holde styr på data bruger vi biblioteket Papa som kan loades med denne kommando
```<script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.3.0/papaparse.min.js"></script>````

Data bliver loadet i denne del af koden når hjemmesiden loades,
```
window.onload = function() {
var xhr = new XMLHttpRequest();
xhr.open("GET", "biler.csv", true);
xhr.responseType = "text";
xhr.onload = function() {
  data = Papa.parse(xhr.responseText, { header: true }).data;
};
xhr.send();
}
```
Det er ok at tage denne del som lidt at en black-box, men den sender en html-reguest om at åbne filen "bilse.csv" og gemmer det i variablen ```data```.

### Øvelse
* Hent de to filer, ex2.html og biler.csv, og prøv at kør programmet i Brackets. Det er ikke muligt bare at klikke på html filen på grund af sikkerhedsbekymringer.
* Lav om i filen så noget andet bliver vist.

## FN og verdensmålene
Vi vender nu tilbage til Hjemmesiden med FNs verdensmål,[FN_goals_loaddata.html](https://mpsteenstrup.github.io/databaser/javascript/FN_goals_loaddata.html). Filen kan ses her, [FN_goals_loaddata.html koden](https://github.com/mpsteenstrup/databaser/blob/main/javascript/FN_goals_loaddata.html).

Koden indeholder fire javaScript funkitoner, ```ny(),valgte(),genererTekst``` og den som loader data. Ideen er at koden vælger en overskrift og en beskrivese der passer til de forskellige verdensmål.

### Øvelse
* Beskriv hvad der sker i linje 28,29,30 og 31 og hvordan det hænger sammen med selve html koden.

For at udvælge teksten bruges funktionen ```genererTekst(x)``` som tager det tilfældige heltal mellem 0 og 3 som argument. Her er koden
```
function genererTekst(x){
  for (var i = 0; i < data.length; i++) {
      if (data[i]["ID"] == x) {
        overskrift = data[i]['overskrift']; 
        beskrivelse = data[i]['beskrivelse']
        break; // exit efter loop
      }
    }
}
Anden linje ```for (var i = 0; i < data.length; i++)``` giver en løkke hvor ```i=0``` til at starte med, og i vokser med 1 ```ì++``` for hver omgang. Løkken kører så længe ```i < data.length``` altså så lange i er mindre end antallet af rækker i data.

betingelsen ```if (data[i]["ID"] == x)```bruger primærnøglern ```ÌD``` og spørger om den er lig med ```x```. Hvis den er det så skal overskrift og beskrivelse opdateres og løkken stoppes.

### Øvelse
* Beskriv hvorfor ```genererTekst(x)``` funktionen virker.
Databasen indeholder også en kolonne ```progression``` hvor det er angivet hvor langt vi som verden var kommet med verdensmålene.
* Lav om i koden så denne information også bliver vist på siden.









