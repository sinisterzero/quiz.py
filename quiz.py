



def askquestion(qucheck, quanswer, correctanswer ):
    while qucheck == False:
    try:
        quanswer = int(input("input 1, 2, 3 or 4 as your answer  "))
        #check if answer correct
        if quanswer == correctanswer:
            correct += 1
            qucheck = True
        #check if answer is acceatpable
        elif 0 < q1answer < 5:
            qucheck = True
        #check if user enter a  unaceatpable number
        else:
            print("you input a unaceaptable option that does not exist as one of the 4 answer listed")   
    #check if user putted a string or float 
    except ValueError:
        print("you inputted a letter. We do not aceapt letter" 
            
        
                   

    
    
    
