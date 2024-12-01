list1 = []
list2 = []
sim_score = 0

with open("dayone.txt") as text:
    for row in text:
        rows = row.split()
        if len(rows) == 2:
            list1.append(int(rows[0]))
            list2.append(int(rows[1]))

list1_nums = set(list1)

for i in range(len(list1)):
    search = list1[i]
    search_count = list2.count(search)
    value = search * search_count
    sim_score += value

print(sim_score)