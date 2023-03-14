import csv
p1 = []
p1paid = []
p2 = []
p2paid = []
with open('march.csv', newline='') as csvfile:
    doc = csv. reader (csvfile, quotechar='|')
    for row in doc:
        if "Not Paid" in row:
            if row[2] != '':
                p1.append(int (row [2]))
            elif row[1] != '':
                p2.append(int (row [1]))
        elif "Paid" in row:
            if row [2] != '':
                p1paid.append (int (row[2]))
            elif row [1] != '':
                p2paid.append(int (row[1]))
print(f"Person 2 paid and Person 1 owes: {sum(p2):, }")
print (f"Person 1 paid and Person 2 owes: {sum(p1):,}")
sum = sum(p2)+ sum(p2paid) +sum(p1)+sum(p1paid)
print (f"The total that Vivian and Tyler spent is {sum:,}")