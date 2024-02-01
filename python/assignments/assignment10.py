# create a class laptop, make it interface with two methods scroll and click. make two class HP and Dell and inherite laptop with implementing only scroll method and make those two class abstract. create two another class Hpnotebook and dellnotebook and implement both scroll and click mehtod in it.

from abc import abstractmethod,ABC

class laptop(ABC):
	@abstractmethod
	def scroll(self):
		pass
	@abstractmethod
	def click(self):
		pass
#d=laptop()
#print(d.click())

class HP(laptop):
	def scroll(self):
		print("Scroll in HP")
	@abstractmethod
	def click(self):
		pass

class DELL(laptop):
	def scroll(self):
		print("Scroll in DELL")
	@abstractmethod
	def click(self):
		pass

class hpnotebook(HP):
	def scroll(self):
		print("Scroll in hpnotebook")
	def click(self):
		print("Click in hpnotebook")
class dellnotebook(DELL):
	def scroll(self):
		print("Scroll in dellnotebook")
	def click(self):
		print("Click in dellnotebook")


hpobject=hpnotebook()
dellobject=dellnotebook()

hpobject.scroll()
dellobject.scroll()
hpobject.click()
dellobject.click()

