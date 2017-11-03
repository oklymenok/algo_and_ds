data = [10,4,1,2,5,13,18,6,20]

def insert_sort(data,key_index):
	key = data[key_index]
	while data[key_index-1]>key and key_index>0:
		data[key_index] = data[key_index-1]
		key_index = key_index - 1
	data[key_index] = key

for i in range(1,len(data)):
	insert_sort(data,i)
