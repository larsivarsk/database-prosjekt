import sqlite3
from tabulate import tabulate 

con = sqlite3.connect("innlevering.db")
cursor = con.cursor()


def vis_togruter():
    data = cursor.fetchall()
    togruter = []
    col_names = ["TogruteID", "Operatørnavn", "Dato", "Startstasjon", "Starttid", "Sluttstasjon", "Sluttid", "", ""]

    for d in data:
        togruter.append(d)
    
    if len(togruter) != 0:
        print("")
        print("Tilgjengelige togruter på valgt strekning, dato og vogntype:")
        print(tabulate(togruter, headers=col_names, tablefmt="grid"))
        return True
    else:
        print('')
        print("Ingen ledige billetter på denne strekningen. Vennligst prøv en annen vogntype eller dato.")
        return False
 
 
def ruter_med_sete(reisedato, startstasjon, sluttstasjon):
    cursor.execute('''SELECT TogruteID, OperatørNavn, Dato, start.JernbanestasjonNavn AS Startstasjon,
                                start.Tid AS Starttid, slutt.JernbanestasjonNavn AS Sluttstasjon, slutt.Tid AS Sluttid, SeteNummer, vognNummer
                FROM Togrute
                INNER JOIN Togruteforekomst USING(TogruteID)
                INNER JOIN tilgjengeligVogn USING(VognoppsettID)
                LEFT OUTER JOIN Sete USING(VognID)
                LEFT OUTER JOIN Sovekupe USING(VognID)
                INNER JOIN togruteStasjon start USING(TogruteID)
                INNER JOIN togruteStasjon slutt USING(TogruteID)
                WHERE Dato = ?
                AND start.NummerInnom < slutt.NummerInnom
                AND start.JernbanestasjonNavn = ?
                AND slutt.JernbanestasjonNavn = ?
                AND SeteNummer IS NOT NULL
                AND NOT EXISTS (
                        SELECT *
                        FROM seteBillett
                        WHERE seteBillett.SeteNummer = Sete.SeteNummer
                        AND seteBillett.VognID = Sete.VognID
                        AND seteBillett.Dato = Togruteforekomst.Dato
                        AND seteBillett.TogruteID = Togrute.TogruteID
                        AND seteBillett.vognNummer = tilgjengeligVogn.vognNummer
                        AND slutt.NummerInnom > seteBillett.Startindeks
                        AND start.NummerInnom < seteBillett.Sluttindeks
                        )
                GROUP BY TogruteID;''', (reisedato, startstasjon, sluttstasjon))        


def ruter_med_kupe(reisedato, startstasjon, sluttstasjon):
    cursor.execute('''SELECT TogruteID, OperatørNavn, Dato, start.JernbanestasjonNavn AS Startstasjon,
                                start.Tid AS Starttid, slutt.JernbanestasjonNavn AS Sluttstasjon, slutt.Tid AS Sluttid
                FROM Togrute
                INNER JOIN Togruteforekomst USING(TogruteID)
                INNER JOIN tilgjengeligVogn USING(VognoppsettID)
                LEFT OUTER JOIN Sete USING(VognID)
                LEFT OUTER JOIN Sovekupe USING(VognID)
                INNER JOIN togruteStasjon start USING(TogruteID)
                INNER JOIN togruteStasjon slutt USING(TogruteID)
                WHERE Dato = ?
                AND start.NummerInnom < slutt.NummerInnom
                AND start.JernbanestasjonNavn = ?
                AND slutt.JernbanestasjonNavn = ?
                AND KupeNummer IS NOT NULL
                AND NOT EXISTS (
                        SELECT *
                        FROM kupeBillett
                        WHERE kupeBillett.KupeNummer = Sovekupe.KupeNummer
                        AND kupeBillett.VognID = Sovekupe.VognID
                        AND kupeBillett.Dato = Togruteforekomst.Dato
                        AND kupeBillett.TogruteID = Togrute.TogruteID
                        AND kupeBillett.vognNummer = tilgjengeligVogn.vognNummer
                        )
                GROUP BY TogruteID;''', (reisedato, startstasjon, sluttstasjon))

    
