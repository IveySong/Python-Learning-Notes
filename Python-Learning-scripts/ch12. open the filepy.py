# coding=utf-8

# open(file, mode='r', encoding=None,errors=None)
f=open('test.txt','w+')  # 可读写方式 w+ 如果没有路径 创建路径
f=write('world')

f=open('test.txt','r+')  # 可读写方式 r+
f.write('hello')


f=open('text.txt','a')
f.write(' ') # 以a模式打开文件，会在文件末尾追加内容


#%% 路径的书写方式
fname='E:/OneDrive - The Chinese University of Hong Kong/Academic/test.txt'
f=open(fname,'w+')
f.write('hello world')

f=open(fname,'a+')
f.write('hahaha')

























