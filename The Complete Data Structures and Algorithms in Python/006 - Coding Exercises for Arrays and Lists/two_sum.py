my_array = [2,7,11,15]
target_value = 18

def two_pairs_Sum( nums, target):    
    for i in range(len(nums)):    
        for j in range(i+1, len(nums)):               
            if nums[i] + nums[j] == target:
                return [i, j]
                
               



print(two_pairs_Sum(my_array,target_value))