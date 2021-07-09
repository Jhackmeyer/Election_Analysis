counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] =='Denver':
    print(counties[1])

score = int(input("What is your test score?"))
if score >=90:
    print("You got an A")
else:
    if score >=80:
        print("You got a B")
    else:
        if score >=70:
            print("You got a C")
        else:
            if score >=60:
                print("You got a D")
            else:
                print("You fail")

