import time
from math import factorial, fabs
from random import randint


calendar=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
calendar_str=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

'''
# left this one here in case I got to test it sometime
def randate()->str: # returns random str date. Not sure how to optimise
    if randint(0,4) == 4:
        day=randint(1,366)
        if day==366:
            return 'Feb 29'
    else:
        day=randint(1,365)
    for i in range(12):
        if day>calendar[i]:
            day-=calendar[i]
        else:
            return calendar_str[i]+' '+str(day)
'''

# I'm proud to announce I actually fixed your code since your forgot ==4
# But I'm just joking, what matters is your idea speeds code up by major 28%
# I really have a lot to learn, thanks!
def randate() -> str:
    month = randint(0, 11)
    days_in_month = calendar[month]
    if month == 1:
        days_in_month += 1 if randint(1,4)==4 else 0
    return calendar_str[month] + ' ' + str(randint(1, days_in_month))


def simulate(times: int, type_ret='bool'): # simulates dates 'times' times and can return True for containing copy
    dates=[]
    if type_ret=='bool':
        for i in range(times):
            dates.append(randate())
            if dates[-1] in dates[:-1]:
                return True
        return False
    elif type_ret=='list':
        for i in range(times):
            dates.append(randate())
        return dates


def simulate_many(times, dates)->tuple: # basically just does the simulation a lot and returns tuple with results
    wins=0
    loses=0
    for i in range(times):
        if simulate(dates):
            wins+=1
        else:
            loses+=1
    return wins, loses


if __name__ == '__main__':
    while True:
        choice = input('Do you wish to simulate a (S)ingle room of people or (M)ultiple? ')

        if choice.lower()=='m':
            b_days = input('How many people are in the given room? ')
            sims = input('How many simulations do you wish to run? ')
            try:
                b_days=int(b_days)
                sims=int(sims)
            except ValueError:
                print('Please enter a number')
                continue
            start = time.process_time()
            print('Please wait...')
            print('')
            result = simulate_many(sims, b_days)
            prediction = 1 - (((factorial(365) / factorial(365 - b_days)) / 365 ** b_days) * 3 + (
                        (factorial(366) / factorial(366 - b_days)) / 366 ** b_days)) / 4
            print(f'''Simulating {sims} scenarios took {time.process_time() - start} seconds. {result[0]} times a room had at 
            least two people with the same birthdays and in {result[1]} simulations every birthday was unique.
            Judging by it, the chance of two people in the same room of {b_days} people having same birthdays is {result[0] / sims:.4%}.
            Predicted value is {prediction:.4%}, which gives us a {fabs((result[0] / sims) - prediction):.4%} margin of error.''')
            print('')

        elif choice.lower()=='s':
            b_days = input('How many birthdays shall I generate? ')
            try:
                b_days=int(b_days)
            except ValueError:
                print('Please enter a number')
            sim=simulate(b_days, type_ret='list')
            print("Here are 23 birthdays:")
            print(', '.join(sim))
            for i in sim:
                if i in sim[sim.index(i)+1:]:
                    print('In this simulation, multiple people have a birthday on', i)
                    sim[sim.index(i)]='0'
            if '0' not in sim:
                print('In this simulation, every birthday is unique')

# Thanks for the advice. I loved this project
# Cleaning up try except helped add around 9% of speed and your randate optimisation gave 28%
# I'd say thats quite impressive. Also, you may have noticed but I added try to single
# I have a few ideas how to realize randate better but I'm behind schedule for my work so not now
# If we worked on github I could've just made a new branch and merged it instead of resending code through distedu