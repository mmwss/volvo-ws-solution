from event import Event
from calendar_app import Calendar

import unittest
from datetime import datetime, date, time

class TestEvent(unittest.TestCase):

    def test_event_initialization(self):
        event = Event(
            title='Team Meeting',
            date=date(2023, 10, 15),
            start_time=time(9, 0),
            end_time=time(10, 0),
            description='Weekly team sync-up.',
            participants=['Alice', 'Bob', 'Charlie']
        )
        self.assertEqual(event.title, 'Team Meeting')
        self.assertEqual(event.date, date(2023, 10, 15))
        self.assertEqual(event.start_time, time(9, 0))
        self.assertEqual(event.end_time, time(10, 0))
        self.assertEqual(event.description, 'Weekly team sync-up.')
        self.assertEqual(event.participants, ['Alice', 'Bob', 'Charlie'])

    def test_event_conflict(self):
        event1 = Event(
            title='Event 1',
            date=date(2023, 10, 15),
            start_time=time(9, 0),
            end_time=time(10, 0)
        )
        event2 = Event(
            title='Event 2',
            date=date(2023, 10, 15),
            start_time=time(9, 30),
            end_time=time(10, 30)
        )
        event3 = Event(
            title='Event 3',
            date=date(2023, 10, 16),
            start_time=time(9, 0),
            end_time=time(10, 0)
        )
        self.assertTrue(event1.conflicts_with(event2))
        self.assertFalse(event1.conflicts_with(event3))

class TestCalendar(unittest.TestCase):

    def setUp(self):
        self.calendar = Calendar()

    def test_add_event_no_conflict(self):
        event = Event(
            title='Team Meeting',
            date=date(2023, 10, 15),
            start_time=time(9, 0),
            end_time=time(10, 0)
        )
        result = self.calendar.add_event(event)
        self.assertTrue(result)
        self.assertIn(event, self.calendar.events)

    def test_add_event_with_conflict(self):
        event1 = Event(
            title='Event 1',
            date=date(2023, 10, 15),
            start_time=time(9, 0),
            end_time=time(10, 0)
        )
        event2 = Event(
            title='Event 2',
            date=date(2023, 10, 15),
            start_time=time(9, 30),
            end_time=time(10, 30)
        )
        self.calendar.add_event(event1)
        result = self.calendar.add_event(event2)
        self.assertFalse(result)
        self.assertNotIn(event2, self.calendar.events)

    def test_get_events_on_date(self):
        event1 = Event(
            title='Event 1',
            date=date(2023, 10, 15),
            start_time=time(9, 0),
            end_time=time(10, 0)
        )
        event2 = Event(
            title='Event 2',
            date=date(2023, 10, 16),
            start_time=time(11, 0),
            end_time=time(12, 0)
        )
        self.calendar.add_event(event1)
        self.calendar.add_event(event2)
        events_on_date = self.calendar.get_events_on_date(date(2023, 10, 15))
        self.assertEqual(len(events_on_date), 1)
        self.assertIn(event1, events_on_date)

    def test_delete_event(self):
        event = Event(
            title='Event to Delete',
            date=date(2023, 10, 15),
            start_time=time(9, 0),
            end_time=time(10, 0)
        )
        self.calendar.add_event(event)
        result = self.calendar.delete_event('Event to Delete', date(2023, 10, 15))
        self.assertTrue(result)
        self.assertNotIn(event, self.calendar.events)

    def test_edit_event(self):
        event = Event(
            title='Original Event',
            date=date(2023, 10, 15),
            start_time=time(9, 0),
            end_time=time(10, 0)
        )
        self.calendar.add_event(event)
        new_event = Event(
            title='Edited Event',
            date=date(2023, 10, 15),
            start_time=time(10, 0),
            end_time=time(11, 0)
        )
        result = self.calendar.edit_event('Original Event', date(2023, 10, 15), new_event)
        self.assertTrue(result)
        self.assertIn(new_event, self.calendar.events)
        self.assertNotIn(event, self.calendar.events)

    def test_get_upcoming_events(self):
        today = date.today()
        past_event = Event(
            title='Past Event',
            date=today.replace(year=today.year - 1),
            start_time=time(9, 0),
            end_time=time(10, 0)
        )
        upcoming_event = Event(
            title='Upcoming Event',
            date=today,
            start_time=time(11, 0),
            end_time=time(12, 0)
        )
        self.calendar.add_event(past_event)
        self.calendar.add_event(upcoming_event)
        upcoming_events = self.calendar.get_upcoming_events()
        self.assertIn(upcoming_event, upcoming_events)
        self.assertNotIn(past_event, upcoming_events)

if __name__ == '__main__':
    unittest.main()
