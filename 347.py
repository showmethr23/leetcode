Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order

Example 1:
    Input:  nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

Example 2:
    Input:  nums = [1], k = 1
    Output: [1]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Solution 1
        # using the bucket sort

        count = {} # make a hash map for counting numbers 
        freq = [[] for i in range(len(nums) + 1)] # this is for number of counts 
                                                  # good thing to know is that this only requires the length of input nums

        # add input numbers in the hash map
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # add what counting numbers in the hash map (count)
        for n, c in count.items():
            freq[c].append(n)

        ans = []

        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                ans.append(n)

                if len(ans) == k:
                    return ans
