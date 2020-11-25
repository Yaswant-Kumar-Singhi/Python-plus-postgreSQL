#Taking input from user
age = input('Enter your age')
convert = age * 365 * 60 * 60
print(convert)

# Using format option 

time = input('Enter your time in hours')
print("time in seconds {}".format(int(time)*60))