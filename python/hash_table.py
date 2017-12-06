#/bin/env python

class HashTable(object):
	def __init__(self):
		self.size = 250
		self.data = [False]*self.size

	def insert(self,key,val):
		self.data[self.hasher(key)] = val

	def get(self,key):
		return self.data[self.hasher(key)]

	def hasher(self,key):
		return sum([ord(x) for x in key]) % self.size

new_table = HashTable()
new_table.insert('foo','a')
new_table.insert('bar',100)

print new_table.get('foo')
print new_table.get('bar')
