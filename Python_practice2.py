##if statements
counties = ["Arapahoe", "Denver", "Jefferson"]
#if counties[1] == "Denver":
#    print(counties[1])

if "Arapahoe" in counties:
    print("True")
else: 
    print("False")

##if-else statement
#temperature = int(input("What is the temperature outside?"))
#if temperature > 80:
#    print("Turn on the AC.")
#else:
#    print("Open the windows.")

##What is the score?
#score = int(input("What is your test score? "))

#Determine the grade. Method 1
#if score >= 90:
#    print('Your grande is an A.')
#else:
#    if score >= 80:
#        print('Your grade is a B.')
#    else:
#        if score >= 70:
#            print('Your grade is a C.')
#        else:
#            if score >= 70:
#                print('Your grade is a D.')

#Determine the grade. Method 2 (preffered)
#if score >= 90:
#    print('Your grade is an A.')
#elif scoure >= 80:
#    print('Your grade is a B.')
#elif score >= 70:
#    print ('Your grande is a C.')
#else:
#    print('YOur grade is a D.')
