
inputvalues = input("Enter all element values: ")
numbers1 = inputvalues.split()
for i in range(len(numbers1)):
  numbers1[i] = int(numbers1[i])
print("The original list: ", numbers1)

numbers2 = []

for j in range(len(numbers1)):
  numbers2.insert(j, numbers1.pop())

print("The new list: ", numbers2)