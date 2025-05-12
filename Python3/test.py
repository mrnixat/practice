

# o(n log n) | Worst case : o(n^2)
def findDisappearedNumbers(nums):
    nums.sort()
    missing = []
    counter = nums[0]

    for i in nums:
        if i != counter:
            while i != counter:
                missing.append(counter)
                counter+=1
        counter+=1
            
    return missing

""" o(n)
def findDisappearedNumbers(nums):
    if not nums:
        return []
    num_set = set(nums)
    min_num = min(nums)
    max_num = max(nums)
    missing = []
    for i in range(min_num, max_num + 1):
        if i not in num_set:
            missing.append(i)
    return missing
"""


print(findDisappearedNumbers([6,7,8,9,10,11,13,14,17,19,21,22,33]))
print(findDisappearedNumbers([1,10]))

print(findDisappearedNumbers([4,3,2,5,6,9]))


