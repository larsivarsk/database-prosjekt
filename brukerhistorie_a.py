import sqlite3
con = sqlite3.connect("innlevering.db")
cursor = con.cursor()

def brukerhistorie_a():
    cursor.execute('''INSERT INTO Banestrekning(Navn, Fremdriftsenergi)
    VALUES("Nordlandsbanen", "diesel");''')

    cursor.execute('''INSERT INTO Jernbanestasjon(Navn, HøydeOverHavet)
    VALUES ("Trondheim S", 5.1);''')

    cursor.execute('''INSERT INTO Jernbanestasjon(Navn, HøydeOverHavet)
    VALUES ("Steinkjer", 3.6);''')

    cursor.execute('''INSERT INTO Jernbanestasjon(Navn, HøydeOverHavet)
    VALUES ("Mosjøen", 6.8);''')

    cursor.execute('''INSERT INTO Jernbanestasjon(Navn, HøydeOverHavet)
    VALUES ("Mo i Rana", 3.5);''')

    cursor.execute('''INSERT INTO Jernbanestasjon(Navn, HøydeOverHavet)
    VALUES ("Fauske", 34.0);''')

    cursor.execute('''INSERT INTO Jernbanestasjon(Navn, HøydeOverHavet)
    VALUES ("Bodø", 4.1);''')

    cursor.execute('''INSERT INTO stasjonType(JernbanestasjonNavn, BanestrekningNavn, Type)
    VALUES("Trondheim S", "Nordlandsbanen", "baneStart");''')

    cursor.execute('''INSERT INTO stasjonType(JernbanestasjonNavn, BanestrekningNavn, Type)
    VALUES("Steinkjer", "Nordlandsbanen", "baneInnom");''')

    cursor.execute('''INSERT INTO stasjonType(JernbanestasjonNavn, BanestrekningNavn, Type)
    VALUES("Mosjøen", "Nordlandsbanen", "baneInnom");''')

    cursor.execute('''INSERT INTO stasjonType(JernbanestasjonNavn, BanestrekningNavn, Type)
    VALUES("Mo i Rana", "Nordlandsbanen", "baneInnom");''')

    cursor.execute('''INSERT INTO stasjonType(JernbanestasjonNavn, BanestrekningNavn, Type)
    VALUES("Fauske", "Nordlandsbanen", "baneInnom");''')

    cursor.execute('''INSERT INTO stasjonType(JernbanestasjonNavn, BanestrekningNavn, Type)
    VALUES("Bodø", "Nordlandsbanen", "baneSlutt");''')

    cursor.execute('''INSERT INTO Delstrekning(startStasjon, sluttStasjon, LengdeKM, HarDobbeltspor)
    VALUES("Trondheim S", "Steinkjer", 120, 1);''')

    cursor.execute('''INSERT INTO Delstrekning(startStasjon, sluttStasjon, LengdeKM, HarDobbeltspor)
    VALUES("Steinkjer", "Mosjøen", 280, 0);''')

    cursor.execute('''INSERT INTO Delstrekning(startStasjon, sluttStasjon, LengdeKM, HarDobbeltspor)
    VALUES("Mosjøen", "Mo i Rana", 90, 0);''')

    cursor.execute('''INSERT INTO Delstrekning(startStasjon, sluttStasjon, LengdeKM, HarDobbeltspor)
    VALUES("Mo i Rana", "Fauske", 170, 0);''')

    cursor.execute('''INSERT INTO Delstrekning(startStasjon, sluttStasjon, LengdeKM, HarDobbeltspor)
    VALUES("Fauske", "Bodø", 60, 0);''')

    con.commit()
    con.close()
    
brukerhistorie_a()
