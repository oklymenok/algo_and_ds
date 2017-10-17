data = [2,3,6,7,8,10,13,5]

def insert_sort(data,key_index):

	key = data[key_index]
	while data[key_index-1]>key:
		data[key_index]=data[key_index-1]
		key_index=key_index-1
	data[key_index]=key
	return data

for i in range(1,len(data)):
	data = insert_sort(data,i)
