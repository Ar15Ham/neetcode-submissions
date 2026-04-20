class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        for char in range(len(strs[0])):
            for string in strs:
                if len(string) == char or string[char] != strs[0][char]:
                    return strs[0][:char]
        
        return strs[0]
    


    