# 1.-------------------------
board = {'Benny', 'Hans', 'Tine', 'Mille', 'Torben', 'Troels', 'Søren'}
management = {'Tine', 'Trunte', 'Rane'}
employees = {'Niels', 'Anna', 'Tine', 'Ole', 'Trunte', 'Bent', 'Rane', 'Allan', 'Stine', 'Claus', 'James', 'Lars'} 

# Who in the board of directors is not an employee?
print(board.difference(employees))

# Who in the board of directors is also an employee?
print(board.intersection(employees))

# How many of the management is also member of the board?
print(len(management.intersection(board)))

# All members of the mamagement also an employee?
print(management.intersection(employees))

# All members of the management also in the board?
print(management.intersection(board))

# Who is an employee, member of the management, and a member of the board?
print(employees.intersection(management, board))

# Who of the employee is neither a member of the board or management
print(employees.difference(management, board))

# 2.-------------------------
list1 = [('a', 'Alpha'), ('b', 'Beta'), ('g', 'Gamma')]

# 3.-------------------------
set1 = {'a', 'e', 'i', 'o', 'u', 'y'}
set2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø', 'å'}

# Union
union = set1.union(set2)

# Symmetric Difference
symmetricDifference = set1.symmetric_difference(set2)

# Difference
difference1 = set1.difference(set2)
difference2 = set2.difference(set1)

# Disjoint
set1.intersection(set2)

# 4.-------------------------
months = {
    'JAN': 1,
    'FEB': 2,
    'MAR': 3,
    'APR': 4,
    'MAJ': 5,
    'JUN': 6,
    'JUL': 7,
    'AUG': 8,
    'SET': 9,
    'OCT': 10,
    'NOV': 11,
    'DEC': 12,
}

def dateDecoder(input):
    splitInput = input.split('-')
    day = splitInput[0]
    month = splitInput[1]
    year = splitInput[2]
    return ('20' + year if int(year) > 0 and int(year) <= 21 else '19' + year, months[month.upper()], day)

print(dateDecoder('08-mar-85'))