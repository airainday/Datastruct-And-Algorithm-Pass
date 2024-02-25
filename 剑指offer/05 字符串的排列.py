class Solution:
    def Permutation(self , str: str):
        # write code here
        n = len(str)
        if n<=1:
            return str
        lst = []
        for i in range(n):
            s1 = str[i]
            for s2 in self.Permutation(str[:i]+str[i+1:]):
                new_str = s1 + s2
                if new_str not in lst:
                    lst.append(new_str)
        lst=sorted(lst)

        return lst
    
if __name__ == "__main__":
    s = Solution()
    res = s.Permutation("qwert")
    print(res,len(res))