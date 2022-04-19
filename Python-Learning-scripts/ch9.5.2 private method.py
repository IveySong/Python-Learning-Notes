# coding=utf-8
# 私有方法： 在类内部可以访问， 在外部不可以调用
# 私有方法： 在方法前加两个下划线 _ 来定义私有方法

#define a class named Account
class Account:
	__interst_rate=0.00568  #this is a class variable, and a private variable

	# define a contrust method
	def __init__(self,owner,amount):
		self.owner=owner  # this is an individual variable, and a public varibale
		self.__amount=amount # this  is an individual variable, and a private variable
	def __getinfo(self):
		return "{0} money number:{1} rate:{2}".format(self.owner,
		self.__amount,Account.__interst_rate) #private variable can be only use in the inside class
    
    # define an individual method
	def desc(self):
		print(self.__getinfo())

# make a new individual case
account=Account('Tony',80000)
account.desc()
# account.__getinfo() # ERROR, due to the private invidual method can not be used outside the class



