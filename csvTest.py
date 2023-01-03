import csv
import re

global highScores
highScores = {}

global scoreOrder
scoreOrder = []

global scoreLblList 
scoreLblList = []


def csvImport2Label():

    with open('scores.csv','r')as file:
        filecontent=csv.reader(file)
        for i in filecontent:
            highScores.update({(i[0]) : (i[1])})
            scoreOrder.append(i[1])

    scoreOrder.sort()
    scoreOrder.reverse()
   

    def get_key(val):
        for key, value in highScores.items():
            if val == value:
                x = (key, value)
                return x

    for i in range(len(highScores)):
        result = get_key(scoreOrder[i])
        scoreLblList.append(result)

   
    for i in range(5):
        highScorer1to5 = str(scoreLblList[i])
        highScorer1to5Formatted = re.sub("[(',)]", '', highScorer1to5)
        print(highScorer1to5Formatted)


csvImport2Label()

