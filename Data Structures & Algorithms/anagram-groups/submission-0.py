class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans_map = {} # {key: [str]}

        for w in strs:
            key = "".join(sorted(w))

            if key not in ans_map:
                ans_map[key] = []

            ans_map[key].append(w)

        return list(ans_map.values())

"""
hash map:
- define a map variable -> ans_map = {key: [str]}
- for every entry in strs, define a sorted "key"
variable of the entry
- if key not in ans_map, create an entry for it in
the map with an empty array
- since we are checking for the sorted strs entry in
the map, anyone that matches is an anagram of that key
- append the current strs entry to its sorted key list

"""