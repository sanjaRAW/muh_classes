file1 = open('spam.txt')
list1 = file1.readlines()
file2 = open('sasa.txt', 'w')
for line in list1:
    line = line.strip()
    if 'help' in line or 'asap' in line or 'urgent' in line or line.isupper():
        file2.write(line + '\n')
    elif line.endswith('!!!'):
        file2.write(line+'\n')

print(file1)
