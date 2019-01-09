
def askquestion(check, uanswer, correctanswer):
    while check == 0:
        try:
            uanswer = int(input("input 1, 2, 3 or 4 as your answer  "))
            #check if answer correct
            if uanswer == correctanswer:
                check += 1
            #check if answer is acceatpable
            elif 0 < uanswer < 5:
                check -= 1
            #check if user enter a  unaceatpable number
            else:
                print("you input a unaceaptable option that does not euansist as one of the 4 answer listed")   
    #check if user putted a string or float 
        except ValueError:
            print("you inputted a letter. We do not aceapt letter")




#question one
print("what is 1+1?")
# 4 answers option
print("1) 11")
print("2) 2")
print("3) winadow")
print("4) 3")

askquestion(0,1,2)

#question 2
print("what Empire started from Italy?")
# 4 answers option
print("1) France")
print("2) Britain")
print("3) Roman Empire")
print("4) Holy roman empire")

askquestion(0,1,3)
