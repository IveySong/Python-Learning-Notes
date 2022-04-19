# coding=utf-8

# 9.6 继承性 Inheritance 
class Animal:  # this is the father class
	def __init__(self,name):
		self.name=name
	def show_info(self):
		return "the name of animal is :{0}".format(self.name)
	def move(self):
		print('move a little bit')


class Cat(Animal):  # this is the child class  
	def __init__(self,name,age):
		super().__init__(name) #here is to call the father class, hence, all the functions or settings in father class can be used in child class
		self.age=age


cat=Cat('Tom',2)
cat.move()  # here, child class also can use individual method in father class
print(cat.show_info())

