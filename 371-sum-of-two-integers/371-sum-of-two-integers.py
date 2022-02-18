class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
		
        while b != 0:
            xor = a ^ b
            xor = xor & mask
            
            carry = (a & b) << 1
            carry = carry & mask
            a, b = xor, carry
            
        max_int = 0x7FFFFFFF
        if a < max_int:
            return a
        else:
            # if there is overflow
			# i.e if a is a negative value
            result = a ^ mask
            result = ~result
            return result
        
        
        
        
        
#         public int getSum(int a, int b) {
#         if(a == 0) {
#             return b;
#         }
        
#         if(b == 0) {
#             return a;
#         }
        
#         int carry = 0;
        
#         while(b != 0) {
            
#             // If both bits are 1, we set the bit to the left (<<1) to 1 -- this is the carry step
#             carry = (a & b) << 1;
            
#             // If both bits are 1, this will give us 0 (we will have a carry from the step above)
#             // If only 1 bit is 1, this will give us 1 (there is nothing to carry)
#             a = a ^ b;
            
#             b = carry;
#         }
        
#         return a;
#     }
