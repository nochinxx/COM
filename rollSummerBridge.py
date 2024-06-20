from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import csv

students = []
attendance = []


# Load students from the file
def load_students(filename):
    with open(filename, mode="r") as file:
        reader = csv.DictReader(file, delimiter="\t")
        for row in reader:
            students.append(row)


def add_student():
    student = {
        "Term": "void",
        "StudentID": input("Enter Student ID: "),
        "LastName": input("Enter Last Name: "),
        "FirstName": input("Enter First Name: "),
        "MiddleName": "void",
        "CRN": "void",
        "InstructorID": "void",
        "InstructorName": "void",
        "CourseID": "void",
        "Title": "void",
        "Phone": "void",
        "COMEmail": "void",
        "PerEmail": "void",
        "Enrolled": "void",
        "CCP": "void",
    }
    students.append(student)


def search_students(query):
    results = []
    for idx, student in enumerate(students):
        full_name = (
            f"{student['FirstName']} {student['MiddleName']} {student['LastName']}"
        )
        if query.lower() in full_name.lower():
            results.append((idx, full_name))
    return results


def mark_attendance(student_index):
    student = students[student_index]
    print(
        f"Marking {student['FirstName']} {student['LastName']} (ID: {student['StudentID']}) as present."
    )
    attendance.append(
        {
            "name": f"{student['FirstName']} {student['LastName']}",
            "id": student["StudentID"],
        }
    )


def generate_pdf(attendance_list):
    pdf_file = f"attendance_{datetime.now().strftime('%m-%d-%Y')}.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter
    c.drawString(
        100, height - 40, f"Attendance Report     {datetime.now().strftime('%Y-%m-%d')}"
    )
    y = height - 60
    for entry in attendance_list:
        c.drawString(100, y, f"{entry['name']} - {entry['id']}")
        y -= 20
    c.save()
    print(f"PDF report generated: {pdf_file}")


def main():
    load_students("peopleESL.txt")
    print("All students:")
    for idx, student in enumerate(students):
        full_name = (
            f"{student['FirstName']} {student['MiddleName']} {student['LastName']}"
        )
        print(f"{idx}: {full_name}")

    while True:
        query = input(
            "Enter the number corresponding to the student, 'add' to add a student, 'search' to search for a student, or 'exit' to quit: "
        )
        if query.lower() == "exit":
            break
        elif query.lower() == "add":
            add_student()
            for idx, student in enumerate(students):
                full_name = f"{student['FirstName']} {student['LastName']}"
                print(f"{idx}: {full_name}")
        elif query.lower() == "search":
            search_query = input("Enter a few letters of the student's name: ")
            results = search_students(search_query)
            if results:
                print("Search results:")
                for idx, full_name in results:
                    print(f"{idx}: {full_name}")
            else:
                print("No matching students found.")
        else:
            try:
                selected_idx = int(query)
                if 0 <= selected_idx < len(students):
                    mark_attendance(selected_idx)
                else:
                    print("Invalid selection. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number, 'add', or 'search'.")

    generate_pdf(attendance)


if __name__ == "__main__":
    main()
