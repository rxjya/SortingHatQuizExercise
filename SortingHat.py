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