import firebase_admin
import csv
from firebase_admin import firestore
from firebase_admin import credentials

cred = credentials.Certificate('.\\aipl-f2835-firebase-adminsdk-f7rcg-a9731ac613.json')
firebase_admin.initialize_app(cred)
db = firestore.client()


def getField(fieldName, dictName):
    if fieldName in dictName:
        return dictName[fieldName]
    else:
        return "-"


tasks_database = db.collection("tasks").get()
final = []
for i in tasks_database:
    data = []
    task = i.to_dict()
    data.append(getField("addedOn", task))
    data.append(getField("title", task))
    data.append(getField("customerName", task))
    data.append(getField("customerNumber", task))
    data.append(getField("customerAddress", task))
    data.append(getField("description", task))
    data.append(getField("type", task))
    data.append(getField("startedAt", task))
    data.append(getField("completedOn", task))
    data.append(getField("status", task))
    data.append(getField("adminId", task))
    data.append(getField("assignedTo", task))
    data.append(getField("deviceName", task))
    data.append(getField("deviceModel", task))
    data.append(getField("time", task))
    final.append(data)

fileName = "tasks.csv"

with open(fileName, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    columns = ["Added on", "Task title", "Customer name", "Customer Number", "Customer Address", "Task description",
               "Task type", "Start time", "End time", "Task status", "Assigned by", "Assigned to", "Device Name",
               "Device model", "Task time"]
    csvwriter.writerow(columns)

    for i in final:
        csvwriter.writerow(i)
