import tkinter as tk
from tkinter import messagebox

# ---------------------------------------------------------------------------
# Mini Python Project — Student Management System
# Modules used: Module 1 (Python Fundamentals), Module 2 (Control Flow),
# Module 3 (Data Structures), Module 4 (Functions)
# ---------------------------------------------------------------------------

# Module 3: List of dictionaries - acts as the student database
students = []

SUBJECTS = ("Math", "Science", "English")  # Module 3: Tuple - fixed subject list

# Theme colors (sidebar-navigation layout, distinct from earlier projects)
SIDEBAR = "#0d3b3e"
SIDEBAR_ACTIVE = "#14545a"
CONTENT_BG = "#fbfbfd"
ACCENT = "#1abc9c"
GOLD = "#d4af37"
RED = "#d64550"
GRAY = "#8a94a6"
WHITE = "#ffffff"
DARK_TEXT = "#1f2937"


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


def grade_color(grade):
    return {"A": ACCENT, "B": "#3b82f6", "C": GOLD, "D": "#f59e0b", "F": RED}.get(grade, GRAY)


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
        self.root.geometry("760x560")
        self.root.config(bg=CONTENT_BG)
        self.root.resizable(False, False)

        self.nav_buttons = {}
        self.build_layout()
        self.show_dashboard()

    # ---------------- LAYOUT: Sidebar + Content ----------------
    def build_layout(self):
        # Sidebar
        self.sidebar = tk.Frame(self.root, bg=SIDEBAR, width=210)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        tk.Label(self.sidebar, text="🎓 Student MS", font=("Helvetica", 16, "bold"),
                 bg=SIDEBAR, fg=WHITE).pack(pady=(30, 5), padx=20, anchor="w")
        tk.Label(self.sidebar, text="Mini Python Project", font=("Helvetica", 9),
                 bg=SIDEBAR, fg="#7fb3ac").pack(pady=(0, 30), padx=20, anchor="w")

        self.add_nav_button("Dashboard", self.show_dashboard)
        self.add_nav_button("Add Student", self.build_add_screen)
        self.add_nav_button("View All Students", self.build_view_screen)
        self.add_nav_button("Find Topper", self.show_topper)

        bottom_frame = tk.Frame(self.sidebar, bg=SIDEBAR)
        bottom_frame.pack(side="bottom", pady=25, padx=20, fill="x")
        tk.Button(bottom_frame, text="Exit", font=("Helvetica", 10, "bold"),
                  bg=RED, fg=WHITE, relief="flat", cursor="hand2",
                  command=self.root.quit).pack(fill="x", ipady=6)

        # Content area
        self.content = tk.Frame(self.root, bg=CONTENT_BG)
        self.content.pack(side="left", fill="both", expand=True)

    def add_nav_button(self, label, command):
        btn = tk.Button(self.sidebar, text=label, font=("Helvetica", 11),
                         bg=SIDEBAR, fg=WHITE, relief="flat", anchor="w",
                         activebackground=SIDEBAR_ACTIVE, activeforeground=WHITE,
                         cursor="hand2", bd=0, command=command)
        btn.pack(fill="x", padx=12, pady=4, ipady=8, ipadx=10)
        self.nav_buttons[label] = btn

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    # ---------------- DASHBOARD ----------------
    def show_dashboard(self):
        self.clear_content()

        tk.Label(self.content, text="Dashboard", font=("Helvetica", 20, "bold"),
                 bg=CONTENT_BG, fg=DARK_TEXT).pack(anchor="w", padx=35, pady=(30, 5))
        tk.Label(self.content, text="Quick overview of your student records",
                 font=("Helvetica", 10), bg=CONTENT_BG, fg=GRAY).pack(anchor="w", padx=35, pady=(0, 25))

        cards = tk.Frame(self.content, bg=CONTENT_BG)
        cards.pack(padx=35, fill="x")

        self.stat_card(cards, "Total Students", str(len(students)), ACCENT, 0)

        if students:
            avgs = [calculate_average(list(s["marks"].values())) for s in students]
            class_avg = sum(avgs) / len(avgs)
            self.stat_card(cards, "Class Average", f"{class_avg:.1f}", GOLD, 1)
        else:
            self.stat_card(cards, "Class Average", "—", GOLD, 1)

        topper_result = find_topper(students)
        topper_name = topper_result[0]["name"] if topper_result else "—"
        self.stat_card(cards, "Current Topper", topper_name, "#3b82f6", 2)

        tk.Button(self.content, text="+  Add a New Student", font=("Helvetica", 12, "bold"),
                  bg=ACCENT, fg=WHITE, relief="flat", cursor="hand2",
                  activebackground="#149174",
                  command=self.build_add_screen).pack(padx=35, pady=40, anchor="w", ipadx=12, ipady=8)

    def stat_card(self, parent, title, value, color, col):
        card = tk.Frame(parent, bg=WHITE, highlightbackground="#e5e7eb",
                         highlightthickness=1, width=200, height=100)
        card.grid(row=0, column=col, padx=(0, 15), sticky="nsew")
        card.grid_propagate(False)

        tk.Frame(card, bg=color, width=5).pack(side="left", fill="y")
        inner = tk.Frame(card, bg=WHITE)
        inner.pack(side="left", fill="both", expand=True, padx=15, pady=15)

        tk.Label(inner, text=title, font=("Helvetica", 9), bg=WHITE, fg=GRAY).pack(anchor="w")
        tk.Label(inner, text=value, font=("Helvetica", 18, "bold"), bg=WHITE, fg=DARK_TEXT).pack(anchor="w", pady=(5, 0))

    # ---------------- ADD STUDENT SCREEN ----------------
    def build_add_screen(self):
        self.clear_content()

        tk.Label(self.content, text="Add New Student", font=("Helvetica", 20, "bold"),
                 bg=CONTENT_BG, fg=DARK_TEXT).pack(anchor="w", padx=35, pady=(30, 20))

        card = tk.Frame(self.content, bg=WHITE, highlightbackground="#e5e7eb", highlightthickness=1)
        card.pack(padx=35, fill="both", expand=True)

        tk.Label(card, text="Student Name", font=("Helvetica", 10, "bold"),
                 bg=WHITE, fg=DARK_TEXT).pack(anchor="w", padx=25, pady=(25, 5))
        self.name_entry = tk.Entry(card, font=("Helvetica", 12), relief="solid", bd=1)
        self.name_entry.pack(padx=25, fill="x", ipady=6)

        # Module 1 & 3: Dictionary to hold entry widgets per subject
        self.marks_entries = {}
        for subject in SUBJECTS:
            tk.Label(card, text=f"{subject} Marks (0-100)", font=("Helvetica", 10, "bold"),
                     bg=WHITE, fg=DARK_TEXT).pack(anchor="w", padx=25, pady=(15, 5))
            entry = tk.Entry(card, font=("Helvetica", 12), relief="solid", bd=1)
            entry.pack(padx=25, fill="x", ipady=6)
            self.marks_entries[subject] = entry

        btn_row = tk.Frame(card, bg=WHITE)
        btn_row.pack(pady=25)

        tk.Button(btn_row, text="Save Student", font=("Helvetica", 11, "bold"),
                  bg=ACCENT, fg=WHITE, relief="flat", cursor="hand2", width=16,
                  activebackground="#149174",
                  command=self.save_student).grid(row=0, column=0, padx=6, ipady=7)

        tk.Button(btn_row, text="Cancel", font=("Helvetica", 11),
                  bg="#e5e7eb", fg=DARK_TEXT, relief="flat", cursor="hand2", width=12,
                  command=self.show_dashboard).grid(row=0, column=1, padx=6, ipady=7)

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
        self.show_dashboard()

    # ---------------- VIEW STUDENTS SCREEN ----------------
    def build_view_screen(self):
        self.clear_content()

        tk.Label(self.content, text="All Students", font=("Helvetica", 20, "bold"),
                 bg=CONTENT_BG, fg=DARK_TEXT).pack(anchor="w", padx=35, pady=(30, 20))

        card = tk.Frame(self.content, bg=WHITE, highlightbackground="#e5e7eb", highlightthickness=1)
        card.pack(padx=35, fill="both", expand=True, pady=(0, 20))

        if not students:  # Module 2: conditional
            tk.Label(card, text="No students added yet.",
                     bg=WHITE, fg=GRAY, font=("Helvetica", 11)).pack(pady=60)
        else:
            list_frame = tk.Frame(card, bg=WHITE)
            list_frame.pack(padx=20, pady=20, fill="both", expand=True)
            scrollbar = tk.Scrollbar(list_frame)
            scrollbar.pack(side="right", fill="y")

            listbox = tk.Listbox(list_frame, font=("Helvetica", 11), height=14,
                                  relief="solid", bd=1, yscrollcommand=scrollbar.set)
            listbox.pack(side="left", fill="both", expand=True)
            scrollbar.config(command=listbox.yview)

            # Module 2: For loop building display strings
            for student in students:
                avg = calculate_average(list(student["marks"].values()))
                grade = calculate_grade(avg)
                # Module 1: f-string
                line = f"{student['name']}   |   Avg: {avg:.1f}   |   Grade: {grade}"
                listbox.insert(tk.END, line)

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
