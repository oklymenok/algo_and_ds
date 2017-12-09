def move_tower(size,source,dest,spare):
	if size == 1:
		move_disk(source,dest)
	else:
		move_tower(size-1,source,spare,dest)
		move_disk(source,dest)
		move_tower(size-1,spare,dest,source)


def move_disk(source,dest):
	print "Move disk from {} to {}".format(source,dest)

move_tower(3,"A","C","B")
