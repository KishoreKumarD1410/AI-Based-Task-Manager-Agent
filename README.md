# AI-Based-Task-Manager-Agent
AI-Based Task Manager Agent
Objective: Develop an AI-Based Task Manager that leverages LLM for task command interpretation, SQL query generation, and task management.

Purpose: Simplify task management using natural language commands and AI-driven processing.

**Vimeo link** : https://vimeo.com/1083191337/18f8841a6b?share=copy

# AI Task Manager Agent

## Overview
The AI Task Manager Agent is a Streamlit-based application that leverages a Language Model (LLM) to manage tasks using natural language commands. This project was developed as part of the assessment for the AI/ML Engineer position at OneData Software Solutions.

## Features
- User Authentication and Session Management
- Task Creation, Update, and Deletion
- Task Querying using Natural Language Commands
- LLM-Based SQL Query Generation
- Data Persistence using SQLite
- Context Management for Interactions

## Tech Stack and Libraries
- Python 3.10
- Streamlit
- SQLite
- Langchain
- dotenv
- pandas

## Installation and Setup
1. **Clone the repository:**
```bash
git clone [REPO_URL]
cd onedata.assessment
```

2. **Create a virtual environment and activate it:**
```bash
python -m venv env
source env/Scripts/activate  # On Windows
source env/bin/activate      # On macOS/Linux
```

3. **Install the required packages:**
```bash
pip install -r requirements.txt
```

4. **Set up the .env file:**
- Create a `.env` file in the root directory and add the following:
```
GOOGLE_API_KEY=your_api_key_here
```

5. **Run the application:**
```bash
streamlit run app.py
```

## Directory Structure
```
/onedata.assessment
├── app.py
├── database.py
├── llm_handler.py
├── requirements.txt
├── .env
├── tasks.db
└── README.md
```

## How to Use
- Login using your name and email.
- Enter commands like:
  - "Add a task 'Meeting with client' due tomorrow at 3 PM"
  - "Show all pending tasks"
  - "Mark 'Meeting with client' as completed"

## Screenshots/Preview
![App Screenshot](screenshot.png)

## Future Enhancements
- Integrate email notifications for due tasks.
- Add a calendar view for tasks.
- Implement voice command support.

## Author
Kishore Kumar D

---

