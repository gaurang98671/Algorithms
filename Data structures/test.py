import uuid
import random

cls = [1, 2, 3]
domain = ["ML", "Web", "Mobile", "Game", "IOT"]
database = []
groups = []
n = 77
for i in range(n):
    id = str(uuid.uuid4())[:7]
    dom = random.choice(domain)
    c = random.choice(cls)
    new_student = (id, c, dom)
    database.append(new_student)



# Need to create grp of 3
# Need all class in grp
# Need to have similar domain

# making grps

database.sort(key=lambda a: a[1])

for i in database:
    print(i)


while len(database) >= 3:
    first_member = database.pop(0)
    score = 0
    member = -1
    req_domain = first_member[2]
    if first_member[1] == 1:
        req_class = 2
    elif first_member[1] == 2:
        req_class = 3
    else:
        req_class = -1

    for i in range(len(database)):
        curr_score = 0
        if database[i][1] == req_class or req_class == -1:
            curr_score += 2
        if database[i][2] == req_domain:
            curr_score += 1
        if curr_score > score:
            score = curr_score
            member = i

    if database[member][1]!= req_class:
        second_member = database.pop(-1)
    else:
        second_member = database.pop(member)

    score = 0
    member = -1
    req_domain = second_member[2]
    if second_member[1] == 1:
        req_class = 2
    elif second_member[1] == 2:
        req_class = 3
    else:
        req_class = -1

    for i in range(len(database)):
        curr_score = 0
        if database[i][1] == req_class or req_class == -1:
            curr_score += 2
        if database[i][2] == req_domain:
            curr_score += 1
        if curr_score > score:
            score = curr_score
            member = i
    third_member = database.pop(member)
    groups.append([len(groups), first_member,second_member,third_member])

print("Grps")
for i in groups:
    print(i)
print(database)
