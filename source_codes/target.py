import re
import string
# remove blank lines 
data=[]

with open('target.txt','r') as file:
    for line in file:
        if not line.isspace():
            data.append(line) 

#listToStr = ' '.join(map(str, data))

#print words in separate lines
nlist =[]

for line1 in data:
    words = re.sub('['+string.punctuation+']', '', line1).split()
    for j in words:
        if j.isalpha():
            nlist.append(j)
            nlist += '\n'
            #break
        else:
            continue
        
listToStr1 = ' '.join(map(str, nlist))



#remove spaces

lines = [line.replace(' ', '') for line in listToStr1]

with open('result.txt', 'w') as f:
    f.writelines(lines) 


