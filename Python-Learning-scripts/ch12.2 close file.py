# coding=utf-8

f_name='test.txt'
f=None
try:
	f=open(f_name)
	print('open file sucessusfully')
	context=f.read()
	print(context)
except FileNotFoundError as e:
	print('the file does not exist')
except OSError as e:
	print('OSerror happens')
finally:
	if f is not None:
		f.close()
		print('close file sucessusfully')


#%% ch12.2.2 using with as to close file
f_name='test.txt'
with open(f_name) as f:
	content=f.read()
	print(content)







