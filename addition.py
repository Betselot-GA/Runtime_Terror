result = []
carry = []

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")


if len(num1) == len(num2):
    if len(num1) > 1:
        for i in range(1,len(num1)+1):
            summ = 0
            if len(carry) > 0:
                summ += int(carry[0])
            summ += int(num1[len(num1)-i]) + int(num2[len(num1)-i])
        
            if summ > 9:
                summ = str(summ)
                carry.append(summ[0])
                result.append(summ[-1])
               
            else:
                summ = str(summ)
                result.append(summ)
        if len(carry)>0:
            result.append(carry[0])
        
                
        for i in range(1,len(result)+1):
            print(result[len(result)-i],end="")
          
    else:
        print(int(num1) + int(num2))
