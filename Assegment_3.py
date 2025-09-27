import datetime

def days_until_birthday(month, day):
    current_date = datetime.date.today()
    current_year = current_date.year

    birthday = datetime.date(current_year,month,day)
    if birthday < current_date:
        birthday = datetime.date(current_year+1,month,day)

    return (birthday -current_date).days


def birthday_message(name,month,day):
    print(f"Hello {name}! Your birthday is in {days_until_birthday(month,day)} days")


birthday_message("Mamy_Jean",5,27)







