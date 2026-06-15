class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = self.clean_sentence(s)
        s_len = len(s)
        if s_len == 0:
            return True
        counter = 1
        pointer = s[s_len - counter]

        for c in s:
            if c != pointer:
                return False
            counter += 1
            pointer = s[s_len - counter]
        return True
    
    def clean_sentence(self, s: str) -> str:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        return s.lower()
        