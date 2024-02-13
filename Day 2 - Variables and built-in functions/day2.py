
# Exercises Level 1

# Day 2 : 30 Days of python programming
firstName  = 'Adam'
lastName = 'Smith'
fullName =  'Adam Smith'
country = "Scotland"
city = "Edinburgh"
age = 67
year = 1770
is_Married = False
is_True = True
is_light_on = True
language, occupation = 'English', 'Economist'

# Exercises Level 2 
1. 

print(type(firstName))
print(type(lastName))
print(type(fullName))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_Married))
print(type(is_light_on))
print(type(language))
print(type(occupation))

2. 

print(len(firstName))

3. 

if len(firstName) < len(lastName):
    print("The lenght of lastname is bigger")

4.

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_two ** num_one
floor_division = num_one// num_two

print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)

5. 

circle_radius = 30 
area_of_circle = 3.14 * circle_radius * circle_radius
circum_of_circle = 2 * 3.14 * circle_radius 

print(area_of_circle)
print(circum_of_circle)

radius = int(input("Enter the radius of the circle = "))
areaOfCircle = 3.14 * radius * radius
print(areaOfCircle)

6. 

first_name = input("Please enter your name = ")
last_name = input("Please enter your last name = ")
user_country = input('Please enter the country= ')
user_age = int(input("Please enter your age = "))

print( first_name, last_name, user_country, user_age)

7. 

help('keywords')