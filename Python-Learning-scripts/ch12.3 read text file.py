# coding=utf-8

read(size=-1)   # 读取字节 size=-1 是读取全部字节
readline(size=-1)  # 从文件中读取并返回一行
readlines()   #读取文件到一个字节列表中，每一行是列表的一个元素

write(s)  #写入s字字符串，返回写入的字节数
writelines(lines) #向文件中写入一个字节列表，不添加行分隔符

flush()  # 写入缓冲区

