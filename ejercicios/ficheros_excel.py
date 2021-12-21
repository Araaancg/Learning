import csv

print("esto es una prueba")

with open("./excel.csv", mode="a") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["003","Candela","Rodriguez"])
    print(next(csv_writer))
