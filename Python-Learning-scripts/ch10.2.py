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



#%% try-except 语句嵌套
i=input('please input a number:')
b=999
# 先处理一个异常，再处理另外一个异常
try:
	i2=int(i)
	try:
		result=b/i2
		print('the {0} divided into {1} equalls to {2}'.format(b,i2,result))
	except ValueError as e1:
		print('ERROR invalid number:{}'.format(e1))
except ZeroDivisionError as e2:
	print('ERROR Zero happens:{}'.format(e2))




#%% ch10.3 使用finally 代码块释放资源
i=input('please input a number:')
b=999
# 先处理一个异常，再处理另外一个异常
try:
	i2=int(i)
	try:
		result=b/i2
		print('the {0} divided into {1} equalls to {2}'.format(b,i2,result))
	except ValueError as e1:
		print('ERROR invalid number:{}'.format(e1))
except ZeroDivisionError as e2:
	print('ERROR Zero happens:{}'.format(e2))

finally:
	print('release the resourse')



