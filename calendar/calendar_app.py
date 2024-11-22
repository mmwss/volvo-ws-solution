from datetime import date

class Calendar:
    """
    Manages a collection of events.

    Attributes:
        events (list of Event): The list of scheduled events.
    """

    def __init__(self):
        self.events = []

    def add_event(self, event):
        """
        Adds a new event to the calendar if there is no conflict.

        Args:
            event (Event): The event to add.

        Returns:
            bool: True if the event was added, False otherwise.
        """
        for existing_event in self.events:
            if event.conflicts_with(existing_event):
                return False
        self.events.append(event)
        self.events.sort(key=lambda e: (e.date, e.start_time))
        return True

    def get_events_on_date(self, event_date):
        """
        Retrieves all events scheduled on a given date.

        Args:
            event_date (datetime.date): The date to retrieve events for.

        Returns:
            list of Event: The list of events on that date.
        """
        return [event for event in self.events if event.date == event_date]

    def delete_event(self, title, event_date):
        """
        Deletes an event based on its title and date.

        Args:
            title (str): The title of the event.
            event_date (datetime.date): The date of the event.

        Returns:
            bool: True if the event was deleted, False otherwise.
        """
        for event in self.events:
            if event.title == title and event.date == event_date:
                self.events.remove(event)
                return True
        return False

    def edit_event(self, title, event_date, new_event):
        """
        Edits an existing event.

        Args:
            title (str): The title of the event to edit.
            event_date (datetime.date): The date of the event to edit.
            new_event (Event): The new event data.

        Returns:
            bool: True if the event was edited, False otherwise.
        """
        self.delete_event(title, event_date)
        return self.add_event(new_event)

    def get_upcoming_events(self):
        """
        Retrieves all upcoming events.

        Returns:
            list of Event: The list of upcoming events.
        """
        today = date.today()
        return [event for event in self.events if event.date >= today]
