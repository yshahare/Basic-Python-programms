# program total marks of 5 subjects, full marks is 100 and percentage of marks.input
# percentage >=80 --grade A   ,  percentage >=60 --grade B   percentage >=40 --grade C
# percentage <40 --grade C

subject1=int(input("Enter the 1 no:-"))
subject2=int(input("Enter the 2 no:-"))
subject3=int(input("Enter the 3 no:-"))
subject4=int(input("Enter the 4 no:-"))
subject5=int(input("Enter the 5 no:-"))
total=subject1+subject2+subject3+subject4+subject5
percent=(total/500)*100
print("percentage", percent)
print("Total Marks", total)
if percent>=80:
    print("Grade A")
elif percent>=60:
    print("Grade B")
elif percent >=40:
    print("Grade C")
elif percent <=40:
    print("Grade D")
else:
    print("fail")                