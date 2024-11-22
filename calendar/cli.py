from calendar_app import Calendar
from event import Event

import sys
from tabulate import tabulate
from datetime import datetime, date, time

def parse_date(date_str):
    """
    Parses a date string into a datetime.date object.

    Args:
        date_str (str): The date string in YYYY-MM-DD format.

    Returns:
        datetime.date: The parsed date object.
    """
    try:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None

def parse_time(time_str):
    """
    Parses a time string into a datetime.time object.

    Args:
        time_str (str): The time string in HH:MM format.

    Returns:
        datetime.time: The parsed time object.
    """
    try:
        return datetime.strptime(time_str, '%H:%M').time()
    except ValueError:
        print("Invalid time format. Please use HH:MM.")
        return None

def main():
    calendar = Calendar()
    while True:
        print("\nCommand-Line Calendar and Meeting Scheduler")
        print("Choose an option:")
        print("1. Add Event")
        print("2. View Events on a Date")
        print("3. View Upcoming Events")
        print("4. Edit Event")
        print("5. Delete Event")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        # Add Event
        if choice == '1':
            title = input("Enter event title: ").strip()
            date_str = input("Enter event date (YYYY-MM-DD): ").strip()
            event_date = parse_date(date_str)
            if not event_date:
                continue

            start_time_str = input("Enter start time (HH:MM): ").strip()
            start_time = parse_time(start_time_str)
            if not start_time:
                continue

            end_time_str = input("Enter end time (HH:MM): ").strip()
            end_time = parse_time(end_time_str)
            if not end_time:
                continue

            if end_time <= start_time:
                print("End time must be after start time.")
                continue

            description = input("Enter description: ").strip()
            participants_str = input("Enter participants (comma-separated): ").strip()
            participants = [p.strip() for p in participants_str.split(',')] if participants_str else []
            new_event = Event(title, event_date, start_time, end_time, description, participants)
            if calendar.add_event(new_event):
                print("Event added successfully!")
            else:
                print("Event conflicts with an existing event.")

        # View Events on a Date
        elif choice == '2':
            date_str = input("Enter date to view events (YYYY-MM-DD): ").strip()
            event_date = parse_date(date_str)
            if not event_date:
                continue
            events = calendar.get_events_on_date(event_date)
            if events:
                print(f"\nEvents on {event_date.strftime('%Y-%m-%d')}:")
                table = [[
                    event.title,
                    f"{event.start_time.strftime('%H:%M')} - {event.end_time.strftime('%H:%M')}",
                    ', '.join(event.participants) if event.participants else 'None',
                    event.description
                ] for event in events]
                headers = ["Title", "Time", "Participants", "Description"]
                print(tabulate(table, headers, tablefmt="grid"))
            else:
                print("No events scheduled on this date.")

        # View Upcoming Events
        elif choice == '3':
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

        # Edit Event
        elif choice == '4':
            title = input("Enter the title of the event to edit: ").strip()
            date_str = input("Enter the date of the event (YYYY-MM-DD): ").strip()
            event_date = parse_date(date_str)
            if not event_date:
                continue

            # Find existing event
            events = calendar.get_events_on_date(event_date)
            event_to_edit = None
            for event in events:
                if event.title == title:
                    event_to_edit = event
                    break
            if not event_to_edit:
                print("Event not found.")
                continue

            # Get new details
            print("Enter new details (leave blank to keep current value):")
            new_title = input(f"Enter new title [{event_to_edit.title}]: ").strip()
            new_title = new_title if new_title else event_to_edit.title
            new_date_str = input(f"Enter new date (YYYY-MM-DD) [{event_to_edit.date.strftime('%Y-%m-%d')}]: ").strip()
            new_date = parse_date(new_date_str) if new_date_str else event_to_edit.date
            new_start_time_str = input(f"Enter new start time (HH:MM) [{event_to_edit.start_time.strftime('%H:%M')}]: ").strip()
            new_start_time = parse_time(new_start_time_str) if new_start_time_str else event_to_edit.start_time
            new_end_time_str = input(f"Enter new end time (HH:MM) [{event_to_edit.end_time.strftime('%H:%M')}]: ").strip()
            new_end_time = parse_time(new_end_time_str) if new_end_time_str else event_to_edit.end_time
            if new_end_time <= new_start_time:
                print("End time must be after start time.")
                continue

            new_description = input(f"Enter new description [{event_to_edit.description}]: ").strip()
            new_description = new_description if new_description else event_to_edit.description
            participants_str = input(f"Enter new participants (comma-separated) [{', '.join(event_to_edit.participants)}]: ").strip()
            new_participants = [p.strip() for p in participants_str.split(',')] if participants_str else event_to_edit.participants
            new_event = Event(new_title, new_date, new_start_time, new_end_time, new_description, new_participants)
            if calendar.edit_event(title, event_date, new_event):
                print("Event edited successfully!")
            else:
                print("Could not edit the event due to a conflict.")

        # Delete Event
        elif choice == '5':
            title = input("Enter the title of the event to delete: ").strip()
            date_str = input("Enter the date of the event (YYYY-MM-DD): ").strip()
            event_date = parse_date(date_str)
            if not event_date:
                continue
            if calendar.delete_event(title, event_date):
                print("Event deleted successfully.")
            else:
                print("Event not found.")

        # Exit
        elif choice == '6':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please select a number between 1 and 6.")
