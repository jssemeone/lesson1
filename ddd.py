def get_summ(one, two, delimiter ='&'):
    one = str(one)
    two = str(two)
    return one + delimiter + two
summ = get_summ('Learn', 'Python')
    
def format_price(price):
    price = int(price)
    price = str(price)
    format = 'цена ' + price + ' руб'
    return format.upper()
    
volume = format_price(56.24)
print(volume)
