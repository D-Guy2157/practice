# **********************************************************************************************************************
import time
# **********************************************************************************************************************
print(time.ctime(0))  # convert a time expressed in seconds since epoch to a readable string
#                       epoch = when your computer thinks time began (reference point)

print(time.time())  # return current seconds since epoch

print("===============================================================================================================")

print(time.ctime(time.time()))  # return current date and time in readable format
time_obj = time.localtime()  # creates a time object
time_utc = time.gmtime()  # UTC
print(time_obj)  # just to show how the time object is formatted
local_time = time.strftime("%B %d %Y %H:%M:%S", time_obj)  # format, time_object
print(local_time)

print("===============================================================================================================")

time_string = "31 July, 2022"
time_objstr = time.strptime(time_string, "%d %B, %Y")
print(time_objstr)

print("===============================================================================================================")

# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2022, 4, 20, 4, 20, 0, 0, 0, 0)
time_tupstr = time.asctime(time_tuple)
print(time_tupstr)

print("===============================================================================================================")

# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2022, 4, 20, 4, 20, 0, 0, 0, 0)
time_tupstr = time.mktime(time_tuple)
print(time_tupstr)