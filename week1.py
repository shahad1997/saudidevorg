from datetime import date# using the libary get time function

if __name__ == "__main__":
    print ("hi in python week 1\n find here calculator system for your age")
    #code for cout the age
    today = date.today()
    current_year=today.strftime("%Y")#to get the current month
    # print(current_year)
    current_month=today.strftime("%m")#to get the current month
    # print(current_month)
    current_day=today.strftime("%d")#to get the current month
    # print(current_day)
    print("Count your age")
    age_year=input("Please enter year:")
    age_month=input("Please enter month:")
    age_day=input("Please enter day:")
    my_age_Y=int(current_year)-int(age_year)
    count_month=abs(int(current_month)-int(age_month))
    my_age_D=int(current_day)-int(age_day)

    if my_age_Y!=0:
        if count_month==0:
            my_age_M = 0
            print(abs(my_age_Y),"Years,",abs(my_age_M),"Months, ",abs(my_age_D)," days 🎉🎆🎆🎉")
        else:
            my_age_M = 12 - count_month
            print(abs(my_age_Y)-1, "Years,", abs(my_age_M), "Months, ", abs(my_age_D), " days 🎉🎆🎆🎉")
    else:
        print("Wow you born this year")



