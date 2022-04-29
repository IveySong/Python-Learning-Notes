# coding=utf-8

i=input('please input a number:')
n=888

# 处理异常
try:
	result=n/int(i)
	print(result)
	print('{0}/{1}=={2}'.format(n,i,result))
except ZeroDivisionError as e:
	print('it can not be 0, error:{}'.format(e))
except ValueError as e:
	# 输入的是无效的数字
	print('non-valid number:{}'.format(e))


#%% 10.2.3 多重异常捕获
# 将多个except 一起处理就是多重异常捕获

i=input('please input a number:')
n=888

try:
	result=n/int(i)
	print(result)
	print('{0}/{1}=={2}'.format(n,i,result))
except (ZeroDivisionError,ValueError) as e:
	print('Error happen: {}'.format(e))

