try: 
    my_list = [] 

    while True: 
        my_list.append(int(input("Enter a number: "))) 

    
    my_list.sort()
    print(my_list)

    new_list = sorted(set(my_list))
    dup_list = []
 
 
    for i in range(len(new_list)):
            if (my_list.count(new_list[i]) > 1 ):
                dup_list.append(new_list[i])

except: 
    print("Repeating Numbers:", dup_list) 