def star(func):

	def inner(*args, **kwargs):
		print("*" * 30)
		func(*args,**kwargs)
		print("*" * 30)
	return inner

def percent(func):

	def inner(*args, **kwargs):
		print("%" * 30)
		func(*args,**kwargs)
		print("%" * 30)
	return inner


@star
@percent
def printer(msg):
	print(msg)
printer("Hello")

@percent
@star
def printer(msg):
	print(msg)
printer("Hii")
'''printer1 = star(percent(printer))
printer1("Hello")
print("================================================================")
printer2 = percent(star(printer))
printer2("Hello")'''

