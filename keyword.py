import re
# D:\learnpython\test.cpp

from os import replace
def output(way):
    if way>=1 and way<=5:
        if 1 <=way:
            print('total num: ',totalnum)
        if 2<=way:
            print('switch num: ',switchnum)
        if 3<=way:
            print('case num:',end='')
            for x in casenums:
                print(' ',x,end='')
            # print('\n')
        if 4<=way:
            print('\nif-else num: ',ifelsenum)
        if 5<=way:
            print('if-elseif-else num: ',ifelseifelsenum)
    else:
        print('error!')

def row_totalnum(line):
    num=0
    for word in line:
        if word in keyword:
            num+=1
    return num

def row_switchnum(line):
    num=0
    for word in line:
        if word=='switch':
            num+=1
    return num  

def row_casenum(line):
    num=0
    for word in line:
        if word =='case':
            num+=1
    return num

path=input("the path to the file: ")
way=int(input("grade: "))
file=open(path)
keyword=('auto','break','case','char','const','continue','default','do','double','else','enum','extern','float','for','goto','if','int','long','register','return','short','signed','sizeof','static','struct','switch','typedef','union','unsigned','void','volatile','while')
totalnum=0
switchnum=0
casenums=[0]
casenum=0
ifelsenum=0
ifelseifelsenum=0
for line in file.readlines():
    line=re.split(r'[\s\,\;\:\(\)\{\}]+',line)
    totalnum+=row_totalnum(line)
    if(way>=2):
        switchnum+=row_switchnum(line)
        if(way>=3):
            if row_switchnum(line)!=0:
                if casenum!=0:
                    if casenums[-1]==0:
                        casenums.pop(-1)
                    casenums.append(casenum)
                    casenum=0
                else:
                    pass
            casenum+=row_casenum(line)



if casenum!=0:
    casenums.append(casenum)



    # for word in keyword:
    #     if word in line:
    #         totalnum+=1
    #         if word=='switch':
    #             switchnum+=1
    #         if word=='case':
    #             casenum+=1

output(way)
# if way>=1 and way<=5:
#     if 1 <=way:
#         print('total num: ',totalnum)
#     if 2<=way:
#         print('switch num: ',switchnum)
#     if 3<=way:
#         print('case num: ',casenum)
#     if 4<=way:
#         print('if-else num: ',ifelsenum)
#     if 5<=way:
#         print('if-elseif-else num: ',ifelseifelsenum)
# else:
#     print('error!')




# for line in file.readline():
#     for word in line:
#         if word in keyword



file .close()