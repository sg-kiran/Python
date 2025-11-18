""""
testing the else if code

"""
week_day = 5
Month: int=1
if(week_day == 1):
    print("Sunday")
elif(week_day ==2):
    print("Monday")
elif(week_day ==3):
    print("Tuesday")
elif(week_day ==4):
    print("wednesday")
elif week_day ==5:
    print("Thursday")
elif(week_day==6):
    print("Friday")
elif(week_day==7):
    print("Saturday")
else:
    print("Not a valid day")
"""
combining two multiple elif also called as nested-if conditions
"""
if(Month == 1):
    if(week_day == 1):
        print("January and Sunday")
    elif(week_day == 2):
        print("January and Monday")
    elif(week_day == 3):
        print("January and Tuesday")
    elif(week_day == 4):
        print("January and Wednesday")
    elif (week_day == 5):
        print("January and Thursday")
    elif (week_day == 6):
        print("January and Friday")
    elif (week_day == 7):
        print("January and Saturday")
else:
    print("Not a valid Month")