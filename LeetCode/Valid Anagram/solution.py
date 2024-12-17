class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = {}
        hashTwo = {}

        for c in s:
            if c not in hash:
                hash[c] = 0
            hash[c] += 1

        for c in t:
            if c not in hashTwo:
                hashTwo[c] = 0
            hashTwo[c] += 1

        return hash == hashTwo

        # return Counter(s) == Counter(t)