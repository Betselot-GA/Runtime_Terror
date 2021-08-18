def sockMerchant(n, ar):
    flag = 0
    pairs = 0
    i = 0
    while i < len(ar):
        if flag ==1 :
            flag = 0
            i=0
        val = i+1
        for track in range(val,len(ar)):
            if track < len(ar):
                pair1 = ar[i]
                pair2 = ar[track]
              
          
                if pair1 == pair2:
                    flag = 1
                    ar.remove(pair1)
                    ar.remove(pair2)
             
                    pairs += 1

        i += 1
        

    return pairs

print(sockMerchant(9,[10,20,20,10,10,30,50,10,20]))
