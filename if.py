age=int(input("enter your age:"))
nationality=input("enter your country")
if age>=18 and nationality=="kenyan":
    print("eligible to vote")
elif age<18 and  nationality=="kenyan":
    print("under age")
elif age>=18 and nationality !="kenyan":
    print("not kenyan")
else: 
    print("not eligible to vote")