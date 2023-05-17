class Solution:
    def convertToBase7(self, num: int) -> str:
        
        negative = True if num < 0 else False
        
        if num == 0:
            return "0"
        
        if negative:
            num = abs(num)
            
        ans = ""
        remainder = ""
        
        while num > 0:

            ans = num //7
            remainder = str(num%7) + remainder
            num = ans 

        if negative:
            remainder = "-" + remainder

        return remainder
            