# versie 5, meer generiek gemaakt en foutcontroles toegevoegd
# Iedereen die op 1 januari 2020 ten minste 6 jaar oud is mag lid worden van onze vereniging.Junioren, dat zijn leden die op 1 januari 2020 jonger zijn dan 18 jaar betalen
# in 2020 een contributie van € 100.
# Senioren, op 1 januari 2020 18 jaar of ouder, betalen in 2020 € 175. Leden die in 2020 lid worden betalen eenmalig € 25 administratiekosten, ongeacht op welk moment van het jaar
# het lidmaatschap ingaat. Als het lidmaatschap gedurende het jaar ingaat dan wordt de contributie evenredig berekend over het resterende aantal maanden in 2020 met ingang van
# de maand volgend op de maand waarop iemand zich aanmeldt als lid.

# Zoek eerst uit wat je van een lid minimaal moet weten om de contributie te berekenen.

# leeftijd
# jaar van aanmelding
# maand van aanmelding

# pseudocode

# ALS leeftijd < 6 DAN
#     geef melding dat je pas lid kunt worden vanaf 6 jaar
# ANDERS
#     ALS leeftijd < 18 DAN
#         jaarcontributie = € 100
#     ANDERS
#         jaarcontributie = € 175


# ALS jaar_van_aanmelding =  2020 DAN
#     administratiekosten =  € 25
#     resterende_maanden = 12 - maand_van_aanmelding
#     jaarcontributie = (jaarcontributie / 12) * resterende_maanden
# ANDERS
#     administratiekosten = € 0

from datumfuncties import *
import csv


def main():

    # hier wordt het bestand 'contributiegegevens.csv' geopend. 
    with open('contributiegegevens.csv', newline='') as csvfile:
        contributiegegevens = csv.DictReader(csvfile, delimiter=',')

        for contributie_record in contributiegegevens:
            peildatum = "01-01-" + contributie_record['contributiejaar']
            # Voor de zekerheid worden getallen waarmee eventueel nog gerekend moet worden (in dit geval hele getallen) omgezet naar integers (hele getallen) met de functie int()
            huidig_contributiejaar = int(contributie_record['contributiejaar'])
            contributie_junior = int(contributie_record['contributie_junior'])
            contributie_senior = int(contributie_record['contributie_senior'])
            senior = int(contributie_record['senior'])
            minimumleeftijd = int(contributie_record['minimumleeftijd'])
            administratiekosten_nieuw_lid = int(contributie_record['administratiekosten'])

    # hier wordt het bestand 'ledenbestand.csv' geopend.
    with open('ledenbestand.csv', newline='') as csvfile:
        ledenbestand = csv.DictReader(csvfile, delimiter=',')
        print('\n\n')

        for lid in ledenbestand: # alle leden worden een voor een behandeld

            naam = lid['naam']
            geboortedatum = lid['geboortedatum']
            aanmeldingsdatum = lid['aanmeldingsdatum']

            # controleer of de geboortedatum een geldige datum is, anders een melding tonen en met 'continue' de rest van de regels overslaan en direct doorgaan naar het volgende lid
            if not geldige_datum(geboortedatum):
                print(f'Bij {naam} staat een ongeldige geboortedatum ({geboortedatum}) in het bestand, de contributie wordt niet berekend.\n')
                continue

            # controleer of de aanmeldingsdatum een geldige datum is, anders een melding tonen en met 'continue' de rest van de regels overslaan en direct doorgaan naar het volgende lid
            if not geldige_datum(aanmeldingsdatum):
                print(f'Bij {naam} staat een ongeldige datum van aanmelding ({aanmeldingsdatum}) in het bestand, de contributie wordt niet berekend.\n')
                continue
            

            leeftijd = bereken_leeftijd_op_peildatum(geboortedatum, peildatum)
            jaar_van_aanmelding = bepaal_jaar_in_datum(aanmeldingsdatum)

            if jaar_van_aanmelding > huidig_contributiejaar:
                print(f"Bij {naam} staat een datum van aanmelding na {huidig_contributiejaar} in het bestand, de contributie over {huidig_contributiejaar} wordt niet berekend.")
                continue

            if leeftijd < senior:
                jaarcontributie = contributie_junior
            else:
                jaarcontributie = contributie_senior

            if jaar_van_aanmelding == huidig_contributiejaar:
                nieuw_lid = True
                administratiekosten = administratiekosten_nieuw_lid
                resterende_maanden = bereken_resterende_maanden(aanmeldingsdatum)
                if resterende_maanden == 1:
                    tekst_maanden = 'maand'
                else:
                    tekst_maanden = 'maanden'
                maandcontributie = round((jaarcontributie / 12), 2) # afronden op twee decimalen om het mooi als bedrag in Euro te kunnen printen
                jaarcontributie = maandcontributie * resterende_maanden
            else:
                nieuw_lid = False
                administratiekosten = 0

            totaalbedrag = jaarcontributie + administratiekosten

            if leeftijd < 6:
                print(
                    f"{naam}, geboortedatum {geboortedatum}, was op {peildatum} {leeftijd} jaar oud maar moet minstens {minimumleeftijd} jaar oud zijn om lid te kunnen worden van onze vereniging.\n")
            elif nieuw_lid:
                print(
                    f"{naam}, geboortedatum {geboortedatum}, was op {peildatum} {leeftijd} jaar oud, heeft zich aangemeld op {aanmeldingsdatum} en betaalt in {huidig_contributiejaar} € {totaalbedrag}")
                print(
                    f"(contributie {resterende_maanden} {tekst_maanden} * € {maandcontributie} = € {jaarcontributie}  + € {administratiekosten} administratiekosten).\n")
            else:
                print(
                    f"{naam}, geboortedatum {geboortedatum}, was op {peildatum} {leeftijd} jaar oud en betaalt in {huidig_contributiejaar} € {jaarcontributie} contributie.\n")

        print('\n\n')


if __name__ == '__main__':
    main()