def opprett_kundeordre():
    
    # HENTER INFORMASJON TIL KUNDEORDRE
    try:
        mobilnummer = input("Oppgi mobilnummeret du står oppført med i kunderegisteret for å bestille billett: ")
        cursor.execute('''SELECT Kundenummer
        FROM Kunderegister
        WHERE Mobilnummer = ?''', (mobilnummer,))
        kundenummer = int(cursor.fetchone()[0])
        
        cursor.execute('''INSERT INTO Kundeordre(Dag, Tid, Kundenummer)
        VALUES("20230330", "0500", ?)''', (kundenummer,))
        con.commit()
        
        # ODRENUMMERET SOM BRUKES TIL BESTILLING AV BILLETT(ER).
        # VELGER DET HØYESTE ORDRENUMMERET SIDEN AUTOINCREMENT BRUKES, 
        # OG DERMED VIL DET GJELDENDE ORDRENUMMERET PÅ DENNE BESTILLINGEN VÆRE DET HØYESTE
        cursor.execute('''SELECT Ordrenummer
        FROM Kundeordre 
        WHERE Ordrenummer = (SELECT max(Ordrenummer) FROM Kundeordre)''')
        ordrenummer = cursor.fetchone()[0]
    except:
        print('')
        print("Mobilnummeret er ikke registrert i databasen")
        print('')
        
    return ordrenummer


def bestill_sete(startstasjon, sluttstasjon, reisedato, ordrenummer, togrute_id):
    
    cursor.execute('''SELECT SeteNummer, vognNummer, start.NummerInnom, slutt.NummerInnom
    FROM Togrute
    INNER JOIN Togruteforekomst USING(TogruteID)
    INNER JOIN tilgjengeligVogn USING(VognoppsettID)
    LEFT OUTER JOIN Sete USING(VognID)
    LEFT OUTER JOIN Sovekupe USING(VognID)
    INNER JOIN togruteStasjon start USING(TogruteID)
    INNER JOIN togruteStasjon slutt USING(TogruteID)
    WHERE Dato = ?
    AND start.NummerInnom < slutt.NummerInnom
    AND start.JernbanestasjonNavn = ?
    AND slutt.JernbanestasjonNavn = ?
    AND Togrute.TogruteID = ?
    AND SeteNummer IS NOT NULL
    AND NOT EXISTS (
            SELECT *
            FROM seteBillett
            WHERE seteBillett.SeteNummer = Sete.SeteNummer
            AND seteBillett.VognID = Sete.VognID
            AND seteBillett.Dato = Togruteforekomst.Dato
            AND seteBillett.TogruteID = Togrute.TogruteID
            AND seteBillett.vognNummer = tilgjengeligVogn.vognNummer
            AND slutt.NummerInnom > seteBillett.Startindeks
            AND start.NummerInnom < seteBillett.Sluttindeks
            )
    GROUP BY TogruteID, vognNummer, SeteNummer;''', (reisedato, startstasjon, sluttstasjon, togrute_id))
    
    data = cursor.fetchone()
    setenummer = data[0]
    vognnummer = data[1]
    startindeks = data[2]
    sluttindeks = data[3]
    
    cursor.execute('''INSERT INTO seteBillett(SeteNummer, vognNummer, VognID, Dato, TogruteID, Ordrenummer, Startindeks, Sluttindeks)
    VALUES(?, ?, 1, ?, ?, ?, ?, ?)''', (setenummer, vognnummer, reisedato,togrute_id, ordrenummer, startindeks, sluttindeks))
    con.commit()
    return setenummer, vognnummer


