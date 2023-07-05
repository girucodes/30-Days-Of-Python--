# 23. 
'''
col:-   1     2       3     4   5

        1     1       1     1   1
        2     1       2     4   8
        3     1       3     9   27
        4     1       4     16  64
        5     1       5     25  125
'''
# Pattern of every col 
# i = 1   # pattern for col 1,3
# for i in range(1,6):
#     print(i)
    
# i=1  # pattern for col 2
# for i in range(1,6):
#     print(1)
    
# i = 1  # pattern for col 4
# for i in range(1,6):
#     print(i**2)
    
# i = 1    # pattern for col 5 
# for i in range(1,6):
#     print(i**3)
    
rows = 5
ctr = 1

for ctr in range(1, rows+1):
    row = []
    # appending here is done by col wise but when we use the 2nd for loop it look likw row wise. 
    row.append(ctr)
    row.append(1)
    row.append(ctr)
    row.append(ctr**2)
    row.append(ctr**3)
    
    for num in row: # this will loop from 1 to 5 rows 
        print(num,end=' ')
    print()
