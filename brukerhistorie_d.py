import sqlite3
from tabulate import tabulate

con = sqlite3.connect("innlevering.db")
cursor = con.cursor()



def lever_togruter(startstasjon, sluttstasjon, dato, klokkeslett): 
    cursor.execute('''
        SELECT TogruteID, KjørerHovedretning, OperatørNavn, Dato, startstasjon.JernbanestasjonNavn as Startstasjon, startstasjon.Tid as Starttid, sluttstasjon.JernbanestasjonNavn as Sluttstasjon, sluttstasjon.Tid as Sluttid
        FROM ((Togrute INNER JOIN Togruteforekomst USING(TogruteID)) 
        INNER JOIN togruteStasjon startstasjon USING(TogruteID)) 
        INNER JOIN togruteStasjon sluttstasjon USING(TogruteID)
        WHERE (((Starttid >= CAST(? AS INTEGER) AND Dato = CAST(? AS INTEGER))
        OR Dato = CAST(?+1 AS INTEGER))
        OR Starttid < ? AND startstasjon.NummerInnom < sluttstasjon.NummerInnom AND Dato = CAST(? AS INTEGER))
        AND startstasjon = ? AND sluttstasjon = ?
        AND startstasjon.NummerInnom < sluttstasjon.NummerInnom
        GROUP BY TogruteID, KjørerHovedretning, OperatørNavn, Dato, Starttid, Sluttid
        ORDER BY Dato, Starttid ASC
    ''', (klokkeslett, dato, dato, klokkeslett, dato, startstasjon, sluttstasjon))

    ruteliste = []
    data = cursor.fetchall()
    for d in data:
        ruteliste.append(d)  

    col_names = ["TogruteID", "Kjører hovedretning", "Operatørnavn", "Dato for ruteavgang", "Startstasjon", "Starttid", "Sluttstasjon", "Sluttid"]
    print(tabulate(ruteliste, headers=col_names, tablefmt="grid"))
        

    

def brukerhistore_d():
    answer = "ja"
    while answer == "ja":
        startstasjon = input("Skriv inn stasjonen du vil reise fra: ")
        sluttstasjon = input("Skriv inn stasjonen du ønsker å reise til: ")
        dato = input("Skriv inn datoen du ønsker å reise på formatet yyyymmdd: ")
        klokkeslett = input("Skriv inn klokkeslettet du ønsker å reise på formatet ttmm: ")
        print('')
        lever_togruter(startstasjon, sluttstasjon, dato, klokkeslett)
        print('')
        answer = input("Skriv 'ja' hvis du ønsker å finne andre ruter: ")


brukerhistore_d()
#lever_togruter("Mosjøen", "Steinkjer", "20230403", "0700")
con.close()
