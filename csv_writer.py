import csv
headers = ['Name', 'Mobile', 'Email']
data = [
    {'Name': 'Tom Jerry', 'Mobile': '1234567891', 'Email': 'tom@test.com'},
    {'Name': 'Vicky', 'Mobile': '9988776655', 'Email': 'vicky@test.com'},
    {'Name': 'Tropsal', 'Mobile': '7766554433', 'Email': 'troposal@test.com'},
    {'Name': 'Mahesh', 'Mobile': '7464646463', 'Email': 'mahesh@test.com'}
]
#open the csv file in write mode
with open('users.csv', mode='w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames = headers)
    #Header writing
    csv_writer.writeheader()
    csv_writer.writerows(data)