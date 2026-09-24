#student management project-1 

# ADD STUDENT
   
def add_student():
    roll_no = input("Enter Roll No.:")
    with open("student.txt" , "r") as f:
        for line in f: 
            nums = line.split(",")

            if nums[0] == roll_no:
                print("Roll No. Already Exists!")
                return
        
    name = input("Enter Name:")
    while True:

         try:
            marks = int(input("Enter Marks:"))

            if 0<= marks <=100:
                break
            else:
                print("Marks should be between 0 and 100")
   
         except:
            print("Invalid Input(ENTER NO. ONLY!)")
        

    category = input("Enter Category:")
    
    with open("student.txt" , "a") as f:
        f.write(f"{roll_no},{name},{marks},{category}\n")

    print(f"""
        Student Added Successfully!
        Roll No:{roll_no}
        Name:{name}
        Marks:{marks}
        Category:{category}
        """) 
    
#VIEW STUDENT

def view_student():
    with open("student.txt" , "r") as f:
        count = 1
 
        for line in f:
            nums = line.split(",")

            print("=====================================")
            print("Student",count)
            print("Roll No:",nums[0])
            print("Name:",nums[1])
            print("Marks:",nums[2])
            print("Category:",nums[3])
            print("=====================================")
        
            count+=1

#SEARCH STUDENT

def search_student():
    number = input("Enter Roll No. To Search:")
    found = False

    with open("student.txt" , "r") as f:
        line_no = 1
        for line in f:
            nums = line.split(",")

            if nums[0] == number:
                line_no += 1
                found=True
                print("Details found at Line No.:" , line_no)
                print("Roll No:", nums[0])
                print("Name:", nums[1])
                print("Marks:", nums[2])
                print("Category:", nums[3])
            
        if found == False:
            print("Student Not Found")

#UPDATE STUDENT

def update_student():
    roll_no = input("Enter Roll No. to Update: ")
    new_name = input("Enter New Name: ")
    new_marks = int(input("Enter New Marks: "))
    new_category = input("Enter New Category: ")

    updated_data = []

#read the old data

    found = False
    with open("student.txt" , "r") as f:
        for line in f:
            nums = line.split(",")
            if nums[0] == roll_no:
                found = True
                updated_data.append(f"{roll_no},{new_name},{new_marks},{new_category}\n")
            
            else:
                updated_data.append(line)

#write the updated data
    
    with open("student.txt" , "w") as f:
        for data in updated_data:
            f.write(data)
    
    if found:
           print("Student Updated Successfully!")
    else:
        print("Student Not Found!")

#DELETE STUDENT

def delete_student():
    number = input("Enter The Roll No. Delete:")
    updated_data = []
    found = False
    
    with open("student.txt" , "r") as f:
        for line in f:
            nums = line.split(",")
            if nums[0] == number:
                found = True
                continue
            else:
                updated_data.append(line)
    
    with open("student.txt" , "w") as f:
        for line in updated_data:
            f.write(line)
        
    if found:
        print("Student Deleted Successfully!")
    else:
        print("Student Not Found")

#TOTAL STUDENT

def total_student():
    count = 0
    with open("student.txt" , "r") as f:
        for line in f:
            count+=1
        print("Total Student:" , count)

#TOPPER STUDENT

def topper_student():
    with open("student.txt" , "r") as f:
        max_mark = 0
        topper_roll = ""
        topper_name = ""
        topper_category = ""

        for line in f:
            nums = line.split(",")
            marks = int(nums[2])

            if (marks>max_mark):
                max_mark = marks
                topper_roll = nums[0]
                topper_name = nums[1]
                topper_category = nums[3]
        
        print(topper_roll)
        print(topper_name)
        print(max_mark)
        print(topper_category)

#AVERAGE MARKS

