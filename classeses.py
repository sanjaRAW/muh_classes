file1 = open('sosg')
list1 = file1.readlines()
file2 = open('sasa','w')
for line in list1:

    if 'help'in line or 'HELP'in line or 'asap'in line or 'ASAP'in line or 'urgent'in line or 'URGENT' in line or line.endswith("!!!") or line.isupper():
        file2.write(line)

print(file1)
print(file2)
