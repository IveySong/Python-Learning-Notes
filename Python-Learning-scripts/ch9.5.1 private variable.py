# coding=utf-8
# 私有变量： 在类内部可以访问， 在外部不可以调用；
# 私有变量： 在变量前加两个下划线 _ 来定义私有变量

#define a class named Account
class Account:
	__interst_rate=0.00568  #this is a class variable, and a private variable

	# define a contrust method
	def __init__(self,owner,amount):
		self.owner=owner  # this is an individual variable, and a public varibale
		self.__amount=amount # this  is an individual variable, and a private variable

    # define an individual method
	def desc(self):
		print('{0} money number:{1} rate:{2}'.format(self.owner,
			self.__amount,Account.__interst_rate)) #private variable can be only use in the inside class


# make a new individual 
account=Account('Tony',80000)
account.desc() #this can correctly return; the private can be used in the inside class

print('account name is {0}'.format(account.owner))
# print('account number is {}'.format(account.__amount)) # ERROR, the private can be used in the outside class
# print('rate is {0}'.format(Account.__interst_rate)) # ERROR, the private can be used in the outside class


