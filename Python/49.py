class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Solution 1
        # Sorting and append into the dictionary

        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        
        return list(anagrams.values())

        # Solution 2
        # using ascii code and hash map

        res = defaultdict(list)

        for string in strs:

            count = [0] * 26 # for alphabets

            for character in string:

                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)

        return res.values()


