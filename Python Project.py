import tkinter as tk
from tkinter import messagebox, simpledialog

# Module 3: List of dictionaries - acts as the student database
students = []

SUBJECTS = ("Math", "Science", "English")  # Module 3: Tuple - fixed subject list


# ---------------- Module 4: Functions ----------------

def calculate_average(marks_list):
    return sum(marks_list) / len(marks_list)

def calculate_grade(average, passing_marks=40):
    # Module 2: Control flow
    if average < passing_marks:
        return "F"
    elif average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "D"

def find_topper(student_list):
    if not student_list:
        return None
    topper = student_list[0]
    top_avg = calculate_average(list(topper["marks"].values()))
    # Module 2: For loop
    for student in student_list[1:]:
        avg = calculate_average(list(student["marks"].values()))
        if avg > top_avg:
            topper = student
            top_avg = avg
    return topper, top_avg


class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("500x500")
        self.root.config(bg="#eef2f7")
        self.root.resizable(False, False)

        self.build_main_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # ---------------- MAIN SCREEN ----------------
    def build_main_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Student Management System",
                 font=("Helvetica", 18, "bold"), bg="#eef2f7",
                 fg="#2c3e50").pack(pady=20)

        tk.Button(self.root, text="Add Student", font=("Helvetica", 12, "bold"),
                  bg="#27ae60", fg="white", width=25,
                  command=self.build_add_screen).pack(pady=8)

        tk.Button(self.root, text="View All Students", font=("Helvetica", 12, "bold"),
                  bg="#2980b9", fg="white", width=25,
                  command=self.build_view_screen).pack(pady=8)

        tk.Button(self.root, text="Find Topper", font=("Helvetica", 12, "bold"),
                  bg="#8e44ad", fg="white", width=25,
                  command=self.show_topper).pack(pady=8)

        tk.Label(self.root, text=f"Total Students: {len(students)}",
                 font=("Helvetica", 10), bg="#eef2f7", fg="#7f8c8d").pack(pady=20)

        tk.Button(self.root, text="Exit", font=("Helvetica", 10),
                  bg="#c0392b", fg="white", width=15,
                  command=self.root.quit).pack(pady=10)

    # ---------------- ADD STUDENT SCREEN ----------------
    def build_add_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Add New Student", font=("Helvetica", 16, "bold"),
                 bg="#eef2f7", fg="#2c3e50").pack(pady=15)

        tk.Label(self.root, text="Student Name", bg="#eef2f7").pack()
        self.name_entry = tk.Entry(self.root, font=("Helvetica", 12), width=25)
        self.name_entry.pack(pady=5)

        # Module 1 & 3: Dictionary to hold entry widgets per subject
        self.marks_entries = {}
        for subject in SUBJECTS:
            tk.Label(self.root, text=f"{subject} Marks (0-100)", bg="#eef2f7").pack()
            entry = tk.Entry(self.root, font=("Helvetica", 12), width=25)
            entry.pack(pady=5)
            self.marks_entries[subject] = entry

        tk.Button(self.root, text="Save Student", font=("Helvetica", 12, "bold"),
                  bg="#27ae60", fg="white", width=18,
                  command=self.save_student).pack(pady=15)

        tk.Button(self.root, text="Back", font=("Helvetica", 10),
                  bg="#eef2f7", fg="#7f8c8d", relief="flat",
                  command=self.build_main_screen).pack()

    def save_student(self):
        # Module 1: string methods
        name = self.name_entry.get().strip().title()

        if name == "":
            messagebox.showwarning("Missing Info", "Please enter a student name.")
            return

        marks = {}
        # Module 2: For loop validating each subject
        for subject, entry in self.marks_entries.items():
            value = entry.get().strip()
            if not value.isdigit() or not (0 <= int(value) <= 100):
                messagebox.showerror("Invalid Input", f"Enter valid marks (0-100) for {subject}.")
                return
            marks[subject] = int(value)

        students.append({"name": name, "marks": marks})  # Module 3: List + dictionary
        messagebox.showinfo("Success", f"{name} added successfully!")
        self.build_main_screen()

    # ---------------- VIEW STUDENTS SCREEN ----------------
    def build_view_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="All Students", font=("Helvetica", 16, "bold"),
                 bg="#eef2f7", fg="#2c3e50").pack(pady=15)

        if not students:  # Module 2: conditional
            tk.Label(self.root, text="No students added yet.",
                     bg="#eef2f7", fg="#7f8c8d").pack(pady=20)
        else:
            frame = tk.Frame(self.root, bg="#eef2f7")
            frame.pack(pady=5, fill="both", expand=True)

            listbox = tk.Listbox(frame, font=("Helvetica", 11), width=55, height=15)
            listbox.pack()

            # Module 2: For loop building display strings
            for student in students:
                avg = calculate_average(list(student["marks"].values()))
                grade = calculate_grade(avg)
                # Module 1: f-string
                line = f"{student['name']} | Avg: {avg:.1f} | Grade: {grade}"
                listbox.insert(tk.END, line)

        tk.Button(self.root, text="Back", font=("Helvetica", 10),
                  bg="#eef2f7", fg="#7f8c8d", relief="flat",
                  command=self.build_main_screen).pack(pady=15)

    # ---------------- TOPPER ----------------
    def show_topper(self):
        result = find_topper(students)
        if result is None:
            messagebox.showinfo("No Data", "No students added yet.")
            return
        topper, avg = result
        messagebox.showinfo("Topper", f"🏆 {topper['name']} is the topper with an average of {avg:.1f}!")


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()