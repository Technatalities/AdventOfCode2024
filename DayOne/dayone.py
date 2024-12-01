list1 = []
list2 = []
diff = 0
sim_score = 0

with open("dayone.txt") as text:
    for row in text: 
        rows = row.split()
        if len(rows) == 2:
            list1.append(int(rows[0]))
            list2.append(int(rows[1]))

sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

# For Difference Score
for i in range(len(sorted_list1)):
    diff += abs(sorted_list1[i] - sorted_list2[i])

# For Similarity Score
for i in range(len(list1)):
    search = list1[i]
    search_count = list2.count(search)
    value = search * search_count
    sim_score += value

print(diff)
print(sim_score)
