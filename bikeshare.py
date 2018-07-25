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
    print('Hello! Bicycling Is Good For Health!')
    
    cities = ['chicago','new york city','washington']
    while True:
        city = input('\nLet\'s explore rich data of some major US Bikeshare database analysis!\n'
                     'Explore for major cities like Chicago, New York City, Washington.\n')
        city = city.lower()
        if city == 'newyork':
            city = 'new york city'     
        elif city == 'new york':
            city = 'new york city'
            
        if city in cities:
            print('Loading for city {}.'.format(city))
            break    
        else:
            print('Couldn\'t find the required data. Please Try Again With Appropriate Name!')
                        
    
    month = input('\nFilter for month - January, February, March, April, May or June or All\n')
    month = month.lower()
    months = ['january', 'february', 'march', 'april',
                   'may', 'june', 'all']
    if month in months:
        print('Loading for month {}'.format(month)) 
    else:
        print('Couldn\'t find any data for the entered month. Please Try Again With Appropriate Month Name Between January-June!')

    
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
    file = CITY_DATA[city]
    df = pd.read_csv(file)
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

    
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    common_month=df['month'].mode()[0]
    print('Most common month is {}.'.format(common_month))
    
    
    df['weekday']=df['Start Time'].dt.weekday
    common_day = df['weekday'].mode()[0]
    print('Most common day is {}.'.format(common_day))

    
    df['Start Hour']=df['Start Time'].dt.hour
    common_hour = df['Start Hour'].mode()[0]
    print('The most common hour of day for start time is {}.'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

   
    common_start = df['Start Station'].mode()[0]
    print('Most common start station is {}.'.format(common_start))

    
    common_end = df['End Station'].mode()[0]
    print('Most common end station is {}.'.format(common_end))

    df['trip'] = df['Start Station'] + ' to ' + df['End Station']
    combination_trip = df['trip'].mode()[0]
    print('The most frequent combination of trip is {}.'.format(combination_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

   
    total_trip_duration = df['Trip Duration'].sum()
    print('The total trip duration is {} seconds.'.format(total_trip_duration))

    
    mean_trip_duration = df['Trip Duration'].mean()
    print('Mean trip duration is {} seconds.'.format(mean_trip_duration))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(city, df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    user_types = df['User Type'].value_counts()
    print('User Types : {}'.format(user_types))

    
    if 'Gender' in df.columns:
        print('\nLoading gender stats of users from city {}...\n'.format(city))
        start_time = time.time()
        gender_types = df['Gender'].value_counts()
        print('Gender stats : {}'.format(gender_types))

    
    if 'Birth Year' in df.columns:
        print('\nLoading birth year stats of users in the city {}...\n'.format(city))
        start_time = time.time()
        common_birth = int(df['Birth Year'].mode()[0])
        print('\nMost common birth year is {}'.format(common_birth))
        oldest_birth = int(df['Birth Year'].min())
        print('\nOldest birth year among users data is {}'.format(oldest_birth))
        youngest_birth = int(df['Birth Year'].max())
        print('\nThe youngest birth year is {}'.format(youngest_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw(df):
    rawdata = ''
    start = 0
    stop = 5
    while rawdata != 'no':
        rawdata = input('You Can Grab Raw Data Here. Enter \'yes\' or \'no\' for that. \n')
        if rawdata.lower().strip() == 'yes':
            for i in range(start,stop):
                print('\n{}'.format(df.iloc[i].drop(df.columns[0]).fillna('Insufficient Data')))
            start += 5
            stop += 5
        elif raw_info.lower().strip() != 'no':
            print("\nInvalid Option. Please tryna enter \'yes\' \'or\' no \n") 

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(city, df)
        raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
