def summ(nums):
    return sum(n for n in nums if n % 2 ==0)
print(summ([1,2,3,4,5,6]))
print(summ([7,9,11]))
print(summ([7,9,10,-2,8]))
