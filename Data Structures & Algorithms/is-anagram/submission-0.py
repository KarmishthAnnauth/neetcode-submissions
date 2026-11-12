class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}

        for c in s:
            if not(c in hash1.keys()):
                hash1.update({c: 1})
            else:
                hash1[c] += 1
        for c in t:
            if not(c in hash2.keys()):
                hash2.update({c: 1})
            else:
                hash2[c] += 1
        print(hash1)
        print(hash2)
        if hash1.keys() == hash2.keys():
            for key in hash1.keys():
                if hash1[key] != hash2[key]:
                    return False
                
            return True
        
        return False
