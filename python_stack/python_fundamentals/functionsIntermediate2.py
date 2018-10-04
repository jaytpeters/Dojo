1. 
x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30

2. 
def iterateDictionary(students):
    for student in students:
        print(f"first_name - {student['first_name']}, last_name - {student['last_name']}")

3. 
def iterateDictionary2(key,list):
    for dict in list:
        print(dict[key])

4. 
def locationsAndInstructors(dict):
    locations = dict['locations']
    instructors = dict['instructors']

    print(len(locations), "LOCATIONS")
    for location in locations:
        print(location)
    
    print("\n")

    print(len(instructors), "INSTRUCTORS")
    for instructor in instructors:
        print(instructor)