# Student-Management-System
A student records app that auto-calculates averages, assigns letter grades, and surfaces the class topper on a live dashboard.

A esktop app that takes student marks, calculates averages and grades automatically, and gives a live dashboard view of class performance — built as a mini Python project to apply core programming concepts in a real, usable tool.

## 📌 The Problem

Tracking student marks manually means doing the same repetitive math over and over: adding up scores, dividing for averages, mapping numbers to grades, and scanning every record just to find who's leading the class. It's slow and easy to get wrong by hand.

## 💡 The Solution

Enter a student's marks once, and the app handles the rest — calculating their average, assigning a letter grade, and updating a live dashboard with class-wide stats, all in a clean sidebar-navigated interface instead of a single cluttered screen.

## ✨ What It Can Do

- Add a student with marks across Math, Science, and English
- Auto-calculate each student's average and assign a grade (A–F)
- Show a live dashboard: total students, class average, and current topper
- Instantly find the class topper with one click
- List all students with their averages and grades, scrollable
- Reject empty names and invalid marks before they're saved

## 🖥️ Using the App

| Step | Action |
|------|--------|
| 1 | Open **Add Student**, enter a name and marks for each subject |
| 2 | The app validates marks (0–100) and saves the record |
| 3 | Check **View All Students** for the full list with grades |
| 4 | Click **Find Topper** to see who's leading the class |
| 5 | The **Dashboard** updates automatically as students are added |

## 🛠️ Built With

- **Python 3**
- **Tkinter** — sidebar layout with dynamic, swappable content panels
- Core concepts: functions, control flow, tuples, and list-of-dictionaries data modeling

## 📂 Files

```
student_management_system.py   # The entire app — GUI, logic, and core functions
```

## ▶️ Run It Locally

```bash
git clone <your-repo-url>
cd student-management-system
python student_management_system.py
```

No extra installs needed — Tkinter ships with standard Python.

## 🧩 Under the Hood

| Function | What it does |
|----------|---------------|
| `calculate_average(marks_list)` | Averages a student's marks |
| `calculate_grade(average, passing_marks=40)` | Converts an average into a letter grade |
| `find_topper(student_list)` | Finds the highest-scoring student |
| `grade_color(grade)` | Maps each grade to a color for the UI |

Each student is stored as a dictionary with their name and a nested dictionary of subject marks, all held in a single list — simple to loop through, calculate, and aggregate.

## 🎯 Concepts Applied

- **Module 2 — Control Flow:** grading logic and input validation
- **Module 3 — Data Structures:** tuples for fixed subjects, list of dictionaries for records
- **Module 4 — Functions:** separating calculation logic from the interface
- **GUI Design:** sidebar navigation, live stat cards, and color-coded grades for at-a-glance readability

## 🚧 What's Next

- Save/load student records to a file or database
- Configurable subject list instead of a fixed tuple
- Search and filter by name or grade
- Export class reports to CSV or PDF
- Charts for grade distribution and performance trends
