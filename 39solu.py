questions = [
  [
    "Which of the three banks will be merged with the other two to create India’s third-largest bank?", "Punjab National Bank", " Indian Bank", "Bank of Baroda ",
    "Dena Bank", "None", 2  #indian bank
  ],
  [
    "What is the name of the weak zone of the earth’s crust?", " Seismic", "Cosmic", "Formic",
    "Anaemic", "None", 1  #Seismic
  ],
  [
    "Where was India’s first national Museum opened?", "Delhi", "Hyderabad", "Rajasthan",
    "Mumbai", "none", 4  #mumbai
  ],
  [
    " In 2019, Which popular singer was awarded the Bharat Ratna award?", " Lata Mangeshkar", "Asha Bhosle", "Bhupen Hazarika ",
    " Manna Dey ", " none", 3  #bhupen hazarika
  ],
  [
    " The world’s nation 5G mobile network was launched by which country?", "Japan", "Asia", "South Korea",
    "Malaysia", " none", 3  #South Korea
  ],
  [
    "When was Pravasi Bhartiya Divas held in Varanasi?", "2017", "2015", "2019",
    "2020", "none ", 3  #2019
  ],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000]
money = 0
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 3):
      money = 10000
    elif(i == 5):
      money = 20000
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")