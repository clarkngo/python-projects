def search(nums: list, target: int) -> int:
    left = 0;
    right = len(nums) - 1;
    while left < right:
        mid = left + (right - left) // 2
        if mid == target:
            right = mid
        else: 
            left = mid + 1
        print(left)
    return left



print(search([1,2,3,4,5,6,7,8,9,10],2))
