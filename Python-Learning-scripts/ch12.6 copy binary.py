# coding=utf-8

f_name='logo.png'

with open(f_name,'r') as f:
	b=f.read()
	copy_f_name='logo2.png'
	with open(copy_f_name,'wb') as copy_binary:
		copy_binary.write(b)










