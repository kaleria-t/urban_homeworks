my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
n = 0
var_ = my_list[n]
end = my_list[-1]
finish = len(my_list) - 1
while n <= int(finish):
    if var_ > 0:
        print (var_)
        n = (n + 1)
        var_ = my_list[n]
    else:
        break


