# Create a program that accepts marks for five subjects, calculates the total, average, percentage, and assigns a grade based on the percentage.

mark1 = int(input("Enter marks of subject 1: "))
mark2 = int(input("Enter marks of subject 2: "))
mark3 = int(input("Enter marks of subject 3: "))
mark4 = int(input("Enter marks of subject 4: "))
mark5 = int(input("Enter marks of subject 5: "))
total_marks = mark1+mark2+mark3+mark4+mark5
print(f"Total marks: {total_marks}/500")
print("Average: ",total_marks/5)
percentage=(total_marks/500)*100
print("percentage: ",percentage,"%")
if percentage >=75:
    print("grade A")
elif percentage >=50 and percentage < 75:
    print("grade B")
elif percentage >=33 and percentage < 50:
    print("grade c")
else:
    print("fail")
