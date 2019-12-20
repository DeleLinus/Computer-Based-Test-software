from tkinter import *
class  CBT:
	def __init__(self):
		self.root=Tk()
		self.QA={"Who is the president of Nigeria?":"Buhari", "What is the product of 2 and 6?":\
    	"12", "Which State in Nigeria is SQI college located?": "Oyo State","What Language is this program written?":\
    		"Python"}
		self.root.mainloop()
exam=CBT()







'''
#3_CBT
#in this case, the key is made the answer to the questions
#from string import punctuations
QA={"Who is the president of Nigeria?":"Buhari", "What is the product of 2 and 6?":\
    "12", "Which State in Nigeria is SQI college located?": "Oyo State","What Language is this program written?":\
    "Python"}
O_List=["(a) Jega (b) Omasola (c) Buhari","(a) 10 (b) 12 (c) 1","(a) Enugu State (b) Oyo State (c) Ondo State",\
      "(a) Anaconda (b) Python (c) Java"]
O_count=0
A_count=0
for i in QA:
    print(i)
    print(O_List[O_count])
    O_count+=1
    UA=input("Enter the correct Answer (Note: as written in the options):")
    print("\n")
    if UA.lower()==QA[i].lower():
        A_count+=1
        #print("You got " ,A_count, " out of ", O_count, " correctly")
    else:
        continue
print ("Your score is ",A_count, " over ", O_count, )'''