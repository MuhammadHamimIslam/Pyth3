import csv

"reading data line by line"
with open('test_data.csv', 'r') as f1: 
    cont = csv.reader(f1)
    next(cont)
    #print(list(cont))
    for data in cont: 
        print(data)
    
"reading data as dictionary"
with open('test_data.csv', 'r') as f2:
    content = csv.DictReader(f2)
    #print(list(content))
    for data in content: 
        print(data)
        

"writing data"
try: 
    with open('test_data.csv', 'a') as f3:
        someData = ["clive, 39, clive290@email.com, cl290, Gulistan", "Paul, 27, paul33@email.com, pl33, Farmgate"]
        csv_writer = csv.writer(f3)
        csv_writer.writerows(someData)
except Exception as e:
    print(e)