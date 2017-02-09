from lxml import html
import requests
import json
import numpy as np

#page = requests.get('http://docs.house.gov/floor/Download.aspx?file=/billsthisweek/20160905/20160905.xml')
#tree = html.fromstring(page.content)

#votes = tree.xpath('/floor-items')
#for x in votes:
#    print(x.descendant)

x = [[1, 2, 3, 4],
     [2, 3, 4, 5],
     [3, 4, 5, 6],
     [7, 8, 9, 10]]

with open('output.json', 'w') as outfile:
    for row in x:
        json.dump(row, outfile)

#For Each Week
#[[date, bill, Legislation Number, Link],
# [date, bill, Legislation Number, Link],
# .
# .
# .
# [date, bill, Legislation Number, Link]]

