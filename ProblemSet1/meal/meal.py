def main():
    time = input("What time is it? ")
    hours, minutes = convert(time)

    if (hours == 7 and minutes <= 59) or (hours == 8 and minutes == 0):
        print("breakfast time")
    
    elif (hours == 12 and minutes <= 59) or (hours == 13 and minutes == 0):
        print("lunch time")
    
    elif (hours == 18 and minutes <= 59) or (hours == 19 and minutes == 0):
        print("dinner time")

    else:
        print(end='')


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = (float(minutes) / 60) * 10
    return hours, minutes


if __name__ == "__main__":
    main()
