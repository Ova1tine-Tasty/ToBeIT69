def sj(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

print(sj([5,1,4,2,3]))
print(sj([10,-2,7,0]))
print(sj([3,3,1]))