import sqlite3
from tabulate import tabulate 

con = sqlite3.connect("innlevering.db")
cursor = con.cursor()

def se_kundeordre():
    mobilnummer = input("Skriv inn mobilnummeret ditt for å se ordrene dine: ")
    cursor.execute('''SELECT Ordrenummer, "Kundenummer", "Navn", "Epost", "Mobilnummer", "Dag", "Tid" 
    FROM Kunderegister
    INNER JOIN Kundeordre USING(Kundenummer)
    WHERE Dag >= 20230330
    AND Mobilnummer = ?''', (mobilnummer,))

    col_names = ["Ordrenummer", "Kundenummer", "Navn", "E-post", "Mobilnummer", "Ordredato", "Ordretid"]
    kundeordre = []
    data = cursor.fetchall()
    if len(data) != 0:
        for d in data:
            kundeordre.append(d)
        print(tabulate(kundeordre, headers=col_names, tablefmt="grid"))
        print('')
       
        ordrenummer = input("Skriv inn ordrenummeret på bestillingen du ønskker å se: ")
        return ordrenummer
    print('')
    print("Ingen kundeordre registrert på dette mobilnummeret. Vennligst prøv et annet.")
    print('')
 
 
def se_setereiser(ordrenummer):   
    
    cursor.execute('''SELECT Ordrenummer, Dag AS Ordredato, Kundeordre.Tid AS Ordretid,
    SeteNummer, vognNummer, Dato, seteBillett.TogruteID, start.JernbanestasjonNavn, start.Tid, slutt.JernbanestasjonNavn, slutt.Tid
    FROM Kunderegister 
    INNER JOIN Kundeordre USING(Kundenummer)
    INNER JOIN seteBillett USING(Ordrenummer)
    INNER JOIN togruteStasjon start ON (seteBillett.TogruteID = start.TogruteID AND Startindeks = start.NummerInnom)
    INNER JOIN togruteStasjon slutt ON (seteBillett.TogruteID = slutt.TogruteID AND Sluttindeks = slutt.NummerInnom)
    WHERE Ordrenummer = ?''', (ordrenummer,))

    data = cursor.fetchall()
        
    if len(data) != 0:
        print(f"Oversikt over reiser på ordrenummer {ordrenummer} i setevogn: ")
        col_names = ["Ordrenummer", "Ordredato", "Ordretid", "Setenummer", "Vognnummer", "Reisedato", "TogruteID", "Startstasjon", "Starttid", "Sluttstasjon", "Sluttid"]
        setereiser = []
        for d in data:
            setereiser.append(d)
        print(tabulate(setereiser, headers=col_names, tablefmt="grid"))


def se_kupereiser(ordrenummer):
    cursor.execute('''SELECT Ordrenummer, Dag AS Ordredato, Kundeordre.Tid AS Ordretid,
    KupeNummer, vognNummer, Dato, kupeBillett.TogruteID, start.JernbanestasjonNavn, start.Tid, slutt.JernbanestasjonNavn, slutt.Tid
    FROM Kunderegister 
    INNER JOIN Kundeordre USING(Kundenummer)
    INNER JOIN kupeBillett USING(Ordrenummer)
    INNER JOIN togruteStasjon start ON (kupeBillett.TogruteID = start.TogruteID AND Startindeks = start.NummerInnom)
    INNER JOIN togruteStasjon slutt ON (kupeBillett.TogruteID = slutt.TogruteID AND Sluttindeks = slutt.NummerInnom)
    WHERE Ordrenummer = ?''', (ordrenummer,))

    data = cursor.fetchall()
        
    if len(data) != 0:
        print(f'Oversikt over reiser på ordrenummer {ordrenummer} i kupévogn: ')
        col_names = ["Ordrenummer", "Ordredato", "Ordretid", "Kupenummer", "Vognnummer", "Reisedato", "TogruteID", "Startstasjon", "Starttid", "Sluttstasjon", "Sluttid"]
        kupereiser = []
        for d in data:
            kupereiser.append(d)
        print(tabulate(kupereiser, headers=col_names, tablefmt="grid"))


def brukerhistorie_h():
    answer = "ja"
    while answer == "ja":
        ordrenummer = se_kundeordre()
        se_setereiser(ordrenummer)
        se_kupereiser(ordrenummer)
        answer = input("Skriv 'ja' hvis du ønsker å se kundeordre for et annet mobilnummer. Trykke enter for å avslutte: ")
        print('')
    
brukerhistorie_h()
con.close()