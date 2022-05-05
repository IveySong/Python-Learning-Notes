# codingf=utf-8
# 手动引发异常


class selfdefine(Exception):
	"""docstring fos selfdefine"""
	def __init__(self, message):
		super().__init__(message)


i=input('please input a number:')
b=999
# 先处理一个异常，再处理另外一个异常
try:
	i2=int(i)
	try:
		result=b/i2
		print('the {0} divided into {1} equalls to {2}'.format(b,i2,result))
	except ValueError as e:
		raise selfdefine('this is invalid number')

except ZeroDivisionError as e:
	raise selfdefine('this is a zero')

finally:
	print('release the resourse')



