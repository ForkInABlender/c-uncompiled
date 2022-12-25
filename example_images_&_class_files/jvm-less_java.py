import cppyy

cppyy.cppdef(''.join(open("java_classes_to_import/java7_classes.c", "r").readlines()))

class r(getattr(cppyy.gbl, "Class")('PyObject')):
	"""
 	This is a java-c-py class. It is imitation of a java class, one that runs inside of python & and the other in cppyy.
  This is setup to run java like code written in c++.

 	"""	
	name='r class'
	def isInterface(self):
		return False
	def isPrimitive(self):
		return False
	def toString(self):
		return str(self)
	def getName0(self):
		return "name"

print(r().getName())

print(r().isInterface())
