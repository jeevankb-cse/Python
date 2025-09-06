a1=int(input("Enter the subject1 marks :"))
a2=int(input("Enter the subject2 marks :"))
a3=int(input("Enter the subject3 marks :"))

#Check for total percentage
total_percentage=(100)*(a1+a2+a3)/300

if(total_percentage>=40 and a1>=33 and a2>=33 and a3>=33 ):
    print("Student has Passed best of luck for next year:",total_percentage )

else:
    print("Student has Failed try again next year:",total_percentage)    
        