import random

# Generate some dates
def generate_years():
	num_people = 500
	first_year = 1920
	last_year = 2018

	people_lived = []
	for i in range(num_people):
		age = random.randint(30,85)
		offset = last_year-age-first_year
		birth = first_year + random.randint(0,offset)
		people_lived.append((birth,birth+age))

	return people_lived

def most_lived(data):
	max_year = max([person[1] for person in data])
	min_year = min([person[0] for person in data])

	people_alive = {}

	for i in range(min_year,max_year):
		for person in data:
			if person[0] <= i and person[1] > i:
				if i in people_alive:
					people_alive[i] = people_alive[i]+1
				else:
					people_alive[i] = 1

		

	return people_alive

data = generate_years()
ma = most_lived(data)
print max(ma,key=ma.get)
