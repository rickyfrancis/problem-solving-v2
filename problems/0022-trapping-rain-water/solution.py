# 42. Trapping Rain Water

def trap(height: list[int]) -> int:
    height_len = len(height)
    
    total_water = 0 
    
    max_arr_left = [0] * height_len 
    max_arr_right = [0] * height_len
    
    left = 0
    left_max = 0
    
    while left < height_len:
        left_max = max(left_max, height[left])
        max_arr_left[left] = left_max
        left += 1
        

    right = height_len - 1
    right_max = 0
    
    while right >= 0:
        right_max = max(right_max, height[right])
        max_arr_right[right] = right_max
        right -= 1
    
    for i, n in enumerate(height):
        
        water_level = min(max_arr_left[i], max_arr_right[i])
        water_at_i = water_level - n
        
        if water_at_i > 0:
            total_water += water_at_i
            
    return total_water
      




height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))