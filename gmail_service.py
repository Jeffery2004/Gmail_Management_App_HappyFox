import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def authenticate_gmail():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)


def get_message(service, msg_id):
    return service.users().messages().get(userId='me', id=msg_id, format='full').execute()

def mark_as_read(service, msg_id):
    service.users().messages().modify(
        userId='me',
        id=msg_id,
        body={'removeLabelIds': ['UNREAD']}
    ).execute()

def mark_as_unread(service, msg_id):
    service.users().messages().modify(
        userId='me',
        id=msg_id,
        body={'addLabelIds': ['UNREAD']}
    ).execute()

def get_label_id(service, label_name, create_if_missing=True):
    labels = service.users().labels().list(userId='me').execute().get('labels', [])
    for label in labels:
        if label['name'].lower() == label_name.lower():
            return label['id']
    if create_if_missing:
        new_label = service.users().labels().create(
            userId='me',
            body={'name': label_name}
        ).execute()
        return new_label['id']
    return None

def move_message(service, msg_id, label_name):
    label_id = get_label_id(service, label_name)
    if not label_id:
        raise Exception(f"Label '{label_name}' not found and could not be created.")
    service.users().messages().modify(
        userId='me',
        id=msg_id,
        body={'addLabelIds': [label_id], 'removeLabelIds': ['INBOX']}
    ).execute()
