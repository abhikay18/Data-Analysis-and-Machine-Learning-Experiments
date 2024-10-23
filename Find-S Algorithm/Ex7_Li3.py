import csv

attr_values = [['Y', 'N'], ['Y', 'N'], ['Y', 'N'], ['Y', 'N']]

num_attrs = len(attr_values)

print("\n The most general hypothesis : ['?', '?', '?', '?']\n")
print("\n The most specific hypothesis : ['0', '0', '0', '0']\n")

a = []
print("\n Training Dataset \n")

with open('finds3.csv', 'r' , encoding='utf-8-sig') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        # Ensure each row has the correct number of attributes plus the target value
        if len(row) == num_attrs + 1:
            a.append(row)
            print(row)
        else:
            print(f"Skipping row due to incorrect length: {row}")

print("\n The initial value of hypothesis: ")
h = ['0'] * num_attrs
print(h)

# The Hypothesis 'h' with the first training instance
for j in range(0, num_attrs):
    h[j] = a[0][j]

# The Hypothesis 'h' with subsequent training instances
print("\n Find S: Finding Maximally Specific Hypothesis\n")

for i in range(0, len(a)):
    if a[i][num_attrs] == 'Positive':  # Checking for 'Positive' instead of 'Yes'
        for j in range(0, num_attrs):
            if a[i][j] != h[j]:
                h[j] = '?'
            else:
                h[j] = a[i][j]

    print(f"Training Instance: {i} the hypothesis 'h' is {h}")

print("\n The Final Maximally Specific Hypothesis 'h' is :")
print(h)
