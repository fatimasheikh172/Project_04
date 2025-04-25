def main():
    
    # define days , minutes , hours $ seconds

    days_in_year = 365
    hours_in_day = 24
    minutes_in_hour = 60
    second_in_minute = 60

    # Calculate total seconds in a year
    seconds_in_year = days_in_year * hours_in_day * minutes_in_hour * second_in_minute

    
    print(f"There are {seconds_in_year} seconds in a year!")



if __name__ == '__main__':
    main()
