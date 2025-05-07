from datetime import datetime


def main():
    todaytime = get_date_python()
    secondSinceFjan = getTimeSinceFjan()
    scientificSinceFjan = "{:.2e}".format(secondSinceFjan)
    print(
        f"Second since January 1, 1970 : {secondSinceFjan} or {scientificSinceFjan} in scientific notation"
    )
    print(todaytime.strftime("%b %d %Y"))


def get_date_python():
    return datetime.today()


def getTimeSinceFjan():
    return get_date_python().timestamp()


main()
