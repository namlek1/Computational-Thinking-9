#beggining 
introvert_points = 0
extrovert_points = 0
ambivert_points  = 0

# middle
answer = input("would you rather A) work alone, or B) work in a group, or c) depends on the work")
if answer == "A":
	introvert_points += 1
elif answer == "B":
	extrovert_points += 1 
elif answer == "C":
	ambivert_points += 1


answer = input("would you rather A) eat alone, or B) go out and eat with other people, or c) both depends how I feel")
if answer == "A":
	introvert_points += 1
elif answer == "B":
	extrovert_points += 1
elif answer == "C":
	ambivert_points += 1


answer = input("Would you rather A) write or text, or B) talk in person, or c) text but when its important in person")
if answer == "A":
	introvert_points += 1
elif answer == "B":
	extrovert_points += 1
elif answer == "C":
	ambivert_points += 1	

#question 4 
answer = input("Would you rather A) be home schooled, or B) normal school, or c) both sound fun")
if answer == "A":
	introvert_points += 1
elif answer == "B":
	extrovert_points += 1
elif answer == "C":
	ambivert_points += 1	


answer = input("Would you rather A) spend free time at home relaxing, or B) spend time with other people, or c) both depends how I feel")
if answer == "A":
	introvert_points += 1
elif answer == "B":
	extrovert_points += 1
elif answer == "C":
	ambivert_points += 1	



# end of quiz:
if introvert_points > extrovert_points:
	print("You are a introvert")
elif extrovert_points > introvert_points:
	print("You are a extrovert")
elif
	print("your a ambivert ")


