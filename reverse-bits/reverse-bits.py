class Solution:
    def reverseBits(self, n: int) -> int:
        tmp = 0
        for _ in range(32):
            tmp = (tmp<<1)|(n % 2) # adding each bits starting right side while shifting to the left
            n >>= 1
        return tmp
        # 수현이가 이걸 못보겠지만, 수현이만 생각하면 걱정되고 이런 마음이 전해졌으면 좋겠다. 
        # 수현이가 조금만 내가 수현이한테 하는거를 알아주고 말해줬으면 나도 거기에 힘을 얻어 누구한테보다 내 여자친구 진심인 사랑할수있었을거같은데. 
        # 내가 아직 철이없어서 수현이가 툭 뱉으면 가슴에 꽂힌다. 
        # 수현이가 앞으로 혼자서 힘든거 굳이 왜 말해 라고 안 하고 혼자 안힘들게 살았으면 좋겠다. 
        # 그래도 수현이가 내가 못해줬던부분 다 해줄수있는 사람을 만났으면 좋겠다. 