n1 = []
n2 = []
result = []
flag = 0


num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

size1 = len(num1)
size2 = len(num2)

if(size1 == size2 and size1 > 1):
    if num1 < num2:
        temp = num1
        num1 = num2
        num2 = temp
        flag = 1
    for i in num1:
        n1.append(i)
    for j in num2:
        n2.append(j)
        
    carry = 0
    check = 0
    for i in range(1,size1+1):
        diff = 0
        
        #print(result)
        if result:
            if carry == 1:
                if n1[size1 - i] == "0":
                    print("debug 0")
                    n1[size1 - i] = "1" + str(n1[size1 - i])
                    n1[size1 - i] =  int(n1[size1 - i])-1
                    #carry = 1
                    print(n1[size1 - i])
                    check = 1
                else:
                    n1[size1 - i] =  int(n1[size1 - i])-1
                    print(n1[size1-i])
                carry = 0
                
            if (int(n1[size1-i]) < int(n2[size2-i])):
                print("debug 2")
                carry = 1
               
                n1[size1 - i] = "1" + str(n1[size1 - i])
                diff = int(n1[size1 - i]) - int(n2[size1 - i])
                
            else:
                print("debug 3")
                if check == 1:
                    diff = int(n1[size1 - i]) - int(n2[size1 - i])
                    carry = 1
                else:
                    diff = int(n1[size1 - i]) - int(n2[size1 - i])
                    print(n1[size1-i])
            
        elif not result:
            if int(n1[size1-i]) < int(n2[size2-i]):
                print("debug 1")
                carry = 1
                n1[size1 - i] = "1" + str(n1[size1 - i])
                diff = int(n1[size1 - i]) - int(n2[size1 - i])
            elif int(n1[size1-i]) > int(n2[size2-i]):
                print("aaaa")
                diff = int(n1[size1 - i]) - int(n2[size1 - i])

        #if carry == 1:
            #n1[size1 - i] =  int(n1[size1 - i])-1
            
        #print(result)  
        result.append(diff)
    if flag == 1:
        print("-",end="")
    for i in range(1,len(result)+1):    
        print(result[len(result)-i],end="")
    
    
        

    
            
            
            
        
