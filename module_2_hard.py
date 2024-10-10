import random
nums = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
first_num = random.choice(nums)
list_nums = []
print (first_num)
for i in range(1, first_num):
    for k in range(i+1, first_num):
        if first_num % (i + k) == 0:
            list_nums.append(i)
            list_nums.append(k)
list_nums = str(list_nums)
print(type(list_nums))
print(''.join(list_nums))
print(list_nums)
