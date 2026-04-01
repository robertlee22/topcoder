class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        all_list = []

        arr = nums
        arr = sorted(arr)
        N = len(arr)
        print(arr)

        


        for a in range(0, N-2):

            if a-1 >= 0 and arr[a] == arr[a-1]:
                continue 

            pc = N-1 
            for b in range(a+1, N-1):
                if b-1 > a and arr[b] == arr[b-1]:
                    continue 
                
                c = pc
                while c > b:
                    if arr[a] + arr[b] + arr[c] == 0:
                        seq = [arr[a] , arr[b], arr[c]]
                        all_list.append(seq)
                        pc = c-1
                        break

                    else: 
                        c -=1 
                
        return all_list
    
s = Solution() 
r = s.threeSum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]) 
# [-10, -5, -5, -4, -4, -3, -2, -2, 0, 0, 1, 2, 2, 2, 2, 5, 5]
print(r)

