"""Generate funny names by randomly combining names from 3 separate tuples."""
import sys
import random

def main():
    """Choose names at random from 3 tuples of names and print to screen."""
    print("Welcome to the Psych 'Sidekick Name Picker.'\n")
    print("A name just like Sean would pick for Gus:\n\n")

    first = ('Bill', 'Bob', 'Boxelder', 'Bud', 'Buttocks', 'Chad',
             'Chesterfield', 'Cleet', 'Dennis', 'Elphonso', 'Figgs', 'Foncy',
             'Greasy Jim', 'Huckleberry', 'Huggy', 'Ignatious', 'Jimbo',
             'Joe', 'Johnny', 'Lemongrass', 'Mergatroid', '"Mr Peabody"',
             'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Pushmeet',
             'Schlomo', 'Scratchensniff', 'Scut', 'Sid', 'Skidmark', 'Snorki',
             'Soupcan Sam', 'Spitzitout', 'TeeTee', 'Wheezy Joe', 'Winston')
    middle = ('Baby Oil', 'Bad News', 'Big Burps', 'Beenie-Weenie',
              'Stinkbug', 'Bowel Noises', 'Lite', 'Butterbean', 'Chewy',
              'Buttermilk', 'Chigger', 'Cinnabuns', 'Cornbread', 'Crab Meat',
              'Crapps', 'Dark Skies', 'Clawhammer', 'Dicman', 'Fancypants',
              'Gootsy', 'Pottin Soil', 'Lil Debil', 'Longbranch',
              '"Lunch Money"', 'Oil-Can', 'Oinks', 'Old Scratch', 'Potato Bug',
              'Rock Candy', 'The Squirts', 'Slaps', 'Snakes', 'Snoobs',
              'Squids', 'Stinky', 'Storyboard', 'Sweet Tea', 'Jazz Hands',
              'Worms')
    last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
            'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
            'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple',
            'Goodensmith', 'Goodpasture', 'Guster', 'Henderson', 'Hooperbag',
            'Hoosenater', 'Hootkins', 'Jefferson', 'Jenkins',
            'Jingley-Schmidt', 'Johnson', 'Kingfish', 'Listenbee', "M'Bembo",
            'McFadden', 'Moonshine', 'Nettles', 'Noseworthy', 'Olivetti',
            'Outerbridge', 'Overpeck', 'Overturf', 'Oxhandler', 'Pealike',
            'Pennywhistle', 'Peterson', 'Pieplow', 'Pinkerton', 'Porkins',
            'Putney', 'Quakenbush', 'Rainwater', 'Rosenthal', 'Rubbins',
            'Sackrider', 'Snuggleshine', 'Splern', 'Stevens', 'Stroganoff',
            'Sugar-Gold', 'Swackhamer', 'Tippins', 'Turnipseed',
            'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax', 'Weiners',
            'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
            'Woolysocks')

    while True:
        first_name = random.choice(first)
        middle_name = random.choice(middle)
        last_name = random.choice(last)
        print("\n\n")
        print(f"{first_name} {middle_name} {last_name}", file=sys.stderr)
        print("\n\n")
        try_again = input("\n\nTry again? (Press Enter, else n to quit)\n")

        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit.")

if __name__ == '__main__':
    main()
