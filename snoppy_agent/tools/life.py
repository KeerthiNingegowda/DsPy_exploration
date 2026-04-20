from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from datetime import datetime, timedelta, timezone
import os

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]


def get_calendar_service():
    """Authentication and a service object to Google calendar"""
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as f:
            f.write(creds.to_json())
    return build("calendar", "v3", credentials=creds)


def fetch_events(days) -> list:
    """Fetch upcoming events in the next X days from Google calendar
    Args:
        days - Number of days ahead
    Returns
        list - Consisting of summary of the events and the date. To not disclose too much personal info i.e creator, email account, invitelink - this decision was made
        The events consist of birthdays, tasks, reminders, training goals and bill due dates. Includes all day events too.
    """

    service = get_calendar_service()

    start_time = datetime.now(timezone.utc)
    end_time = start_time + timedelta(days=days)

    events = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=start_time.isoformat(),
            timeMax=end_time.isoformat(),
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    items = events.get("items", [])
    return [
        f"Event - {ele["summary"]} on {ele["start"].get("dateTime") or ele["start"].get("date")}"
        for ele in items
    ]
