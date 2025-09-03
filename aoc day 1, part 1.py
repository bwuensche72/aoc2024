# auslesen des Inputs aus der Datei
with open("input.txt", "r") as file:
  input_data = file.readlines()

# Spalten zu Listen umwandeln
leftColumn = []
rightColumn = []
for line in input_data:
  leftColumn.append(int(line.split()[0].strip()))
  rightColumn.append(int(line.split()[1].strip()))

# beide Spalten sortieren
leftColumn.sort()  
rightColumn.sort()

# Berechnet für jedes "Zeilen-Paar" die Differenz der beiden Werte
# und addiert den Wert zu der Variable 'total' dazu
total = 0
for i in range(0, len(leftColumn)):
  total += abs(rightColumn[i] - leftColumn[i])

print(total)