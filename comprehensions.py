# 列表推导式 生成列表
# 格式:
# var = [out_exp_res for out_exp in input_list if out_exp == 2]
mul = [i for i in range(30) if i % 3 is 0]
print(mul)


# lambda 表达式 , 就是函数的一种缩写
my_func = lambda arg1, arg2 : arg1 + arg2
print(my_func(1, 10))