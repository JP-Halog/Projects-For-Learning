import pandas as pd
import random
from random import randint
from datetime import datetime, timedelta

def generate_random_events(num_events):
    # List of possible events
    events = ['td_dateOpened', 'td_dateClosed', 'td_dateLastActive', 'td_dateLastPayment', 'td_dateMajorDelinquency']

    # Generate random dates within a range
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2022, 12, 31)

    date_list = [start_date + timedelta(days=randint(1, (end_date - start_date).days)) for _ in range(num_events)]

    # Randomly assign events to these dates
    event_list = [random.choice(events) for _ in range(num_events)]

    # Create DataFrame
    df = pd.DataFrame({
        'ttb_dateReported': date_list,
        'event': event_list
    })
