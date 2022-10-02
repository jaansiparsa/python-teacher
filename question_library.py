import turtle
import random
import keyboard
numRight = 0
numAttempted = 0

wn = turtle.Screen()
QDict = {"create_images/typesoperators_q1.gif": "C",
         "create_images/typesoperators_q2.gif": "B", "create_images/typesoperators_q3.gif": "C",  "create_images/typesoperators_q4.gif": "B",
         "create_images/typesoperators_q5.gif": "A", "create_images/typesoperators_q6.gif": "A", "create_images/typesoperators_q7.gif": "B",
         "create_images/typesoperators_q8.gif": "C", "create_images/typesoperators_q9.gif": "B", "create_images/typesoperators_q10.gif": "B",
         "create_images/typesoperators_q11.gif": "D", "create_images/typesoperators_q12.gif": "A", "create_images/typesoperators_q13.gif": "C",
          "create_images/typesoperators_q14.gif": "C", "create_images/typesoperators_q15.gif": "B", "create_images/typesoperators_q16.gif": "B",
          "create_images/typesoperators_q17.gif": "C", "create_images/typesoperators_q18.gif": "A", "create_images/typesoperators_q19.gif": "D",
          "create_images/typesoperators_q20.gif": "B", "create_images/typesoperators_q21.gif": "A", "create_images/typesoperators_q22.gif": "A"}

QList = []
for i in QDict.keys():
    QList.append(i)

def question_generator(category):
    AList = []
    BList = []
    CList = []
    DList = []
    EList = []
    FList = []
    for i in QList:
        if "typesoperators" in i:
            AList.append(i)
        if "decisions" in i:
            BList.append(i)
        if "docstructure" in i:
            CList.append(i)
        if "troubleshooting" in i:
            DList.append(i)
        if "inputoutput" in i:
            EList.append(i)
        if "modules" in i:
            FList.append(i)
    if category.upper() == "A":
        accuracy_checker(AList)
    elif category.upper() == "B":
        accuracy_checker(BList)
    elif category.upper() == "C":
        accuracy_checker(CList)
    elif category.upper() == "D":
        accuracy_checker(DList)
    elif category.upper() == "E":
        accuracy_checker(EList)
    elif category.upper() == "F":
        accuracy_checker(FList)
    elif category.upper() == "ALL":
        accuracy_checker(QList)
    else:
        print("Please try again and enter a valid input")

def accuracy_checker(list):
    global numRight
    global numAttempted
    turtle.clearscreen()
    tr = turtle.Turtle()
    random_question = random.choice(list)
    wn.addshape(random_question)
    correct = QDict[random_question]
    tr.shape(random_question)
    numAttempted += 1
    if keyboard.read_key() == correct.lower():
        print("y")
        numRight += 1
    accuracy = "{:.2f}".format((numRight / numAttempted) * 100)
    print(str(accuracy) + "%")
    accturtle = turtle.Turtle()
    accturtle.speed(200)
    accturtle.penup()
    accturtle.hideturtle()
    accturtle.setpos(-200, -300)
    accturtle.write("Current Accuracy: " + str(accuracy), font=("Arial", 30, "normal"))




## tr.shape(list[0]) - this puts shape on screen
