# Funktioner i Ruby/Python

Den här uppgiften går ut på att skriva några olika matematiska funktioner

## Bedömningsmatris ##

## Planering ##

| Förmågor                         | E 																																   | C | A |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|---|---|
| Aktivitetsdiagram och pseudokod  | Du använder pseudokod och/eller aktivitetsdiagram för att planera dina uppgifter utifrån exempel, eller i samråd med utbildaren.  | Som för E, men utan exempel eller handledning |   |
| Utvärdering | Du utvärderar, med viss säkerhet, med enkla omdömen, programmets prestanda, använder datalogiska begrepp, och bedömer din egen förmåga | som för E, men med nyanserade omdömen | Som för C, men med säkerhet, och med förbättringsförslag

## Syntax och Teori ##
| Förmågor                                       | E 																			| C | A |
|------------------------------------------------|------------------------------------------------------------------------------|---|---|
| Datatyper					                     | Du kan redogöra för och använda de vanligaste datatyperna                    |   |   |
| Grundläggande syntax		                     | Du kan redogöra för och använda programmeringsspråkets grundläggande syntax  |   |   |

## Kodning och kodningsstil ##

| Förmågor                                      | E                                                                         | C                                               | A                                              |
|-----------------------------------------------|---------------------------------------------------------------------------|-------------------------------------------------|------------------------------------------------|
| Komplexitet									| **Du kan skriva enkla program**                                               | Du kan skriva lite mer avancerade program       | Du kan skriva komplexa program
| Sekventiell- & funktionsbaserad programmering | Du använder dig av sekventiell programmering och fördefinerade funktioner | **Du skapar och använder enkla funktioner**         | Du skapar mer komplexa funktioner              |
| Struktur		 				                | Du skriver kod som är delvis strukturerad, har en konsekvent kodningsstil och tydlig namngivning | Som för E, men du skriver kod som är helt strukturerad |   			   |
| Felsökning                                    | Du felsöker på egen hand enkla syntaxfel | Som för E, men systematiskt, och dessutom även körtidsfel och programmeringslogiska fel | Som för C, men med effektivitet   	   |
| Undantagshantering                            |     																		| Du validerar användardata						  | Som för C, men du skriver även kod som använder undantagshantering |
| Dokumentering 								| Du skriver kod som är delvis dokumenterad									|  												  | Du skriver kod som är utförligt dokumenterad   |

## Uppgiftsbeskrivning ##

Du ska skriva några olika matematiska funktioner: `halve`, `add`, `subtract`, `multiply`, `square` och `square_of_square_root`

* `halve` tar ett tal som argument, och returnerar det halverade talet
* `add` tar två termer som argument, adderar de två talen, och returnerar summan
* `subtract` tar två termer som argument, och returnerar differensen
* `multiply` tar två faktorer som argument och returnerar produkten
* `square` tar ett tal som argument, och returnerar kvadraten av talet
* `square_of_square_root` tar ett tal som argument och returnerar kvadraten av kvadratroten av talet

### Exempel ###
	
	halve(value: 4) #=> 2
	halve(value: 9) #=> 4.5

	add(term1: 3, term2: :2) #=> 5
	add(term1: 3, term2: -6) #=> -3

	subtract(term1: 9, term2: 3) #=> 6
	subtract(term1: 3, term2: 5) #=> -2

	multiply(factor1: 3, factor2: 5) #=> 15
	multiply(factor1: 3, factor2: -2) #=> -6

	square(value: 4) #=> 16
	square(value: 16) #=> 256

	square_of_square_root(value: 4) #=> 4
	square_of_square_root(value: 256) #=> 256


## Genomförande ##

### Versionshantering ###

Gör en `fork` av repot. Klona sen ner till din dator. Kom ihåg att checka in dina ändringar och synka med GitHub.

### Flödesschema ###

Skapa en funktion åt gången.
Innan du börjar koda ska du skapa ett flödesschema för funktionen.
När du känner att du har ett fungerande flödesschema, be läraren att kolla på det.

### Kodning ###

Programmet skall utvecklas med hjälp av testerna.

##### Ruby #####

Kör `bundle install` för att installera alla dependencies.

Skapa funktionerna i `lib/maths_helpers.rb.rb`

Testerna finns i `spec/funktionens_namn_spec.rb`

Kör `ruby spec/funktionens_namn_spec` för att köra testerna för den specifika funktionen.

## Tips och länkar ##

* Om du inte kan beskriva lösningen i ord kommer det vara så gott som omöjligt att skapa ett flödesschema
* Fundera på vilka variabler som behövs
* Testa flödesschemat med hjälp av penna och papper

