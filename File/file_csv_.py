import csv
with open("j.csv","w") as f:
    writer=csv.writer(f)
    writer.writerow(["Name","Age"])
    writer.writerow(["John",25])
    writer.writerow(["Alice",30])