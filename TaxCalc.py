hours = float(input("Please Enter the Number of Hours you worked this week: "))
minimum_wage = 15
gross_income = minimum_wage * hours
print("Gross Income:", gross_income)

def net():
    if hours > 40:
        net_income = gross_income * 0.1738
        print("Net Income:", net_income)
    
    elif hours > 30:
        net_income = gross_income * 0.1230
        print("Net Income:", net_income)
    
    elif hours > 25:
        net_income = gross_income * 0.106
        print("Net Income:", net_income)
    
    elif hours > 20:
        net_income = gross_income * 0.0628
        print("Net Income:", net_income)
    
    elif hours > 15:
        net_income = gross_income * 0.0580
        print("Net Income:", net_income)
    
    elif hours > 10:
        net_income = gross_income * 0.0494
        print("Net Income:", net_income)

net()

