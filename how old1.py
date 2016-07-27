def calculate_age(year_of_birth, current_year):
    if year_of_birth == current_year:
        return "You were born this very year!"
    elif year_of_birth < current_year:
        after_born = current_year - year_of_birth
        if after_born == 1:
            return 'You are 1 year old.'
        else:
            return 'You are ' + str(after_born) + ' years old.'
    elif year_of_birth > current_year:
        until_born = current_year - year_of_birth
        if until_born == -1:
            return 'You will be born in 1 year.'
        else:
            return 'You will be born in ' + str(until_born * -1) + ' years.'


print calculate_age(1990,2017)