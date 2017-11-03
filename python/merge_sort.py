data = [10,4,1,2,5,13,18,6,20]

def merge_sort(data):

	if len(data)>1:
		# split
		mid = len(data)//2
		leftpart = data[:mid]
		rightpart = data[mid:]

		merge_sort(leftpart)
		merge_sort(rightpart)

		# left
		i = 0
		# right
		j = 0
		# merged (overwritten original array)
		k = 0

		# We assume array doesn't contain dup numbers
		while i<len(leftpart) and j<len(rightpart):
			if leftpart[i]<rightpart[j]:
				data[k] = leftpart[i]
				i = i + 1
				k = k + 1
			elif leftpart[i]>rightpart[j]:
				data[k] = rightpart[j]
				j = j + 1
				k = k + 1

		if i<len(leftpart):
			while i<len(leftpart):
				data[k] = leftpart[i]
				i = i + 1
				k = k + 1
		if j<len(rightpart):
			while j<len(rightpart):
				data[k] = rightpart[j]
				j = j + 1
				k = k + 1
