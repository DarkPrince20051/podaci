import json

# Naziv datoteke za spremanje podataka
DATA_FILE = "person_data.json"

# Učitavanje podataka iz datoteke
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

# Spremanje podataka u datoteku
def save_data():
    with open(DATA_FILE, "w") as file:
        json.dump(people, file, indent=2)

# Dodavanje osobe
def add_person():
    name = input("Unesi ime: ")
    birthdate = input("Unesi datum rođenja: ")
    birthplace = input("Unesi mjesto rođenja: ")
    oib = input("Unesi OIB: ")

    if name and birthdate and birthplace and oib:
        people.append({
            "name": name,
            "birthdate": birthdate,
            "birthplace": birthplace,
            "oib": oib
        })
        save_data()
        print("Osoba uspješno dodana!")
    else:
        print("Greška: Sva polja moraju biti ispunjena!")

# Prikaz svih osoba
def list_people():
    if not people:
        print("Nema unesenih osoba.")
    else:
        print("\nPopis osoba:")
        for idx, person in enumerate(people, start=1):
            print(f"{idx}. {person['name']} - {person['birthdate']} - {person['birthplace']} - {person['oib']}")

# Pretraga osobe po imenu
def find_person():
    search_name = input("Unesi ime za pretragu: ")
    found = [p for p in people if p["name"].lower() == search_name.lower()]
    
    if found:
        for person in found:
            print(f"Pronađeno: {person['name']} - {person['birthdate']} - {person['birthplace']} - {person['oib']}")
    else:
        print("Osoba nije pronađena.")

# Brisanje osobe
def delete_person():
    search_name = input("Unesi ime osobe za brisanje: ")
    global people
    people = [p for p in people if p["name"].lower() != search_name.lower()]
    save_data()
    print(f"Osoba '{search_name}' je obrisana (ako je postojala).")

# Glavni meni
def main():
    while True:
        print("\n========== MENI ==========")
        print("1 - Dodaj osobu")
        print("2 - Prikaži sve osobe")
        print("3 - Pretraži osobu")
        print("4 - Obriši osobu")
        print("5 - Izlaz")

        choice = input("\nOdaberi opciju: ")

        if choice == "1":
            add_person()
        elif choice == "2":
            list_people()
        elif choice == "3":
            find_person()
        elif choice == "4":
            delete_person()
        elif choice == "5":
            save_data()
            print("Izlaz iz programa...")
            break
        else:
            print("Pogrešan unos, pokušajte ponovo!")

# Učitavanje podataka prilikom pokretanja
people = load_data()
main()
