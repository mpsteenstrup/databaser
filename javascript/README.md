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


