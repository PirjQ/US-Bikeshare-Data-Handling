import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to 

handle invalid inputs
    city = ''
    while city.lower() not in ['chicago', 'new york', 'washington']:
        city = input('\nLet\'s explore rich data of some major US Bikeshare database analysis!\n'
                     'Explore for major cities like Chicago, New York City, Washington.\n')
        if city.lower() == 'chicago':
            return 'chicago.csv'
        elif city.lower() == 'new york':
            return 'new_york_city.csv'
        elif city.lower() == 'new york city':
            return 'new_york_city.csv'
        elif city.lower() == 'washington':
            return 'washington.csv'
        else:
            print('Couldn\'t find the required data. Please Try Again With Appropriate Name!')
                        
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ''
    months_dict = {'january': 1, 'february': 2, 'march': 3, 'april': 4,
                   'may': 5, 'june': 6}
    while months.lower() not in months_dict.keys():
        months = input('\nMonth - January, February, March, April, May, or June?\n')
        if months.lower() not in months_dict.keys():
            print('Couldn\'t find any data for the entered month. Please Try Again With Appropriate 

Month Name Between January-June!')
    month = months_dict[months.lower()]
    return ('2018-{}'.format(month), '2018-{}'.format(month + 1)) 

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    this_month = get_month()[0]
    month = int(this_month[5:])
    valid_date = False
    while valid_date == False:    
        is_int = False
        day = input('\nEnter the day(WeekDays) you\'d like to search for. Type response in integer.\n')
        while is_int == False:
            try:
                day = int(day)
                is_int = True
            except ValueError:
                print('Couldn\'t find any. Please type your response as an integer.')
                day = input('\nEnter the day you\'d like to search for. Type response in integer.\n')
        try:
            start_date = datetime(2018, month, day)
            valid_date = True
        except ValueError as e:
            print(str(e).capitalize())
    end_date = start_date + timedelta(days=1)
    return (str(start_date), str(end_date))

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = ''
    while df.lower() not in ['month', 'day', 'none']:
        df = input('\nFilter the data by month, day, or type \'All\' for no filter at all.\n')
        if df.lower() not in ['month', 'day', 'none']:
            print('Couldn\'t find any. Please Try Again!')

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    common = int(df['start_time'].dt.month.mode())
    common_month = months[common - 1]
    print('Most common month is {}.'.format(common_month))
    
    # TO DO: display the most common day of week
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    common = int(df['start_time'].dt.day.mode())
    common_day = days[common - 1]
    print('Most common day is {}.'.format(common_day))

    # TO DO: display the most common start hour
    common_hour = int(df['start_time'].dt.hour.mode())
    if common_hour == 0:
        am_pm = 'am'
        common_hour_obt = 12
    elif 1 <= common_hour < 13:
        am_pm = 'am'
        common_hour_obt = common_hour
    elif 13 <= common_hour < 24:
        am_pm = 'pm'
        common_hour_obt = common_hour - 12
    print('The most common hour of day for start time is {}{}.'.format(common_hour_obt, am_pm))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['start_station'].mode().to_string(common = False)
    print('Most common start station is {}.'.format(common_start))

    # TO DO: display most commonly used end station
    common_end = df['end_station'].mode().to_string(common = False)
    print('Most common end station is {}.'.format(common_end))

    # TO DO: display most frequent combination of start station and end station trip
    df['journey'] = df['start_station'].str.cat(df['end_station'], sep=' to ')
    combination_trip = df['journey'].mode().to_string(common = False)
    print('The most frequent combination of trip is {}.'.format(combination_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration = df['trip_duration'].sum()
    m, s = divmod(total_duration, 60)
    h, m = divmod(m, 60)
    print('The total trip duration is {} hours, {} minutes and {} seconds.'.format(h, m, s))

    # TO DO: display mean travel time
    mean_trip_duration = round(df['trip_duration'].mean())
    m, s = divmod(average_duration, 60)
    if m > 60:
        h, m = divmod(m, 60)
        print('Mean trip duration is {} hours, {} minutes and {} seconds.'.format(h, m, s))
    else:
        print('Mean trip duration is {} minutes and {} seconds.'.format(m, s))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    subscriber = df.query('user_type == "Subscriber"').user_type.count()
    customer = df.query('user_type == "Customer"').user_type.count()
    print('There are {} Subscribers and {} Customers.'.format(subscriber, customer))

    # TO DO: Display counts of gender
    male = df.query('gender == "Male"').gender.count()
    female = df.query('gender == "Male"').gender.count()
    print('There are {} male users and {} female users.'.format(male, female))

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest = int(df['birth_year'].min())
    most_recent = int(df['birth_year'].max())
    most_common = int(df['birth_year'].mode())
    print('Oldest users using this Bikeshare are born in {}. \nYoungest users are born in {}. \nMost 

common birth year of users is {}'.format(earliest, most_recent, most_common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
