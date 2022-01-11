import pandas as pd
import copy
import numpy as np
import sys

# path to open files class
pathopen = "D:\Python\Excercise\Assesment2\Data Files"
path1 = pathopen + "\class1.txt"
path2 = pathopen + "\class2.txt"
path3 = pathopen + "\class3.txt"
path4 = pathopen + "\class4.txt"
path5 = pathopen + "\class5.txt"
path6 = pathopen + "\class6.txt"
path7 = pathopen + "\class7.txt"
path8 = pathopen + "\class8.txt"

classname = input('Please input class name:')

fileclass = {'class1': path1, 'class2': path2, 'class3': path3, 'class4': path4, 'class5': path5,
             'class6': path6, 'class7': path7, 'class8': path8}
listclass = ['class1', 'class2', 'class3', 'class4', 'class5', 'class6', 'class7', 'class8']

# Task1 - read file
try:
    if classname in listclass:
        for i in fileclass.keys():
            if i == classname:
                df = pd.read_fwf(fileclass.get(i))
                print('Successfully opened:', i)
                readfile = fileclass[i]

    else:
        raise Exception
except:
    print('There is no file', classname, 'exist, please input again!!')
    sys.exit()

# Task2

with open(readfile) as task2:
    lines = task2.readlines()
    task2.seek(0)
    pointpass = []  # save point pass
    pointfail = []  # save point fail
    listpass = []  # append lines pass to list for task 3
    for i in lines:
        convertlist = i.split(',')
        if convertlist[0][0] == 'N' and len(convertlist[0]) == 9 and convertlist[0][1:].isdigit() and len(
                convertlist) == 26:
            pointpass.append(1)
            listpass.append(i)
        if convertlist[0][0] != 'N' or len(convertlist[0]) != 9 or not convertlist[0][1:].isdigit() or len(
                convertlist) != 26:
            print('------ Error detected', convertlist[0], '------')
            if convertlist[0][0] != 'N':
                pointfail.append(1)
                print('Not the first N character', convertlist)
            elif len(convertlist[0]) != 9:
                pointfail.append(1)
                print('Registration number is not enough 9 characters', convertlist)
            elif not convertlist[0][1:].isdigit():
                pointfail.append(1)
                print('8 numbers after N are not in the correct format', convertlist)
            elif len(convertlist) != 26:
                pointfail.append(1)
                print('Not correct 26 values', convertlist)
    print('--Total valid lines of data:', sum(pointpass))
    print('--Total invalid lines of data:', sum(pointfail))

# Task3 - mark for student
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
answer_key = answer_key.split(',')
answer_key = np.array(answer_key)
sumpoint = []
for i in listpass:
    eachpoint = []
    listtask3 = i.split(',')
    listtask3[25] = listtask3[25].strip()  # remove \n at the end
    listtask3 = np.array(listtask3[1:])
    for j, k in zip(answer_key, listtask3):  # loop parallel 2 array co compare answer
        if k == j:
            eachpoint.append(4)
        if k == '':
            eachpoint.append(0)
        if k != j and k != '':
            eachpoint.append(-1)
    sumpoint.append(sum(eachpoint))  # sum point of student
sumpoint = np.array(sumpoint)  # present point of all student in a array, use fore task 4
sumpointsort = np.sort(sumpoint)
mean = np.mean(sumpointsort)
median = np.median(sumpointsort)

print('Mean (average) score:', mean)
print('Highest score:', sumpointsort.max())
print('Lowest score:', sumpointsort.min())
print('Range of scores:', sumpointsort.max() - sumpointsort.min())
print('Median score:', median)

# Task 4
pathsave = 'D:\Python\Excercise\Assesment2\Data Files\Test Output'
path11 = pathsave + '\class1_grades.txt'
path12 = pathsave + '\class2_grades.txt'
path13 = pathsave + '\class3_grades.txt'
path14 = pathsave + '\class4_grades.txt'
path15 = pathsave + '\class5_grades.txt'
path16 = pathsave + '\class6_grades.txt'
path17 = pathsave + '\class7_grades.txt'
path18 = pathsave + '\class8_grades.txt'
fileclass2 = {'class1': path11, 'class2': path12, 'class3': path13, 'class4': path14, 'class5': path15,
              'class6': path16, 'class7': path17, 'class8': path18}

if classname in listclass:
    for i in fileclass2.keys():
        if i == classname:
            with open(fileclass2.get(i), 'w') as writefile:
                for k, j in zip(listpass, sumpoint):
                    writefile.write(("{}\n".format(k[:9] + ',' + str(j))))
