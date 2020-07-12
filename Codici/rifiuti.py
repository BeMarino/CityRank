import csv
import re

citta = ["Palermo", "Napoli", "Roma", "Milano", "Torino"] #Definiamo la lista delle province che ci servono

def get_data():
    f = open("Raccolta Differenziata_Produzione Rifiuti.csv","wt")      #Apriamo il file che conterrà solo i dati che ci servono
    writer = csv.writer(f)
    writer.writerow(["Provincia","Raccolta rifiuti urbani(kg/abitante)","Raccolta differenziata(%)"])       #Scriviamo l'intestazione
    with open("Open Data/dataset/RIFIUTI_URBANI_2018.csv") as file:
        reader = csv.reader(file)
        
        for row in reader:
            if row[0] in citta:         #Andiamo a filtrare il dataset in base alle province
                writer.writerow([row[0],'%.2f'%float(row[7].replace(",",".")),'%.1f'%float(row[15].replace(",","."))])

    f.close()

if __name__ == '__main__':
    get_data()
    
