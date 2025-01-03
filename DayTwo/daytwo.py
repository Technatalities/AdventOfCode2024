from functools import reduce
safeone = 0
safetwo = 0

def dec(nums):
    diff_list = []
    seqd = lambda nums: bool(reduce(lambda i, j: j if i > j else 9999, nums) != 9999)
    if seqd:
        for x, y in zip(nums[0::], nums[1::]):
            diff_list.append(y-x)
        res = all(ele <= 3 and ele >= 1 for ele in diff_list)
        return res
    else: 
        return False

def inc(nums):
    diff_list = []
    seqi = lambda nums: bool(reduce(lambda i, j: j if i < j else 0, nums) != 0)
    if seqi:
        for x, y in zip(nums[0::], nums[1::]):
            diff_list.append(x-y)
        res = all(ele <= 3 and ele >= 1 for ele in diff_list)
        return res
    else:
        return False


def exclude(list, i):
    return list[:i] + list[i + 1 :]


# Part One
with open("daytwo.txt") as text:
    for row in text:
        nums = list(map(int, row.split()))  
        if dec(nums):
            safeone += 1
        elif inc(nums):
            safeone += 1

# Part Two
with open("daytwo.txt") as text:
    for row in text:
        nums = list(map(int, row.split()))
        for i in range(len(nums)):
            if dec(exclude(nums, i)):
                safetwo += 1
                break 
            elif inc(exclude(nums, i)):
                safetwo += 1
                break

print("Part One:", safeone)
print("Part Two:", safetwo)
