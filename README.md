Gmail Management App – HappyFox
----Project Overview----
The Gmail Management App is a Python-based tool designed to automate the organization of emails in your Gmail account. 
The app fetches emails, stores them in a local SQLite database, and allows you to define custom rules to automatically perform actions like:
Mark emails as read or unread
Move emails to specific folders/labels
Filter emails based on sender, subject, body, or date
It works both with Gmail credentials (for live synchronization) and offline using the local database.
This project is useful for automating email management, especially for repetitive sorting tasks.


----Installation Guide----
Prerequisites
Python 3.8+ installed
Git installed (optional, for cloning the repository)
Gmail API credentials (optional for live Gmail sync)

Steps to Setup
Clone the repository
bash:
git clone https://github.com/Jeffery2004/Gmail_Management_App_HappyFox.git
cd Gmail_Management_App_HappyFox
Create a virtual environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
