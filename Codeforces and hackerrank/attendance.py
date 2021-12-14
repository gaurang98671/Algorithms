import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import calendar
import csv

"""a = {'j88bfH5A9UgCRkMULzO5t3iuJJS206-10-21': {'logged': '06/10/21 02:55:24', 'logout_time': '06/10/21 11:13:27',
                                              'userID': 'j88bfH5A9UgCRkMULzO5t3iuJJS2'},
     'j88bfH5A9UgCRkMULzO5t3iuJJS207-10-21': {'userID': 'j88bfH5A9UgCRkMULzO5t3iuJJS2', 'logged': '07/10/21 05:31:57',
                                              'logout_time': '07/10/21 05:44:31'},
     'j88bfH5A9UgCRkMULzO5t3iuJJS227-09-21': {'logged': '27/09/21 11:44:03', 'userID': 'j88bfH5A9UgCRkMULzO5t3iuJJS2'},
     'j88bfH5A9UgCRkMULzO5t3iuJJS228-09-21': {'logged': '28/09/21 02:00:50', 'userID': 'j88bfH5A9UgCRkMULzO5t3iuJJS2'},
     'j88bfH5A9UgCRkMULzO5t3iuJJS229-09-21': {'logged': '29/09/21 05:45:33', 'userID': 'j88bfH5A9UgCRkMULzO5t3iuJJS2'},
     'j88bfH5A9UgCRkMULzO5t3iuJJS230-09-21': {'logout_time': '30/09/21 02:44:55',
                                              'userID': 'j88bfH5A9UgCRkMULzO5t3iuJJS2', 'logged': '30/09/21 02:41:39'},
     'ls517hrR2dZxCImSDEYLRbRXZBi207-10-21': {'logged': '07/10/21 05:56:25', 'userID': 'ls517hrR2dZxCImSDEYLRbRXZBi2'}}

b = {'Z1nLFMwzuGbF6HWtwJNXNA5CWzu225-09-21': {'userID': 'Z1nLFMwzuGbF6HWtwJNXNA5CWzu2', 'date': '25/09/21'},
     'Z1nLFMwzuGbF6HWtwJNXNA5CWzu227-09-21': {'userID': 'Z1nLFMwzuGbF6HWtwJNXNA5CWzu2', 'date': '27/09/21'},
     'j88bfH5A9UgCRkMULzO5t3iuJJS229-09-21': {'date': '29/09/21', 'userID': 'j88bfH5A9UgCRkMULzO5t3iuJJS2'},
     'j88bfH5A9UgCRkMULzO5t3iuJJS230-09-21': {'date': '30/09/21', 'userID': 'j88bfH5A9UgCRkMULzO5t3iuJJS2'}}
"""
y = 2021
m = 11

# Use the application default credentials
cred = credentials.Certificate('.\\aipl-f2835-firebase-adminsdk-f7rcg-a9731ac613.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# Getting days
num_days = calendar.monthrange(y, m)[1]
days = []
for day in range(1, num_days + 1):
    if day < 10:
        d = "0" + str(day)
    else:
        d = str(day)

    if m < 10:
        new_m = "0" + str(m)
    else:
        new_m = str(m)
    date = d + "-" + new_m + "-" + str(y)[-2:]
    days.append(date)

#Get tasks
tasks_database = db.collection("tasks").get()

# Get all emps
employee_database = db.collection("employee").get()

final = []
logs = {}
leaves = {}

# Get logs and store in dict
log_database = db.collection("log").get()
for i in log_database:
  logs[i.id] = i.to_dict()
print(logs)

#Get leaves and store them in dict
leaves_database = db.collection("leaves").get()
for i in leaves_database:
  leaves[i.id] = i.to_dict()

# For each employee store name, id and log in list
for employee in employee_database:


    data = {}
    e = employee.to_dict()
    id = employee.id
    data["name"] = e["name"]
    data["id"] = id
    data["attendance"] = []
    for d in days:

        new_date = [d]
        logId = employee.id + str(d)

        
        if logId in leaves:
            print("dd")
            new_date.append("leave")
        elif logId in logs:
            new_date.append(logs[logId]["logged"])
            if "logout_time" in logs[logId]:
                new_date.append(logs[logId]["logout_time"])
            else:
                new_date.append("-")
        else:
            new_date.append("-")
        data["attendance"].append(new_date)
    final.append(data)

#Add into csv
flag = True
file_name = f"{str(m)}-{str(y)}-data.csv"
with open(file_name, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    row_names = ["Id   ", "Names   "]
    data = []
    for i in final:
        new_lis = [i['id'], i['name']]
        for j in i['attendance']:
            if flag:
                row_names.append(j[0] + "      ")
            if len(j) == 3:
                new_lis.append(j[1] + " to " + j[2])
            else:
                new_lis.append(j[1])
        data.append(new_lis)
        flag = False

    csvwriter.writerow(row_names)
    for i in data:
        csvwriter.writerow(i)
