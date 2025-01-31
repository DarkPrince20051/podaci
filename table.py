# Podaci
data = [
    ["ID", "Name", "Age"],
    ["1", "Alice", "28"],
    ["2", "Bob", "32"],
    ["3", "Charlie", "22"]
]

# Izračunavanje širine kolona
col_widths = [max(len(row[i]) for row in data) for i in range(len(data[0]))]

# Funkcija za crtanje horizontalne linije
def print_line():
    print("+" + "+".join("-" * (col_widths[i] + 2) for i in range(len(col_widths))) + "+")

# Ispis tabele
print_line()  # Gornja linija
for i, row in enumerate(data):
    print("| " + " | ".join(f"{val:<{col_widths[j]}}" for j, val in enumerate(row)) + " |")
    if i == 0 or i == len(data) - 1:  # Crta nakon zaglavlja i na kraju
        print_line()
