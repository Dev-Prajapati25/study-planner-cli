# 📚 Study Planner CLI

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/Dev-Prajapati25/study-planner-cli)](https://github.com/Dev-Prajapati25/study-planner-cli)
[![GitHub stars](https://img.shields.io/github/stars/Dev-Prajapati25/study-planner-cli?style=social)](https://github.com/Dev-Prajapati25/study-planner-cli)

A simple and interactive **Command-Line Interface (CLI)** tool to help students manage and track their study hours effectively.  
This tool lets users **add subjects**, **set goal hours**, **log study progress**, **view summaries with progress bars**, and **persist data** between sessions using a local JSON file.

---

## 🧭 Table of Contents
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Example Session](#-example-session)
- [Project Structure](#-project-structure)
- [Dependencies](#-dependencies)
- [How It Works](#-how-it-works)
- [Packaging for PyPI](#-packaging-for-pypi)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features
- 📖 **Add subjects** with optional goal hours  
- ⏱️ **Log study hours** for each subject  
- 📊 **View progress summaries** with ASCII-style progress bars  
- 🗑️ **Delete subjects** when no longer needed  
- 💾 **Automatic data persistence** in a `data.json` file  
- 🧮 **Input validation** for cleaner and safer user interaction  

---

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Dev-Prajapati25/study-planner-cli.git
   cd study-planner-cli
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

Run the main script:
```bash
python main.py
```

You’ll see a simple interactive menu:
```
===== STUDY PLANNER =====
1. Add Subject
2. Log Study Hours
3. View Summary
4. Delete Subject
5. Save & Exit
```

### Available Options
| Option | Description |
|:--:|:--|
| **1** | Add a new subject with optional goal hours |
| **2** | Log study hours for a specific subject |
| **3** | View study progress in a summary table |
| **4** | Delete an existing subject |
| **5** | Save all data and exit |

---

## 🧩 Example Session

```
===== STUDY PLANNER =====
1. Add Subject
2. Log Study Hours
3. View Summary
4. Delete Subject
5. Save & Exit

Enter choice : 1
----- ADD SUBJECT -----
Enter Subject Name(enter to cancel) : Physics
Enter goal hours (enter for default '0'): 20
```

After logging hours:
```
----- VIEW SUMMARY -----
Physics : 5/20
    [████░░░░░░] 25% Done
```

---

## 🗂️ Project Structure

```
study-planner-cli/
├── core.py          # Main CLI logic (menu actions)
├── storage.py       # Handles data storage and JSON persistence
├── utility.py       # Input validation utilities
├── main.py          # Entry point script
├── requirements.txt # Dependencies list
└── data.json        # User data (created automatically)
```

---

## 📦 Dependencies

Listed in `requirements.txt`:
```
tabulate
```

---

## 🧠 How It Works

- The program stores all study data in `data.json`.
- `Subject` objects (in `storage.py`) represent subjects and handle saving/loading.
- `core.py` manages user choices like adding subjects, logging hours, and showing summaries.
- Progress visualization is generated dynamically using ASCII blocks.

---

## 📦 Packaging for PyPI

To package and distribute this CLI as a pip-installable tool:

1. Create a `setup.py` file in the root directory:
   ```python
   from setuptools import setup, find_packages

   setup(
       name="study-planner-cli",
       version="1.0.0",
       packages=find_packages(),
       install_requires=["tabulate"],
       entry_points={
           "console_scripts": [
               "study-planner=main:main",
           ],
       },
   )
   ```

2. Build and upload to PyPI:
   ```bash
   python setup.py sdist bdist_wheel
   twine upload dist/*
   ```

3. Then users can install and run it with:
   ```bash
   pip install study-planner-cli
   study-planner
   ```

---

## 🧰 Troubleshooting

| Issue | Possible Fix |
|-------|---------------|
| `FileNotFoundError: 'data.json'` | Run the app once; it auto-creates the file. |
| `JSONDecodeError` | Delete `data.json` if it becomes corrupted. |
| Invalid input errors | Ensure you enter numeric values where required. |

---

## 🤝 Contributing

Contributions, feature requests, and bug reports are welcome!  
Feel free to open a pull request or file an issue on the GitHub repository.

---

## 🪪 License

This project is open source and available under the **MIT License**.  
You’re free to use, modify, and distribute it with attribution.

---
