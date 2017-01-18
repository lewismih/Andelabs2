
def words(input):

	
	data = input.split(' ') 
	unique_word = set(data)
	occurances = {}
	
	
	for word in unique_word:
		count = 0
		
		#second loop to comapare first loop variable
		for y in data:
		  
			# this check compares the looping variable
			if word  == y:
				count = count + 1
				
				# the check below identifies an integer in a string, if true the string is casted to an integer
				if word.isdigit() == True:
						word = int(word)
						
		occurances[word] = count
	
	return occurances
