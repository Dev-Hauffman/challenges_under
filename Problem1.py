#receive a timestamp and converts from 12 hours format into 24 hours format
def convert_time(time):
    hour = time[0] + time[1] #retrieves the hours from the timestamp as it's the "only" thing that changes from one format to the other
    if time[8] == 'A': #identify if it's morning by searching the letter 'A' in 'AM'
        if hour == '12':
            final_time = "00"+(time[2:8])
        else:
            final_time = time[:8]
    else:
        if hour == '12':
            final_time = time[:8]
        else:
            hour_converted = int(hour)+12 #treating case from 1PM to 11PM
            final_time = str(hour_converted)+(time[2:8])
    return final_time
    

time = input('Enter a time: ')
result = convert_time(time)
print(result)
