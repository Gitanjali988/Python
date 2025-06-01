 #!/usr/bin/python

"""
Python  Functions
"""


# Write a Python function unique_list() that takes a list and returns a new list with unique elements of the first list.
# unique_list: (1,2,3,3,3,3,4,4,5)

def unique_list(l):
  x = []
  for number in l:
    if number in x:
       continue
    else:
        x.append(number)
  return x

print(unique_list([1,2,3,3,3,3,4,4,5]))

   


#Write a Python function multiply()to multiply all giving numbers in a list.
#Sample List : (9, 2, 3, -6, 7)
#Expected Output : -2268

 def multiply(num):  
    total = 1
    for n in num:
        total *= n  
    return total  
print(multiply((9,2,3,-6,7)))


# Write a function get_average() that takes an arbitrary number of arguments and returns the average of them
# Number of arguments : (5,6,8,10,31)
# Expected Output : 12

def get_average(num):
    
    sum_num = 0
    for n in num:
     sum_num= sum_num + n
    num=sum_num / len(num)
    return num
 
print(get_average([5,6,8,10,31]))


   
