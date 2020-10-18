import csv
with open('emp.csv', 'w', newline='') as f:
    w = csv.writer(f)
    lstHeaders = ['EmpNum', 'EmpName', 'EmpSal', 'EmpAddress']
    w.writerow(lstHeaders)
    # Inserting data
    w.writerow(['1', 'Kumar', '10000', 'Hyderabad'])
    w.writerow(['2', 'Sai', '12000', 'Hyderabad'])
    w.writerow(['3', 'Rajesh', '13000', 'Bangalore'])
    w.writerow(['4', 'Sahasra', '20000', 'Chennai'])
    w.writerow(['5', 'Anwitha', '25000', 'Delhi'])

print('Data insertion completed')

