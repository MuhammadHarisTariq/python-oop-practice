class Student:
    
    def __init__(self,myname,sub1_marks,sub2_marks,sub3_marks,no_of_subject):
        self.name = myname

        self.Sub1 = sub1_marks
        self.Sub2 = sub2_marks
        self.Sub3 = sub3_marks
        self.no_of_subject = no_of_subject
        
    def averageMarks(self):
        totalmarks = self.Sub1 + self.Sub2 + self.Sub3
        average = self.Sub1 + self.Sub2 + self.Sub3 / self.no_of_subject
        print("Total Marks is:",totalmarks)
        print("Average Marks is:",average)
        
std_name = input("Enter your Name:")
std_no_of_sub = int(input("Enter your number of subjects:"))
std_Sub_1_marks = int(input("Enter your Subject 1 Marks : "))
std_Sub_2_marks = int(input("Enter your Subject 2 Marks : "))
std_Sub_3_marks = int(input("Enter your Subject 3 Marks : "))

s1 = Student(std_name,std_Sub_1_marks,std_Sub_2_marks,std_Sub_3_marks,std_no_of_sub)

print("Name:",s1.name)
print("Sub 1 Marks:",s1.Sub1)
print("Sub 2 Marks:",s1.Sub2)
print("Sub 3 Marks:",s1.Sub3)
s1.averageMarks()


        

        
        