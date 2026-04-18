class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

# Longest common prefix:
# Input:
# Array of strings: strs
            
# Output:         
# 1) if prefix: "prefix"
# 2) else: ""
# 
# Cases:
# strs = ['hello'] -> output: "hello"
# 
# Example:
# strs = ['hello', 'he', 'here'] -> output: "he"
#          i
# 1) Go through each letter incrementally of the strs[0]
# 2) Check whether each letter in each string in strs is the same as strs[o]
# 3) If there is a difference in one of the letters 
#  OR the length of the current string is equal to the position up to now
# 4) return the current subsequence
# 5) If the loop is completed without breaking then the first word is the common subsequence

        if len(strs) == 0:
            return ""

        for i in range(len(strs[0])):
            char = strs[0][i]

            for string in strs[1:]:
                if len(string) == i or string[i] != char:
                    return strs[0][:i]
        
        return strs[0]
    


    