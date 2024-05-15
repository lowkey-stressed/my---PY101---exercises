
def calculate_bill():
    bill = int(input('What is the bill? '))
    tip_percent = int(input('What is the tip percentage? '))
    tip_total = bill * (tip_percent/100)
    total = int(bill + tip_total)
    print(total)


calculate_bill()

    