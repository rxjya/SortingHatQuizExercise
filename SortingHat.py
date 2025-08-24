# houses
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("The Sorting Hat Quiz")

#if statements for q1
answerq1 = int(input(" Q1)  Do you like Dawn or Dusk? 1) Dawn 2) Dusk - Enter your answer (1-2): "))
if answerq1==1:
  Gryffindor = Gryffindor+1 
  Ravenclaw = Ravenclaw+1
elif answerq1 == 2:
  Hufflepuff= Hufflepuff+1
  Slytherin= Slytherin+1
else:
  print("Wrong input")

# if statements for q2
answerq2 = int(input(" Q2) When I'm dead, I want people to remember me as: 1) The Good 2) The Great 3) The Wise 4) The Bold - Enter your answer (1-4): "))
if answerq2==1:
  Hufflepuff= Hufflepuff+2
elif answerq2==2:
  Slytherin= Slytherin+2
elif answerq2==3:
  Ravenclaw= Ravenclaw+2
elif answerq2==4:
  Gryffindor= Gryffindor+2
else:
  print("Wrong input.")

# if statements for q3
answerq3 = int(input(" Q3) Which kind of instrument most pleases your ear? 1) The violin 2) The trumpet 3) The piano 4) The drum - Enter your answer (1-4): "  ))
if answerq3==1:
  Slytherin= Slytherin+4
elif answerq3==2:
  Hufflepuff= Hufflepuff+4
elif answerq3==3:
  Ravenclaw= Ravenclaw+4
elif answerq3==4:
  Gryffindor= Gryffindor+4
else:
  print("Wrong input.")

# printing final scores for each house
print("Gryffindor: ", Gryffindor)
print("Hufflepuff: ", Hufflepuff )
print("Ravenclaw: ", Ravenclaw)
print("Slytherin: ", Slytherin)