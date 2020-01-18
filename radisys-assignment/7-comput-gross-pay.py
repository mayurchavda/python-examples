hours = eval(input('Enter Hours: '))
rate = eval(input('Rate: '))
comp = rate * 1.5

def find_gross_pay(hours, rate):
    if(hours >= 0 and rate >= 0):
        if hours > 40 :
            extrahours = hours - 40
            gp = 40*rate + extrahours * comp
        elif hours < 40:
            gp = hours * rate
        print("Gross Pay: %s "%gp)
    else:
        print("hours and rate can not be negative")

find_gross_pay(hours, rate)
