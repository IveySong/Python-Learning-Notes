# coding=utf-8
# * is for tuple
def sum(*numbers):
	total=0.0
	for number in numbers:
		total+=number
	return total

print(sum(1,2,3))


# ** is for dict
def show_info(**info):
	print('---show info---')
	for key,value in info.items():
		print('{0}-{1}'.format(key,value))

show_info(name='Tony',age=18,sex=True)



# function using function
def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def calc(opr):
	if opr=='+':
		return add
	else:
		return sub

f1=calc('+')
f2=calc('-')
print("10+5={0}".format(f1(10,5)))
print("10-5={0}".format(f2(10,5)))



# filter function
def f1(x):
	return x>50
data1=[66,15,67,34,67,78,90]
filtered=filter(f1,data1)

def f2(x):
	return x<30
data2=[12,33,45,22,23,34]
filtered2=filter(f2,data2)


##map function
def f3(x):
	return x*x

data3=[1,2,3,4,5]
mapf=map(f3,data3)
mapf=list(mapf)









