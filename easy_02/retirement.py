
import datetime

current_age = int(input('What is your age? '))
retire_age = int(input('At what age would you like to retire? '))
years_left = retire_age - current_age
current_year = datetime.date.today().year

print(f'It is {current_year}. You will retire in '
      f'{current_year + (years_left)}.\n'
      f'You only have {years_left} years of work to go! ')