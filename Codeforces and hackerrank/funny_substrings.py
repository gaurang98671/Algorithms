for _ in range(int(input())):
    count = 0
    declare = []
    assign = []
    variables = {}
    n = int(input())
    last= ''
    #Taking inputs
    for i in range(n):
        x = input()
        if ":=" in x:
            declare.append(x.split(" := "))
            if i == n-1:
                last = x.split(' := ')
        else:
            assign.append(x.split(" = "))

    #Dclaring and storing all variables
    if last is not None:
       for i in declare:
           variables[i[0]] = i[1]

           # Assigning new values to variables
       for i in assign:
           addend1, addend2 = i[1].split(" + ")
           sum = i[0]
           addend1_value = variables[addend1]
           addend2_value = variables[addend2]
           variables[sum] = addend1_value + addend2_value

       if len(assign) != 0:
           final = variables[assign[-1][0]]
           if len(final) >= 4:
               for i in range(len(final) - 3):
                   if final[i:i + 4] == 'haha':
                       count += 1
    else:
       final  = last[1]
       if len(final) >= 4:
           for i in range(len(final) - 3):
               if final[i:i + 4] == 'haha':
                   count += 1

    print(count)


