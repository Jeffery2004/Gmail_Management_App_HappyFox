# Gmail Management App – HappyFox

## Installation Guide

### Prerequisites
- Python 3.8 or higher
- Git (optional, for cloning the repository)
- Gmail API credentials (optional, for live Gmail sync)

### Installation and Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Jeffery2004/Gmail_Management_App_HappyFox.git
    cd Gmail_Management_App_HappyFox
    ```

2. **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```
    - **Activate the environment:**
        - **Windows:**
            ```bash
            venv\Scripts\activate
            ```
        - **macOS/Linux:**
            ```bash
            source venv/bin/activate
            ```

3. **Install required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## Set Up Gmail API (Optional)

Enable live Gmail access by configuring the Gmail API:

1. **Go to [Google Cloud Console](https://console.cloud.google.com/)** and sign in.
2. **Create a new project:**
    - Click the “Select a project” dropdown, then **New Project**
    - Enter a name (e.g., Gmail Management App) and click **Create**
3. **Enable Gmail API:**
    - Go to **APIs & Services > Library**
    - Search for **Gmail API** and click **Enable**
4. **Create OAuth 2.0 credentials:**
    - Go to **APIs & Services > Credentials**
    - Click **Create Credentials > OAuth client ID**
    - If prompted, configure the OAuth consent screen:
        - Select **External** and click **Create**
        - Fill in the required fields (App Name, Support Email, Developer Email)
        - Save configuration
    - After configuring, select **Desktop app**, provide a name, and click **Create**
5. **Download credentials:**
    - Click **Download JSON**
    - Save the file as `credentials.json` in your project folder (where `main.py` is located)
6. **Run the app for the first time:**
    - The app will detect `credentials.json` and prompt for authorization.
    - A browser window will open for you to sign in and grant access.
    - After authorization, a `token.json` file will be generated in your project folder.
7. **Security Tip:**
    - Keep `credentials.json` and `token.json` secure.
    - **Do NOT upload these files to public repositories.**

---

## Running the App

- **Fetch all data stored in the database:**
    ```bash
    python main.py
    ```
- **Apply email rules stored in `rules.json`:**
    ```bash
    python rule_processor.py
    ```

---

## Disclaimer

By default, the app runs using the local database (`emails.db`).  
To enable real-time Gmail access, follow the steps above to set up the Gmail API and OAuth credentials.

Please note that the Email data shared with you does contain any Personally Identifiable Information (PII). 
All personal identifiers have been removed  prior to transmission.

---
````
