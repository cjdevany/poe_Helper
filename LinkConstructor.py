# This class is responsible for constructing the request link from poe.ninja
# Takes a league name and an item type and will construct a link to fetch the relevant data

# poe.ninja example request links:
# Currency 	https://poe.ninja/api/data/currencyoverview?league=Blight&type=Currency
# Fragment 	https://poe.ninja/api/data/currencyoverview?league=Blight&type=Fragment
# Oils 	    https://poe.ninja/api/data/itemoverview?league=Blight&type=Oil
# Scarabs 	https://poe.ninja/api/data/itemoverview?league=Blight&type=Scarab
# Fossil 	https://poe.ninja/api/data/itemoverview?league=Blight&type=Fossil
# Essence 	https://poe.ninja/api/data/itemoverview?league=Blight&type=Essence

# a list of valid leagues, add new leagues here or program won't work
leagues = ['Standard', 'Crucible']
item_types = ['Currency', 'Fragment', 'Oil', 'Scarab', 'Fossil', 'Essence']

class LinkConstructor:
    def __init__(self, league, item_type):
        if league not in leagues:
            raise Exception('An invalid league was provided. If this should not be the case add the league name to Leagues list in LinkConstructor.py')
        if item_type not in item_types:
            raise Exception('An invalid item type was provided. If this should not be the case check your syntax, as the item type passed to the constructor must be defined in item_types list in LinkConstructor.py')
        
        self.link = 'https://poe.ninja/api/data/'

        if item_type == 'Currency' or item_type == 'Fragment':
            self.link += 'currencyoverview'
        else:
            self.link += 'itemoverview'
        
        self.link += '?league=' + str(league) + '&type=' + str(item_type)
        self.league = league
        self.item_type = item_type

    def __str__(self):
        return self.link


# testing
if __name__ == '__main__':
    test_link1 = LinkConstructor('Crucible', 'Currency')
    test_link2 = LinkConstructor('Crucible', 'Fragment')
    test_link3 = LinkConstructor('Crucible', 'Oil')
    test_link4 = LinkConstructor('Crucible', 'Scarab')
    test_link5 = LinkConstructor('Crucible', 'Fossil')
    test_link6 = LinkConstructor('Crucible', 'Essence')

    print(test_link1)
    print(test_link2)
    print(test_link3)
    print(test_link4)
    print(test_link5)
    print(test_link6)
