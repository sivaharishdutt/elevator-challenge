import time
floor=1
flag="true"
while(flag):
    print("********WELCOME********")
    print("YOU ARE AT FLOOR:%d" % (floor))
    print("Functions in Elevator")
    print("Select a Floor ==> (s/S)")
    print("Fire Alarm ==> (f/F)")
    print("Quit ==> (q/Q)")
    print("***********************")
    sel = input("Select an option in the Elevator:")
    try:
        if(sel=='s' or sel=='S'):
            choice1=input("Please Enter the floor(1-10) you want to go:")
            choice=int(choice1)
            if (choice > 10 or choice < 0):
                # If floor not in b/w 1-10
                print("SORRY")
                print("INVALID choice...Please make the true selection b/w 1-10")
                flag = "true"
                continue
            elif (choice == floor):
                # If floor and choice are equal
                floor = choice
                print("You have selected the destination as current floor")
                print("YOU ARE AT FLOOR:%d" % (floor))
                flag = "true"
                continue

            elif (choice > floor):
                # If choice  exceeds the floor
                # Elevator goes up
                print("Going Up")
                for i in range(floor+1,choice+1):
                    print("..%d"%(i))
                print("..Ding!")
                floor = choice
                flag = "true"
                continue

            elif (choice < floor):
                # If choice  belows the floor
                # Elevator goes down
                print("Going Down")
                for i in range(floor-1,choice-1,-1):
                    print("..%d" % (i))
                print("..Ding!")
                floor = choice
                flag="true"
                continue


        elif(sel=='f' or sel=='F'):
            print("DANGER! You must exit from the Elevator now!")
            print("Don't be panic...WAIT....Eerything will be good")
            pass
            pass
            time.sleep(10)
            print("Now,Elevator is ready")
            print("YOU ARE AT FLOOR:1")
            floor = 1
            flag="true"
            continue
        elif(sel=='q' or sel=='Q'):
            #Quit
            #Exit from the Elevator
            print("Thank you...VISIT AGAIN")
            exit
            flag="false"
            break
        else:
            #Invalid selection
            print("SORRY")
            print("INVALID choice...Please make the true selection of 'S'or'F'or'Q'")
            flag = "true"
            continue
    except:
        print("Please select the correct chice...........")
