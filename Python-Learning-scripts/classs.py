# coding=utf-8

# class 
class Dog:
	def __init__(self,name,age):
		self.name=name
		self.age=age

d=Dog('qiuqiu',2)
print('my dog names {0}, ages {1}'.format(d.name,d.age))


#
class Dog:
	def __init__(self,name,age,sex='female'):
		self.name=name
		self.age=age
		self.sex=sex

d=Dog('qiuqiu',2)
e=Dog('haha',1,'male')
f=Dog('tuobu',sex='female',age=3)
print('{0}:{1} old {2}'.format(d.name,d.age,d.sex))

# 
class Dog:
	def __init__(self,name,age,sex):
		self.name=name
		self.age=age
		self.sex=sex
		# invidual 
	def run(self):
		print('{0} is runnning'.format(self.name))
	def speak(self,sound):
		print('{0} is speaking {1}'.format(self.name,sound))

d=Dog('qiuqiu',2,'female')
d.run()
d.speak('wangwang')


# class variable
class Account:
	#this is the class variable  
	interest_rate=0.0568
	# construct method 
	def __init__(self,owner,amount):
		self.name=owner
		self.amount=amount
	# class method
	@classmethod
	def interest_by(cls,amt):
		return cls.interest_rate*amt
		

account=Account('zhangsan',5000)
print('the {0} has money of {1}'.format(account.name,account.amount))
print('rate is {0}'.format(Account.interest_rate))