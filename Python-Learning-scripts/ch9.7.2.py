# coding=utf-8

def start(object):
	object.speak()


class Animal:
	 def speak(self):
	 	print('animal bark, but do not know which one barks')

class Dog(Animal):
	def speak(self):
		print('dog bark')

class Cat(Animal):
	def speak(self):
		print('Cat meow')

class Car:
	def speak(self):
		print('Car didi')


start(Dog())
start(Cat())
start(Car())


#


