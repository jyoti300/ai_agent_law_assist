from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta

def add_event(name, email, date, time):
    creds = service_account.Credentials.from_service_account_file(
        "credentials.json",
        scopes=["https://www.googleapis.com/auth/calendar"]
    )

    service = build("calendar", "v3", credentials=creds)

    start = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
    end = start + timedelta(minutes=30)

    event = {
        "summary": f"Legal Appointment - {name}",
        "start": {"dateTime": start.isoformat(), "timeZone": "Asia/Kolkata"},
        "end": {"dateTime": end.isoformat(), "timeZone": "Asia/Kolkata"},
        "attendees": [{"email": email}],
    }

    service.events().insert(calendarId="primary", body=event).execute()
