import sqlite3
from tabulate import tabulate

con = sqlite3.connect("innlevering.db")
cursor = con.cursor()

def lever_togruter(jernbanestasjon, ukedag):
    tabell = []
    cursor.execute('''
    SELECT DISTINCT Togrute.TogruteID, KjørerHovedretning, OperatørNavn, 
            avgangsstasjon.JernbanestasjonNavn AS Startstasjon, 
            endestasjon.JernbanestasjonNavn AS Sluttstasjon, 
            valgtstasjon.JernbanestasjonNavn AS Ønsketstasjon, 
            valgtstasjon.Tid AS "Tid på oppgitt stasjon", DagsNavn
    FROM Togrute 
    INNER JOIN togruteStasjon valgtstasjon ON Togrute.TogruteID = valgtstasjon.TogruteID
    INNER JOIN UkedagTabell ON Togrute.TogruteID = UkedagTabell.TogruteID
    INNER JOIN togruteStasjon endestasjon ON Togrute.TogruteID = endestasjon.TogruteID 
                                        AND endestasjon.NummerInnom = (SELECT max(NummerInnom) 
                                                                        FROM togruteStasjon 
                                                                        WHERE togruteStasjon.TogruteID = Togrute.TogruteID)
    INNER JOIN togruteStasjon avgangsstasjon ON Togrute.TogruteID = avgangsstasjon.TogruteID 
                                            AND avgangsstasjon.NummerInnom = 1
    WHERE valgtstasjon.JernbanestasjonNavn = ?
    AND DagsNavn = ?
    ORDER BY Togrute.TogruteID;
    ''', (jernbanestasjon, ukedag))
    
    data = cursor.fetchall()
    for d in data:
        tabell.append(d)
    col_names = ["TogruteID", "Kjører hovedretning", "Operatørnavn", "Rutens startstasjon", "Rutens sluttstasjon", "Valgt stasjon", "Tidspunkt på valgt stasjon", "Dag"]
    print(tabulate(tabell, headers=col_names, tablefmt="grid"))
        
def brukerhistorie_c():     
    answer = "ja"
    while answer == "ja":   
        jernbanestasjon = input("Oppgi en jernbanestasjon: ")
        ukedag = input("Oppgi ønsket ukedag: ").capitalize()
        print('')
        lever_togruter(jernbanestasjon, ukedag)
        print('')
        answer = input("Skriv 'ja' hvis du ønsker å finne andre togruter: ")

brukerhistorie_c()
con.close()
