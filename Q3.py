# Consider the following array [{id:1, name:"rajesh"}, {id:2, name:"rahul"}, {id:3, name:"sruthi"}] Write a program to accept a number and print the name of the student with that id.

students = [
    {"id" : 1, "name": "rajesh"},
    {"id" : 2, "name": "rahul"},
    {"id" : 3, "name": "sruthi"}
]
input_id = int(input("Enter student ID : "))
found = False

for student in students :
    if student ["id"] == input_id:
        print ("Student Name: ", student ["name"])
        found =True
        break
if not found:
    print ("Student with given ID not found")