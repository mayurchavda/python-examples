import random
import threading

def list_append(count, id, out_list):
	"""
        Creates an empty list and then appends a random number 
        to the list 'count' number of times. A CPU-heavy operation!
	"""
	for i in range(count):
		out_list.append(random.random())

if __name__ == "__main__":
	size = 10000000
	threads = 2

	jobs = []
	for i in range(0, threads):
		out_list = list()
		thread = threading.Thread(target=list_append(size, i, out_list))
		jobs.append(thread)

	for j in jobs:
		j.start()

	for j in jobs:
		j.join()

	print("List processing complete")
