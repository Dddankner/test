import pandas as pd

diamonds = pd.read_csv('diamonds.csv')

def highest_price():
    price_list = diamonds['price'].to_list()
    highest = 0
    for price in price_list:
        if price > highest: 
            highest = price
    return highest

def avg_price():
    price_list = diamonds['price'].to_list()
    sum = 0
    for price in price_list:
        sum += price
    return sum / len(price_list)

def how_many_ideal():
    cut_list = diamonds['cut'].to_list()
    counter = 0
    for cut in cut_list:
        if cut == 'Ideal': 
            counter += 1
    return counter

def how_many_colors():
    colors_set = set()
    colors_list = diamonds['color'].to_list()
    for color in colors_list:
        colors_set.add(color)
    print(f'there are {len(colors_set)} colors of diamonds:')
    for color in colors_set:
        print(color)
    return colors_set

def how_many_cuts():
    cuts_set = set()
    cuts_list = diamonds['cut'].to_list()
    for cut in cuts_list:
        cuts_set.add(cut)
    return cuts_set

def half_carat_of_premium():
    premium_carat_list =  list()
    cut_list = diamonds['cut'].to_list()
    carat_list = diamonds['carat'].to_list()
    for i, cut in enumerate(cut_list):
        if cut == 'Premium':
            premium_carat_list.append(carat_list[i])
    premium_carat_list.sort()
    return premium_carat_list[len(premium_carat_list) // 2]

def avg_carat_per_cut(cut_type):
    carat_list = diamonds['carat'].to_list()
    cut_list = diamonds['cut'].to_list()
    sum = 0
    counter = 0
    for i, cut in enumerate(cut_list):
        if cut == cut_type:
            sum += carat_list[i]
            counter += 1
    return sum / counter

def price_avg_per_color(color_name):
    colors_list = diamonds['color'].to_list()
    price_list = diamonds['price'].to_list()
    sum = 0
    counter = 0
    for i, color in enumerate(colors_list):
        if color == color_name:
            sum += price_list[i]
            counter += 1
    return sum / counter

if __name__ == '__main__':
    print('this is the most expensive diamond: ', highest_price())
    print('---------------------------------------------------------------')
    print('this is the average price: ', avg_price())
    print('---------------------------------------------------------------')
    print('this is the amount of Ideal cut diamonds: ', how_many_ideal())
    print('---------------------------------------------------------------')
    colors_set = how_many_colors()
    print('---------------------------------------------------------------')
    print('this is the half carat of Premium cut: ', half_carat_of_premium())
    print('---------------------------------------------------------------')
    cuts_set = how_many_cuts()
    for cut in cuts_set:
        print(f'this is the avg of carat for {cut} cut is: {avg_carat_per_cut(cut)}')
    print('---------------------------------------------------------------')
    for color in colors_set:
        print(f'this is the avg of price for {color} color is: {price_avg_per_color(color)}')
    


