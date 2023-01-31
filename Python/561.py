def arrayPairSum(self, nums: List[int]) -> int:
    # input:  nums = [1,4,3,2]
    # Output: 4

    # Input:  nums = [6,2,6,5,1,2]
    # Output: 9


    # Solution 1
    # Ascending Order
    
    sum = 0
    pair = []
    nums.sort()

    for i in nums:
        pair.append(i)
        if len(pair) == 2:
            sum += min(pair)
            pair = []
    
    return sum


    # Solution 2
    # Sum of Even indices

    sum = 0
    nums.sort()

    for i, num in enumerate(nums):
        if i % 2 == 0:
            sum += num
    
    return sum
