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
    while True:
        city_input = input('Please Enter the name of the City you want to explore: chicago, new york city or washignton\n').lower()
        try:
            if city_input in ('chicago','new york city','washington'):
                city = city_input
                break
            else:
                print('Please enter a valid city from the list\n')
                continue
        # Handle Value and type Errors        
        except ValueError:
            print("Incorrect value")
        except TypeError:
            print('needs String')


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month_input = input('Please select a month for the data you want to filter: all, january, february, ... , june\n').lower()
        months = ['january','february','march','april','may','june']
        try:
            if (month_input == 'all') or (month_input in months):
                month = month_input
                break
            elif month_input not in months:
                print('Please enter a valid month from the list.')
                continue
        except ValueError:
            print("Incorrect value")
        except TypeError:
            print('needs String')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day_input = input('Please enter the day of the week you want to filter by: all, monday, tuesday, ... sunday\n').lower()
        days = ['monday','teusday','wednesday','thursday','friday','saterday','sunday']
        try:
            if (day_input == 'all') or (day_input in days):
                day = day_input
                break
            elif day_input not in days:
                print('Please enter a valid day of the week')
                continue
        except ValueError:
            print("Incorrect value")
        except TypeError:
            print('needs String')

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

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Filter by Month:
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    # Filter by day_of_week:
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is {}'.format(common_month))

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day of the week is, ',common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common start hour is, ',common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used Start Station was, ',common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most commonly used End Station was, ',common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_combination = df['combination'].mode()[0]
    print('The most frequently used combination of Start and End Stations are, ',common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel time was: ',(((total_travel_time)/60)/60)/24, ' days')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel time was: ',(mean_travel_time)/60, ' mins')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = pd.value_counts(df['User Type'])
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_types = pd.value_counts(df['Gender'])
        print(gender_types)
    else:
        print('Gender column does not exist for this city!')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth = np.nanmin(df['Birth Year']).min()
        print('The Earliest Birth year is, ',earliest_birth)

        most_recent_birth = np.nanmax(df['Birth Year']).max()
        print('The Most Recent Birth year is, ',most_recent_birth)

        most_common_birth = df['Birth Year'].mode()[0]
        print('The Most Common Birth Year is ,',most_common_birth)
    else:
        print('Birth Year Column does not exist for this city!')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw(df):
    """ Displays Raw Data Upon User Request"""

    print('\nRaw Data Options...\n')
    start_time = time.time()


    while True:
        user_input = input('Do you want to display the raw data (yes or no) ?\n').lower()
        if user_input != 'yes':
            break
        else:

            n = 5
            print(df[0:][:n])

            while True:
                # Display 5 lines of Raw Data:
                user_input = input('Would you like to see an additional 5 lines of data?\n (yes or no)\n').lower()

                if user_input != 'yes':
                    break
                else:
                    n += 5

                    print(df[0:][:n])
        break




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

        # Raw Data Display Function:
        display_raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
