# Houses
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

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