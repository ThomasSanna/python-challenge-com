file = open('3.txt', 'r', encoding='utf-8')

count = 0
legrale = ""

for line in file:
    for i in range (len(line)):
        if line[i-1].isupper() and count==0:
            count=0
            legrale=''
        elif line[i].isupper() and (count<3 or count>3) and count<=6:
            count += 1
            legrale += line[i]
        elif count == 3 and line[i].islower():
            count += 1
            legrale += line[i]
        elif count == 7 and line[i].islower():
            print(legrale)
            legrale=''
            count=0
        else:
            count = 0
            legrale = ""
