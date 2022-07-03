inputs = []

while True:
    i = input()
    if i != "/":
        inputs.append(int(i))
    else:
        break

last = inputs[0]
count = 0
for i in inputs[1:]:
    if i > last:
        count += 1
    last = i

print(count)