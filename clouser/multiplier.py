def make_multiplier_of(n):
	def multiplier(x):
		return x * n

	return multiplier


time3 = make_multiplier_of(3)

time5 = make_multiplier_of(5)


print(time3(5))
print(time5(5))

print(time5(time3(2)))

print(dir(time3.__closure__[0]))
print(make_multiplier_of.__closure__)
print(time3.__closure__)
print(time3.__closure__[0].cell_contents)
print(time5.__closure__[0].cell_contents)
