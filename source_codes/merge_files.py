# importing the library
#from itertools import count
import os

# giving directory name
dirname = 'E:\\informatica_project'


# giving file extension
ext = ('.txt')
data = []
# iterating over all files
for files in os.listdir(dirname):
    if files.endswith(ext):
        with open(files) as inf:
            data.append(inf.read())
        data += '\n'
    else:
        continue

listToStr = ' '.join(map(str, data))
lower = listToStr.lower()
with open ('target.txt', 'w') as fp:
	fp.write(lower)

   
