#Written by Shivam Parikh
#Wednesday, March 8th, 2017

import numpy as np
import csv
import matplotlib.pyplot as plt


def formDictPerYear(year):
    dict = {'100':0, '95':0, '90':0, '85':0, '80':0, 'together':0, 'total': 0, 'nonpart':0}
    file_name = "./bills/" + str(year) + "_bills.csv"
    with open(file_name, 'r', errors = 'ignore') as f:
        reader = csv.reader(f)
        dataset = list(reader)
    total = int(dataset[1][23])+int(dataset[1][24])

    for vote in dataset[2:]:
        try:
            if(int(vote[21]) == 0 or int(vote[22])==0):
                dict['total'] += 1
                dict['together'] += 1
                continue
            repYes = int(vote[9])/int(vote[21])
            demYes = int(vote[13])/int(vote[21])
            repNo = int(vote[10])/int(vote[22])
            demNo = int(vote[14])/int(vote[22])
            biPart = [repYes,demYes,repNo,demNo]
            totalYes = int(vote[21])/(int(vote[21])+int(vote[22]))
            totalNo = int(vote[22])/(int(vote[21])+int(vote[22]))
            if(testPercentage([totalYes, totalNo], 0.95)):
                dict['together'] += 1
            elif(testPercentage(biPart, 1)):
                dict['100'] += 1
            elif(testPercentage(biPart, 0.95)):
                dict['95'] += 1
            elif(testPercentage(biPart, 0.9)):
                dict['90'] += 1
            elif(testPercentage(biPart, 0.85)):
                dict['85'] += 1
            elif(testPercentage(biPart, 0.8)):
                dict['80'] += 1
            else:
                dict['nonpart'] += 1
            dict['total'] += 1
        except IndexError:
            continue
    return dict

def testPercentage(array, percentage):
    for each in array:
        if(each >= percentage):
            return True
    return False

def generateLine():
    dict = {}
    plt.axis([1989, 2018, 0, 100])
    for year in range(1990, 2018):
        temp = formDictPerYear(year)
        partisan = temp['together']/temp['total']
        bipartisan = (temp['100']+temp['95'])/temp['total']
        nonpart = (temp['nonpart']+temp['80']+temp['85']+temp['90'])/temp['total']
        dict[year] = (partisan, bipartisan, nonpart)
    for v in dict.values():
        print(sum(v))
    plt.plot(sorted(dict.keys()), [dict[x][0]*100 for x in sorted(dict.keys())],
             'k', c='g', label=">=95% Agreement in Congress")
    plt.plot(sorted(dict.keys()), [dict[x][1]*100 for x in sorted(dict.keys())],
             'k', c='r', label="Vote on a >=95% Party Line (Bi-Partisan)")
    plt.plot(sorted(dict.keys()), [dict[x][2]*100 for x in sorted(dict.keys())],
             'k', c='b', label="All Other Votes (Not Extreme Agreement or Disagreement)")
    plt.legend()
    plt.title("(Bi)Partisan Voting in the U.S. House from 1990-2017")
    plt.ylabel("Percentage of Total Votes in the House (0-100%)")
    plt.xlabel("Years (1990-2017)")
    plt.grid(b=True, which='minor', color='k')
    plt.show()
    return dict
