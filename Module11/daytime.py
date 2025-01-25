import datetime
import os

current_time = datetime.datetime.now()

print("Year: ", current_time.year)
print("Month: ", current_time.month)
print("Day: ", current_time.day)
print("Hour: ", current_time.hour)
print("Minute: ", current_time.minute)
print("Second: ", current_time.second)
print("Microsecond: ", current_time.microsecond)

current_date = datetime.datetime.now().date()

print(current_date)

print("Year: ", current_date.year)
print("Month: ", current_date.month)
print("Day: ", current_date.day)

settime = datetime.datetime.now()

specific_time = datetime.date(2000,1,1)

print(specific_time.year)
print(specific_time.month)
print(specific_time.day)

future_time = settime + datetime.timedelta(days=100)
past_time = settime - datetime.timedelta(days=100)

print(future_time)
print(past_time)

teksti = "hello this is the text \n i want to write"

with open("example.txt","w") as file:
    file.write(teksti)

file_path = "example.txt"
file = open(file_path,"r")

content = file.read()
print(content)
file.close()

with open("example.txt","r") as file:
    lines = file.readlines()
    print(lines)

with open("example.txt", "r") as file:
        line = file.readline()
        print(line)

with open("example.txt", "a") as file:
        file.write("\nnew data appended")

if os.path.exists("example.txt"):
    print("file exists")

