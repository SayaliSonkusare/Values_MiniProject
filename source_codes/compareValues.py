#compare value list with the contents of file
data=[]
data1=[]
with open('valueNew.txt','r') as file:
    for line in file:
        data.append(line) 

with open('result.txt','r') as f:
    for line in f:
        if line in data:
            data1.append(line) 
        else:
            continue

listToStr = ' '.join(map(str, data1))
with open('finalResult.txt','w') as file:
    file.write(listToStr)

#display top 10 values in the file
word =[]
wordCount =[]
with open('finalResult.txt', 'r') as fp:
    for line in fp:
        word.extend(line.split())

from collections import Counter
counts = Counter(word)
top10 = counts.most_common(10)
wordCount.append(top10)
print(top10)
toStr = ' '.join(map(str, wordCount))
with open('topTen.txt', 'w') as op:
    op.write(toStr)