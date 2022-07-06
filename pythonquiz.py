print("welcome to python quiz")

playing=input("do you want to play :")

if playing.lower()!="yes":
    quit()
print("okay!lets play...")
score=0
answer=input("who developed python?")
if answer.lower()=="guido van rossum" :
    print("correct!")
    score=+1
else:
    print("incorrect!")

answer=input("what is the correct extension of visual code?")
if answer.lower()==".py":
    print("the second answer is right!")
    score=score+1
else:
    print("incorrect answer!")

answer=input("what do we use to define a block of code?")
if answer.lower()=="indentation":
    print("the thrid answer is right!")
    score=score+1
else:
    print("incorrect!")

answer=input("what are the comments?")
if answer.lower()=="single-comments":
    print("the fourth answer is right!")
    score=score+1
else:
    print("incorrect answer!")

answer=input("what are the datatypes?")
if answer.lower()=="numbers":
    print("the fifth answer is right!")
    score=score+1
else:
    print("incorrect answer!")

answer=input("what are the conditional statements?")
if answer.lower()=="if statement":
    print("the six answer is right!")
    score=score+1
else:
    print("incorrect answer!")

answer=input("what are entity of a class?")
if answer.lower()=="objects":
    print("the seventh answer is right!")
    score=score+1
else:
    print("incorrect answer!")

answer=input("what are collections of objects called?")
if answer.lower()=="classes":
    print("the eighth answer is right!")
    score=score+1
else:
    print("incorrect answer!")

answer=input("what are the specified functions of the python?")
if answer.lower()=="aruguments":
    print("the ninth answer is right!")
    score=score+1
else:
    print("incorrect answer!")

answer=input("what are the syntax errors also called as?")
if answer.lower()=="prasing errors":
    print("the tenth answer is right!")
    score=score+1
else:
    print("incorrect answer!")
print("you got "+str(score)+"questions correct!")
print("you have got:"+str((score/10)*100)+"%")