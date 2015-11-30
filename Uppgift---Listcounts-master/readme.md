#ListCounts

Många programmeringspråk har funktioner för att summera, hitta största och minsta värdet i listor av tal.
Er uppgift här är att skriva egna funktioner som gör detta och några till som kanske saknas i ert programmeringsspråk.

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
| Loopar & iteration                             | Du kan redogöra för och använda loopar och iterera över listor               |   |   |

### Kodning och kodningsstil ###

| Förmågor                                      | E                                                                         | C                                               | A                                              |
|-----------------------------------------------|---------------------------------------------------------------------------|-------------------------------------------------|------------------------------------------------|
| Komplexitet									| **Du kan skriva enkla program**                                               | Du kan skriva lite mer avancerade program       | Du kan skriva komplexa program
| Sekventiell- & funktionsbaserad programmering | Du använder dig av sekventiell programmering och fördefinerade funktioner | **Du skapar och använder enkla funktioner**         | Du skapar mer komplexa funktioner              |
| Struktur		 				                | Du skriver kod som är delvis strukturerad, har en konsekvent kodningsstil och tydlig namngivning | Som för E, men du skriver kod som är helt strukturerad |   			   |
| Felsökning                                    | Du felsöker på egen hand enkla syntaxfel | Som för E, men systematiskt, och dessutom även körtidsfel och programmeringslogiska fel | Som för C, men med effektivitet   	   |

## Uppgiftsbeskrivning ##

Ni ska skriva funktionerna sum,min,max,average och median som tar in en lista av tal, *listOfNumbers* och returnerar ett tal.
Lägg funktioner i en fil listcounts.py respektive listcounts.rb

- sum returnerar summan av alla tal i listan
- min returnerar det minsta värdet i listan
- max returnerar det högsta värdet i listan
- average returnerar det medelvärdet av alla tal i listan
- median returnerar det mittersta värdet i listan, om det mittersta värdet ligger mellan två värden, medelvärdet av dessa två värden

om argumentet till listan är en tom lista [], returneras `nil` (ruby) eller `None` (python.)


### Exempel ###

#### Ruby ####

	sum(numbers: [])
	#=> nil
    
	sum(numbers: [2,3,4,5])
	#=> 14
	
	min(numbers: [2,3,4,5])
	#=> 2
	
	max(numbers: [2,3,4,5])
	#=> 5

	average(numbers: [1,2,3,4])
	#=> 2.5
	
	median(numbers: [1,2,3,4,5])
	#=> 3

#### Python ####
	
	sum(listOfNumbers=[])
	#=> None

	sum(listOfNumbers=[2,3,4,5])
	>>> 14
	
	min(listOfNumbers=[2,3,4,5])
	>>> 2
	
	max(listOfNumbers=[2,3,4,5])
	>>> 5

	average(listOfNumbers=[1,2,3,4])
	>>> 2.5
	
	median(listOfNumbers=[1,2,3,4,5])
	>>> 3


## Genomförande ##

### Versionshantering ###

Gör en `fork` av repot. Klona sen ner till din dator. Kom ihåg att checka in dina ändringar och synka med GitHub.

### Flödesschema ###

Innan du börjar koda ska du skapa ett flödesschema för programmet.
När du känner att du har ett fungerande flödesschema, be läraren att kolla på det.

### Kodning ###

Programmet skall utvecklas med hjälp av testerna.

##### Ruby #####

Kör `bundle install` för att installera alla dependencies om du inte redan har allt installerat.

Skapa funktionerna i `lib/listcounts.rb`

Testerna finns i `spec/<funktion>_spec.rb`

Kör `ruby spec/funktionens_namn_test.rb` för att köra testerna.

##### Python #####

Skapa funktionerna i `lib/listcounts.py`

Testerna finns i `test/test_<funktion>.py`

Kör `nosetests --rednose` för att köra testerna.
Kör `nosetests --rednose` test/<testnamn> för att köra enskilda tester. 

## Tips och länkar ##

* Om du inte kan beskriva lösningen i ord kommer det vara så gott som omöjligt att skapa ett flödesschema
* Fundera på vilka variabler som behövs
* Testa flödesschemat med hjälp av penna och papper

### Ruby ###

Läs mer om listor och loopar och i övning 32 & 34 i [*Learn Ruby the Hard Way*](http://ruby.learncodethehardway.org/book)

* [Learn Ruby the Hard Way - Exercise 32: Loops and Arrays](http://learnrubythehardway.org/book/ex32.html)
* [Learn Ruby the Hard Way - Exercise 34: Accessing Elements of Arrays](http://learnrubythehardway.org/book/ex34.html)

### Python ###

Läs mer om listor och loopar i övning 32 & 34 i [*Learn Python the Hard Way*](http://learnpythonthehardway.org)

* [Learn Python the Hard Way - Exercise 32: Loops and Lists](http://learnpythonthehardway.org/book/ex32.html)
* [Learn Python the Hard Way - Exercise 34: Accessing Elements of Lists](http://learnpythonthehardway.org/book/ex34.html)