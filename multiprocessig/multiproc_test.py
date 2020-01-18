import random
import multiprocessing

def list_append(count, id, out_list):
	"""
	Creates an empty list and then appends a random number to the listr 'count' mumber of times. ACP-heavy operation!
	"""

	for i in range(count):
		out_list.append(random.random())

if __name__ == "__main__":

	size = 10000000
	procs = 2

	jobs = []
	for i in range(0,procs):
		out_list = list()
		process = multiprocessing.Process(target=list_append, args=(size, i, out_list))
		jobs.append(process)

	for j in jobs:
		j.start()

	for j in jobs:
		j.join()

	print("List processing complete")
