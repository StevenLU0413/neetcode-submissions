class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = []

        for s in strs:
            encoded_string.append(str(len(s)))
            encoded_string.append('#')
            encoded_string.append(s)
    
        return ''.join(encoded_string)

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            s_len = int(s[i:j])
            start = j + 1
            end = start + s_len

            decoded_string.append(s[start:end])
            i = end

        return decoded_string
