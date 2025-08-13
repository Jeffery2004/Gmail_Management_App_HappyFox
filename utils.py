import base64
from dateutil import parser as date_parser
from datetime import datetime, timezone

def decode_body(payload):
    if 'data' in payload.get('body', {}):
        data = payload['body']['data']
        return base64.urlsafe_b64decode(data).decode('utf-8', errors='ignore')
    if 'parts' in payload:
        for part in payload['parts']:
            text = decode_body(part)
            if text:
                return text
    return ""

def parse_headers(headers):
    result = {}
    for h in headers:
        name = h['name'].lower()
        if name == 'from':
            result['sender'] = h['value']
        elif name == 'to':
            result['recipient'] = h['value']
        elif name == 'subject':
            result['subject'] = h['value']
        elif name == 'date':
            dt = date_parser.parse(h['value'])
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            else:
                dt = dt.astimezone(timezone.utc)
            result['received'] = dt.isoformat()
    return result

def match_condition(email, condition):
    field = condition['field'].lower()
    if field == 'from':
        field = 'sender'
    elif field == 'to':
        field = 'recipient'

    predicate = condition['predicate'].lower()
    value = condition['value'].lower()

    email_value = str(email.get(field, "")).lower()

    if predicate == 'contains':
        return value in email_value
    if predicate == 'does not contain':
        return value not in email_value
    if predicate == 'equals':
        return email_value == value
    if predicate == 'does not equal':
        return email_value != value

    if field == 'date received':
        try:
            cond_value = int(value)
        except ValueError:
            return False
        email_date = datetime.fromisoformat(email['received'])
        now = datetime.now(tz=email_date.tzinfo)
        diff_days = (now - email_date).days
        diff_months = diff_days / 30

        if predicate == 'less than days':
            return diff_days < cond_value
        if predicate == 'greater than days':
            return diff_days > cond_value
        if predicate == 'less than months':
            return diff_months < cond_value
        if predicate == 'greater than months':
            return diff_months > cond_value

    return False
