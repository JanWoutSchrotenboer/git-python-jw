from datetime import datetime, date

# De functie geldige_datum() controleert of een datum is vastgelegd in het formaat 'dd-mm-jjjj'. Invoer is een string
# met de datum, uitvoer is True als de datum geldig is, anders False.
def geldige_datum(str_datum):
    geldig = True
    try:
        datum_object = datetime.strptime(str_datum, '%d-%m-%Y')
    except ValueError:
        geldig = False
    return geldig

# De functie bereken_leeftijd_vandaag() berekent de leeftijd in jaren op de huidige datum. Invoer is de 
# geboortedatum in formaat 'dd-mm-jjjj'. Uitvoer is de leeftijd in hele jaren. Let op, deze functie
# controleert niet of de datum correct is ingevoerd, hiervoor kan de functie geldige_datum() worden gebruikt.
def bereken_leeftijd_vandaag(str_geboortedatum):
    vandaag = date.today()
    geboortedatum = datetime.strptime(str_geboortedatum, '%d-%m-%Y') 
    nogNietJarigInHuidigJaar = (vandaag.month, vandaag.day) < (geboortedatum.month, geboortedatum.day)

    if nogNietJarigInHuidigJaar:
        leeftijd = vandaag.year - geboortedatum.year - 1
    else:
        leeftijd = vandaag.year - geboortedatum.year

    return leeftijd

# De functie bereken_leeftijd_op_peildatum() berekent de leeftijd in jaren op een peildatum. Invoer de 
# geboortedatum en de peildatum in formaat 'dd-mm-jjjj'. Uitvoer is de leeftijd in hele jaren. Let op, deze functie
# controleert niet of de data correct zijn ingevoerd, hiervoor kan de functie geldige_datum() worden gebruikt.
def bereken_leeftijd_op_peildatum(str_geboortedatum, str_peildatum):
    geboortedatum = datetime.strptime(str_geboortedatum, '%d-%m-%Y') 
    peildatum = datetime.strptime(str_peildatum, '%d-%m-%Y') 
    nogNietJarigOpPeildatum = (peildatum.month, peildatum.day) < (geboortedatum.month, geboortedatum.day)

    if nogNietJarigOpPeildatum:
        leeftijd = peildatum.year - geboortedatum.year - 1
    else:
        leeftijd = peildatum.year - geboortedatum.year

    return leeftijd


# De functie bereken_resterende_maanden() berekent het aantal maanden in het jaar, met ingang van de maand volgend op de maand in de meegegeven datum 
# in formaat 'dd-mm-jjjj'. Uitvoer is het aantal maanden dat nog resteert in het jaar met ingang van de eerstvolgende maand
# controleert niet of de datum correct is ingevoerd, hiervoor kan de functie geldige_datum() worden gebruikt.
def bereken_resterende_maanden(str_datum):
    datum = datetime.strptime(str_datum, '%d-%m-%Y') 
    resterende_maanden = 12 - int(datum.month)
    
    return resterende_maanden

# De functie bepaal_jaar_in_datum() bepaalt het jaar in de ontvangen datum in formaat 'dd-mm-jjjj'. 
# Uitvoer is het jaar als integer.
# controleert niet of de datum correct is ingevoerd, hiervoor kan de functie geldige_datum() worden gebruikt.
def bepaal_jaar_in_datum(str_datum):
    datum = datetime.strptime(str_datum, '%d-%m-%Y') 
    jaar = int(datum.year)
    
    return jaar
