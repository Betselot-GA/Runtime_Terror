def reverse(x):
    l = []
    result = ""
    str_x = ""
    negative = 0
    int_result = 0
    
    if x >= -2147483648 and x <= 2147483647:
        if x == 0:
            return x
        if x < 0:
            negative = 1
            str_x1 = str(x)
            for i in range(1,len(str_x1)):
                str_x += str_x1[i]
                
        else:
            str_x = str(x)

        for i in range(1,len(str_x)+1):
            l.append(str_x[len(str_x)-i])
        
        for i in range(len(l)):
            track = 0
            if l[track] == '0':
                l.remove(l[track])
                track += 1
            elif l[track] != '0':
                break
        
        if negative == 1:
            result = "-"
        for j in range(len(l)):
            result += l[j]
        
        int_result = int(result)
        if int_result <= 2147483647 and int_result >= -2147483648:
            return int_result
        else:
            return 0
    

