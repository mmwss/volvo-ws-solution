from calendar_app import Calendar
from event import Event

from datetime import datetime
from tabulate import tabulate

def populate_calendar(calendar):
    """
    Populates the calendar with predefined events for testing purposes.
    """
    events_data = [
        {
            'title': 'Project Kickoff',
            'date': '2024-11-20',
            'start_time': '09:00',
            'end_time': '10:30',
            'description': 'Initial project kickoff meeting with the team.',
            'participants': ['Alice', 'Bob', 'Charlie']
        },
        {
            'title': 'Client Presentation',
            'date': '2024-11-21',
            'start_time': '11:00',
            'end_time': '12:00',
            'description': 'Present the project proposal to the client.',
            'participants': ['Dave', 'Eve']
        },
        {
            'title': 'Weekly Sync-Up',
            'date': '2024-11-22',
            'start_time': '14:00',
            'end_time': '15:00',
            'description': 'Weekly team sync-up to discuss progress.',
            'participants': ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']
        },
        {
            'title': 'Code Review Session',
            'date': '2024-11-23',
            'start_time': '16:00',
            'end_time': '17:30',
            'description': 'Review codebase for the new feature implementation.',
            'participants': ['Frank', 'Grace']
        },
        {
            'title': 'Design Workshop',
            'date': '2024-11-24',
            'start_time': '10:00',
            'end_time': '12:00',
            'description': 'Workshop on UI/UX design principles.',
            'participants': ['Heidi', 'Ivan', 'Judy']
        },
        {
            'title': 'Sprint Planning',
            'date': '2024-11-25',
            'start_time': '09:30',
            'end_time': '11:00',
            'description': 'Plan tasks for the next sprint.',
            'participants': ['Alice', 'Bob', 'Charlie']
        },
        {
            'title': 'Database Migration',
            'date': '2024-11-26',
            'start_time': '13:00',
            'end_time': '15:00',
            'description': 'Migrate the database to the new server.',
            'participants': ['Frank', 'Grace', 'Heidi']
        },
        {
            'title': 'Team Building Activity',
            'date': '2024-11-27',
            'start_time': '15:30',
            'end_time': '17:00',
            'description': 'Outdoor activities to promote team bonding.',
            'participants': ['All Team Members']
        },
        {
            'title': 'Performance Review',
            'date': '2024-11-28',
            'start_time': '10:00',
            'end_time': '11:30',
            'description': 'Quarterly performance review meeting.',
            'participants': ['Manager', 'Alice', 'Bob']
        },
        {
            'title': 'Security Training',
            'date': '2024-11-29',
            'start_time': '09:00',
            'end_time': '12:00',
            'description': 'Mandatory security awareness training.',
            'participants': ['All Team Members']
        }
    ]

    for event_data in events_data:
        event_date = datetime.strptime(event_data['date'], '%Y-%m-%d').date()
        start_time = datetime.strptime(event_data['start_time'], '%H:%M').time()
        end_time = datetime.strptime(event_data['end_time'], '%H:%M').time()
        participants = event_data['participants']
        new_event = Event(
            title=event_data['title'],
            date=event_date,
            start_time=start_time,
            end_time=end_time,
            description=event_data['description'],
            participants=participants
        )
        if calendar.add_event(new_event):
            print(f"Added event: {new_event.title} on {new_event.date}")
        else:
            print(f"Conflict detected, could not add event: {new_event.title} on {new_event.date}")

def main():
    calendar = Calendar()
    populate_calendar(calendar)

    # Display all upcoming events
    events = calendar.get_upcoming_events()
    if events:
        print("\nUpcoming Events:")
        table = [[
            event.date.strftime('%Y-%m-%d'),
            event.title,
            f"{event.start_time.strftime('%H:%M')} - {event.end_time.strftime('%H:%M')}",
            ', '.join(event.participants) if event.participants else 'None',
            event.description
        ] for event in events]
        headers = ["Date", "Title", "Time", "Participants", "Description"]
        print(tabulate(table, headers, tablefmt="grid"))
    else:
        print("No upcoming events.")

if __name__ == '__main__':
    main()
