list1 = []
list2 = []
diff = 0

with open("dayone.txt") as text:
    for row in text: 
        rows = row.split()
        if len(rows) == 2:
            list1.append(int(rows[0]))
            list2.append(int(rows[1]))

sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

for i in range(len(sorted_list1)):
    diff += abs(sorted_list1[i] - sorted_list2[i])

print(diff)
