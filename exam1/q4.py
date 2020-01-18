#import numpy as np

#print(bin( ~ np.uint32(7))

a=1

print("{0:032b}".format(a))
print(int('111', 2))

uint32 =  bin(7)[2:].zfill(32)
print(uint32)
b_string = uint32
ib_string = ""

for bit in b_string:
  if bit == "1":
    ib_string += "0"
  else:
    ib_string += "1"

print(ib_string)
print(int(ib_string, 2))
