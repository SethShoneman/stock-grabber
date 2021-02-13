import requests
import json
from datetime import datetime

# grab information on given stocks, and create a wanted number of files containing that information
def stockFunc(num,stocks):
    for x in range(int(num)):
        #gets data from API
        url = "https://api.tdameritrade.com/v1/marketdata/quotes?apikey=JITOXNVGAC9TICFWUG4VTPS3ZIRQEDE4&symbol="+stocks
        querystring = {"region":"US","lang":"en"}
        response = requests.request("GET", url, params=querystring)

        #puts data into a usable form
        data=json.loads(response.text)

        #records all stocks requested to loop through
        stockList = []
        for stock in data:
            stockList.append(stock)

        #gets all stock values contained together, separated by stock, into a list
        values = []
        for symbol in stockList:
            stockValues = []
            for val in data[symbol].values():
                stockValues.append(val)
            values.append(stockValues)

        #changes name of file
        #this is where I placed the files, the path would be changed to where output files are wanted         
        name = 'C:\\Users\\sidda\\Documents\\ameritrade\\outputFiles'+"\\output"+str(x+1)+".csv"
        print(name)

        #writes final values to a csv file
        with open(name, 'w') as f:
            for stock in values:
                for val in stock:
                    f.write("\""+str(val)+"\",")
                f.write("\""+str(datetime.now())+"\"")
                f.write("\n")
