# 📌 Exercises - Day 3

# 1. 
age = 35

# 2. 
height = 5.8

# 3. 
comp = 1+5j

# 4. 
base = int(input("Enter base: "))
height = int(input("Enter height: "))
area = 0.5 * base * height
print("Area of Triange is ",int(area))

# 5. 
side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print("The Perimeter of triangle is ",perimeter)

# 6. 
length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = length * width
perimeterR = 2 * (length + width)
print("Area of Rectangle is ",area)
print("Perimeter of Rectangle is ",perimeterR)

# 7.
radius = float(input("Enter radius: "))
pi = 3.14
area = pi * radius**2 
c = 2*pi*radius
print("Area of Circle is ",area)
print("Perimeter of Circle is ",c)

# 8. 
# Calculate the slope, x-intercept and y-intercept of y = 2x -2

# slope = (y2-y1)/(x2-x1)

# x_intercept = 1

# y_intercept = -2 

# 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

# a(2,2) = (x1,y1)
# b(6,10) = (x2,y2)

x1 = 2
x2 = 6,
y1 = 2
y2 = 10

slope = 8/4
print("Slope is ",slope)

Edistance = ((6-2)**2 + (10-2)**2)**0.5
print("The Euclidean Distance is ",Edistance)

# 10.

# 11. 

# 12. 
print(len('python'))
print(len('dragon'))

print("Length of both python & dragon are same")

# 13. 
p = 'python'
d = 'dragon'
('on' in p) and ('on' in d)
    
# 14.
sent = "I hope this course is not full of jargon"
print("jargon" in sent)

# 15. There is no 'on' in both dragon and python
d = 'dragon'
p = 'python'
print(('on' not in d) and ('on' not in p))

# 16. 
text = 'Python'
print(len(text))
val = len(text)
text_float = float(val)
print(text_float)
type(text_float)
st1 = str(text_float)
print(st1)
type(st1)

# 17. 
num = int(input('Enter a number:- '))
if (num%2==0):
    print(num,' is an even number')
else:
    print(num,' is an odd number')

# 18.
ans = 7//3
print(ans) 
if ans == 2.7:
    print('OK')
else:
    print('Not OK')
    
# 19. 
val = '10'
val2 = 10 
if type(val) == type(val2):
    print(True)
else:
    print(False)
    
# 20. 
value = int(9.8)
value2 = 10 
if type(value) == type(value2):
    print(True)
else:
    print(False)
    
# 21. 
hours = int(input('Enter hours: '))
ratePerHour = int(input('Enter rate per hour: '))
print('Your weekly earning is ',hours*ratePerHour)

# 22. 
yrs = int(input('Enter number of years you have lived: '))
seconds = 31536000
print("You have lived for", yrs*seconds, "seconds.")

# 23. 
'''
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''
# see the logic of this pattern in s1.py 

rows = 5
ctr = 1
for ctr in range(1, rows+1):
    row = []
    row.append(ctr)
    row.append(1)
    row.append(ctr)
    row.append(ctr**2)
    row.append(ctr**3)
    
    for num in row: # this will loop from 1 to 5 rows 
        print(num,end=' ')
    print()
   
