# score
global score
score = int(0)
def askquestion(check, uanswer, correctanswer):
    while check == 0:
        try:
            uanswer = int(input("input 1, 2, 3 or 4 as your answer  "))
            #check if answer correct
            if uanswer == correctanswer:
                #add score
                check += 1
                global score
                score += 1
            #check if answer is acceatpable
            elif 0 < uanswer < 5:
                check -= 1
            #check if user enter a  unaceatpable number
            else:
                print("you input a unaceaptable option that does not euansist as one of the 4 answer listed")   
    #check if user putted a string or float 
        except ValueError:
            print("you inputted a letter. We do not aceapt letter")