def bestill_kupe(startstasjon, sluttstasjon, reisedato, ordrenummer, togrute_id, antall_senger):
    
    cursor.execute('''SELECT KupeNummer, vognNummer, start.NummerInnom, slutt.NummerInnom
    FROM Togrute
    INNER JOIN Togruteforekomst USING(TogruteID)
    INNER JOIN tilgjengeligVogn USING(VognoppsettID)
    LEFT OUTER JOIN Sete USING(VognID)
    LEFT OUTER JOIN Sovekupe USING(VognID)
    INNER JOIN togruteStasjon start USING(TogruteID)
    INNER JOIN togruteStasjon slutt USING(TogruteID)
    WHERE Dato = ?
    AND start.NummerInnom < slutt.NummerInnom
    AND start.JernbanestasjonNavn = ?
    AND slutt.JernbanestasjonNavn = ?
    AND KupeNummer IS NOT NULL
    AND Togrute.TogruteID = ?
    AND NOT EXISTS (
            SELECT *
            FROM kupeBillett
            WHERE kupeBillett.KupeNummer = Sovekupe.KupeNummer
            AND kupeBillett.VognID = Sovekupe.VognID
            AND kupeBillett.Dato = Togruteforekomst.Dato
            AND kupeBillett.TogruteID = Togrute.TogruteID
            AND kupeBillett.vognNummer = tilgjengeligVogn.vognNummer
            )
    GROUP BY TogruteID, vognNummer, KupeNummer;''', (reisedato, startstasjon, sluttstasjon, togrute_id))

    data = cursor.fetchone()
    kupenummer = data[0]
    vognnummer = data[1]
    startindeks = data[2]
    sluttindeks = data[3]
    
    
    cursor.execute('''INSERT INTO kupeBillett(KupeNummer, vognNummer, VognID, Dato, TogruteID, Ordrenummer, AntallSenger, Startindeks, Sluttindeks)
    VALUES(?, ?, 2, ?, ?, ?, ?, ?, ?)''', (kupenummer, vognnummer, reisedato, togrute_id, ordrenummer, antall_senger, startindeks, sluttindeks))
    con.commit()
    
    return kupenummer, vognnummer


def brukerhistorie_g():
    
    ordrenummer = opprett_kundeordre()
    
    # INFORMASJON FOR Å HENTE UT AKTUELLE TOGRUTER
    startstasjon = input("Hvor ønsker du å reise fra?: ")
    sluttstasjon = input("Hvor ønsker du å reise til?: ")
    reisedato = input("Hvilken dato (yyyymmdd) ønsker du å reise?: ")

    answer = "ja"
    while answer == "ja":
        valg = input("Velg vogntype ved å taste '1' for sittevogn og '2' for sovevogn: ")

        
        if int(valg) == 1:
            
            ruter_med_sete(reisedato, startstasjon, sluttstasjon)
            togruter = vis_togruter()
            print('')
           
            if togruter:
                togrute_id = input("Tast inn TogruteID-en til ruten du ønsker å ta: ")
                nummere = bestill_sete(startstasjon, sluttstasjon, reisedato, ordrenummer, togrute_id)
                print('')
                print(f"Du har nå bestilt billett for sete nr. {nummere[0]} i vogn nr. {nummere[1]}. \nStartstasjon: {startstasjon}. \nSluttstasjon: {sluttstasjon}. \nDato: {reisedato}. \nTogrute: {togrute_id}")
                print('')
            
        if int(valg) == 2:
            
            ruter_med_kupe(reisedato, startstasjon, sluttstasjon)
            togruter = vis_togruter()
            print('')
            
            if togruter:
                togrute_id = input("Tast inn TogruteID-en til ruten du ønsker å ta: ")
                antall_senger = input("Hvor mange senger vil du ha (tast '1' eller '2'): ")
                nummere = bestill_kupe(startstasjon, sluttstasjon, reisedato, ordrenummer, togrute_id, antall_senger)
                print('')
                print(f"Du har nå bestilt billett for sovekupe nr. {nummere[0]} i vogn nr. {nummere[1]}. \nAntall senger: {antall_senger}. \nStartstasjon: {startstasjon}. \nSluttstasjon: {sluttstasjon}. \nDato: {reisedato}. \nTogrute: {togrute_id}")
                print('')
        
                
        answer = input("Ønsker du å bestille flere billetter på denne strekningen og datoen? Svar 'ja'. Trykk på enter for å avslutte: ")
        print('')
    
    

brukerhistorie_g()

con.close()
