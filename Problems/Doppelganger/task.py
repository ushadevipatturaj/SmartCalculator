# the object_list has already been defined
# write your code here
from collections.abc import Hashable
object_list = [1, 397, 27468, -95, 1309, 397, -539874, -240767, -95, 397]
temp_list = []
count_val = 0
for i in object_list:
    if isinstance(i, Hashable):
        temp_list.append(i.__hash__())
for i in temp_list:
    if temp_list.count(i) > 1:
        count_val += 1
print(count_val)
