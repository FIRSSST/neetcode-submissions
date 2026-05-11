class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ""
        for s in strs:
            new_str = new_str + str(len(s)) + '%' + s
               
        print(new_str)
        return new_str

    def decode(self, s: str) -> List[str]:
        print(s)
        left = 0
        lst = []
        while left < len(s):
            right = left 
            while s[right].isdigit():
                right += 1
            length = int(s[left:right])
            right += 1

            word = s[right:right+length]
            lst.append(word)
            
            left= right + length
        return lst



