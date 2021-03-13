def convert_time(time):
    hour = time[0] + time[1]
    if time[8] == 'A':
        if hour == '12':
            final_time = "00"+(time[2:8])
        else:
            final_time = time[:8]
    else:
        if hour == '12':
            final_time = time[:8]
        elif hour[0] == '1':
            hour_converted = int(hour)+12
            final_time = str(hour_converted)+(time[2:8])
        else:
            hour_converted = int(time[1])+12
            final_time = str(hour_converted)+(time[2:8])
    return final_time
    

time = input('Enter a time: ')
result = convert_time(time)
print(result)
