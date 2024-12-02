class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_i = -1
        for i in range(len(strs[0])):
            car = strs[0][i]
            for str in strs:
                if len(str)==i or car != str[i]:
                    if max_i>=0:
                        return strs[0][:i]
                    else:
                        return ""
            max_i += 1
        return strs[0]