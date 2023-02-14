def print_div_3(num):
    if num == 10:
        return
    print(num // 3)
    print_div_3(num+1)


print_div_3(0)
