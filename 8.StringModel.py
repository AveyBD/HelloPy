#lenght Of a string
course = 'let\'s Learn Python'
print(len(course))

#Dot Function

newcourse = course.upper()
print(newcourse)
#We can print directly too
print(course.upper())

#same goes for lowercase.
print(course.lower())

#Find a specific alphabet in string
print(course.find('L'))

#Replace
print(course.replace('Python', 'with fun'))

#Replace a alphabte
print(course.replace('P', 'F'))

#Search in string in boolean
print('Python' in course)
#Here to remember "IN" is a operator  to find boolean result.

#Title to make first letter Upper
print(course.title())
