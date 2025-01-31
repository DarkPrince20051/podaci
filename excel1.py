import csv
import os

# Naziv datoteke
naziv_datoteke = "podaci.csv"

# Funkcija za inicijalizaciju datoteke
def inicijaliziraj_datoteku():
    if not os.path.exists(naziv_datoteke):
        with open(naziv_datoteke, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Ime", "Prezime", "Datum rođenja", "Mjesto", "OIB"])

# Funkcija za dodavanje podataka
def dodaj_podatke():
    with open(naziv_datoteke, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        while True:
            ime = input("Unesi ime: ")
            prezime = input("Unesi prezime: ")
            datum_rodjenja = input("Unesi datum rođenja (dd.mm.gggg): ")
            mjesto = input("Unesi mjesto: ")
            oib = input("Unesi OIB: ")
            writer.writerow([ime, prezime, datum_rodjenja, mjesto, oib])
            nastavak = input("Želite li dodati još jedan unos? (da/ne): ").lower()
            if nastavak != "da":
                break

# Funkcija za prikaz podataka
def prikazi_podatke():
    with open(naziv_datoteke, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        print("\nSadržaj datoteke:")
        for row in reader:
            print("{:<10} {:<10} {:<15} {:<15} {:<15}".format(*row))
    print()

# Funkcija za brisanje podataka
def obrisi_podatke():
    potvrda = input("Jeste li sigurni da želite obrisati sve podatke? (da/ne): ").lower()
    if potvrda == "da":
        with open(naziv_datoteke, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Ime", "Prezime", "Datum rođenja", "Mjesto", "OIB"])
        print("Svi podaci su obrisani.")
    else:
        print("Podaci nisu obrisani.")

# Glavni program
def glavni_program():
    inicijaliziraj_datoteku()
    while True:
        print("\nIzbornik:")
        print("1. Dodaj podatke")
        print("2. Prikaži podatke")
        print("3. Obriši sve podatke")
        print("4. Izlaz iz programa")
        
        izbor = input("Odaberite opciju (1-4): ")
        if izbor == "1":
            dodaj_podatke()
        elif izbor == "2":
            prikazi_podatke()
        elif izbor == "3":
            obrisi_podatke()
        elif izbor == "4":
            print("Izlaz iz programa. Doviđenja!")
            break
        else:
            print("Neispravan unos. Pokušajte ponovno.")

# Pokretanje programa
glavni_program()
