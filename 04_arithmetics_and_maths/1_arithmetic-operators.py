# Basic arithmetic operators 

num = 10
print(f"num = {num}")
# augmneted addition
num +=5                           # num+=10 is same as num = num + 10
print(f"10 + 5 = {num}")
# Augmented substraction
num -= 10                         # num-=10 is same as num = num - 10
print(f"15 - 10 = {num}")
# Multiplication
num *= 5                          # num*=5 is same as num = num * 5
print(f"5 X 5 = {num}")
#division
num /= 5                          # num/=5 is same as num = num / 5
print(f"25 / 5 = {num}")
#division with remainder as output
print(f"The remainder of {num}% {num} is :",end=" ")
num = num% 5                  # num%=5 is same as num = num % 5
print(num)
# raised too
num += 10
print(f"The square of {num} is : ",end=" ")
num = num**2
print(num)