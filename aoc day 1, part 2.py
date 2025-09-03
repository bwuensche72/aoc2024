# auslesen des Inputs aus der Datei
with open("input.txt", "r") as file:
  input_data = file.readlines()

# Spalten zu Listen umwandeln
leftColumn = []
rightColumn = []
for line in input_data:
  leftColumn.append(int(line.split()[0].strip()))
  rightColumn.append(int(line.split()[1].strip()))

# Jede Nummer in 'leftColumn' wird multipliziert in der Anzahl,
# wie oft es vor kommt als Nummer in 'rightColumn'
total = 0
for num in leftColumn:
  total += num * rightColumn.count(num)

print(total)