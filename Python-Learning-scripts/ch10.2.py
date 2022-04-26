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



#%% 10.2.2多个except 代码块
