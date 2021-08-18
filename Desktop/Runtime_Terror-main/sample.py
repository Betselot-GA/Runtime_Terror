def sockMerchant(n, ar):

    flag = 0
    pairs = 0
    # for i in range(len(ar)):
    i = 0
    while i < len(ar):
        if flag ==1 :
            flag = 0
            i=0
        print("i1 ",i)
        print("len(ar) ",len(ar))
        val = i+1
        for track in range(val,len(ar)):
            print("i2 = ",i)
            if track < len(ar):
                pair1 = ar[i]
                pair2 = ar[track]
                print("d-pair1 ",pair1)
                print("d-pair2 ",pair2)
                # if i==0 and pair1!=pair2:
                #     flag = 1
                if pair1 == pair2:
                    # if i == 0:
                    flag = 1
                    print("Flag on ")
                    ar.remove(pair1)
                    ar.remove(pair2)
                    print("pair2 ",pair2)
                    
                    pairs += 1
                else:
                    print("--------------------------passed")
                
        
            print("array ",ar)
        i += 1
        

    return pairs

print(sockMerchant(15,[6,5,2,3,5,2,2,1,1,5,1,3,3,3,5]))


