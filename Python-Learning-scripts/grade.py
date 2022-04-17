# coding=utf-8

score=int(input("please input a number:"))

if score>=90:
	grade='A'
elif score>=80:
	grade='B'
elif score<=70:
	grade='C'
elif score>=60:
	grade='D'
else:
	grade='F'

print("Grade="+ grade)