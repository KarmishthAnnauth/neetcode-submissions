class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        inarray = set()

        for num in nums:
            if num in inarray:
                return True
            else:
                inarray.add(num)
        
        return False