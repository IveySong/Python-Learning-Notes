# coding=utf-8

# 多继承： 一个子类有多个父类
# Note 很多语言不支持多个父类
class Horse:
	def __init__(self,name):
		self.name=name
	def show_info(self):
		return "the name of Horse is: {0}".format(self.name)
	def run(self):
		print("horse runs...")

class Donkey:
	def __init__(self, name):
		self.name=name
	def show_info(self):
		return "the name of Donkey is: {0}".format(self.name)
	def run(self):
		print("donkey runs...")
	def roll(self):
		print('donkey rolls...')

class Mule(Horse,Donkey):  #father class, Horse and Donkey
	def __init__(self,name,age):
		super().__init__(name)   # here, call the father class, Horse and Donkey sequencly
		self.age=age

m=Mule('Lvluoli',2)
m.run()  #here,call the father class Horse
m.roll()  #here, call the fathe class Donkey
print(m.show_info()) #here,call the father class Horse