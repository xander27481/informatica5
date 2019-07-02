matrix = []
rows = 20
largest = 0

for i in range(rows):
    matrix.append(input().split(' '))



# horizotal
for row in matrix:
     largest = max(max([int(row[i]) * int(row[i + 1]) * int(row[i + 2]) * int(row[i + 3]) for i in range(rows - 4)]), largest)

# vertical
matrix_ver = [[matrix[row][colom] for row in range(rows)] for colom in range(rows)]
for row in matrix_ver:
     largest = max(max([int(row[i]) * int(row[i + 1]) * int(row[i + 2]) * int(row[i + 3]) for i in range(rows - 4)]), largest)

# diagenal (/)


#print(largest)