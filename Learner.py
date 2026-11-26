from datetime import date
def calculate_age(birthday_str: str) -> int:
    birthday = date.fromisoformat(birthday_str)
    today = date.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    return age
user_bday = input("enter birthday in format yyyy-mm-dd: ")
calculate_age(user_bday)