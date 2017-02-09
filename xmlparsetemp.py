import xml.etree.ElementTree as ET
import requests

web_one ='http://docs.house.gov/floor/Download.aspx?file=/billsthisweek/'
web_two = '.xml'
def get_data(dateString):
    page = requests.get(web_one+dateString+"/"+dateString+web_two)
    root = ET.fromstring(page.content)
    #root = tree.getroot()
    dataset = []
    for child in root.getchildren():
        if child.tag == "category":
            for c in child.getchildren()[0].getchildren(): #c is every floor-item
                temp = []
                kid_c = c.getchildren()
                temp.append(c.attrib['add-date']) #add-data
                for e in kid_c:
                    if (e.tag == "legis-num"):
                        temp.append(e.text)
                    #adding extra if so legis-num done first
                    elif (e.tag == "floor-text"):
                        temp.append(e.text)
                    elif (e.tag == "files"):
                        filelist = []
                        for f in e.getchildren():
                            filelist.append(f.attrib['doc-url'])
                        temp.append(filelist)
                dataset.append(temp)
    f = open((dateString+".csv"), 'w')
    for row in dataset:
        f.write(str(row)[1:])
        f.write(";\n")
    f.close()
    return dataset

strings = ["20160905", "20160912", "20160919"]
for date in strings:
    get_data(date)


"""<script>
    for(i=0; i<45; i++){
    var table = document.getElementById("myTable");
    var row = table.insertRow(-1);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    cell1.innerHTML = "<a href=\"http://www.google.com\">BILLSONBILLS</a>";
    cell2.innerHTML = "NEW CELL2";
    cell3.innerHTML = "TEMP3";
    }
    </script>"""
