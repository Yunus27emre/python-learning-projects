def student_grade():
    name = input("Enter student's first and last name: ")
    visa = float(input("Enter visa score:"))
    final = float(input("Enter final score:"))

    total = visa * 0.4 + final * 0.6
    letter_score = ""

    if total >= 85:
        letter_score = "AA"
    elif total >= 70:
        letter_score = "BA"
    elif total >= 60:
        letter_score = "BB"
    elif total >= 50:
        letter_score = "CB"
    elif total >= 40:
        letter_score = "CC"
    else:
        letter_score = "FF"

    print("Success Grade: {}".format(total))
    print("{} received the letter grade {} in this course.".format(name, letter_score))

    with open("notes.txt", "a") as file:
        file.writelines("{}\t{}\t{}\t{}\t{}\n".format(name, visa, final, total, letter_score))

stud_num=int(input("How many students will you enroll?: "))
for i in range(stud_num):
    student_grade()