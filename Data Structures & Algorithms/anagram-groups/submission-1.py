from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        for str in strs:
            char_count = [0] * 26

            for char in str:
                index = ord(char) - ord("a")
                char_count[index] += 1

            group_signature = tuple(char_count)
            anagram_groups[group_signature].append(str)

        return list(anagram_groups.values())
