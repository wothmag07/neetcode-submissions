class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        out = ''
        sizes = []
        for i in strs:
            out += str(len(i)) + "$" + i
        return out


    def decode(self, s: str) -> List[str]:
        out = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            le = int(s[i:j])
            i = j + 1
            j = i + le
            out.append(s[i:j])
            i = j
        return out

