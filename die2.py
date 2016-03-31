
""" Print the mean, min, and max values."""
from random import randint
def get_dice():
    entree = input ("How many die would you like to roll?  ")
    total_die = int(entree)

    die_val = [ ]
    while total_die > 0:
        die_val.append(randint (1, 6))
        total_die -= 1
    print(die_val)

def count_total(die_val):
    total = 0
    for dice in die_val:
        total += dice
    return (total)
def mean(total, total_die):
    mean = total/total_die
    return(mean)

def show_user(die_val, total, mean):
    print('These are your {} rolls: {}'.format(len(die_val), die_val))
    print('They add together to equal {}.'.format(total))
    print('The mean value of your rolls is {}.'.format(mean))
​

get_dice()
count_total()
mean()
show_user()
