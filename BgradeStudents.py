import re
def grades():
    with open ("assets/grades.txt", "r") as file:
        grades = file.read()
        lstStudents=[]
        students = grades.replace("\n",'/').split("/")#remove line jumps and seccionate the list of grades by each student
        #here comes the pattern
        pattern="[B]"
        for student in students:
            stA=student.split(': ')
            if re.search(pattern,stA[1]):
                lstStudents.append(stA[0])#listing the name of the students that get B grade in the exam
        return lstStudents
