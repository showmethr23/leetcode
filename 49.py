class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Solution 1
        # Sorting and append into the dictionary

        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        
        return list(anagrams.values())

        # Solution 2


