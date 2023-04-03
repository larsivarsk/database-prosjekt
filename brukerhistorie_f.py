import sqlite3
con = sqlite3.connect("innlevering.db")
cursor = con.cursor()

def brukerhistorie_f():
    #Togruteforekomster for 3. april og 4. april
    cursor.execute('''INSERT INTO Togruteforekomst(TogruteID, Dato)
    VALUES(1, "20230403");''')
    cursor.execute('''INSERT INTO Togruteforekomst(TogruteID, Dato)
    VALUES(2, "20230403");''')
    cursor.execute('''INSERT INTO Togruteforekomst(TogruteID, Dato)
    VALUES(3, "20230403");''')
    cursor.execute('''INSERT INTO Togruteforekomst(TogruteID, Dato)
    VALUES(1, "20230404");''')
    cursor.execute('''INSERT INTO Togruteforekomst(TogruteID, Dato)
    VALUES(2, "20230404");''')
    cursor.execute('''INSERT INTO Togruteforekomst(TogruteID, Dato)
    VALUES(3, "20230404");''')
    
    
    con.commit()
    con.close()

brukerhistorie_f()