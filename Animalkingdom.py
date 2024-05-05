class Animal:
   	def getAnimal(self,name):
		   print(f"My dog is a {name} ")
class cat(Animal):
	def getcat(self):
		print("cat meow")
class dog(Animal):
	def noise(self):
		print("cat meow")
A = Animal()
A.getAnimal()
s = cat()
s.getAnimal()
s.getcat()