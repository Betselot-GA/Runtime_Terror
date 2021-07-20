def two_sum(nums, target):
    output = []
    len1 = len(nums)
    summ = 0
    first_num = 0
    second_num = 0
    for i in range (len1):
        for j in range (i+1,len1):
            summ = nums[i] + nums[j]
            if summ == target:
                first_num = i
                second_num = j
                
    
    output.append(first_num)
    output.append(second_num)

    return output
