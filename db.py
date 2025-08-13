import sqlite3

def init_db():
    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS emails (
            id TEXT PRIMARY KEY,
            sender TEXT,
            recipient TEXT,
            subject TEXT,
            body TEXT,
            received TEXT,
            is_unread INTEGER,
            labels TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_email(email):
    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR IGNORE INTO emails 
        (id, sender, recipient, subject, body, received, is_unread, labels)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        email['id'], email['sender'], email['recipient'], email['subject'],
        email['body'], email['received'], email['is_unread'], email['labels']
    ))
    conn.commit()
    conn.close()

def get_all_emails():
    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM emails")
    rows = cursor.fetchall()
    conn.close()
    return rows
