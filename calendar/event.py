class Event:
    """
    Represents a calendar event.

    Attributes:
        title (str): The title of the event.
        date (datetime.date): The date of the event.
        start_time (datetime.time): The start time of the event.
        end_time (datetime.time): The end time of the event.
        description (str): A description of the event.
        participants (list of str): A list of participants.
    """

    def __init__(self, title, date, start_time, end_time, description='', participants=None):
        self.title = title
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.description = description
        self.participants = participants if participants else []

    def conflicts_with(self, other_event):
        """
        Determines if this event conflicts with another event.

        Args:
            other_event (Event): The other event to check against.

        Returns:
            bool: True if there is a conflict, False otherwise.
        """
        if self.date != other_event.date:
            return False
        return not (self.end_time <= other_event.start_time or self.start_time >= other_event.end_time)

    def __str__(self):
        participants = ', '.join(self.participants) if self.participants else 'None'
        return (f"Title: {self.title}\n"
                f"Date: {self.date.strftime('%Y-%m-%d')}\n"
                f"Time: {self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')}\n"
                f"Description: {self.description}\n"
                f"Participants: {participants}")
