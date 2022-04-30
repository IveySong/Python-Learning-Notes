# coding=utf-8

f_name='text.txt'

with open(f_name, 'r', encoding='gbk') as f:
	lines=f.readlines()
	copy_f_name='dest_file.txt'
	with open(copy_f_name,'w',encoding='utf-8') as copy_f:
		copy_f.writelines(lines)
		print('copy successfully')



		