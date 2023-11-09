x,y,z = eval(input("3개의 정수 x,y,z입력 : "))  
if x > y : 
    if y < z : print("제일 작은 정수는 ",y,)
    else : print("제일 작은 정수는 ",z)  
else:
    if x < z : print("제일 작은 정수는 ",x) 
    else: print("제일 작은 정수는 ",z) 
 
