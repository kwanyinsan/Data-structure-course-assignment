import os

class Student:
    def __init__(self, sid=None, name=None, gender=None, pid=None):
        if sid is None:
            self.id = ""
        else: self.id = sid
        if name is None:
                self.name = ""
        else:
            self.name = name
        if gender is None:
                self.gender = ""
        else:
            self.gender = gender
        if pid is None:
                self.pid = ""
        else:
            self.pid = pid




def menu():
	os.system('cls')
	print("\n")
	print("\n")
	print("\n")
	print("        Please type 0-11 for student record action")
	print("        1 - Return the size of the list")
	print("        2 - Append a new record at the end")
	print("        3 - Insert a new record at position i")
	print("        4 - Delete the record at position i")
	print("        5 - Search a record based on student ID")
	print("        6 - Display the record at position i")
	print("        7 - Display all the records")
	print("        8 - Save data in 'data.txt'")
	print("        9 - Load data from 'data.txt'")
	print("       10 - Display Programmes")
	print("       11 - Programme Statistics")
	print("        0 - Quit")
	print("\n")
	print("	Your choice: ", end='')
	choice=int(input())
	print("\n")
	print("\n")
	print("\n")
	return choice

def inputstinfo():
        sid = input("Please input the student's id: ")
        name = input("Please input the student's name: ")
        gender = input("Please input the student's gender: ")    
        pid = input("Please input the student's program id: ")
        tmps = Student(sid, name, gender, pid)
        return tmps;

def displaystinfo(student):
        print(f"The student's info are: {student.id}, {student.name}, {student.gender}, {student.pid}.")


