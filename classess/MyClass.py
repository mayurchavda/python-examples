class MyClass:
	"""My Class sample example"""
	i = 1234

	def f(self):
		print("Hello world!")


x = MyClass()
print(x)

x.counter = 1
while x.counter < 10:

	x.counter = x.counter * 2

print(x.counter)

del x.counter
