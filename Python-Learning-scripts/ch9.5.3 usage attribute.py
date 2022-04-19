# coding=utf-8

class Dog:
    # construction method
	def __init__(self,name,age,sex='female'):
		self.name=name
		self.__age=age  # this is a private individual variable, it can not be used outside the class
    # Individual method
	def run(self):
		print("{0} is running".format(self.name))

    # get method
	def get__age(self):
		return self.__age  # return the private individual variable; it makes private individual variable can be used outside the class
    # set method
	def set__age(self,age):
		self.__age=age  #set()，using the set method to update the private individual variable; it makes private individual variable can be changed outside the class
    
    # Note: using get method and set method is kind of complex, instead, using the properity could be more easier
	
	@property # this is a decorate box (装饰器)； ==get(); to get the value of the private varibale
	def age(self):  # the name 'age' here is equal to __age without __
		return self.__age
	@age.setter #this is also a decorate box; ==set(); to update the value of the private variable
	def age(self,age):
		self.__age=age


dog=Dog('qiuqiu',2)

print('{0} ages {1}'.format(dog.name,dog.age))

f=Dog('tuobu',sex='female',age=3)
print('{0}:{1} old {2}'.format(d.name,d.age,d.sex))



