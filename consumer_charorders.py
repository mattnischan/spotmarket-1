#-----------------------------------------------------------------------------
# consumer_charorders.py
# https://github.com/brentnowak/spotmarket
#-----------------------------------------------------------------------------
# Version: 0.1
# - Initial release
#-----------------------------------------------------------------------------

from _utility import *
from _consumer_charorders import *
import evelink.char
import evelink.api

def main():
    service = "consumer_charorders.py"

    # Get characters with walletEnabled = 1
    characters = json.loads(getcharacters())

    # Empty table
    trunkcharorders()

    for character in characters:
        characterID = character['characterID']
        keyID = character['keyID']
        vCode = character['vCode']

        api_key = (keyID, vCode)
        eveapi = evelink.api.API(base_url='api.eveonline.com', api_key=api_key)
        charapi = evelink.char.Char(characterID, eveapi)
        charresponse = charapi.orders()
        charresponse = charresponse[0]

        for key, value in charresponse.iteritems():
            orderID = key
            stationID = value['station_id']
            volEntered = value['amount']
            volRemaining = value['amount_left']
            orderState = value['status']
            typeID = value['type_id']
            range = value['range']
            accountKey = value['account_key']
            duration = value['duration']
            escrow = value['escrow']
            price = value['price']
            bid = value['type']
            issued = value['timestamp']

            issued = arrow.get(issued)
            issued = issued.format('YYYY-MM-DD HH:mm:ss')

            insertorders(characterID, orderID, stationID, volEntered, volRemaining, orderState, typeID, range, accountKey, duration, escrow, price, bid, issued)

if __name__ == "__main__":
    main()
