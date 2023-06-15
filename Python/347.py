class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Solution 1
        # using the bucket sort

        count = {} # make a hash map for counting numbers 
        freq = [[] for i in range(len(nums) + 1)]   # this is for number of counts 
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
