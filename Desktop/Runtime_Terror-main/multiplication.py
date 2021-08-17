result = []
carry = []
product = []
flag = 0
negative = 0

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

size1 = len(num1)
size2 = len(num2)

if int(num1) < 0  and int(num2) > 0 or int(num1) > 0 and int(num2)<0:
    negative = 1
    


if size1 == size2:
    if size1 > 1:
        if int(num1) < int(num2):
            temp = num1
            num1 = num2
            num2 = temp
            
        for i in range(1,size1+1):
            product.append(int(num1) * int(num2[i-1]))
            
        if size1 == 2:
            if len(str(product[1])) == len(str(product[0])): 
                product[0] = str(product[0]) + "0"
                product[-1] = "0" + str(product[-1])
            elif len(str(product[0])) == 3 and len(str(product[1])) == 1:
                product[0] = str(product[0]) + "0"
                product[-1] = "0" + "0" + "0" + str(product[-1])
            elif len(str(product[0])) == 3 and len(str(product[1])) == 2:
                product[0] = str(product[0]) + "0"
                product[-1] = "0" + "0" + str(product[-1])
            elif len(str(product[0])) == 1 and len(str(product[1])) == 3:
                product[0] = str(product[0]) + "0" + "0" + "0"
                product[-1] = "0"  + str(product[-1])
            elif len(str(product[0])) == 2 and len(str(product[1])) == 3:
                product[0] = str(product[0]) + "0" + "0"
                product[-1] = "0"  + str(product[-1])
            elif len(str(product[0])) == 1 and len(str(product[1])) == 2:
                product[0] = str(product[0]) + "0" + "0"
                product[-1] = "0"  + str(product[-1])
            elif len(str(product[0])) == 2 and len(str(product[1])) == 1:
                product[0] = str(product[0])  + "0"
                product[-1] = "0" + "0"  + str(product[-1])
            
        pro0 = len(str(product[0]))
        pro1 = len(str(product[1]))
        product0 = product[0]
        product1 = product[1]
        for i in range(1,pro0+1):
            summ = 0
            if len(carry) > 0:
                pop = carry.pop()
                summ += int(pop)
            summ += int(product0[pro0-i]) + int(product1[pro1-i])
        

            if summ > 9:
                summ = str(summ)
                carry.append(summ[0])
                result.append(summ[-1])
            else:
                summ = str(summ)
                result.append(summ)
        if len(carry) > 0:
            result.append(carry[0])

        if negative == 1:
            print("-",end="")

        for i in range(1, len(result)+1):
            print(result[len(result)-i],end="")
            #print(result)
        
            
            
            
                
            
            
            
