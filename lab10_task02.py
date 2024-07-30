import csv

with open('information.csv','w') as csvfile:
    fieldnames=['name','nationality','gender','age','note']
    writer=csv.DictWriter(csvfile , fieldnames=fieldnames , delimiter='\t' , quotechar='|')

    writer.writeheader()
    writer.writerow({'name':'Imran Khan','nationality':'Pakistani','gender':'Male','age':'72.3','note':'legend'})
    writer.writerow({'name':'Baber Azam','nationality':'Pakistani','gender':'Male','age':'72.3','note':'G.O.A.T'})
