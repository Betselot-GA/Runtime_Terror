n1 = []
n2 = []
result = []
flag = 0
carry = 0
remainder = ""

product = 1
diff = 0
diff1 = 0
diff2 = 0
quotient = ""

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")


gap1 = len(num1) - len(num2)

if(len(num2) < len(num1)):
    if gap1 == 1:
        num2 = "0" + num2
    elif gap1==2:
        num2 = "0" + "0" + num2


size1 = len(num1)
size2 = len(num2)

print(size1,size2)
print(num1,num2)

if size1 == size2:
    
    for i in range(1,10):
        product = i * int(num2)
        diff = int(num1) - product
        if diff < int(num2):
            diff1 = str(num1)
            diff2 = str(product)
            quotient = str(i)
            break;

    for i in str(diff1):
        n1.append(i)
    for j in str(diff2):
        n2.append(j)

    for i in range(1,size1+1):
        difference = 0
        if len(result) > 0:
            if (int(n1[size1-i]) < int(n2[size2-i])):
                n1[size1 - i] = "1" + str(n1[size1 - i])
                difference = int(n1[size1 - i]) - int(n2[size1 - i])
                carry = 1
            else:
                difference = int(n1[size1 - i]) - int(n2[size1 - i])
            if carry == 1:
                n1[size1 - i] =  int(n1[size2 - i])-1
        if(len(result)==0) and int(n1[size1-i]) < int(n2[size2-i]):
            n1[size1 - i] = "1" + str(n1[size1 - i])
            difference = int(n1[size1 - i]) - int(n2[size1 - i])
            carry = 1
        elif((len(result)==0) and int(n1[size1-i]) > int(n2[size2-i])): 
            difference = int(n1[size1 - i]) - int(n2[size1 - i])
                    
                        
        result.append(diff)
        if flag == 1:
            print("-",end="")
    for i in range(1,len(result)+1):    
        remainder = str(result[len(result)-i])

    print("Remainder = ",remainder)
    print("Quotient = ",quotient)
        
    

                
            
        
