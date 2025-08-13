Gmail Management App – HappyFox

----Installation Guide----
Prerequisites--
Python 3.8+ installed
Git installed (optional, for cloning the repository)
Gmail API credentials (optional for live Gmail sync)

Installation and Setup--
Open Command Prompt (Windows) or Terminal (macOS/Linux).
Clone the repository:
Command:
      git clone https://github.com/Jeffery2004/Gmail_Management_App_HappyFox.git
      cd Gmail_Management_App_HappyFox
Create a virtual environment (optional but recommended):
      python -m venv venv
      Activate the environment:
      For Windows:
         venv\Scripts\activate
      For macOS/Linux:
         source venv/bin/activate
Install required dependencies:
      pip install -r requirements.txt (All the required packages are available in requirements.txt).


Set up Gmail API (Optional for live Gmail access)--
To enable the app to access your Gmail account, follow these steps carefully:

1.Go to Google Cloud Console:
    Open https://console.cloud.google.com/ in your browser. Make sure you are signed in with your Google account.
2.Create a new project:
    Click on the Select a project dropdown at the top.
    Click New Project.
    Enter a name for your project (e.g., Gmail Management App).
    Click Create.
3.Enable Gmail API for the project:
    In the left-hand menu, go to APIs & Services → Library.
    Search for Gmail API.
    Click Gmail API and then click Enable.
4.Create OAuth 2.0 credentials:
    Go to APIs & Services → Credentials.
    Click Create Credentials → OAuth client ID.
    You may be prompted to configure the OAuth consent screen first:
       Select External and click Create.
       Fill in App Name, User Support Email, and Developer Email Address.
       Add any scopes if needed (can skip for basic Gmail API access).
       Save the configuration.
    After configuring consent screen, select Application type → Desktop app.
    Give it a name (e.g., Gmail Desktop Client) and click Create.
5.Download credentials.json:
    After creating the OAuth client, click Download JSON.
    Save the file as credentials.json in your project folder (where main.py is located).
6.Run the app for the first time:
    The app will detect credentials.json and ask you to authorize access.
    A browser window will open prompting you to sign in to your Google account and grant permission to access Gmail.
    After authorization, the app will generate a token.json file in the project folder. 
    This token allows the app to access Gmail without requiring login every time.
7.Security tip:
    Keep credentials.json and token.json secure.
    Do not upload these files to public repositories.


Run the app in Command Prompt / Terminal:--
Command :python main.py (To fetch all the data stored in the database).
Command :python rule_processor (To apply email rules that are stored in rules.json)
