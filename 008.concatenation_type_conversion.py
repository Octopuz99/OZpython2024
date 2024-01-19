'''
008 concatenation & Type conversion

'''
first_name = 'Octavio'
last_name = 'Zenteno'
born_year = 1980

#print(first_name + ' ' + last_name)

full_name = first_name+ ' ' + last_name

#print(full_name)
#print(full_name + ' ' + born year) va a fallar porque no concatena texto y numero

print(full_name+ '  ' + str(born_year))