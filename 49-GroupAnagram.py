# Done

import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for str in strs:
            s = tuple(sorted(str))
            d[s].append(str)
        return list(d.values())

soln = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]
print(soln.groupAnagrams(strs))