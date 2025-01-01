nums=[0,3,2,5,4,6,1,1]
sorted_nums = sorted(set(nums))
removed = 0

for i in sorted_nums:
    print("original:", sorted_nums)
    removed = i
    sorted_nums.remove(i)

    print("This is the list now:", sorted_nums)
    print("and this is the removed now:", removed)