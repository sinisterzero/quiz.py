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




#question one
print("""what is 1+1?
1) 11
2) 2
3) window
4) 3""")
#call functiom
askquestion(0,1,2)

#question 2
print("""what Empire started from Italy?
1) France")
2) Britain
3) Roman Empire
4) Holy roman empire""")

askquestion(0,2,3)

#question 3
print("""if a = 2 and b = 4. What is ab?
1) 8
2) 2
3) 24
4) 6""")

askquestion(0,3,1)

#question 4
print("""what the shape of the Earth?
1) Sphere
2) circle
3) flat
4) rectangle""")

askquestion(0,4,1)

#question 5
print("""what is flammable?
1) iron
2) water
3) alcohol
4) coppor""")

askquestion(0,5,3)

#question 6
print("""what is 6666?
1) god
2) holy
3) savior
4) The devil""")

askquestion(0,6,4)

#question 7
print("""what is the lucky number?
1) 6666
2) 4
3) 0
4) 7""")

askquestion(0,7,4)

#question 8
print("""what is square root of 16
1) 2
2) 8
3) 4
4) 6""")

askquestion(0,8,3)

#question 9
print("""In lord of the ring what was everyone after?
1) ring
2) hobbit
3) orc
4) sword""")

askquestion(0,9,1)

#question 10
print("""What 9*4*5*3*5(2)^2+10000-69-69+5+2+3+5/6*500*4*0+1
1) what?
2) 78994
3) 1966794
4) 1""")

askquestion(0,10,4)




print(score*10, "%")

