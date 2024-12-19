class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "empty"
        if strs == [""]:
            return "emtpy_string"
        full_string = ""
        for i in range(len(strs)):
            if i == len(strs) - 1:
                full_string+=strs[i]
                return full_string
            full_string+=strs[i] + ';'

    def decode(self, s: str) -> List[str]:
        if s == "empty":
            return []
        if s == "emtpy_string":
            return [""]
        return s.split(";")


# or neet code solved it this way (optimal solution):

class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res