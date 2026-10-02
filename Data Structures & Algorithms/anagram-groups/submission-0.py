class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # create list to hold the characters from a-z in the input
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26 # maps a-z
            for c in s:
                count[ord(c) - ord("a")] += 1 # map a to be zero and z to be 26
            res[tuple(count)].append(s)
        return list(res.values())
