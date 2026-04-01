class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        arr = nums
        N = len(arr)

        all_list = []

        def walks(a, b, sel):
            copy_sel_1 = sel[:]
            copy_sel_2 = sel[:]

            if b == N-3:
                if a==3: 
                    sel = sel + arr[N-3:N]

                    all_list.append(sel)
                    return 1
            if b == N-2:
                if a==2:
                    
                    sel = sel + arr[N-2:N]

                    all_list.append(sel)
                    return 1

            if b == N-1:
                if a==1:
                    
                    sel = sel + arr[N-1:N]

                    all_list.append(sel)
                    return 1

            if a==1:
            # choose
                copy_sel_1.append( arr[b]) 

                all_list.append(copy_sel_1)

            # not chose 
                return 1 + walks(1, b+1, sel)

        
            c1 = walks(a, b+1, sel[:])
            copy_sel_2.append(arr[b])
            c2 = walks(a-1, b+1, copy_sel_2) 
            return c1 + c2 
        
        r = walks(3, 0, [])

        all_list_2 =[]
        for each in all_list:
            s = sum(each)
            if s==0:
                all_list_2.append(each)

        all_list_3 = [] 
        all_list_3_map = {}
        for each in all_list_2:
            each2 = sorted(each)
            each2 = str(each2) 
            all_list_3_map[each2] = each 

        for k in all_list_3_map:
            all_list_3.append(all_list_3_map[k])
        
        return all_list_3


            


# arr = [-1,0,1,2,-1,-4]
# N = len(arr)

# all_list = []

# def walks(a, b, sel):
#     copy_sel_1 = sel[:]
#     copy_sel_2 = sel[:]

#     if b == N-3:
#         if a==3: 
#             sel = sel + arr[N-3:N]

#             all_list.append(sel)
#             return 1
#     if b == N-2:
#         if a==2:
            
#             sel = sel + arr[N-2:N]

#             all_list.append(sel)
#             return 1

#     if b == N-1:
#         if a==1:
            
#             sel = sel + arr[N-1:N]

#             all_list.append(sel)
#             return 1

#     if a==1:
#     # choose
#         copy_sel_1.append( arr[b]) 

#         all_list.append(copy_sel_1)

#     # not chose 
#         return 1 + walks(1, b+1, sel)

   
#     c1 = walks(a, b+1, sel[:])
#     copy_sel_2.append(arr[b])
#     c2 = walks(a-1, b+1, copy_sel_2) 
#     return c1 + c2 
    
    

# r = walks(3, 0, [])

# all_list_2 =[]
# for each in all_list:
#     s = sum(each)
#     if s==0:
#         all_list_2.append(each)

# all_list_3 = [] 
# all_list_3_map = {}
# for each in all_list_2:
#     each2 = sorted(each)
#     each2 = str(each2) 
#     all_list_3_map[each2] = each 

# for k in all_list_3_map:
#     all_list_3.append(all_list_3_map[k])
# print(all_list_3)
    

nums = [-1,0,1,2,-1,-4]
all_list = []

arr = nums 
arr = sorted(arr)
# print(arr)
N = len(arr)


for a in range(0, N-2):

    if a-1 > 0 and arr[a] == arr[a-1]:
        continue 

    for b in range(a+1, N-1):
        if b-1 > a and arr[b] == arr[b-1]:
            continue 
        for c in range(b+1, N):
            if c-1 > b and arr[c] == arr[c-1]:
                continue 
            seq = [arr[a] , arr[b], arr[c]]
            if (arr[a] + arr[b] + arr[c] == 0):
                all_list.append(seq)

print(all_list)
