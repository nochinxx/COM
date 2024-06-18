from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

students = [
    {
        "Term": 202460,
        "StudentID": "M00315946",
        "LastName": "Bastos",
        "FirstName": "Leticia",
        "MiddleName": "De Melo",
        "CRN": 60882,
        "InstructorID": "M00246143",
        "InstructorName": "Arbona, Shaila",
        "CourseID": "COUN 105NC",
        "Title": "Achieving Success in College",
        "Phone": "",
        "COMEmail": "lbastos1016@mycom.marin.edu",
        "PerEmail": "lmelo5209@gmail.com",
        "Enrolled": 18,
        "CCP": "",
    },
    {
        "Term": 202460,
        "StudentID": "M00314902",
        "LastName": "Castro Marroquin",
        "FirstName": "Edgar",
        "MiddleName": "Denilson",
        "CRN": 60882,
        "InstructorID": "M00246143",
        "InstructorName": "Arbona, Shaila",
        "CourseID": "COUN 105NC",
        "Title": "Achieving Success in College",
        "Phone": "(415) 497-2238",
        "COMEmail": "ecastro1780@mycom.marin.edu",
        "PerEmail": "edgardenilsoncastromarroquin@gmail.com",
        "Enrolled": 18,
        "CCP": "",
    },
    # Add the rest of the students here...
]

attendance = []


def mark_attendance(student_index):
    student = students[student_index]
    print(
        f"Marking {student['FirstName']} {student['MiddleName']} {student['LastName']} (ID: {student['StudentID']}) as present."
    )
    attendance.append(
        {
            "name": f"{student['FirstName']} {student['MiddleName']} {student['LastName']}",
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
    print("All students:")
    for idx, student in enumerate(students):
        full_name = (
            f"{student['FirstName']} {student['MiddleName']} {student['LastName']}"
        )
        print(f"{idx}: {full_name}")

    while True:
        query = input(
            "Enter the number corresponding to the student (or 'exit' to quit): "
        )
        if query.lower() == "exit":
            break

        try:
            selected_idx = int(query)
            if 0 <= selected_idx < len(students):
                mark_attendance(selected_idx)
            else:
                print("Invalid selection. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    generate_pdf(attendance)


if __name__ == "__main__":
    main()
