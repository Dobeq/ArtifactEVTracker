import requests, json

def getAveragePrice(rarity):
    rarity = translateRarity(rarity)
    rarityJson = requests.get("https://steamcommunity.com/market/search/render/?search_descriptions=0&category_583950_Rarity%5B%5D=" + rarity + "&sort_dir=desc&appid=583950&norender=1&count=500").json()
    total = 0
    sumPrice = 0
    for card in rarityJson['results']:
        total += 1
        sumPrice += card['sell_price']
    sumPrice /= total
    sumPrice /= 100
    return sumPrice
def getHeroPrice():
    heroes = requests.get("https://steamcommunity.com/market/search/render/?search_descriptions=0&category_583950_Card_Type[]=tag_Hero&sort_dir=desc&appid=583950&norender=1&count=500")
    heroesJson = heroes.json()
    total = 0
    sumPrice = 0
    for card in heroesJson['results']:
        total += 1
        if card['asset_description']['type'] == 'Common Card':
            sumPrice += card['sell_price']
        elif card['asset_description']['type'] == 'Uncommon Card':
            sumPrice += (card['sell_price'] * 2) / 9
        elif card['asset_description']['type'] == 'Rare Card':
            sumPrice += card['sell_price'] / 9
        
    sumPrice /= total
    sumPrice /= 100
    return sumPrice
def translateRarity(rarity):
    if rarity == "common":
        return "tag_Rarity_Common"
    elif rarity == "uncommon":
        return "tag_Rarity_Uncommon"
    elif rarity == "rare":
        return "tag_Rarity_Rare"
def calcEv(common, uncommon, rare, hero):
    return common * 8 + uncommon * 2 + rare + hero
if __name__ == '__main__':
    print(calcEv(getAveragePrice('common'), getAveragePrice('uncommon'),getAveragePrice('rare'), getHeroPrice()))
#not sure on the exact ratios - change out the 2s for 1s and the 9s for 10s for something lower, then cut uncommons for minimum