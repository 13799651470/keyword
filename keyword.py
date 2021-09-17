import re
# D:\learnpython\test.cpp

from os import replace


path=input("the path to the file: ")
way=int(input("grade: "))
file=open(path)
keyword=('auto','break','case','char','const','continue','default','do','double','else','enum','extern','float','for','goto','if','int','long','register','return','short','signed','sizeof','static','struct','switch','typedef','union','unsigned','void','volatile','while')
totalnum=0
switchnum=0
casenum=0
ifelsenum=0
ifelseifelsenum=0
for line in file.readlines():
    line=re.split(r'[\s\,\;\:\(\)\{\}]+',line)
    for word in keyword:
        if word in line:
            totalnum+=1
            if word=='switch':
                switchnum+=1
            if word=='case':
                casenum+=1

if way>=1 and way<=5:
    if 1 <=way:
        print('total num: ',totalnum)
    if 2<=way:
        print('switch num: ',switchnum)
    if 3<=way:
        print('case num: ',casenum)
    if 4<=way:
        print('if-else num: ',ifelsenum)
    if 5<=way:
        print('if-elseif-else num: ',ifelseifelsenum)
else:
    print('error!')




# for line in file.readline():
#     for word in line:
#         if word in keyword



file .close()