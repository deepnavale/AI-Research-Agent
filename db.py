import sqlite3
import datetime

def init_db():
    conn = sqlite3.connect('research_reports.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query TEXT NOT NULL,
            report TEXT NOT NULL,
            timestamp DATETIME NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_report(query: str, report: str):
    conn = sqlite3.connect('research_reports.db')
    cursor = conn.cursor()
    timestamp = datetime.datetime.now()
    cursor.execute(
        "INSERT INTO reports (query, report, timestamp) VALUES (?, ?, ?)",
        (query, report, timestamp)
    )
    conn.commit()
    conn.close()

def get_all_reports():
    conn = sqlite3.connect('research_reports.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, query, report, timestamp FROM reports ORDER BY timestamp DESC")
    reports = cursor.fetchall()
    conn.close()
    return reports