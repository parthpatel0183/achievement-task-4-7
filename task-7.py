# File name: task-7.py
# Author: Dane Wills
# Date created: 10/28/2022
# Date last modified: 10/29/2022


firstname = input('Enter the firstname of the student: ') #this code asks the user to input his/her firstname
lastname = input('Enter the lastname of the student: ')   #this code asks the user to input his/her lasttname
Studentnumber = input('Enter the studentnumber of the student: ')  #this code asks the user to input his/her studentnumber

my_dict = {''' 'Course1': 'Career Success', 'Course code': 1830 
        'Course2': 'Readind and writing', 'Course code': 4566
        'Course3': 'IT infrastructure', 'Course code': 3908
        'Course4': 'Networking Basics', 'Course code': 7855 '''}  #this code gives the list of the courses.

print(my_dict)  #this code print the dictionary
list = []                                                      
Course_list = input("Please enter course code"  +  " list : ") #user needs to give the courses that he/she wants to register for
list.append(Course_list)
list = Course_list.split(",") #this code puts separate the course in the list 
print('List : ',list)   #this code print the list of the courses that are registered



