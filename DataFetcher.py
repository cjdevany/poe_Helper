from LinkConstructor import LinkConstructor
import requests, json
# use linkconstructor to construct a proper link
# fetch the data and return a dictionary with the relevant data

# fetches the data from poe.ninja from being passed a relevant link
# returns a dictionary with all the items returned from the link
def fetch_data(ninja_link):
    result = requests.get(ninja_link)
    dict = json.loads(result.text)
    return dict['lines']

# takes the data from fetch_data and creates a dict with items and values as key value pairs.
class DataFetcher:
    def __init__(self, ninja_link):
        fetch = fetch_data(ninja_link)
        name_key, value_key = '', ''

        # the name and value keys are named differently depending on the type of currency.
        if ninja_link.item_type == 'Currency' or ninja_link.item_type == 'Fragment':
            name_key, value_key = 'currencyTypeName', 'chaosEquivalent'
        else:
            name_key, value_key = 'name', 'chaosValue'
        data = {}
        for item in fetch:
            # data[name_key] = data[value_key]
            data[item[name_key]] = item[value_key]
        
        self.league = ninja_link.league
        self.item_type = ninja_link.item_type
        self.data = data

if __name__ == '__main__':
    # data = fetch_data(LinkConstructor('Crucible', 'Currency'))
    # print(data[0]['currencyTypeName'])

    data = DataFetcher(LinkConstructor('Crucible', 'Essence'))
    print(data.data)