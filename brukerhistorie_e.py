import sqlite3
from tabulate import tabulate

con = sqlite3.connect("innlevering.db")
cursor = con.cursor()

def registrer_kunde(navn, epost, mobilnummer):
    cursor.execute('''INSERT INTO Kunderegister(Navn, Epost, Mobilnummer) VALUES(?, ?, ?)''', (navn, epost, mobilnummer))
    con.commit()
    
def se_kunderegister():
    tabell = []
    cursor.execute('''SELECT * FROM Kunderegister''')
    data = cursor.fetchall()
    for d in data:
        tabell.append(d)
    col_names = ["Kundenummer", "Navn", "E-post", "Mobilnummer"]
    print(tabulate(tabell, headers=col_names, tablefmt="grid"))    
    


def brukerhistorie_e():      
    print("Her kan du registrere deg i kunderegisteret:")
    answer = "ja"
    while answer == "ja":
        navn = input("Navn: ")
        epost = input("E-post: ")
        mobilnummer = input("Mobilnummer: ")
        print('')
        print(f"Hei, {navn}! Du er nå registrert som kunde med e-post: {epost} og mobilnummer: {mobilnummer}")
        print('')
        answer = input("Skriv 'ja' hvis du ønsker å registrere ny kunde: ")
        registrer_kunde(navn, epost, mobilnummer)
    

brukerhistorie_e()
#se_kunderegister()
con.close()