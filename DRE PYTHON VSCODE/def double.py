def double(x=0, y=0, z=0):
    # exits the fuction and returns the result
    num = x * 2
    num2 = num + 4
    num3 = num2 + y
    num4 = num2 + z
    return num2, num3, num4

result1, result2, result3 = double(3, 1, 2)
print(result1)   
print(result2)  
print(result3) 