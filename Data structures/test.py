#array ek to consecutive 01 honge ya fir consecutive 10 so apn dono ke liye count nikalenge aur usme se minimum lenge
first_count = 0
second_count = 0
arr = [1,1,0,1,1,1]
second_arr = arr.copy()
for i in range(0,len(arr)-1, 2):
    #check for 10 in arr
    #check for 01 in second_arr
    if not (arr[i] == 1 and arr[i+1] == 0):
        if arr[i] != 1:
            arr[i] = 1
            first_count += 1
        if arr[i+1] != 0:
            arr[i+1] = 0
            first_count += 1
    if not (second_arr[i] == 0 and second_arr[i+1] == 1):
        if second_arr[i]!= 0:
            second_arr[i] = 0
            second_count += 1
        if second_arr[i+1]!=1:
            second_arr[i+1] = 1
            second_count += 1

if len(arr)%2!=0:
    if arr[-1] != 1:
        first_count += 1
    if second_arr[-1] != 0:
        second_count += 1
print(first_count, second_count) #issme se minimum lenge