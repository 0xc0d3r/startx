from ctypes import *

class Student(Union):
	_fields_ = [
		("Id",c_long),
		("Age",c_int),
		("Name",c_char * 8)
	]

value = raw_input(">>> ")

student = Student(int(value))

print "%ld" %student.Id
print "%d" %student.Age
print "%s" %student.Name