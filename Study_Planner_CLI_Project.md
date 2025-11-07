# 🧠 Project: Study Planner CLI

A **command-line study planner** that helps you manage study subjects, track progress, and review your schedule — simple enough to write solo, yet broad enough to revise key Python concepts.

---

## 🎯 Goal

Create a terminal-based app that lets you:

- Add, view, and remove subjects/topics  
- Log daily study time for each subject  
- Display a summary of total study hours per subject  
- Save and load all data from a local file (JSON or CSV)  
- Optionally set study goals and check your progress  

---

## 🧩 Core Concepts You’ll Revise

| Concept | How It’s Used |
|----------|---------------|
| **Variables & data types** | Storing subjects, hours, goals |
| **Control flow** | Menu loops, input handling, validation |
| **Functions** | Separate logic: add subject, view summary, save/load data |
| **Lists & dictionaries** | Manage study data structures |
| **File I/O** | Persist data using JSON or CSV |
| **Error handling** | Handle invalid inputs and file read/write issues |
| **Modules** | Split logic into 2–3 files (e.g. `main.py`, `file_ops.py`) |
| **String formatting** | Nicely formatted console output |
| **Datetime module** | Optional: log by date or calculate daily averages |

---

## 🧱 Suggested Structure

```
study_planner/
├── main.py          # Handles menu and user interaction
├── planner.py       # Core functions (add_subject, log_hours, summary)
├── storage.py       # Load/save data (JSON/CSV)
├── data.json        # Saved user data
└── README.md
```

---

## 🧩 Basic Menu Example

```
===== STUDY PLANNER =====
1. Add Subject
2. Log Study Hours
3. View Summary
4. Delete Subject
5. Save & Exit
Enter choice: _
```

---

## 🧮 Example Data Format (JSON)

```json
{
  "Mathematics": {"hours": 12, "goal": 40},
  "Physics": {"hours": 8, "goal": 30}
}
```

---

## 🌟 Extra Features (Optional, for challenge)

- Add **progress bar** in terminal (e.g., `[#######-----] 70% done`)
- Allow **date-wise logs** and plot trends using `matplotlib`
- Export report as a **CSV file**
- Auto-backup on each run
- Sort subjects by completion percentage

---

## 📚 Concepts Revisited

✅ Variables, loops, conditionals  
✅ Functions and modularity  
✅ Lists, dicts, string formatting  
✅ File handling and exception management  
✅ JSON/CSV manipulation  
✅ Basic user interface (CLI)

---

## 🧠 When You Finish

You’ll have refreshed nearly every core Python concept.  
Then you can confidently start the **intermediate roadmap** — especially OOP and modular design — by refactoring this project into an OOP version later.
