# coding=utf-8

s_dict={102:"zhangsan",105:'lsi',109:'wangwu'}

print('--遍历键--')
for s_id in s_dict.keys():
	print('学号：'+str(s_id))

print('--遍历值--')
for s_value in s_dict.values():
	print('name'+s_value)

print('--遍历键 和 遍历值--')
for s_id,s_value in s_dict.items():
	print('学号:{0}-学生：{1}'.format(s_id,s_value))