class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        val = "a" * 201

        for i in strs:
            if len(val) > len(i):
                val = i
        
        dic = {}

        for i in range(0, len(val)):
            dic[i + 1] = val[0:i + 1]

        result = ""

        for i in dic.keys():
            fail = False

            for j in strs:
                if j[0:i] != dic[i]:
                    fail = True
                    break
            
            if not fail:
                result = dic[i]

        return result