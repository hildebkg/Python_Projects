# Assignment title: HW 3p1
# File: HW_3p1_hildebkg
# Date: 29 January 2021
# By:   Katy Hildebrant
# Section: 008
# Team: 122
#
# ELECTRONIC SIGNATURE
# Katy Hildebrant

# The electronic signature above indicates the script submitted
# for evaluation is my individual work, and I have a general understanding
# of all aspects of its development and execution.
#
# BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# Student final grade calculator and analysis
# 

import math

HW = open('HW3p1.txt','r')
Results = open('CourseGrade.txt','w')

Data = []
ID = []
Quiz = []
HW_AVG = []
HW_AVG2 = []
Project = []
Midterm = []
Final = []
Final_2 = []
FinalGrades = ['Final grade']
AsExams = [1000]
AsAndBsFinalGrades = []
DsAndFsHWavg = []
AsIDs = [0]

numAs = 0
numBs = 0
numCs = 0
numDs = 0
numFs = 0

for i in HW:
    Data.append(i)

for i in range(len(Data)):
    Line = Data[i].split()
    ID.append(Line[0])
    Quiz.append(Line[1])
    HW_AVG.append(Line[2])
    HW_AVG2.append(Line[2])
    Project.append(Line[3])
    Midterm.append(Line[4])
    Final.append(Line[5])
    Final_2.append(Line[5])

for i in range(1, len(Quiz)):
    quizContribution = (float(Quiz[i])) * 0.15
    Quiz[i] = (quizContribution)

for i in range(1, len(HW_AVG)):
    HW_AVG_Contribution = (float(HW_AVG[i])) * 0.20
    # replace hw values with their contribution to the final grade
    HW_AVG[i] = HW_AVG_Contribution

for i in range(1, len(Project)):
    projectContribution = (float(Project[i])) * 0.25
    Project[i] = projectContribution

for i in range(1, len(Midterm)):
    midtermContribution = (float(Midterm[i])) * 0.20
    Midterm[i] = midtermContribution

for i in range(1, len(Final)):
    finalContribution = (float(Final[i])) * 0.20
    Final[i] = finalContribution

for i in range(1, len(ID)):
    finalGrade = round(Quiz[i] + HW_AVG[i] + Project[i] + Midterm[i] + Final[i])
    FinalGrades.append(finalGrade)

#create list right size for storing letter grades
LetterGrades = ['Letter grade']
for i in range(len(FinalGrades)):
    LetterGrades.append(i)
#
#
#

for i in range(1, len(FinalGrades)):
    if (FinalGrades[i] >= 90):
        LetterGrades[i] = 'A'
        AsExams.append(float(Final_2[i]))
        AsIDs.append(ID[i])
        AsAndBsFinalGrades.append(FinalGrades[i])
        numAs = numAs + 1
        
    elif (FinalGrades[i] >= 80):
        LetterGrades[i] = 'B'
        AsAndBsFinalGrades.append(FinalGrades[i])
        numBs = numBs + 1
        
    elif (FinalGrades[i] >= 70):
        LetterGrades[i] = 'C'
        numCs = numCs + 1
        
    elif (FinalGrades[i] >= 60):
        LetterGrades[i] = 'D'
        DsAndFsHWavg.append(HW_AVG2[i])
        numDs = numDs + 1
        
    else:
        LetterGrades[i] = 'F'
        DsAndFsHWavg.append(HW_AVG2[i])
        numFs = numFs + 1
#
#

for i in range(len(ID)):
    Results.write('{0}  {1}  {2} \n'.format(ID[i], FinalGrades[i], LetterGrades[i]))

#

#Task 2 Question 1
totalStudents = len(ID) - 1
percentAorB = 100 * ((numAs + numBs) / totalStudents)
print('The percentage of students with an A or B in the course was {0:.2f}%. \n'.format(percentAorB))
#
#

#Task 2 Question 2
lowestExamScoreWithA = 10000
for i in range(1, len(AsExams)):
    if (AsExams[i] < lowestExamScoreWithA):
        lowestExamScoreWithA = AsExams[i]
        studentIDnumber = AsIDs[i]
print('The lowest final exam score of those who got an A was {0}. \n'.format(lowestExamScoreWithA))
print('The ID of the person with that score was {0}. \n'.format(studentIDnumber))
#
#

#Task 2 Question 3
sumHW = 0
for i in range(1, len(HW_AVG2)):
    sumHW = sumHW + float(HW_AVG2[i])

DandFaverageHW = sumHW / (numFs + numDs)
print('The average overall homework for those who got a D or F was {0:.2f}. \n'.format(DandFaverageHW))

#Task 2 Question 4
variance1 = 0
for i in range(1, len(HW_AVG2)):
    variance1 = variance1 + (float(HW_AVG2[i]) - DandFaverageHW)**2
variance2 = variance1 / (len(HW_AVG2) - 2) 
STD = math.sqrt(variance2)
print('The standard deviation was {0:.2f}. \n'.format(STD))

HW.close()  
Results.close()