def average_mark():
    with open("student.txt","r") as f:
        total_marks = 0
        count = 0
        for line in f:
            count+=1
            nums = line.split(",")
            marks = int(nums[2])
            total_marks += marks

        if count == 0:
            print("No Students Available")
        else:
            print("Average Marks:",total_marks/count)

#SEARCH NAME
 
def search_name():
    name = input("Enter The Name To Search:")
    found = False

    with open("student.txt","r") as f:
        line_no = 0
        for line in f:
            nums = line.split(",")
            line_no +=1
            if nums[1] == name:
                found = True
                print("Details found at Line No.:" , line_no)
                print("Roll No:", nums[0])
                print("Name:", nums[1])
                print("Marks:", nums[2])
                print("Category:", nums[3])
            
        if found == False:
             print("Student Not Found")

#SEARCH CATEGORY

def search_category():
    category = input("Enter Category:").upper()
    found = False

    with open("student.txt" , "r") as f:
        line_no = 0

        for line in f:
            nums = line.split(",")
            line_no+=1
            if nums[3].strip().upper() == category:
                found= True
                print("==============================================")
                print("Details found at Line No.:" , line_no)
                print("Roll No:", nums[0])
                print("Name:", nums[1])
                print("Marks:", nums[2])
                print("Category:", nums[3])
                print("----------------------------------------------")
        if found == False:
            print("Student Not Found!")

#*SORT STUDENTS

def sort_student():
    student = []
    with open("student.txt", "r") as f:
        for line in f:
            nums = line.split(",")
            marks = int(nums[2])

            student.append([nums[0]
                            ,nums[1],
                            nums[2],
                            nums[3].strip()
                            ])

    student.sort(key=lambda x:x[2],reverse = True)
    for data in student:
        print(data)

#RANK LIST

def rank_list():
    student = []
    with open("student.txt" , "r") as f:
        for line in f:
            nums = line.split(",")
            marks = int(nums[2])

            student.append([nums[0],nums[1],nums[2],nums[3].strip()])

    student.sort(key=lambda x:x[2],reverse=True)
    rank = 1
    print("="*60)
    print(f"{'Rank':<6}{'Roll No':<10}{'Name':<20}{'Marks':<10}{'Category':<10}")
    print("="*60)

    for data in student:
        print(f"{rank:<6}{data[0]:<10}{data[1]:<20}{data[2]:<10}{data[3]:<10}")
        rank+=1
        
#PASS/FAIL COUNT.
def pass_count():
    pass_count = 0
    fail_count = 0
    with open("student.txt" , "r") as f:
        for line in f:
            nums = line.split(",")
            marks = int(nums[2])
            if marks >= 35:
                pass_count +=1
            elif marks <35:
                fail_count +=1
        print("Total Student:",pass_count + fail_count)
        print("Pass Student:",pass_count)
        print("Fail Student:",fail_count)


# STUDENT STATISTICS

def stu_statistics():
    with open("student.txt","r") as f:
        total_student = 0
        pass_count = 0
        fail_count = 0
        Total_marks = 0
        Highest_marks = 0
        open_count = 0
        obc_count = 0
        sc_count = 0
        st_count = 0
        ews_count = 0
        ebc_count = 0

        for line in f:
            total_student +=1
            nums = line.split(",")
            marks = int(nums[2])
            Total_marks+=marks

            if (marks>Highest_marks):
                Highest_marks = marks
            else:
                pass


            if (marks>=35):
                pass_count += 1
            elif (marks<35):
                fail_count += 1

            category = nums[3].strip().upper()


            if category == "OPEN":
                open_count +=1
            elif category == "OBC":
                obc_count +=1
            elif category == "SC":
                sc_count += 1
            elif category == "ST":
                st_count += 1
            elif category == "EBC":
                ebc_count += 1
            elif category == "EWS":
                ews_count += 1
        avg_marks = int(Total_marks/total_student)

        print("=" *60 )
        print(" " * 18 , "STUDENTS SUMMARY")
        print("="*60)
        print()

        print("📚 General Information")
        print("-"*60)
        print(f"Total Students          :{total_student}")
        print(f"Average Marks           : {avg_marks:.2f}")
        print(f"Highest Marks           :{Highest_marks}")
        print()

        print("-"*60)
        print("📈Result Summary")
        print("-"*60)
        print(f"Pass                    :{pass_count}")
        print(f"Fail                    :{fail_count}")
        print()

        print("-"*60)
        print("👥Category Distribuution")
        print("-"*60)
        print(f"OPEN                    :{open_count}")
        print(f"OBC                     :{obc_count}")
        print(f"SC                      :{sc_count}")
        print(f"ST                      :{st_count}")
        print(f"EWS                     :{ews_count}")
        print(f"EBC                     :{ebc_count}")

        print("=" * 60)


        

