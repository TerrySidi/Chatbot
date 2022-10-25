print("Hello! I'm the squad six chatbot. How may i help you today?")
while True:
 input("Press [enter] to continue.")
 questions = ["Tell me about the squad","Tell me about their home countries","Tell me about the Squads Teaching assistant","Tell me a programming joke","Exit"]
 for (i,questions) in enumerate(questions):
  print(f"{i+1}. {questions}")

 print()

 user_choice = input("Choose a number:")

 squad6_members = ["Terry S","Beatrice K","Israel B","Ige O","Audrey G","Oluwaseyfunmi A","Adetomiwa B","Godwin A","Marshall"]

 home_country = ["Terry S is a young lady from Kenya","Beatrice K is a young lady from Kenya","Israel B is a young gentleman from Nigeria","Ige O is a young man from Nigeria","Audrey G is a young lady from Uganda","Oluwaseyfunmi A is a young lady from nigeria","Adetomiwa is a young man from Nigeria","Godwin A is a young man from Nigeria","Marshall is a young man from Nigeria"]

 teaching_assistant = ("The Teaching assistant of squad six is Mr Stanley U.He is a tech enthusiast and proffessional working with a reputable tech industry in Nigeria,Africa.He is patient,committed and outgoing not forgetting his good taste for music ")

 programming_joke = ("I just saw my life flash before my eyes and all I could see was a close tag…")

 if user_choice == "1":
  print("Squad six members are young tech enthusiasts who recently met in the Try Kibo program to acquire skills in tech and learn a new programming language:python.These are the members in squad six:")
  for (members,squad6_members) in enumerate(squad6_members):
    print(f"{members+1}.{squad6_members}")

  user_choice2 = input("Pick a squad member:")
  if user_choice2 == "1":
    print(squad6_members[0] + "is a final year student persuing Computer science and majoring in software development.She is a tech enthusiast who loves travelling apart from programming")    
  elif user_choice2 == "2":
    print(squad6_members[1] + "is a young lady doing sound engineering.She loves listening to music when bored and loves art")
  elif user_choice2 == "3":
    print(squad6_members[2] + "is a young man that has a passion in tech and is currently going through a tech program so as to acquire more tech skills")
  elif user_choice2 == "4":
    print(squad6_members[3] + "is a young tech enthusiast witha passion in tech and is currently going through a tech program so as to acquire more tech skills")
  elif user_choice2 == "5":
    print(squad6_members[4] + "is a young lady with a passion for tech and programming as a whole.She loves trying and acquiring new skills so as to improve her problem solving abilities")
  elif user_choice2 == "6":
    print(squad6_members[5] + "is a young lady doing medicine but with a passion for tech and currently learning a new programming language to expand her skills ")
  elif user_choice2 == "7":
    print(squad6_members[6] +"is a young tech enthusiast with a passion in tech and is currently going through a tech program so as to acquire more skills")
  elif user_choice2 == "8":
    print(squad6_members[7] + "is a young tech enthusiast with a passion in tech and is currently going through a tech program to acquire more skills")
  elif user_choice2 == "9":
    print(squad6_members[8] + "is a young tech enthusist with a passion in tech and is currently going through a tech program to acquire more skills")
  else:
    print ("You have to enter a number between 1 and 9")
    
 elif user_choice == "2":
  print("Squad six members are from different countries.")
  for (members,squad6_members) in enumerate(squad6_members):
    print(f"{members+1}.{squad6_members}")
    
  user_choice3 = input("Pick a number to continue:")
  if user_choice3 == "1":
    print(home_country[0])
  elif user_choice3 == "2":
    print(home_country[1])
  elif user_choice3 == "3":
    print(home_country[2])
  elif user_choice3 == "4":
    print(home_country[3])
  elif user_choice3 == "5":
    print(home_country[4])
  elif user_choice3 == "6":
    print(home_country[5])
  elif user_choice3 == "7":
    print(home_country[6])
  elif user_choice3 == "8": 
    print(home_country[7])
  elif user_choice3 == "9":
    print(home_country[8])

 elif user_choice == "3":
  print(teaching_assistant)

 elif user_choice == "4":
  print(programming_joke)
 elif user_choice == "5":
   break


 else:
   print("please enter a number betweem 1 and 5")