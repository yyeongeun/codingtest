def solution(nums):
    answer = 0
    
    choose = int(len(nums)/2)
    nums = set(nums)
    print(nums)
    answer = min(len(nums),choose)
    
    return answer