def make_pretty(func):
	def inner():
		print("I am going to pretty")
		func()
	return inner

@make_pretty
def ordinary():
	 print("I am ordinary")

ordinary()
