set1 = {1,2,3,4}
set2 = {3,4,5,6}

union_set = set1 | set2
print(f"union_set: {union_set}") #หมด

intersection_set = set1 & set2
print(f"intersection: {intersection_set}") #หาตัวเหมือนกัน

difference_set = set1 - set2
print(f"diff: {difference_set}") #เอาแค่่ฝั่งใดฝั่งหนึ่ง

symmetric_difference_set = set1 ^ set2
print(f"sym_diff_set: {symmetric_difference_set}") #