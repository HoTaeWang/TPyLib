state_capitals = {
	'Arkansas': 'Little Rock',
	'Colorado': 'Denver',
	'California': 'Sacramento',
	'Georgia': 'Atlanta'
}

ca_capital = state_capitals['California']
print("Capital of California = " + ca_capital)

for k in state_capitals.keys():
	print('{} is the capital of {}'.format(state_capitals[k], k))
 
