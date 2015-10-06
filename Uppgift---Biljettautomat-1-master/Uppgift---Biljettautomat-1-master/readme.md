# Biljettautomat 1 #

Den här uppgiften går ut på att skriva en del av mjukvaran i en biljettautomat för pendeltåg.

## Bedömningsmatris ##

### Planering ###

| Förmågor                         | E 																																   | C | A |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|---|---|
| Aktivitetsdiagram och pseudokod  | Du använder pseudokod och/eller aktivitetsdiagram för att planera dina uppgifter utifrån exempel, eller i samråd med utbildaren.  | Som för E, men utan exempel eller handledning |   |

### Syntax och Teori ###
| Förmågor                                       | E 																			| C | A |
|------------------------------------------------|------------------------------------------------------------------------------|---|---|
| Grundläggande syntax		                     | Du kan redogöra för och använda programmeringsspråkets grundläggande syntax  |   |   |
| Villkor och IF-satser		                     | Du kan redogöra för och använda villkor och IF-satser                        |   |   |

### Kodning och kodningsstil ###

| Förmågor                                      | E                                                                         | C                                               | A                                              |
|-----------------------------------------------|---------------------------------------------------------------------------|-------------------------------------------------|------------------------------------------------|
| Komplexitet									| **Du kan skriva enkla program**                                               | Du kan skriva lite mer avancerade program       | Du kan skriva komplexa program
| Sekventiell- & funktionsbaserad programmering | Du använder dig av sekventiell programmering och fördefinerade funktioner | **Du skapar och använder enkla funktioner**         | Du skapar mer komplexa funktioner              |
| Struktur		 				                | Du skriver kod som är delvis strukturerad, har en konsekvent kodningsstil och tydlig namngivning | Som för E, men du skriver kod som är helt strukturerad |   			   |
| Felsökning                                    | Du felsöker på egen hand enkla syntaxfel | Som för E, men systematiskt, och dessutom även körtidsfel och programmeringslogiska fel | Som för C, men med effektivitet   	   |

## Uppgiftsbeskrivning ##

Du har blivit inhyrd för att skriva den del av mjukvaran i en biljettautomat som räknar ut vad biljetten kostar.

Priserna ser ut som följer

* Från och med 0 till och med 17 år: 10 kr
* Från och med 18 till och med 64 år: 20 kr
* Från och med 65 år: 15kr.

Du skall skriva två funktioner: `ask_age` och `ticket_price`

`ask_age` frågar användaren efter dess ålder och returnerar åldern som en integer

`ticket_price` tar en ålder som argument, och sen returnerar biljettens pris.

## Genomförande ##

### Versionshantering ###

Gör en `fork` av repot. Klona sen ner till din dator. Kom ihåg att checka in dina ändringar och synka med GitHub.

### Flödesschema ###

Innan du börjar koda ska du skapa ett flödesschema för programmet.
När du känner att du har ett fungerande flödesschema, be läraren att kolla på det.

### Kodning ###

Programmet skall utvecklas med hjälp av testerna.

##### Ruby #####

Kör `bundle install` för att installera alla dependencies (och `rbenv rehash` om rspec inte redan var installerat)

Skapa funktionerna i `lib/ticket.rb`

Testerna finns i `spec/ask_age_spec.rb` & `spec/price_spec.rb`.

Kör `rspec` för att köra testerna.

##### Python #####

Skapa funktionerna i `lib/ticket.py`

Testerna finns i `test/ask_age_test.py` & `test/price.py`

Kör `nosetests --rednose` för att köra testerna.

## Tips och länkar ##

* Om du inte kan beskriva lösningen i ord kommer det vara så gott som omöjligt att skapa ett flödesschema
* Fundera på vilka variabler som behövs
* Testa flödesschemat med hjälp av penna och papper

### Ruby ###

Läs mer om villkor och if-satser i övning 27-30 i [*Learn Ruby the Hard Way*](http://ruby.learncodethehardway.org/book)

* [Learn Ruby the Hard Way - Exercise 27: Memorizing Logic](http://ruby.learncodethehardway.org/book/ex27.html)
* [Learn Ruby the Hard Way - Exercise 28: Boolean Practice](http://ruby.learncodethehardway.org/book/ex28.html)
* [Learn Ruby the Hard Way - Exercise 29: What If](http://ruby.learncodethehardway.org/book/ex29.html)
* [Learn Ruby the Hard Way - Exercise 30: Else and If](http://ruby.learncodethehardway.org/book/ex30.html)

### Python ###

Läs mer om villkor och if-satser i övning 27-30 i [*Learn Python the Hard Way*](http://learnpythonthehardway.org)

* [Learn Python the Hard Way - Exercise 27: Memorizing Logic](http://learnpythonthehardway.org/book/ex27.html)
* [Learn Python the Hard Way - Exercise 28: Boolean Practice](http://learnpythonthehardway.org/book/ex28.html)
* [Learn Python the Hard Way - Exercise 29: What If](http://learnpythonthehardway.org/book/ex29.html)
* [Learn Python the Hard Way - Exercise 30: Else and If](http://learnpythonthehardway.org/book/ex30.html)