# Encapsulation. Create a class patient, 3 fields: id,name,ssn. Make them private and access them through getter and setter.

class Patient:
	def set_id(self,id):
		self.__id=id
	def set_name(self,name):
		self.__name=name
	def set_ssn(self,ssn):
		self.__ssn=ssn
	def get_id(self):
		return self.__id
	def get_name(self):
		return self.__name
	def get_ssn(self):
		return self.__ssn

p=Patient()
p.set_id(1)
p.set_name("Hi")
p.set_ssn(123)
#print(p.id)
print(p.get_id())
print(p.get_name())
print(p.get_ssn())

	 
