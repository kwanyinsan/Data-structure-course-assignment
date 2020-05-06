from listm import *
from studentm import *

students = List()

choice = menu() 
while (choice!=0):
    if (choice == 1):
        listlen = length(students)
        print(f"The size of the student list is {listlen}.")
        print("Press enter to continue.")
        input('')
    elif (choice == 2):
        student = inputstinfo()
        insert(students, length(students)+1, student)
        print("The appending function is done.")
        print("Press enter to continue.")
        input('')
    elif (choice == 3):
        print("Please input the position:", end='')
        position = int(input())
        student = inputstinfo()
        insert(students, position, student)
        print("The insertion function is done.")
        print("Press enter to continue.")
        input('')
    elif (choice == 4):
        print("Please input the position:", end='')
        position = int(input())
        delete(students, position)
        print("The deletion function is done.")
        print("Press enter to continue.")
        input('')
    elif (choice == 5):
        print("Please input the student id:", end='')
        sid = input()
        position = locatebyid(students, sid)
        if position < 0:
            print(f"Student with sid={sid} does not exist.")
        else:
            print(f"Student with sid={sid} is at position {position}")
        print("The locate function is done.")
        print("Press enter to continue.")
        input('')
    elif (choice == 6):
        print("Please input the position:", end='')
        position = int(input())
        student = get(students, position)
        if student != -1:
            displaystinfo(student)
        else:
            print(f"There is no student at position {position}")
        print("The get function is done.")
        print("Press enter to continue.")
        input('')
    elif (choice == 7):
        for i in range(1, length(students)+1):
            student = get(students, i)
            displaystinfo(student)
        print("The display function is done.")
        print("Press enter to continue.")
        input('')
    elif (choice == 8):
        with open("data.txt", "w") as f:
            for i in range(1, length(students)+1):
                student = get(students, i)
                f.write(f"{student.id},{student.name},{student.gender},{student.pid}\n")
            f.close()
        print("The save function is done.")
        print("Press enter to continue.")
        input('')
    elif (choice == 9):
        with open("data.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                parts = line.split(",")
                tmps = Student(parts[0], parts[1], parts[2], parts[3])
                insert(students, length(students)+1, tmps)
            f.close()
        print("The load function is done.")
        print("Press enter to continue.")
        input('')
    elif (choice == 10):
        if isempty(students) == True:
            print("There have no student records.")
        else:
            pidlist = List()
            for i in range(1, length(students)+1):
                student = get(students, i)
                insert(pidlist, length(pidlist)+1, student.pid)
            for i in range(1, length(pidlist)+1):
                tmp = get(pidlist, i)
                for i in range(i, length(pidlist)+1):
                    check = get(pidlist, i+1)
                    if tmp == check:
                        delete(pidlist, i+1)
            for i in range(1, length(pidlist)+1):
                p = get(pidlist, i)
                print(p, end = "\n")
        print("The display programmes function is done.")
        print("Press enter to continue.")
        input('')
    elif (choice == 11):
        print("Please input a programme id:", end='')
        pid = input()
        totalNum = 0
        BNum = 0
        GNum = 0
        genlist = List()
        for i in range(1, length(students)+1):
            student = get(students, i)
            if student.pid == pid:
                insert(genlist, length(genlist)+1, student.gender)
        if isempty(genlist) == True:
            print("The programme id is not exist")
        else:
            for i in range(1, length(genlist)+1):
                totalNum = length(genlist)
                tmp = get(genlist, i)
                if tmp == "M":    
                    BNum = BNum + 1
                elif tmp == "F":
                    GNum = GNum + 1 
        print(f"The total number of students in programme with pid={pid} is {totalNum}.\nAmong them, there are {GNum} girl(s) and {BNum} boy(s).\n")
        print("\nFollowing are the information of the girl(s) in the programme.")
        for i in range(1, length(students)+1):
            student = get(students, i)    
            if student.gender == "F" and student.pid == pid:
                displaystinfo(student)
                print("\n")
        print("\nFollowing are the information of the boy(s) in the programme.")
        for i in range(1, length(students)+1):
            student = get(students, i)    
            if student.gender == "M" and student.pid == pid:
                displaystinfo(student)    
                print("\n")                
        print("The programme statistic function is done.")
        print("Press enter to continue.")
        input('')
    elif (choice == 0):
        print("Now quit, thank you!")
    choice = menu()






