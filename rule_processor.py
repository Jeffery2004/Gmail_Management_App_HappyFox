import json
from db import get_all_emails
from utils import match_condition
from gmail_service import authenticate_gmail, mark_as_read, mark_as_unread, move_message

def load_rules():
    with open("rules.json", "r") as f:
        return json.load(f)

def process_rules():
    print("Starting to process rules...\n")

    # Try to authenticate with Gmail; if fails, use local DB only
    try:
        service = authenticate_gmail()
        GMAIL_AVAILABLE = True
        print("Gmail authenticated. Actions on Gmail will be performed.\n")
    except FileNotFoundError:
        service = None
        GMAIL_AVAILABLE = False
        print("Gmail credentials not found. Using local database only.\n")

    rules_data = load_rules()
    emails = get_all_emails()  # Returns list of tuples

    print(f"Loaded {len(rules_data)} rules and {len(emails)} emails\n")

    for rule_idx, rule in enumerate(rules_data, start=1):
        predicate_type = rule['predicate'].lower()
        rule_conditions = rule['rules']
        actions = rule['actions']

        matched_any = False
        for email in emails:
            # Build email dict from tuple returned by get_all_emails()
            email_dict = {
                'id': email[0],
                'sender': email[1],
                'recipient': email[2],
                'subject': email[3],
                'body': email[4],
                'received': email[5],
                'is_unread': email[6],
                'labels': email[7],
            }

            # Check conditions
            matches = [match_condition(email_dict, cond) for cond in rule_conditions]
            matched = (predicate_type == 'any' and any(matches)) or (predicate_type == 'all' and all(matches))

            if matched:
                matched_any = True
                print(f"✔ Matched Email ID: {email_dict['id']}")
                print(f"  From   : {email_dict['sender']}")
                print(f"  Subject: {email_dict['subject']}")
                print(f"  Actions:")

                for action in actions:
                    action_lower = action.lower()
                    try:
                        if GMAIL_AVAILABLE:
                            if action_lower == "mark as read":
                                mark_as_read(service, email_dict['id'])
                                print(f"    - Marked as read")
                            elif action_lower == "mark as unread":
                                mark_as_unread(service, email_dict['id'])
                                print(f"    - Marked as unread")
                            elif action_lower.startswith("move message:"):
                                label_name = action.split(":", 1)[1].strip()
                                move_message(service, email_dict['id'], label_name)
                                print(f"    - Moved message to label '{label_name}'")
                        else:
                            # Gmail not available; only print actions
                            print(f"    - Would perform action: '{action}' ")
                    except Exception as e:
                        print(f"    - Error performing action '{action}': {e}")
                print("-"*80)

        if not matched_any:
            print("No emails matched this rule.\n")

if __name__ == '__main__':
    process_rules()
