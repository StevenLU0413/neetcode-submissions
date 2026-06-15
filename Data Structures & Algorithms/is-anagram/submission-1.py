class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s = {}
        dict_t = {}
        for ch_s in s:
            dict_s[ch_s] = dict_s.get(ch_s, 0) + 1
        for ch_t in t:
            dict_t[ch_t] = dict_t.get(ch_t, 0) + 1
        return dict_t == dict_s