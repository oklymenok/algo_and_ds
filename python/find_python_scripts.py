import os

def find_files(path):

	os.chdir(path)
	path = os.getcwd()

	sd = []
	for i in os.listdir(path):
		if os.path.isfile(i) and i.endswith('py'):
			print path+"/"+i
		elif os.path.isdir(i):
			sd.append(i)
	if len(sd)>0:
		for d in sd:
			find_files(path+"/"+d)

find_files("../")
