answer = input("Are you ready for your Msoma exams?(y/n) ")

if answer.lower().strip() == "y":

    answer = input("Sitting for these exams is what will determine if you will proceed to the next level. Would you like to sit for them now or later?")
    if answer == "now":
        answer == input("Go to room 1 Red. Are you in the machine learning or entry class?")

        if answer == "entry class":
            print("You will sit for your exams in the morning")
        else:
            print("You will sit for your exams in the afternoon")

    elif answer == "later":
        print ("You will have to retake the entry course")

    else:
         print ("Thats an invalid choice. You only had two choices!")

else:
    print("That's too bad! You have had enough time to prepare")
