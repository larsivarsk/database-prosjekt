import sqlite3
con = sqlite3.connect("innlevering.db")
cursor = con.cursor()

def brukerhistorie_b():
    cursor.execute('''INSERT INTO Operatør(Navn)
    VALUES("SJ");''')

    cursor.execute('''INSERT INTO Vogntype(VognID, Navn, OperatørNavn)
    VALUES(1, "SJ-sittevogn-1", "SJ");''')

    cursor.execute('''INSERT INTO Vogntype(VognID, Navn, OperatørNavn)
    VALUES(2, "SJ-sovevogn-1", "SJ");''')

    cursor.execute('''INSERT INTO Sittevogn(VognID, AntallRader, SeterPerRad)
    VALUES(1, 3, 4);''')

    cursor.execute('''INSERT INTO Sovevogn(VognID, AntallKupeer)
    VALUES(2, 4);''')

    cursor.execute('''INSERT INTO Vognoppsett(ID)
    VALUES(1);''')

    cursor.execute('''INSERT INTO Vognoppsett(ID)
    VALUES(2);''')

    cursor.execute('''INSERT INTO Vognoppsett(ID)
    VALUES(3);''')

    cursor.execute('''INSERT INTO Sete(SeteNummer, VognID)
    VALUES(1, 1);''')

    cursor.execute('''INSERT INTO Sete(SeteNummer, VognID)
    VALUES(2, 1);''')

    cursor.execute('''INSERT INTO Sete(SeteNummer, VognID)
    VALUES(3, 1);''')

    cursor.execute('''INSERT INTO Sete(SeteNummer, VognID)
    VALUES(4, 1);''')

    cursor.execute('''INSERT INTO Sete(SeteNummer, VognID)
    VALUES(5, 1);''')

    cursor.execute('''INSERT INTO Sete(SeteNummer, VognID)
    VALUES(6, 1);''')

    cursor.execute('''INSERT INTO Sete(SeteNummer, VognID)
    VALUES(7, 1);''')

    cursor.execute('''INSERT INTO Sete(SeteNummer, VognID)
    VALUES(8, 1);''')

    cursor.execute('''INSERT INTO Sete(SeteNummer, VognID)
    VALUES(9, 1);''')

    cursor.execute('''INSERT INTO Sete(SeteNummer, VognID)
    VALUES(10, 1);''')

    cursor.execute('''INSERT INTO Sete(SeteNummer, VognID)
    VALUES(11, 1);''')

    cursor.execute('''INSERT INTO Sete(SeteNummer, VognID)
    VALUES(12, 1);''')

    cursor.execute('''INSERT INTO Sovekupe(KupeNummer, VognID)
    VALUES(1, 2);''')

    cursor.execute('''INSERT INTO Sovekupe(KupeNummer, VognID)
    VALUES(2, 2);''')

    cursor.execute('''INSERT INTO Sovekupe(KupeNummer, VognID)
    VALUES(3, 2);''')

    cursor.execute('''INSERT INTO Sovekupe(KupeNummer, VognID)
    VALUES(4, 2);''')

    cursor.execute('''INSERT INTO tilgjengeligVogn(VognID, VognoppsettID, vognNummer)
    VALUES(1, 1, 1);''')

    cursor.execute('''INSERT INTO tilgjengeligVogn(VognID, VognoppsettID, vognNummer)
    VALUES(1, 1, 2);''')

    cursor.execute('''INSERT INTO tilgjengeligVogn(VognID, VognoppsettID, vognNummer)
    VALUES(1, 2, 1);''')

    cursor.execute('''INSERT INTO tilgjengeligVogn(VognID, VognoppsettID, vognNummer)
    VALUES(2, 2, 2);''')

    cursor.execute('''INSERT INTO tilgjengeligVogn(VognID, VognoppsettID, vognNummer)
    VALUES(1, 3, 1);''')



    cursor.execute('''INSERT INTO Togrute(KjørerHovedretning, OperatørNavn, VognoppsettID)
    VALUES(1, "SJ", 1);''')

    cursor.execute('''INSERT INTO togruteStasjon(JernbanestasjonNavn, TogruteID, Tid, NummerInnom)
    VALUES("Trondheim S", 1, "0749", 1);''')

    cursor.execute('''INSERT INTO togruteStasjon(JernbanestasjonNavn, TogruteID, Tid, NummerInnom)
    VALUES("Steinkjer", 1, "0951", 2);''')

    cursor.execute('''INSERT INTO togruteStasjon(JernbanestasjonNavn, TogruteID, Tid, NummerInnom)
    VALUES("Mosjøen", 1, "1320", 3);''')

    cursor.execute('''INSERT INTO togruteStasjon(JernbanestasjonNavn, TogruteID, Tid, NummerInnom)
    VALUES("Mo i Rana", 1, "1431", 4);''')

    cursor.execute('''INSERT INTO togruteStasjon(JernbanestasjonNavn, TogruteID, Tid, NummerInnom)
    VALUES("Fauske", 1, "1649", 5);''')

    cursor.execute('''INSERT INTO togruteStasjon(JernbanestasjonNavn, TogruteID, Tid, NummerInnom)
    VALUES("Bodø", 1, "1734", 6);''')



    cursor.execute('''INSERT INTO Togrute(KjørerHovedretning, OperatørNavn, VognoppsettID)
    VALUES(1, "SJ", 2);''')

    cursor.execute('''INSERT INTO togruteStasjon(JernbanestasjonNavn, TogruteID, Tid, NummerInnom)
    VALUES("Trondheim S", 2, "2305", 1);''')

    cursor.execute('''INSERT INTO togruteStasjon(JernbanestasjonNavn, TogruteID, Tid, NummerInnom)
    VALUES("Steinkjer", 2, "0057", 2);''')

    cursor.execute('''INSERT INTO togruteStasjon(JernbanestasjonNavn, TogruteID, Tid, NummerInnom)
    VALUES("Mosjøen", 2, "0441", 3);''')

    cursor.execute('''INSERT INTO togruteStasjon(JernbanestasjonNavn, TogruteID, Tid, NummerInnom)
    VALUES("Mo i Rana", 2, "0555", 4);''')

    cursor.execute('''INSERT INTO togruteStasjon(JernbanestasjonNavn, TogruteID, Tid, NummerInnom)
    VALUES("Fauske", 2, "0819", 5);''')

    cursor.execute('''INSERT INTO togruteStasjon(JernbanestasjonNavn, TogruteID, Tid, NummerInnom)
    VALUES("Bodø", 2, "0905", 6);''')



    cursor.execute('''INSERT INTO Togrute(KjørerHovedretning, OperatørNavn, VognoppsettID)
    VALUES(0, "SJ", 3);''')

    cursor.execute('''INSERT INTO togruteStasjon(JernbanestasjonNavn, TogruteID, Tid, NummerInnom)
    VALUES("Mo i Rana", 3, "0811", 1);''')

    cursor.execute('''INSERT INTO togruteStasjon(JernbanestasjonNavn, TogruteID, Tid, NummerInnom)
    VALUES("Mosjøen", 3, "0914", 2);''')

    cursor.execute('''INSERT INTO togruteStasjon(JernbanestasjonNavn, TogruteID, Tid, NummerInnom)
    VALUES("Steinkjer", 3, "1231", 3);''')

    cursor.execute('''INSERT INTO togruteStasjon(JernbanestasjonNavn, TogruteID, Tid, NummerInnom)
    VALUES("Trondheim S", 3, "1413", 4);''')



    cursor.execute('''INSERT INTO UkedagTabell(TogruteID, DagsNavn)
    VALUES(1, "Mandag");''')

    cursor.execute('''INSERT INTO UkedagTabell(TogruteID, DagsNavn)
    VALUES(1, "Tirsdag");''')

    cursor.execute('''INSERT INTO UkedagTabell(TogruteID, DagsNavn)
    VALUES(1, "Onsdag");''')

    cursor.execute('''INSERT INTO UkedagTabell(TogruteID, DagsNavn)
    VALUES(1, "Torsdag");''')

    cursor.execute('''INSERT INTO UkedagTabell(TogruteID, DagsNavn)
    VALUES(1, "Fredag");''')

    cursor.execute('''INSERT INTO UkedagTabell(TogruteID, DagsNavn)
    VALUES(2, "Mandag");''')

    cursor.execute('''INSERT INTO UkedagTabell(TogruteID, DagsNavn)
    VALUES(2, "Tirsdag");''')

    cursor.execute('''INSERT INTO UkedagTabell(TogruteID, DagsNavn)
    VALUES(2, "Onsdag");''')

    cursor.execute('''INSERT INTO UkedagTabell(TogruteID, DagsNavn)
    VALUES(2, "Torsdag");''')

    cursor.execute('''INSERT INTO UkedagTabell(TogruteID, DagsNavn)
    VALUES(2, "Fredag");''')

    cursor.execute('''INSERT INTO UkedagTabell(TogruteID, DagsNavn)
    VALUES(2, "Lørdag");''')

    cursor.execute('''INSERT INTO UkedagTabell(TogruteID, DagsNavn)
    VALUES(2, "Søndag");''')

    cursor.execute('''INSERT INTO UkedagTabell(TogruteID, DagsNavn)
    VALUES(3, "Mandag");''')

    cursor.execute('''INSERT INTO UkedagTabell(TogruteID, DagsNavn)
    VALUES(3, "Tirsdag");''')

    cursor.execute('''INSERT INTO UkedagTabell(TogruteID, DagsNavn)
    VALUES(3, "Onsdag");''')

    cursor.execute('''INSERT INTO UkedagTabell(TogruteID, DagsNavn)
    VALUES(3, "Torsdag");''')

    cursor.execute('''INSERT INTO UkedagTabell(TogruteID, DagsNavn)
    VALUES(3, "Fredag");''')

    con.commit()
    con.close()
    
    
brukerhistorie_b()