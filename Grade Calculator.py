print("Enter Marks Obtained in 5 Subjects: ")
markOne = float(input())
markTwo = float(input())
markThree = float(input())
markFour = float(input())
markFive = float(input())

total = markOne+markTwo+markThree+markFour+markFive
avg = total/5

if avg>=91 and avg<=100:
    print("Your Grade is A1")
elif avg>=81 and avg<91:
    print("Your Grade is A2")
elif avg>=71 and avg<81:
    print("Your Grade is B1")
elif avg>=61 and avg<71:
    print("Your Grade is B2")
elif avg>=51 and avg<61:
    print("Your Grade is C1")
elif avg>=41 and avg<51:
    print("Your Grade is D")
elif avg>=33 and avg<41:
    print("Your Grade is E")
elif avg>=0 and avg<33:
    print("Your Grade is F")
else:
    print("Invalid Input!")
