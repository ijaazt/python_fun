day_num = int(input("What day Number? "))
day_names = ["Sunday", "Monday", "Tuesday", "Wendnesday", "Thursday", "Fridaay", "Saturday"]

if day_num < 7 and day_num >= 0:
    print(day_names[day_num])
else:
    day_num = int(input("There is only 7 days in a week. We start at 0: "))
    if day_num > 6 or day_num < 0:
       pass
    else:
        print(day_names[day_num])