def menu():
        while True:
            print("="*60)
            print(" "*18 ,"STUDENT MANAGEMENT SYSTEM")
            print("="*60)
            while True:
                try:
                    main_choice = int(input("""


1)Student Operation
2)Reports
3)Exit


Enter Choice: """)) 
                    break

                except ValueError:
                    print("\nInvalid Input ! Please enter a number.\n")
            if main_choice == 1:
                while True:
                    print("="*60)
                    print(" "*18 ,"Student Operation")
                    print("="*60)

                    while True:
                        try:
                            
                            operation_choice =int(input("""
                    1)Add Student
                    2)View Student
                    3)Search Student
                    4)Update Student
                    5)Delete Student
                    6)Back

                    Enter Choice: """))
                            break

                        except ValueError:
                            print("\nInvalid Input! Please enter a number.\n")

                    if operation_choice == 1:
                        add_student()

                    elif operation_choice == 2:
                        view_student()

                    elif operation_choice == 3:
                        while True:

                            try:
                                
                                search_choice = int(input("""========= Search Student =========
                            
                            1)Search by Roll No.
                            2)Search by Name
                            3)Search by Category
                            4)Back

                            Enter Choice:"""))
                                break

                            except ValueError:
                                print("\nInvalid Input! Please enter a number.\n")
                            
                            
                            if search_choice == 1:
                                search_student()
                            elif search_choice == 2:
                                search_name()
                            elif search_choice == 3:
                                search_category()
                            elif search_choice == 4:
                                break

                    elif operation_choice == 4:
                        update_student()

                    elif operation_choice == 5:
                        delete_student()

                    elif operation_choice == 6:
                        break


            elif main_choice == 2:
                while True:
                    print("="*60)
                    print(" "*18 ,"Reports")
                    print("="*60)
                    print()
                    while True:
                        try:

                            report_choice = int(input("""
1)Total Student
2)Topper Sudent
3)Average Marks
4)Rank List
5)Pass/Fail Count
6)Student Statistics
7)Sort Student
8)Back

Enter Choice:"""))
                            break

                        except ValueError:
                            print("\nInvalid Input! Please enter a number.\n")
                    print("-"*60)
                    if report_choice == 1:
                        total_student()

                    elif report_choice == 2:
                        topper_student()

                    elif report_choice == 3:
                        average_mark()

                    elif report_choice == 4:
                        rank_list()

                    elif report_choice == 5:
                        pass_count()

                    elif report_choice == 6:
                        stu_statistics()

                    elif report_choice == 7:
                        sort_student()

                    elif report_choice == 8:
                        break


            elif main_choice == 3:
                print("👋THANK YOU FOR USING OUR SERVICE!")
                break

            else:
                print("Invalid Choice!")

import time

print("=" * 60)
print(f"{'WELCOME TO STUDENT MANAGEMENT SYSTEM':^60}")
print("=" * 60)
print(f"{'Version : 2.1':^60}")
print(f"{'Developed by Sanskar':^60}")
print("=" * 60)

time.sleep(2)

menu()

