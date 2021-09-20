import re

from os import replace
# D:\learnpython\test.cpp

def output(way):    # 进行输出
    if 1 <= way <= 4:
        if 1 <= way:
            print('total num: ', totalnum)
        if 2 <= way:
            print("switch num: ", switchnum)
            print('case num:', end='')
            for x in casenums:
                print(' ', x, end='')
        if 3 <= way:
            print('\nif-else num: ', ifelsenum)
        if 4 <= way:
            print('if-elseif-else num: ', ifelseifelsenum)
    else:
        print('error!')


def row_totalnum(line):    #对每行关键词进行计数
    num = 0
    for word in line:
        if word in keyword:
            num += 1
    return num


def row_switchnum(line):    #对每行switch进行计数
    num = 0
    for word in line:
        if word == 'switch':
            num += 1
    return num


def row_casenum(line):    #对case进行计数
    num = 0
    for word in line:
        if word == 'case':
            num += 1
    return num


path = input("the path to the file: ")  # D:\learnpython\test.cpp
way = int(input("grade: "))
file = open(path)
keyword = (
    'auto', 'break', 'case', 'char',
    'const', 'continue', 'default', 'do',
    'double', 'else', 'enum', 'extern',
    'float','for', 'goto', 'if',
    'int', 'long','register', 'return',
    'short', 'signed', 'sizeof', 'static',
    'struct', 'switch', 'typedef', 'union',
    'unsigned', 'void', 'volatile', 'while')    #将关键词放入tuple集合中
totalnum = 0             #关键词总数
switchnum = 0            #Switch总数
casenums = [0]           #将每次Switch下的case总数放入list集合中
casenum = 0              #每次Switch下的case数
ifelsenum = 0            #ifelse总数
ifelseifelsenum = 0      #ifelseifelse总数
flag = 1                 #如果是ifelse语句则为1,ifelseifelse语句为0
y = 1                    #用来遍历每行中的字符串
for line in file.readlines():       #遍历file中的每行
    line = re.split(r'[\s\,\;\:\(\)\{\}]+', line)       #运用正则表达式将每行中的标点符号换成空格，并且将一整行字符串切分为list
    totalnum += row_totalnum(line)                      #累加每行关键词的数量
    if way >= 2:
        switchnum += row_switchnum(line)                #累加每行Switch的数量
        if row_switchnum(line) != 0:  # 遇到Switch,将之前的casenum添加到casenums集合中,然后将casenum清0
            if casenum != 0:
                if casenums[-1] == 0:
                    casenums.pop(-1)
                casenums.append(casenum)
                casenum = 0
            else:
                pass
        casenum += row_casenum(line)
        if way >= 3:
            for word in line:
                elseifflag = 0
                if word == 'if':
                    flag = 1
                    for x in line:
                        if x == 'else':
                            flag = 0
                            elseifflag = 1
                            break
                if elseifflag == 1:
                    continue
                if word == 'elif':
                    flag = 0
                    continue
                if word == 'else':
                    for y in line:
                        if y == 'if':
                            break
                    if y == 'if':
                        continue
                    if flag == 1:
                        ifelsenum += 1
                    else:
                        ifelseifelsenum += 1

if casenum != 0:        #将最后一次Switch中的case数加到casenums集合中
    casenums.append(casenum)

output(way)

file.close()
