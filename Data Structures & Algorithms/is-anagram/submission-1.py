class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}

        for char in s:
            if not (char in dict1.keys()):
                dict1.update({char: 1})
            else:
                dict1[char] += 1
        
        for char in t:
            if not (char in dict2.keys()):
                dict2.update({char: 1})
            else:
                dict2[char] += 1

        if dict1.keys() == dict2.keys():

            for key in dict1.keys():
                if dict1[key] != dict2[key]:
                    return False
            return True

        return False