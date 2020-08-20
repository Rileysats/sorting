#MERGESORT ALOGRITHM
#RILEY SATANEK
import numpy



def randomize(n):
	"""Create a randomized list/array of size n between 0-100 exclusive"""
	rand_list = numpy.random.randint(0,100,n)
	return rand_list


def merge(l,r):
	"""Merges the smaller arrays together in order"""
	s_arr = []

	while(len(l) > 0 or len(r) > 0):
		if(len(l) > 0 and len(r) > 0):
			if(l[0] <= r[0]):
				s_arr.append(l[0])
				l = l[1:]
			else:
				s_arr.append(r[0])
				r = r[1:]
		elif(len(l) > 0):
			s_arr += l
			l = []
		elif(len(r) > 0):
			s_arr += r
			r = []
	return s_arr



def mergesort(arr):
	"""Mergesort function that calls recurvisely breaking the arrays into size=2"""	
	if(len(arr) == 1):
		return arr
	elif(len(arr) == 2):
		if(arr[0] > arr[1]):
			return [arr[1], arr[0]]
		else: 
			return arr

	mid = int((len(arr)+1)/2)

	right = arr[mid:]
	left = arr[:mid]

	l = mergesort(left) #Left side
	r = mergesort(right) #Right side
	
	return merge(l,r)
	

if __name__=="__main__":	
	size = int(input("How many random ints do you want sorted?: "))
	rand_list = list(randomize(size))

	print(mergesort(rand_list))

