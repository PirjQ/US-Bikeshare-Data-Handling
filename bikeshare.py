import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april',
                   'may', 'june', 'all']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Explore for major cities like Chicago, New York City, Washington.Type in your choice\n')
    city = city.lower()
    while city not in ['chicago', 'new york', 'washington']:
        city = input('\nLet\'s explore rich data of some major US Bikeshare database analysis!\n'
                     'Explore for major cities like Chicago, New York City, Washington.\n')
        if city == 'chicago':
            return 'chicago.csv'
        elif city == 'new york':
            return 'new_york_city.csv'
        elif city == 'new york city':
            return 'new_york_city.csv'
        elif city == 'washington':
            return 'washington.csv'
        else:
            print('Couldn\'t find the required data. Please Try Again With Appropriate Name!')
                        
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('\nFilter for month - January, February, March, April, May or June or All\n')
    month = month.lower()
    months = ['january', 'february', 'march', 'april',
                   'may', 'june', 'all']
    if month in months:
        print('Loading for month {}'.format(month)) 
    else:
        print('Couldn\'t find any data for the entered month. Please Try Again With Appropriate Month Name Between January-June!')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\nFilter by Week day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All\n')
    day = day.title().lower()
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
 
    if day in days:
        print('Loading for day {}'.format(day))
    else:
        print('Couldn\'t find any data for the entered day. Please Try Again With Appropriate Week Day Name!')
            
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
    file_name = CITY_DATA[city]
    df = pd.read_csv(file_name)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['weekday']=df['Start Time'].dt.weekday
    if month in months != 'all':
        month = months.index(month)+1
        df=df[df['month']==month]
    if day in days != 'all':
        day=days.index(day)
        df = df[df['weekday'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    common_month=months[df['month'].mode()[0]-1]
    print('Most common month is {}.'.format(common_month))
    
    # TO DO: display the most common day of week
    df['weekday']=df['Start Time'].dt.weekday
    common_day = days[df['weekday'].mode()[0]]
    print('Most common day is {}.'.format(common_day))

    # TO DO: display the most common start hour
    df['Start Hour']=df['Start Time'].dt.hour
    common_hour = df['Start Hour'].mode()[0]
    print('The most common hour of day for start time is {}.'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('Most common start station is {}.'.format(common_start))

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('Most common end station is {}.'.format(common_end))

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + ' to ' + df['End Station']
    combination_trip = df['trip'].mode()[0]
    print('The most frequent combination of trip is {}.'.format(combination_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    print('The total trip duration is {} seconds.'.format(total_trip_duration))

    # TO DO: display mean travel time
    mean_trip_duration = df['Trip Duration'].mean()
    print('Mean trip duration is {} seconds.'.format(mean_trip_duration))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(city, df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types : {}'.format(user_types))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print('\nLoading gender stats of users from city {}...\n'.format(city))
        start_time = time.time()
        gender_types = df['Gender'].value_counts()
        print('Gender stats : {}'.format(gender_types))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('\nLoading birth year stats of users in the city {}...\n'.format(city))
        start_time = time.time()
        common_birth = int(df['Birth Year'].mode()[0])
        print('\nMost common birth year is {}'.format(common_birth))
        oldest_birth = int(df['Birth year'].min())
        print('\nOldest birth year among d is {}'.format(oldest_birth))
        youngest_birth = int(df['Birth Year'].max())
        print('\nThe youngest birth year is {}'.format(youngest_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(city, df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
