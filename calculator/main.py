def colint(qst, min, max):
    while True:
        try:
            val = int(input(qst))
        except ValueError:
            print('Your must provide a valid number.')
            continue
        if val < min or val > max:
            print('You must provide a valid number.')
            continue
        else:
            break
    return val

acthrs = colint('About how many hours are you active per day? Set to any number if you don\'t have or need this information. >> ', 1, 24)
while True:
    curlvl = colint('What is your current level? >> ', 1, 100000)
    deslvl = colint('What is your desired level? >> ', 1, 100000)
    if curlvl >= deslvl:
        print('Please check your inputs for current/desired level and try again.')
        continue
    else:
        break
while True:
    curexp = colint('How much XP do you have toward the next level? (in rank card)\n(Please type full number. e.g. 33.6k > 33600) >> ', 0, 1000000000)
    if curexp > (5 * (curlvl ** 2) + (50 * curlvl) + 100 - 0):
        print('Please check your input and try again.')
        continue
    else:
        break

def frm(lvl, exp):
    return 5*(lvl**2)+(50*lvl)+100-exp # mee6 formula

def equ(cur, des, exp, act):
    tnl = frm(cur, exp) # calculate xp to get from current level to next.
    lft = des - cur - 1
    while lft > 0: 
        new = des - lft
        tnl += frm(new,0 ) # calculate xp from new level to one above it, add result to total.
        lft -= 1
    print('You need {} xp to reach level {}.'.format(tnl, des))
    min = round(tnl / 20) # user averages 20xp per minute, if they talk at least once per minute. divide total xp by 20 to get minutes.
    hrs = round(min / 60) # divide minutes by 60 to get hours.
    day = round(hrs / act, 2) # divide hours by the amount of hours the user spends chatting to get average days.
    return print('You\'ll need to talk for an average of {} minutes straight to reach your desired level.\nThat\'s about {} straight hours, or a little over {} days,\nbased on the amount of hours per day you are active.'.format(min, hrs, day))

equ(curlvl, deslvl, curexp, acthrs)

input('Press enter to exit >')
