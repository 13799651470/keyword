import re

from os import replace


def output(way):
    if 1 <= way <= 5:
        if 1 <= way:
            print('total num: ', totalnum)
        if 2 <= way:
            print("switch num: ", switchnum)
        if 3 <= way:
            print('case num:', end='')
            for x in casenums:
                print(' ', x, end='')
            # print('\n')
        if 4 <= way:
            print('\nif-else num: ', ifelsenum)
        if 5 <= way:
            print('if-elseif-else num: ', ifelseifelsenum)
    else:
        print('error!')


def row_totalnum(line):
    num = 0
    for word in line:
        if word in keyword:
            num += 1
    return num


def row_switchnum(line):
    num = 0
    for word in line:
        if word == 'switch':
            num += 1
    return num


def row_casenum(line):
    num = 0
    for word in line:
        if word == 'case':
            num += 1
    return num


path = input("the path to the file: ")  # D:\learnpython\test.cpp
way = int(input("grade: "))
file = open(path)
keyword = (
    'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double', 'else', 'enum', 'extern', 'float',
    'for', 'goto', 'if', 'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static', 'struct', 'switch',
    'typedef', 'union', 'unsigned', 'void', 'volatile', 'while')
totalnum = 0
switchnum = 0
casenums = [0]
casenum = 0
ifelsenum = 0
ifelseifelsenum = 0
flag = 1
y = 1
for line in file.readlines():
    line = re.split(r'[\s\,\;\:\(\)\{\}]+', line)
    totalnum += row_totalnum(line)
    if way >= 2:
        switchnum += row_switchnum(line)
        if way >= 3:
            if row_switchnum(line) != 0:
                if casenum != 0:
                    if casenums[-1] == 0:
                        casenums.pop(-1)
                    casenums.append(casenum)
                    casenum = 0
                else:
                    pass
            casenum += row_casenum(line)
            if way >= 4:
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

if casenum != 0:
    casenums.append(casenum)

output(way)

file.close()
