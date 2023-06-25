# 📌 Exercises: Level 2

# 1. 
first_name = 'Girija'
last_name = 'Varma'
full_name = 'Girija Varma'
country = 'India'
city = 'Mumbai' 
age = 1000
year = 2023 
is_married = False 
is_true = True
is_light_on = False 
myname, city, food = 'Girija Varma', 'Jaipur', 'Kachori'

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(myname))
print(type(food))

# 2.
print(len(first_name))

# 3. 
print(len(first_name))
print(len(last_name))
print('Comparing len of first_name & last_name')

if (len(first_name) == len(last_name)):
    print("Comaparison is True")
else:
    print("Comparison is False")
    
# 4. 
num_one = 5
num_two = 4
total = num_one + num_two
print("Addition: ",total)

diff = num_two - num_one
print("Subtraction: ",diff)

product = num_two * num_one
print("Multiplication: ",product)

division = num_one/num_two
print("Division: ",division)

remainder = num_two%num_one 
print("Modulus: ",remainder)

exp = num_one**num_two
print("Exponent: ",exp)

floor_division = num_one // num_two 
print("Floor Division: ",floor_division)

# 5. 
# 5a. 
area_of_circle = 3.14 * 30**2
print("Area of Circel: ",area_of_circle)

# 5b. 
circum_of_circle = 2*3.14*30
print("Circumference of Circle: ",circum_of_circle)

# 5c. 
radius = int(input("Enter radius of circle: "))
area_circle = 3.14 * radius**2
print("Area of Circle:- ",area_circle)

# 6. 
first_Name = input("Enter your First Name: ")
last_Name = input("Enter your Last Name: ")
Country= input("Enter your Country Name: ")
Age = int(input("Enter Your Age: "))

print("Your first name is ",first_Name)
print("Your Last name is ",last_Name)
print("Your country name is ",Country)
print("Your age is ",Age)

# 7. 
help('keywords')