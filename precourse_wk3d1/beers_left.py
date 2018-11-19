# Checks if there are any beers left on the wall.
def beers_left(beers = input('How many beers remain? ')):
    if beers == 0:
        return 'No beers left.'
    else:
        return 'Beers left!'
print(beers_left())
