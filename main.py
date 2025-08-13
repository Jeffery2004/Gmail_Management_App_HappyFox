from gmail_service import authenticate_gmail, get_message
from utils import decode_body, parse_headers
from db import init_db, insert_email, get_all_emails
from tabulate import tabulate

def truncate_text(text, max_len=50):
    if len(text) > max_len:
        return text[:max_len-3] + "..."
    return text

def main():
    init_db()
    emails_to_print = []

    try:
        service = authenticate_gmail()
        # Gmail available, fetch emails
        all_messages = service.users().messages().list(userId='me', labelIds=['INBOX']).execute().get('messages', [])
        print(f"Found {len(all_messages)} messages in INBOX.")
        for msg in all_messages:
            full_msg = get_message(service, msg['id'])
            headers = parse_headers(full_msg['payload']['headers'])
            body = decode_body(full_msg['payload'])

            email_data = {
                'id': msg['id'],
                'sender': headers.get('sender', ''),
                'recipient': headers.get('recipient', ''),
                'subject': headers.get('subject', ''),
                'body': body,
                'received': headers.get('received', ''),
                'is_unread': 1 if 'UNREAD' in full_msg.get('labelIds', []) else 0,
                'labels': ",".join(full_msg.get('labelIds', []))
            }

            insert_email(email_data)

            emails_to_print.append([
                truncate_text(email_data['sender'], 30),
                truncate_text(email_data['subject'], 50),
                email_data['received'] or "N/A"
            ])

    except FileNotFoundError:
        # If credentials/token missing, use local db
        print("Gmail credentials not found. Using local database instead.")
        db_emails = get_all_emails()  # fetch_emails() returns list of tuples
        print(f"Found {len(db_emails)} emails in local database.")

        for row in db_emails:
            sender = truncate_text(row[1], 30)   # sender index
            subject = truncate_text(row[3], 50)  # subject index
            received = row[5] or "N/A"           # received index
            emails_to_print.append([sender, subject, received])

    headers = ["Sender", "Subject", "Received"]
    print(tabulate(emails_to_print, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    main()
