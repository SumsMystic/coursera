'''
Created on Apr 2, 2018

@author: Sumeet Agrawal
'''

score = input("Enter Score: ")
fscore = float(score)

if(fscore > 0.0):
    if(fscore < 1.0):
        if(fscore >= 0.9):
            print("A")
        elif(fscore >= 0.8):
            print("B")
        elif(fscore >= 0.7):
            print("C")
        elif(fscore >= 0.6):
            print("D")
        else:
            print("F")
    else:
        print("Invalid input")
else:
    print("Invalid input")