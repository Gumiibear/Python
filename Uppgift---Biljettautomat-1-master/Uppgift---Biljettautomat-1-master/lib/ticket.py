
def ask_age():
    age = raw_input("What is your age: ")
    age = int(age)
    if age < 0:
       print "Then you are not born yet."
       ask_age()
    return age

def ticket_price(age):
    if age < 18:
        return "10 Kr."
    elif age < 65:
        return "20 Kr."
    else:
        return "15 Kr."

print ticket_price(age=ask_age())