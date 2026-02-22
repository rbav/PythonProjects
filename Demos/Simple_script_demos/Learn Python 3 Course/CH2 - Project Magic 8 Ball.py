# CH2 - Project Magic 8 Ball
## Program is utilized to learn how to use if statements and random number modules
## Magic 8-Ball program
## magic8.py
## Code by NOVA_TAGO
import random
random_number = random.randint(1,12)
print(random_number)

variable = random_number
name = ""
qstate = "Is this a program"
Program = "Magic 8-Ball's answer: "


if variable == 1 and qstate != "":
  answer = "Yes - definitely"
elif variable ==2 and qstate != "":
  answer = "It is decidedly so"
elif variable == 3 and qstate != "":
  answer = "Without a doubt"
elif variable == 4 and qstate != "":
  answer = "Reply hazy, try again"
elif variable == 5 and qstate != "":
  answer = "Ask again later"
elif variable == 6 and qstate != "":
  answer = "Better not tell you now"
elif variable == 7 and qstate != "":
  answer = "My sources say no"
elif variable == 8 and qstate != "":
  answer = "outlook not so good"
elif variable == 9 and qstate != "":
  answer = "Very doubtful"
elif variable == 10 and qstate != "":
  answer = "I didnt see that coming"
elif variable == 11 and qstate != "":
  answer = "What did you just ask?"
elif variable == 12 and qstate != "":
  answer = "... I dont have time for you..."
else:
  answer = "ERROR"
  print("Error")

if name == "" and qstate != "":
  print("Question: " + qstate)
  print(Program + answer)
else:
  print(name + " asks: " + qstate)
  print(Program + answer)