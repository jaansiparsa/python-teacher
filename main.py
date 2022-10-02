print("All questions are from the PowerPoint 'MTA: Python' created by my AP CSP teacher (who I will not name because "
      "I think it's identifiable information)/AP CSP class, or the practice Python tests: ")
import turtle
import time
import random
import keyboard
from question_library import question_generator
from question_library import QList
from question_library import QDict

wn = turtle.Screen()

print("A: Perform Operations Using Data Types and Operators\nB: Control Flow with Decisions and Loops\nC: Document and Structure Code\nD: Perform Troubleshooting and Error Handling\nE: Perform Input and Output Operations\nF: Perform Operations Using Modules and Tools\nALL: all of the above")
category = input("Type A, B, C, D, E, F, or ALL depending on which category you would like to practice. Or, type ESC to stop.")

while category.upper() != "ESC":
      print("Type the letter that corresponds with your answer.")
      question_generator(category)
      category = input("Type A, B, C, D, E, F, or ALL depending on which category you would like to practice. Or, type ESC to stop.")



wn.mainloop()
