hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

			# 1. Calculate the total number of minutes from the start of the day
            
total_mins = (hour * 60) + mins + dura

"""
 2. Find the end time hour and correct it to the (0..23) range
 Get the total number of hours: divide total_mins by 60
 Use modulo 24 to correct hours to fall in the (0..23) range
"""

end_hour = (total_mins // 60) % 24

"""
 3. Correct minutes to fall in the (0..59) range
 Get the remaining minutes: total_mins modulo 60
"""

end_mins = total_mins % 60

"""
 Print the result
 The sep='' ensures no extra spaces are printed between the hour,
 the colon, and the minutes.
"""

print(end_hour, ":", end_mins, sep='')