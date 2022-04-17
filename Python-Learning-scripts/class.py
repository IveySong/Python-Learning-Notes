# coding=utf-8

class Account:
	interested_rate=0.568

	def __init__(self,owner,amount):
		self.owner=owner
		self.amount=amount

try1=Account('Tony',8000)

print('try1 name:{0}'.format(try1.owner))
print('try1 amount:{0}'.format(try1.amount))
print('rate is {0}'.format(Account.interested_rate))

