from operator import itemgetter
from beautifultable import BeautifulTable
import pprint
import requests


def create_table(list):
    table = BeautifulTable()
    table.column_headers = ["S.No", "Name", "Symbol", "Market cap", "price", "Circulating Supply","Volume (24h)","% 1h","%24 h","% 7d"]
    for i,item in enumerate(list):
        table.append_row([i+1, list[i]["name"],list[i]["symbol"],list[i]["market cap"],
                                    list[i]["price"],list[i]["circulating_supply"],list[i]["volume"],
                                    list[i]["percent_1hr"],list[i]["percent_24h"],list[i]["percent_7d"]])

    table.left_border_char = '|'
    table.right_border_char = '|'
    table.top_border_char = '='
    table.bottom_border_char = '='
    table.header_separator_char = '='
    table.row_separator_char = '='
    table.intersection_char = '|'
    table.column_separator_char = '|'
    return table


def create_list(codes,c_list):
    for key in codes.keys():
        inner = codes[key]
        price = inner["quotes"]["USD"]
        info  = {
            "name" : inner['name'],
            "rank" : inner['rank'],
            "symbol":inner["symbol"],
            "circulating_supply":inner["circulating_supply"],
            'price' : price["price"],
            "volume": price["volume_24h"],
            "market cap": price["market_cap"],
            "percent_1hr" : price["percent_change_1h"],
            "percent_24h": price["percent_change_24h"],
            "percent_7d" : price["percent_change_7d"]
          } 
        c_list.append(info)

    newlist = sorted(c_list, key=itemgetter('rank'))
    return newlist

def run_crypto():
    url = ('https://api.coinmarketcap.com/v2/ticker/?limit=10')
    res= requests.get(url)
    dic = res.json()
    codes= dic['data']
    c_list = []
    newlist = create_list(codes,c_list)
    table = create_table(newlist)
    BeautifulTable.WEP_WRAP
    print(table) 

  
