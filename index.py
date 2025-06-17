# def display_student_summary(numbers : int):
#     students = [[], []] 
#     for number in range(numbers):
#         name = input("Name of student number " + str(number + 1) + ": ")
#         grade = input("grade of student number " + str(number + 1) + ": ")
#         students[0].append(name)
#         students[1].append(grade)

#     print("\nSummary:")
#     for number in range(numbers):
#         print("Student", number + 1, ":", students[number][0], "- Grade:", students[number][1])
#     return students
    
# num = int(input("select the number of students "))
# students=display_student_summary(num)
# print(students[0][0])
# print(students[0][1])
# print(students[1][0])
# print(students[1][1])
# print(students[0][2])
# print(students[1][2])


def display_student_summary(numbers : int):
    names=[]
    grades=[]
    for number in range(numbers):
        name = input("Name of student number " + str(number + 1) + ": ")
        # if grade<0:
        #     grade=0
        # elif grade>100:
        #     grade=100
        names.append(name)
        while True:     
            grade = input("Grade of student number " + str(number + 1) + ": ")
            if int(grade) >=0 and int(grade) <=100:
                grades.append(int(grade))
                break
            else:
                print(" The Grade Should Be Between 0 and 100")
     
          
   
    for number in range(numbers):
        print("Student", number + 1, ":", names[number], "and the Grade is:", grades[number])
    return names,grades    
        
        
def get_avg_grade(grades):
    totalgrade = 0
    for grade in (grades):
       totalgrade +=grade
    avg= totalgrade/len(grades)
    print("The Grades Average is :",avg) 
     

def get_heighest_grade(names,grades):
    highest_grade=0
    for grade in range(len(grades)):
        if grades[grade]>highest_grade:
            highest_grade=grades[grade]
            student=names[grade]
    print("The Student",student,"got the highest grade :",highest_grade)  
      
def count_passed(grades,iteration:int):
    if iteration==len(grades):
        return 0
    if grades[iteration]>=60:
        count=1
    else:
        count=0
    return count + count_passed(grades,iteration+1)
         
     
    
     
           
num = int(input("select the number of students "))
if num < 1:
    print("Welcome to our program. You cannot continue the process if there are no students. Thank you.")
    exit() 
names,grades=display_student_summary(num)
get_avg_grade(grades)
get_heighest_grade(names,grades)
print("The Number of Passed Student is:",count_passed(grades,0))