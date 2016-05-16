# filename: underscore.py
# author: Guy Whorley
# description: Equivelent Python functions that mirror some of the
#   Underscore.js library.

class Underscore(object):

	def map(self, arr, myLambda):
		"""
		Produces a new array of values by mapping each value in arr
		through a transformation function (myLambda).
		"""
		ret = []
		for val in arr:
			ret.append(myLambda(val))
		return ret

	def reduce(self, arr, myLambda, startVal=0):
		"""
		Also known as inject and fold, reduce boils down a list of values
		into a single value.
		"""
		ret = startVal
		for i in range(0, len(arr)):
			ret += myLambda(arr[i])
		return ret

	def find(self, arr, myLambda):
		"""
		Looks through each value in the list, returning the first one that passes a
		truth test (predicate), or undefined if no value passes the test.

		The function returns as soon as it finds an acceptable element, and doesn't
		traverse the entire list.
		"""
		for el in arr:
			if (myLambda(el) is True):
				return el

	def filter(self, arr, myLambda):
		"""
		Looks through each value in the list, returning an array of all the values
		that pass a truth test (predicate).
		"""
		ret = []
		for el in arr:
			if myLambda(el):
				ret.append(el)
		return ret

	def reject(self, arr, myLambda):
		"""
		Returns the values in list without the elements that the truth test (predicate)
		passes. The opposite of filter.
		"""
		ret = []
		for el in arr:
			if not myLambda(el):
				ret.append(el)
		return ret

# Examples
#_ = Underscore()
#arr = [ 'Bob', 'Chris', 'Christina', 'Rachel', 'Moka']
#arr = [ -4, 5, -1, 90, 23, -23, 101, 42, 98]
#print(_.filter(arr,lambda x: x % 2 == 1))
#print(_.reject(arr, lambda x: len(x)>4))
#print(_.filter(arr, lambda x: len(x)>4))
#print(_.find(arr,lambda x: x=='Jared'))
# print(_.map(arr, lambda x: x*1.5))
#print(_.reduce(arr, lambda x: x,5))
# evens = _.filter([1,2,3,4,5,6], lamdba x: x%2 == 0) # ret = [2,4,6]
