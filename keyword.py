import re
# D:\learnpython\test.cpp

from os import replace


path=input("the path to the file: ")
way=input("grade: ")
file=open(path)
keyword=('auto','break','case','char','const','continue','default','do','double','else','enum','extern','float','for','goto','if','int','long','register','return','short','signed','sizeof','static','struct','switch','typedef','union','unsigned','void','volatile','while')
sum=0

for line in file.readlines():
    line=re.split(r'[\s\,\;\:\(\)\{\}]+',line)
    for word in keyword:
        if word in line:
            sum+=1

print(sum)
# for line in file.readline():
#     for word in line:
#         if word in keyword



file .close()