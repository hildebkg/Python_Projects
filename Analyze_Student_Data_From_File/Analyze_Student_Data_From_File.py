# this program uses data from a text file to calculate and output various pieces of information based on the data in the 
# text file. some information outputs to the screen and some outputs to a separate text file.

import math

text = open('data.txt','r')
results = open('results.txt','w')
Data = []
ID = ['ID']
quiz = ['quiz']
HW = ['HW']
project = ['project']
midterm = ['midterm']
final = ['final']
finalGrades = [' final']
letterGrades = ['letter']

for i in text:
    Data.append(i)

for i in range(1, len(Data)):
    Line = Data[i].split()
    ID.append(Line[0])
    quiz.append(float(Line[1]))
    HW.append(float(Line[2]))
    project.append(float(Line[3]))
    midterm.append(float(Line[4]))
    final.append(float(Line[5]))

# calculate final grade for every student
minAexamScore = 10000
numAs = 0
numBs = 0
numCs = 0
numDs = 0
numFs = 0

for i in range(1, len(ID)):
    finalGrade = []
    finalGrade = round((quiz[i] * 0.15) + (HW[i] * 0.20) + (project[i] * 0.25) + (midterm[i] * 0.20) + (final[i] * 0.20))
    finalGrades.append(finalGrade)

    # calculate letter grade for every student
    if (finalGrade >= 90):
        letterGrades.append('A')
        numAs = numAs + 1
    elif (finalGrade >= 80):
        letterGrades.append('B')
        numBs = numBs + 1
    elif (finalGrade >= 70):
        letterGrades.append('C')
        numCs = numCs + 1
    elif (finalGrade >= 60):
        letterGrades.append('D')
        numDs = numDs + 1
    else:
        letterGrades.append('F')
        numFs = numFs + 1
    # calculate lowest exam grade for those who got an A
    if (final[i] < minAexamScore) and (letterGrades[i] == 'A'):
        minAexamScore = final[i]
        studentID = ID[i]

# print ID, final grade, and letter grade to file
for i in range(len(ID)):
    results.write('{0}  {1}  {2} \n'.format(ID[i], finalGrades[i], letterGrades[i]))

# output percentage of students with A/ B overall
percentAsAndBs = 100 * ((numAs + numBs) / (len(ID) - 1))
print('The percentage of students who earned an A or B was {0:.2f}%. \n'.format(percentAsAndBs))

# output lowest exam score out of those who got an A/ B overall and their ID number
print('The lowest exam score for a student who got an A or B was {0} \n'.format(minAexamScore))
print("That ID number of that student was {0}. \n".format(studentID))

# output overall homework average for people who got a D/ F overall
sumHW = 0
for i in range(len(ID)):
    if ((letterGrades[i] == 'D') or (letterGrades[i] == 'F')):
        sumHW = sumHW + HW[i]
averageHW = sumHW / (numDs + numFs)
print('The overall homework average for students who received a D or F was {0:.2f}. \n'.format(averageHW))

# output standard deviation for overall homework average
variance1 = 0
for i in range(1, len(HW)):
    if ((letterGrades[i] == 'D') or (letterGrades[i] == 'F')):
        variance1 = variance1 + (HW[i] - averageHW)**2
variance2 = variance1 / (numDs + numFs - 1)
STD = math.sqrt(variance2)
print('The standard deviation for the overall homework average was {0:.2f}. \n'.format(STD))

# close all files
text.close()
results.close()
