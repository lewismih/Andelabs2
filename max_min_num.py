# Function to check the Minimum and maximum number in an array
def find_max_min(list_main):
  
  #First check to assertain variables are equal
  if all(a == list_main [0] for a in list_main) == True: 
    list_2 = []
    list_2.append(len(list_main))
    
    #Returning the length of the list
    return list_2 
  
  else:
    #Find the maximum value
    max_val = max(list_main) 
    
    #Find the minimum value
    min_val = min(list_main) 
    
    #Then we combine maximum and minimum values to a list and return the list
    max_min = []                   
    max_min.append(min_val)
    max_min.append(max_val)    
  return max_min
