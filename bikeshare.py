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
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    global city
    
    city = input("Please enter the city name that you would like to look at: ").lower()

    while city != "chicago" and city != "new york city" and city != "washington":
        city = input("Sorry, we do not currently operate in the city you specified. Please input another: ")

    print('Thanks for that. You selected "{}".'.format(city))


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please enter the month name that you would like to look at. please type "all" if you want to see all months: ').lower()

    while month != "january" and month != "february" and month != "march" and month != "april" and month != "may" and month != "june" and month != "all": 
        month = input("Sorry, we didnt get that. Please input another month e.g. (all, january, february, ... , june): ")

    print('Thanks for that. You selected "{}".'.format(month))
    

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please enter the day name that you would like to look at. please type "all" if you want to see all days: ').lower()

    while day != "monday" and day != "tuesday" and day != "wednesday" and day != "thursday" and day != "friday" and day != "saturday" and day != "sunday" and day != "all":
        day = input("Sorry, we didnt get that. Please input another day e.g. (all, monday, tuesday, ... sunday)): ")

    print('Thanks for that. You selected "{}".'.format(day))
    
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month, day of week and hour from Start Time to create new columns for each
    df['month'] = pd.DatetimeIndex(df['Start Time']).month 
    df['day_of_week'] = pd.DatetimeIndex(df['Start Time']).dayofweek
    df['hour'] = pd.DatetimeIndex(df['Start Time']).hour
    #print(df.head()) #test print to check correct columns have been added
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1 
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day)
        df = df[df['day_of_week']==day]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    common_month = months[common_month-1] # index back so that months are displayed as there name, not a number.
    print('The most common month was {}.'.format(common_month))

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    common_day = days[common_day] # index back so that days are displayed as there name, not a number.
    print('The most common day was {}.'.format(common_day))
    
    
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('The most common start hour was {}:00.'.format(popular_hour))
    
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df.groupby(['Start Station']).size().nlargest(1)
    print('The most common start station was:\n{}.'.format(popular_start_station))
    
    
    # TO DO: display most commonly used end station
    popular_end_station = df.groupby(['End Station']).size().nlargest(1)
    print('\nThe most common end station was:\n{}.'.format(popular_end_station))
    
    # TO DO: display most frequent combination of start station and end station trip
    frequent_combo = df.groupby(['Start Station','End Station']).size().nlargest(1)
    print('\nThe most frequent combination of start and end station trip:\n{}.'.format(frequent_combo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()
    travel_time = (travel_time / 60) # display time in minutes instad of seconds
    print('The total travel time in minutes is:\n{}.'.format(travel_time))
    
    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    mean_time = (mean_time / 60) # display time in minutes instad of seconds
    print('\nThe mean travel time in minutes is:\n{}.'.format(mean_time))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count = df['User Type'].value_counts()
    print('Count of user types:\n{}.'.format(user_count))
    
    # TO DO: Display counts of gender
    if city == 'new york city' or city == 'chicago':
        gender_count = df['Gender'].value_counts()
        print('\nCount of genders:\n{}.'.format(gender_count))

    # TO DO: Display earliest, most recent, and most common year of birth
    # earliest year of birth:
    if city == 'new york city' or city == 'chicago':
        earliest_year = df['Birth Year'].min()
        print('\nEarliest birth year:\n{}.'.format(earliest_year))
    

        # most recent year of birth:
    if city == 'new york city' or city == 'chicago':
        recent_year = df['Birth Year'].max()
        print('\nMost recent birth year:\n{}.'.format(recent_year))
    
        # Most common year of birth:
    if city == 'new york city' or city == 'chicago':
        common_year = df['Birth Year'].mode()[0]
        print('\nMost common birth year:\n{}.'.format(common_year))
    
    
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
        
        raw_code = input("Would you like to see the first 5 rows of raw data? Enter yes or no: ")
        if raw_code.lower() == 'yes':
            print(df.head())

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
